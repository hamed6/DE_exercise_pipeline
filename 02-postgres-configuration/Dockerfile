# Run postgres db
docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="dump_data" \
-v C:/postgres_config:/var/lib/postgresql/data \
-p 5432:5432 \
postgres:13

# Run pgadmin gui
docker run -it \
-e PGADMIN_DEFAULT_EMAIL=user@domain.com \
-e PGADMIN_DEFAULT_PASSWORD=root \
-p 8080:80 \
dpage/pgadmin4

#================================ Docker network
# Create docker network
docker network create pg_database

# Run postgres db
docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="dump_data" \
-v C:/postgres_config:/var/lib/postgresql/data \
-p 5432:5432 \
--network=pg_database \
--name pg_database \
postgres:13

docker run -it \
-e PGADMIN_DEFAULT_EMAIL=user@domain.com \
-e PGADMIN_DEFAULT_PASSWORD=root \
-p 8080:80 \
--network=pg_database \
--name pgadmin \
dpage/pgadmin4