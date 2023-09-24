# OpenThaiGPT Volunteer AI Application Engineer Backend

## Getting Started

Create table in database

```
docker compose -f docker-compose-migration-commit.yaml up --build
```

Start backend service

```
docker compose up --build
```

## Editing Database Scehma

If you want to edit database schema, run migration

```
docker compose -f docker-compose-migration.yaml up --build
```

Then commit

```
docker compose -f docker-compose-migration-commit.yaml up --build
```
