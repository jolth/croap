ALTER TABLE gps ADD COLUMN imei varchar(20);

CREATE TABLE IF NOT EXISTS soap_server (
  id serial PRIMARY KEY,
  name varchar(50)
);

INSERT INTO soap_server (name) VALUES ('controlt');

CREATE TABLE IF NOT EXISTS vehicle_soap (
  id serial PRIMARY KEY,
  vehicle_id INT UNIQUE NOT NULL,
  gps_id INT UNIQUE NOT NULL,
  last_position_gps_id INT NOT NULL,
  created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  soap_server INT NOT NULL,
  last_delivery TIMESTAMP,
  FOREIGN KEY (vehicle_id) REFERENCES vehiculos (id),
  FOREIGN KEY (gps_id) REFERENCES gps (id),
  FOREIGN KEY (soap_server) REFERENCES soap_server (id)
);