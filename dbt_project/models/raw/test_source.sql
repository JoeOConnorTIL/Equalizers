with input AS (
    select * from {{ source('main', 'test_upload')}}
)

select * from input