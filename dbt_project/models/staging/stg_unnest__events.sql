with source as (
Select distinct
    fixture_id,
    unnest(nested_events, recursive:= true)
from 
{{ref('stg_second_level_unnest__fixtures')}}
)
,s2 as (

    select * from source

),

renamed as (

    select
        fixture_id,
        elapsed,
        extra,
        id,
        name,
        logo,
        id_1,
        name_1,
        id_2,
        name_2,
        type,
        detail,
        comments

    from s2

)

select * from renamed