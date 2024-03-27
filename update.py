# Script to create a temporary sites_routes table and compare it to the latter for route_counts value modification


import psycopg2

# Connect to the db
conn = psycopg2.connect(
    dbname="bleauinfo",
    user="postgres",
    password="hello",
    host="localhost",
    port="5432"
)

# Open a cursor to perform db operations 
cur = conn.cursor()

# Create temporary tables with same structure as the main tables 
cur.execute("CREATE TEMPORARY TABLE IF NOT EXISTS temp_sites_routes (id serial PRIMARY KEY, site_name int NOT NULL, route_type int NOT NULL, route_count int NOT NULL, FOREIGN KEY (site_name) REFERENCES temp_sites (id), FOREIGN KEY (route_type) REFERENCES temp_routes (id));")


# Execute the transaction to create the relation table of routes types and count associate to a site 
def insertRelations(sites_routes):
    try:
        # Iterate over each (key) site and its associated (value) routes and route count
        for site_name, routes_and_counts in sites_routes.items():
            # Fetch the site ID from the temporary sites table where id matches the current site name 
            cur.execute("SELECT id FROM sites WHERE name = %s", (site_name,))
            site_id = cur.fetchone()[0]

            # Iterate over each route and its count
            for route_name, route_count in routes_and_counts:
                # Fetch the route ID from the temporary routes table where id matches the current route name
                cur.execute("SELECT id FROM routes WHERE name = %s", (route_name,))
                route_id = cur.fetchone()[0]

                # Insert site_id, route_id and route_count in the temporary sites_routes table
                cur.execute("INSERT INTO temp_sites_routes (site_name, route_type, route_count) VALUES (%s, %s, %s)", (site_id, route_id, route_count))
        
        conn.commit()
        print("Creation of temporary table committed successfully")


    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print("Error occurred during creation of temporary table:", error)

# Compare temp_sites_routes route_counts column to sites_routes same column and update if any difference
def compareAndUpdate():
    try:
        cur.execute("""
            UPDATE temp_sites_routes AS temp
            SET route_count = sites.route_count
            FROM sites_routes AS sites
            WHERE temp.site_name = sites.site_name
            AND temp.route_type = sites.route_type
            AND temp.route_count != sites.route_count
        """)

        conn.commit()
        print("Route counts compared and updated successfully")

    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print("Error occurred during the update of route_counts:", error)


# Exclude any row where the route count is equal to or less than zero
def deleteNegativeRouteCounts():
    try:
        cur.execute("""
            DELETE FROM sites_routes
            WHERE rout_count <= 0
        """)

        conn.commit()
        print("Rows with zero or negative route counts deleted successfully")

    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print("Error occurred during the delete of negative route_counts:", error)


def executeInsertionAndUpdate(sites_routes):
    try:
        insertRelations(sites_routes)
        compareAndUpdate()
        deleteNegativeRouteCounts()

    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print("Error occurred during execution of update script:", error)

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()
