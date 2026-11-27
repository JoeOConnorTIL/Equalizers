with input AS (
    select * from {{ source('motherduck', 'fixtures_raw')}}
)

select 
    get,
    parameters,
    errors,
    results,
    paging,
    response
from input