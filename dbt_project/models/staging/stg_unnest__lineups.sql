Select distinct
    fixture_id,
    unnest(nested_lineups, recursive:= true)
from 
{{ref('stg_second_level_unnest__fixtures')}}