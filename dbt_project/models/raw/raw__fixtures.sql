with input AS (
    select * from {{ source('motherduck', 'fixtures_raw')}}
)

select * from input