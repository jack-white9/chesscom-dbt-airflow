{{ config(materialized='view') }}

with source_data as (
    select * from source.players
    where ingestion_date = (
        select max(ingestion_date) from source.players
    )
)

select *
from source_data
