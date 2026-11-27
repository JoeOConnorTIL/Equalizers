with source as (

    select * from {{ ref('raw__fixtures') }}

),

renamed as (

    select distinct
        -- get,
        -- parameters,
        -- errors,
        -- results,
        -- paging,
        -- response,
        unnest(response, recursive := true)

    from source

)

select * from renamed