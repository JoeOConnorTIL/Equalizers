with source as (

    select * from {{ ref('stg_first_level_unnest__fixtures') }}

),

renamed as (

    select
        id AS fixture_id,
        referee,
        timezone,
        date AS match_timestamp,
        --timestamp,
        --first,
        --second,
        id_1 AS stadium_id,
        name AS stadium_name,
        city AS stadium_city,
        long AS match_status_long,
        short AS match_status_short,
        --elapsed,
        --extra,
        id_2 AS league_id,
        name_1 AS league_name,
        country AS league_country,
        logo AS league_logo_url,
        --flag,
        season AS season_year,
        round AS matchweek,
        --standings,
        id_3 AS home_team_id,
        name_2 AS home_team_name,
        logo_1 AS home_team_logo,
        winner AS home_team_win,
        id_4 AS away_team_id,
        name_3 AS away_team_name,
        logo_2 AS away_team_logo,
        winner_1 AS away_team_win,
        home AS home_team_goals,
        away AS away_team_goals,
        home_1 AS home_team_goals_1H,
        away_1 AS away_team_goals_1H,
        home_2 AS home_team_goals_2H,
        away_2 AS away_team_goals_2H,
        home_3 AS home_team_goals_ET1H,
        away_3 AS away_team_goals_ET1H,
        home_4 AS home_team_goals_ET2H,
        away_4 AS away_team_goals_ET2H,
        events AS nested_events,
        lineups AS nested_lineups,
        statistics AS nested_statistics,
        players AS nested_players

    from source

)

select * from renamed