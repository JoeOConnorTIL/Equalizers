{#  {{ codegen.generate_source(schema_name= 'main', database_name= 'my_db', table_names=['test_upload']) }} #}

{{ codegen.generate_source(schema_name= 'main', database_name= 'my_db', table_names= ['fixtures_raw', 'statistics_raw', 'standings_raw'], generate_columns=true, include_descriptions=true, include_data_types=true) }}