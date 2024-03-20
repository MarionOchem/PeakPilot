
## Exemple of the sql query to manage the insertion of routes types and count of the latter : 
# INSERT INTO sites_routes (site_name, route_type, route_count)
# VALUES (:site_name_value, :route_type_value, 1)
# ON CONFLICT (site_name, route_type) DO UPDATE
# SET route_count = sites_routes.route_count + 1;

