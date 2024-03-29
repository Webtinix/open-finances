#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	
    ALTER ROLE $POSTGRES_USER SET client_encoding TO 'utf8';
    
    ALTER ROLE $POSTGRES_USER SET default_transaction_isolation TO 'read committed';

    GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;

    ALTER DATABASE $POSTGRES_DB OWNER TO $POSTGRES_USER;
    
EOSQL