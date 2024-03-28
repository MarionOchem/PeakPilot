-- Database tables creation, wrapped inside a sql transaction for error handling and consistency. 

BEGIN;
CREATE TABLE IF NOT EXISTS sites (
    id bigserial NOT NULL,
    name text NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS routes (
    id bigserial NOT NULL,
    name text NOT NULL,
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
COMMIT;


-- This is the sql query to get all infos from the relation table sites_routes : 
/*
SELECT sr.id AS site_route_id, s.name AS site_name, r.name AS route_type, sr.route_count
FROM sites_routes sr
JOIN sites s ON sr.site_name = s.id
JOIN routes r ON sr.route_type = r.id;
*/
