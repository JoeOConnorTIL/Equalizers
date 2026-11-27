with source as (

Select distinct
    fixture_id,
    unnest(nested_events, recursive:= true)
from 
{{ref('stg_second_level_unnest__fixtures')}}

)
,
renamed as (

    select
        fixture_id,
        elapsed AS game_minute,
        extra AS added_time,
        id AS team_id,
        name AS team_name,
        -- logo,
        id_1 AS player_id,
        name_1 AS player_name,
        id_2 AS second_player_id,
        name_2 AS second_player_name,
        type AS event_type,
        detail AS event_detail,
        comments AS extra_detail

    from source

)

select * from renamed