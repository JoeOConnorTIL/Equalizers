with input AS (
    select * from {{ source('motherduck', 'statistics_raw')}}
)

select * from input