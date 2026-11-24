{% macro generate_ref_model(model_name) %}

{% set model_relation = ref(model_name) %}
{% set columns = adapter.get_columns_in_relation(model_relation) %}
{% set column_names = columns | map(attribute='name') | list %}

{% set base_model_sql %}
with source as (

    select * from {{ "{{ ref('" ~ model_name ~ "') }}" }}

),

renamed as (

    select
        {%- for column in column_names %}
        {{ column | lower }}{{ "," if not loop.last }}
        {%- endfor %}

    from source

)

select * from renamed
{% endset %}

{% if execute %}
{{ log(base_model_sql, info=True) }}
{% do return(base_model_sql) %}
{% endif %}

{% endmacro %}
