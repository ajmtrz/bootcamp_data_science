CREATE DATABASE co2_emissions;

USE co2_emissions;

CREATE TABLE fuel_type (
    fuel_type_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    fuel_type VARCHAR(20)
);
    
CREATE TABLE make (
make_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
make VARCHAR(64)
);

CREATE TABLE model (
model_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
model VARCHAR(64)
);

CREATE TABLE vehicle_class (
vehicle_class_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
vehicle_class VARCHAR(64)
);

CREATE TABLE transmission (
transmission_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
transmission VARCHAR(64)
);


CREATE TABLE vehicle (
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
model_year INT,
make_id INT UNSIGNED,
model_id INT UNSIGNED,
vehicle_class_id INT UNSIGNED,
FOREIGN KEY (make_id) REFERENCES make(make_id),
FOREIGN KEY (model_id) REFERENCES model(model_id),
FOREIGN KEY (vehicle_class_id) REFERENCES vehicle_class(vehicle_class_id)
);

CREATE TABLE fuel (
id INT UNSIGNED PRIMARY KEY,
fuel_consumption_city FLOAT,
fuel_consumption_hwy FLOAT,
fuel_consumption_comb FLOAT,
fuel_consumption_comb_mpg FLOAT,
co2_emissions FLOAT,
FOREIGN KEY (id) REFERENCES vehicle(id)
);

CREATE TABLE vehicle_engine (
id INT UNSIGNED PRIMARY KEY,
fuel_type_id INT UNSIGNED,
engine_size FLOAT,
cylinders FLOAT,
transmission_id INT UNSIGNED,
FOREIGN KEY (id) REFERENCES vehicle(id),
FOREIGN KEY (fuel_type_id) REFERENCES fuel_type(fuel_type_id),
FOREIGN KEY (transmission_id) REFERENCES transmission(transmission_id)
);

CREATE TABLE co2_prediction (
id INT UNSIGNED PRIMARY KEY,
prediction FLOAT,
FOREIGN KEY (id) REFERENCES vehicle(id)
);
