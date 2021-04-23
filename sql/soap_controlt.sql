
ALTER TABLE gps ADD COLUMN imei varchar(20); 

--- Test:
-- insert into gps (name, type, active, aka) VALUES ('864180038790106', 5, 't', 'TK001');
-- UPDATE gps SET  

CREATE TABLE IF NOT EXISTS soap_controlt (
  id serial PRIMARY KEY,
  vehicle_id INT NOT NULL,
  last_position_gps_id INT NOT NULL,
  created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_delivery TIMESTAMP,
  FOREIGN KEY (vehicle_id) REFERENCES vehiculos (id)
  --FOREIGN KEY (last_position_gps_id) REFERENCES last_positions_gps (id)
);
