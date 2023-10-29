# Chess.com Pipeline (dbt + Airflow)

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

4. Create a Postgres database and schema

```shell
psql -U postgres
CREATE DATABASE chesscom;
\c chesscom;
CREATE SCHEMA source;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA source TO postgres;
```

### Running data ingestion

1. Add Postgres credentials to `ingestion/.env`

```env
PG_USERNAME=<username>
PG_PASSWORD=<password>
PG_HOST=<host>
PG_PORT=<port>
PG_DATABASE=chesscom
```

2. Install packages

```shell
pip install -r ingestion/requirements.txt
```

3. Run ingestion script

```shell
python ingestion/main.py
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
      dbname: chesscom
      schema: source
```
