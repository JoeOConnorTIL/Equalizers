with input AS (
    select * from {{ source('motherduck', 'standings_raw')}}
)

select * from input