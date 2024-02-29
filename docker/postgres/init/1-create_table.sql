\c general_purpose_server;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;

CREATE TYPE location_type_enum AS ENUM ('indoor', 'outdoor');

CREATE TABLE applications (
    id VARCHAR(20) PRIMARY KEY CHECK (id ~ '^[A-Z0-9]+$'),
    secret_key VARCHAR(40) CHECK (secret_key ~ '^[A-Za-z0-9+/]+$'),
    application_name VARCHAR(50) NOT NULL,
    representative_name VARCHAR(50) NOT NULL,
    corporate_name VARCHAR(100) NOT NULL,
    mail VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE users (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name VARCHAR(50),
    mail VARCHAR(255),
    gender VARCHAR(10),
    age INT,
    height DECIMAL(5, 2),
    weight DECIMAL(5, 2),
    address VARCHAR(255),
    occupation VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    application_id VARCHAR(20) REFERENCES applications(id)
);


CREATE TABLE spots (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name VARCHAR(50),
    floor INT,
    location_type location_type_enum,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
);

CREATE TABLE coordinates (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    latitude DECIMAL(9, 6) NOT NULL,
    longitude DECIMAL(9, 6) NOT NULL,
    spot_id UUID REFERENCES spots(id)
);

CREATE TABLE wifis (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name VARCHAR(50),
    ssid VARCHAR(50),
    mac_address VARCHAR(17) NOT NULL CHECK (
        mac_address ~* '([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})'
    ) NOT NULL,
    ip_address VARCHAR(15) NOT NULL CHECK (
        ip_address ~* '^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    ),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    spot_id UUID REFERENCES spots(id)
);


CREATE TABLE bles (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name VARCHAR(50),
    ssid VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    spot_id UUID REFERENCES spots(id)
);

CREATE TABLE wifi_thresholds (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    threshold INT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    wifi_id UUID REFERENCES wifis(id)
);


CREATE TABLE ble_thresholds (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    threshold INT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    ble_id UUID REFERENCES bles(id)
);

CREATE TABLE fp_models (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    file_extension VARCHAR(10) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    spot_id UUID REFERENCES spots(id)
);

CREATE TABLE raw_data (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    spot_id UUID REFERENCES spots(id)
);

CREATE TABLE spots_bles (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    spot_id UUID REFERENCES spots(id) NOT NULL,
    ble_id UUID REFERENCES bles(id) NOT NULL
);

CREATE TABLE spots_wifis (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    spot_id UUID REFERENCES spots(id) NOT NULL,
    wifi_id UUID REFERENCES wifis(id) NOT NULL
);

CREATE TABLE objects (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name VARCHAR(50),
    file_extension VARCHAR(10),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,
    deleted_at TIMESTAMP WITH TIME ZONE,
    user_id UUID REFERENCES users(id),
    spot_id UUID REFERENCES spots(id)
);

CREATE TABLE object_browsing_logs (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    reading_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    user_id UUID REFERENCES users(id),
    object_id UUID REFERENCES objects(id)
);