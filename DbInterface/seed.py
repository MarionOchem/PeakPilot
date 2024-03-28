# Create the tables and insert the scraped data into them

import psycopg2


# Connect to the db
conn = psycopg2.connect(
    dbname="bleauinfo",
    user="postgres",
    password="hello",
    host="localhost",
    port="5432"
)

# TODO: unitest / pytest (py lib for testing)

'''
Debug dataset :
routes = {'avec corde', 'trous', 'saut', 'jeté', 'traversée d-g', 'monodoigts', 'traversée', 'haut', 'pincettes', 'fissure', 'inversées', 'bombé', 'aplats', 'descente', 'cheminée', 'bidoigts', 'réglettes', 'pilier', 'dalle', 'départ assis', 'arête', 'expo', 'dièdre', 'proue', 'traversée g-d', 'boucle', 'toit', 'surplomb', 'mur', 'réta', 'dévers'}
sites = ['Bas Cuvier', 'Cuvier Bellevue', 'Cuvier Camp de Chailly', 'Cuvier Est', 'Cuvier Merveille', 'Cuvier Nord', 'Cuvier Ouest (Réserve biologique)', 'Cuvier Rempart', 'Cuvier Sorcières', 'La Mare �\xa0 Piat', 'La Reconnaissance', 'Monts & Merveilles (Réserve biologique)', 'Petit Rempart', 'Apremont', 'Apremont Belvédère', 'Apremont Bizons', 'Apremont Brûlis', 'Apremont Butte aux Dames', 'Apremont Butte aux Peintres', 'Apremont Buvette', 'Apremont Désert', 'Apremont Envers', 'Apremont Est', 'Apremont Fond des Gorges', 'Apremont Haut des Gorges', 'Apremont Mare aux Biches', 'Apremont Marie-Thérèse', 'Apremont Milan', 'Apremont Ouest', 'Apremont Portes du Désert', 'Apremont Sanglier', 'Apremont Vallon de la Solitude', 'Apremont Vallon de Sully', 'Cuisinière', 'Cuisinière Carnage', 'Cuisinière Crête Sud', 'Franchard Basses Plaines', 'Franchard Druides', 'Franchard Ermitage', 'Franchard Hautes Plaines', 'Franchard Hauts Sablons', 'Franchard Isatis', 'Franchard Meyer', 'Franchard Point de Vue', 'Franchard Raymond', 'Franchard Sablons', 'Franchard Sablons Carriers', 'Franchard Sablons Ouest', 'Gorge aux Merisiers', 'Gorges du Houx', 'Gorges du Houx Oiseaux de Proie', 'Gorges du Houx Parjure', 'Gorges du Houx Petit Paradis', 'Gorges du Houx Rocher du Renard', 'Long Boyau', 'Long Boyau Ouest', 'Mont Aigu', 'Cassepot Roches Grises', 'Cassepot Roches Oranges', 'Cassepot Roches Roses', 'Grotte de Seine-Port', 'Le Calvaire', 'Le Calvaire Est', 'Le Petit Mont', 'Mont Chauvet', 'Mont Ussy', 'Mont Ussy Est', "Roche d'Hercule", 'Rocher Canon', 'Rocher Canon Ouest']
sites_routes = {'Bas Cuvier': [('mur', 339), ('dalle', 177), ('aplats', 131), ('réglettes', 91), ('arête', 90), ('départ assis', 72), ('fissure', 63), ('traversée g-d', 62), ('dévers', 52), ('surplomb', 45), ('traversée d-g', 40), ('réta', 39), ('pilier', 38), ('jeté', 22), ('inversées', 18), ('proue', 16), ('expo', 14), ('traversée', 12), ('haut', 12), ('bombé', 10), ('trous', 9), ('toit', 6), ('cheminée', 4), ('bidoigts', 3), ('boucle', 2), ('saut', 2), ('monodoigts', 1), ('pincettes', 1), ('descente', 1), ('dièdre', 1)], 'Cuvier Bellevue': [('départ assis', 88), ('dalle', 66), ('aplats', 47), ('dévers', 36), ('mur', 34), ('arête', 29), ('surplomb', 17), ('proue', 16), ('réglettes', 16), ('réta', 14), ('traversée d-g', 13), ('traversée g-d', 12), ('pilier', 8), ('fissure', 8), ('expo', 6), ('bombé', 5), ('trous', 5), ('jeté', 4), ('traversée', 2), ('toit', 2), ('inversées', 2), ('dièdre', 1), ('haut', 1)], 'Cuvier Camp de Chailly': [('départ assis', 17), ('dévers', 9), ('traversée d-g', 7), ('aplats', 7), ('réta', 7), ('réglettes', 6), ('fissure', 3), ('traversée g-d', 2), ('inversées', 2), ('mur', 2), ('surplomb', 2), ('proue', 1), ('dièdre', 1), ('pilier', 1)], 'Cuvier Est': [('mur', 125), ('dalle', 53), ('arête', 41), ('aplats', 32), ('départ assis', 28), ('réglettes', 26), ('dévers', 20), ('fissure', 18), ('traversée g-d', 17), ('réta', 15), ('expo', 13), ('surplomb', 11), ('haut', 11), ('pilier', 10), ('jeté', 9), ('traversée d-g', 7), ('inversées', 6), ('proue', 4), ('bombé', 2), ('trous', 2), ('toit', 1), ('monodoigts', 1), ('dièdre', 1), ('cheminée', 1)], 'Cuvier Merveille': [('mur', 58), ('aplats', 25), ('réglettes', 23), ('départ assis', 22), ('dalle', 20), ('arête', 20), ('haut', 13), ('fissure', 13), ('dévers', 12), ('réta', 11), ('pilier', 10), ('surplomb', 8), ('proue', 6), ('expo', 6), ('bombé', 5), ('traversée g-d', 4), ('traversée d-g', 4), ('jeté', 3), ('inversées', 3), ('toit', 2), ('pincettes', 2), ('bidoigts', 2), ('cheminée', 2), ('trous', 1)], 'Cuvier Nord': [('départ assis', 73), ('mur', 71), ('aplats', 60), ('dalle', 49), ('dévers', 46), ('arête', 38), ('réta', 36), ('traversée g-d', 26), ('réglettes', 18), ('traversée d-g', 18), ('jeté', 16), ('proue', 13), ('inversées', 11), ('fissure', 11), ('surplomb', 10), ('trous', 10), ('pilier', 8), ('toit', 7), ('bombé', 5), ('expo', 5), ('haut', 5), ('pincettes', 4), ('traversée', 2), ('monodoigts', 1), ('dièdre', 1), ('cheminée', 1)], 'Cuvier Ouest (Réserve biologique)': [('départ assis', 53), ('mur', 47), ('aplats', 39), ('arête', 34), ('réta', 27), ('surplomb', 20), ('traversée g-d', 20), ('dévers', 18), ('proue', 16), ('expo', 16), ('dalle', 13), ('traversée d-g', 12), ('réglettes', 11), ('fissure', 11), ('toit', 6), ('jeté', 5), ('traversée', 2), ('haut', 1), ('inversées', 1), ('trous', 1), ('pilier', 1), ('cheminée', 1)], 'Cuvier Rempart': [('mur', 270), ('dalle', 165), ('aplats', 135), ('réglettes', 124), ('arête', 114), ('départ assis', 92), ('surplomb', 65), ('expo', 64), ('fissure', 57), ('pilier', 45), ('réta', 43), ('dévers', 42), ('haut', 40), ('inversées', 35), ('traversée g-d', 24), ('traversée d-g', 22), ('jeté', 21), ('proue', 16), ('toit', 15), ('bombé', 15), ('traversée', 10), ('bidoigts', 6), ('trous', 6), ('cheminée', 4), ('dièdre', 2), ('saut', 1), ('descente', 1)], 'Cuvier Sorcières': [('départ assis', 15), ('dévers', 15), ('mur', 12), ('réta', 9), ('aplats', 9), ('proue', 6), ('pilier', 6), ('traversée g-d', 5), ('arête', 5), ('dalle', 4), ('toit', 3), ('jeté', 3), ('traversée d-g', 3), ('expo', 3), ('surplomb', 2), ('fissure', 2), ('saut', 2), ('réglettes', 1), ('inversées', 1)], 'La Mare �\xa0 Piat': [('mur', 37), ('départ assis', 21), ('aplats', 15), ('dévers', 12), ('réta', 12), ('fissure', 11), ('toit', 11), ('expo', 10), ('réglettes', 8), ('haut', 8), ('jeté', 7), ('traversée g-d', 6), ('arête', 5), ('surplomb', 4), ('proue', 4), ('inversées', 3), ('bombé', 3), ('traversée d-g', 2), ('bidoigts', 2), ('dalle', 2), ('pilier', 1), ('dièdre', 1)], 'La Reconnaissance': [('mur', 115), ('dalle', 62), ('départ assis', 39), ('arête', 38), ('réglettes', 16), ('réta', 16), ('dévers', 15), ('jeté', 15), ('traversée g-d', 13), ('fissure', 13), ('aplats', 9), ('traversée d-g', 7), ('surplomb', 6), ('toit', 5), ('proue', 3), ('inversées', 2), ('bidoigts', 2), ('traversée', 1), ('expo', 1), ('bombé', 1), ('monodoigts', 1), ('pilier', 1), ('dièdre', 1), ('trous', 1), ('haut', 1)], 'Monts & Merveilles (Réserve biologique)': [('dalle', 44), ('réglettes', 40), ('aplats', 38), ('mur', 36), ('dévers', 20), ('arête', 17), ('départ assis', 15), ('réta', 13), ('fissure', 9), ('pilier', 8), ('surplomb', 5), ('dièdre', 5), ('inversées', 4), ('proue', 3), ('bombé', 2), ('jeté', 2), ('pincettes', 2), ('traversée g-d', 1), ('traversée d-g', 1), ('toit', 1)], 'Petit Rempart': [('départ assis', 58), ('dévers', 42), ('mur', 39), ('aplats', 31), ('dalle', 21), ('proue', 19), ('arête', 17), ('surplomb', 12), ('traversée g-d', 11), ('réglettes', 10), ('pilier', 8), ('traversée d-g', 8), ('fissure', 7), ('réta', 6), ('inversées', 2), ('expo', 2), ('bidoigts', 2), ('jeté', 2), ('traversée', 1), ('pincettes', 1), ('dièdre', 1), ('bombé', 1), ('trous', 1)], 'Apremont': [('mur', 79), ('départ assis', 52), ('expo', 43), ('aplats', 38), ('arête', 36), ('dalle', 32), ('dévers', 30), ('réta', 23), ('fissure', 19), ('traversée g-d', 18), ('surplomb', 16), ('traversée d-g', 15), ('réglettes', 15), ('proue', 10), ('jeté', 8), ('pilier', 8), ('haut', 5), ('inversées', 5), ('toit', 4), ('pincettes', 3), ('trous', 3), ('saut', 1), ('avec corde', 1), ('bidoigts', 1), ('bombé', 1)], 'Apremont Belvédère': [('aplats', 3), ('départ assis', 3), ('traversée g-d', 2), ('surplomb', 1)], 'Apremont Bizons': [('mur', 194), ('dalle', 166), ('départ assis', 112), ('réta', 82), ('aplats', 81), ('arête', 61), ('traversée g-d', 50), ('dévers', 47), ('traversée d-g', 46), ('fissure', 36), ('expo', 31), ('pilier', 18), ('surplomb', 17), ('proue', 17), ('jeté', 14), ('bombé', 11), ('toit', 10), ('réglettes', 10), ('haut', 3), ('descente', 3), ('trous', 3), ('bidoigts', 2), ('traversée', 2), ('inversées', 1), ('pincettes', 1), ('dièdre', 1)]}
'''

