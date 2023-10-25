# Valorant Pipeline (dbt + Airflow)

## Getting Started

### Spinning up a Postgres database

1. Start a local Postgres container

```shell
docker run --name postgres-db -e POSTGRES_PASSWORD=<password> -p 5432:5432 -d postgres
```

2. Find the container id

```shell
docker ps | grep postgres-db
```

3. Enter the Docker container

```shell
docker exec -it <container_id> bash
```

4. Create a Postgres database

```shell
psql
CREATE DATABASE strava;
```

### Connect to Postgres with dbt

1. Navigate to the `dbt/` directory

2. Create `profiles.yml` with the following content:

```yml
valorant_dbt_airflow:
  target: dev
  outputs:
    dev:
      type: postgres
      host: 127.0.0.1
      port: 5432
      user: postgres
      password: <password>
      dbname: strava
      schema: strava
```
