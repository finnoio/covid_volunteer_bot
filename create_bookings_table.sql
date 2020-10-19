CREATE TABLE bookings
(
    id SERIAL PRIMARY KEY,
    c_location VARCHAR(100) NOT NULL,
  	c_phone_number VARCHAR(20) NOT NULL,
    b_date DATE NOT NULL,
    details VARCHAR(100) NOT NULL
);