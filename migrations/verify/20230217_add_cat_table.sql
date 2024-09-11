-- Verify vertical_slices:20230217_add_cat_table on pg

BEGIN;

select * from cat limit 1;

ROLLBACK;
