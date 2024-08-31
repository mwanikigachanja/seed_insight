USE seedinsight;

INSERT INTO ecozones (name, min_altitude, max_altitude, description) VALUES
('Lowland Altitude', 0, 1200, 'Lowland regions with lower altitudes.'),
('Dryland Altitude', 1201, 1400, 'Dry regions with minimal rainfall.'),
('Medium Altitude', 1401, 1500, 'Regions with moderate altitudes.'),
('Transitional Altitude', 1501, 1800, 'Transitional regions between low and high altitudes.'),
('Highland Altitude', 1801, 2800, 'Highland regions with higher altitudes.'),
('Very High Altitude', 2801, 4000, 'Very high altitude regions.');

INSERT INTO crops (name, variety, ecozone_id, maturity_period, seed_rate_per_acre, yield_per_acre, attributes) VALUES
('Maize', 'H614D', 5, 160, 20, 40, 'Good yield, resistant to diseases'),
('Rice', 'NERICA 1', 1, 105, 20, 15, 'Blast resistant, heat tolerant'),
('Maize', 'PH 1', 1, 100, 25, 20, 'Drought resistant, short maturity');
