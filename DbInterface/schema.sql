-- Database tables creation, wrapped inside a sql transaction for error handling and consistency. 

BEGIN;
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
COMMIT;
