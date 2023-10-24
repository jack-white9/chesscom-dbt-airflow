# Valorant Pipeline (dbt + Airflow)

## Getting Started

### Spinning up a Postgres database

1. Navigate to the `postgres/` directory

2. Create a `.env` file and populate with the following secrets:

```shell
PG_USER=<...>
PG_PASSWORD=<...>
PG_DB=<...>
```

3. Start a detached Postgres container

```shell
docker-compose up -d
```
