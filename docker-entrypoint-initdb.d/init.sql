CREATE USER opfina WITH ENCRYPTED PASSWORD 'opfina$123@_';

ALTER ROLE opfina SET client_encoding TO 'utf8';

ALTER ROLE opfina SET default_transaction_isolation TO 'read committed';

CREATE DATABASE openfina;

GRANT ALL PRIVILEGES ON DATABASE openfina TO opfina;

ALTER DATABASE openfina OWNER TO opfina;