
--- Test:
-- insert into gps (name, type, active, aka) VALUES ('864180038790106', 5, 't', 'TK001');
-- UPDATE gps SET  

--CREATE TABLE IF NOT EXISTS soap_controlt (
--  id serial PRIMARY KEY,
--  vehicle_id INT UNIQUE NOT NULL,
--  gps_id INT UNIQUE NOT NULL,
--  last_position_gps_id INT NOT NULL,
--  created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--  last_delivery TIMESTAMP,
--  FOREIGN KEY (vehicle_id) REFERENCES vehiculos (id)
  --FOREIGN KEY (last_position_gps_id) REFERENCES last_positions_gps (id)
--);



--------------------------------------------------------------------------------- 28/05/2021

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
 
  --FOREIGN KEY (last_position_gps_id) REFERENCES last_positions_gps (id)
);


-- insertar un vehiculo para el web service de controlT:

INSERT INTO vehicle_soap (vehicle_id, last_position_gps_id, gps_id, soap_server)
SELECT v.id, lpg.id, v.gps_id, ss.id
FROM vehiculos AS v
LEFT JOIN last_positions_gps AS lpg ON (v.gps_id=lpg.gps_id)
LEFT JOIN soap_server AS ss ON (ss.name='controlt') -- ---> OJO: poner el nombre del service
WHERE placa=lower('VZI171');


------------------------- TEST:
