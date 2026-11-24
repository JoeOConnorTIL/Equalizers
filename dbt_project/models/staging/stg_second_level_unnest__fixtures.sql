with source as (

    select * from {{ ref('stg_first_level_unnest__fixtures') }}

),

renamed as (

    select
        id,
        referee,
        timezone,
        date,
        timestamp,
        first,
        second,
        id_1,
        name,
        city,
        long,
        short,
        elapsed,
        extra,
        id_2,
        name_1,
        country,
        logo,
        flag,
        season,
        round,
        standings,
        id_3,
        name_2,
        logo_1,
        winner,
        id_4,
        name_3,
        logo_2,
        winner_1,
        home,
        away,
        home_1,
        away_1,
        home_2,
        away_2,
        home_3,
        away_3,
        home_4,
        away_4,
        events,
        lineups,
        statistics,
        players

    from source

)

select * from renamed