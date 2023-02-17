-- Revert vertical_slices:20230217_add_cat_table from pg

BEGIN;

Drop table cat;

COMMIT;