# Open a cursor to perform db operations 
cur = conn.cursor()

# Create tables if not exists
cur.execute("CREATE TABLE IF NOT EXISTS sites (id serial PRIMARY KEY, name text NOT NULL);")
cur.execute("CREATE TABLE IF NOT EXISTS routes (id serial PRIMARY KEY, name text NOT NULL);")
cur.execute("CREATE TABLE IF NOT EXISTS sites_routes (id serial PRIMARY KEY, site_name int NOT NULL, route_type int NOT NULL, route_count int NOT NULL, FOREIGN KEY (site_name) REFERENCES sites (id), FOREIGN KEY (route_type) REFERENCES routes (id));")

# Execute the insertion of the scrapped sites names in sites table
def insertSites(sites):
    for s in sites:
        cur.execute("INSERT INTO sites (name) VALUES (%s)", (s,))

# Execute the insertion of the scrapped routes names in routes table
def insertRoutes(routes):
    for r in routes:
        cur.execute("INSERT INTO routes (name) VALUES (%s)", (r,))

# Execute the transaction to create the relation table of routes types and count associate to a site 
def insertRelations(sites_routes):
    # Iterate over each (key) site and its associated (value) routes and route count
    for site_name, routes_and_counts in sites_routes.items():
        # Fetch the site ID from the sites table where id matches the current site name 
        cur.execute("SELECT id FROM sites WHERE name = %s", (site_name,))
        site_id = cur.fetchone()[0]

        # Iterate over each route and its count
        for route_name, route_count in routes_and_counts:
            # Fetch the route ID from the routes table where id matches the current route name
            cur.execute("SELECT id FROM routes WHERE name = %s", (route_name,))
            route_id = cur.fetchone()[0]

            # Insert site_id, route_id and route_count in the sites_routes table
            cur.execute("INSERT INTO sites_routes (site_name, route_type, route_count) VALUES (%s, %s, %s)", (site_id, route_id, route_count))


def executeInsertions(sites, routes, sites_routes):
    try:
        # Insert values into tables
        insertSites(sites)
        insertRoutes(routes)
        insertRelations(sites_routes)

        # Commit the transaction
        conn.commit()
        print("Transaction committed successfully")

    except (Exception, psycopg2.DatabaseError) as error:
        # Rollback the transaction in case of error
        conn.rollback()
        print("Error occurred:", error)

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()


