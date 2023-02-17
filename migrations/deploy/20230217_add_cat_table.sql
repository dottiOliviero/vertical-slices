-- Deploy vertical_slices:20230217_add_cat_table to pg

BEGIN;

    CREATE table IF NOT EXISTS cat (
        id BIGSERIAL PRIMARY KEY,
	    name VARCHAR(100),
	    color VARCHAR(20),
	    age INTEGER
    );

COMMIT;
