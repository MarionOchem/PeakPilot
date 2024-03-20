CREATE TABLE IF NOT EXISTS sites (
    id bigserial NOT NULL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS routes (
    id bigserial NOT NULL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS sites_routes (
    id bigserial NOT NULL,
    site_name int NOT NULL,
    route_type int NOT NULL,
    route_count int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (site_name) REFERENCES sites (id),
    FOREIGN KEY (route_type) REFERENCES routes (id)
);


-- Exemple of the sql query to manage the insertion of routes types and count of the latter : 
INSERT INTO sites_routes (site_name, route_type, route_count)
VALUES (:site_name_value, :route_type_value, 1)
ON CONFLICT (site_name, route_type) DO UPDATE
SET route_count = sites_routes.route_count + 1;

-- Question : 
-- Do i have to put this tables creation inside a sql transaction ? 