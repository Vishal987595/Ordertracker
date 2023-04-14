drop database if exists food_token;
create database food_token;
use food_token;

-- Outlet Table
-- drop table if exists outlet;
create table outlet (
outlet_id int primary key,
name varchar(25) not null,
email varchar(50) not null unique,
phone_no varchar(13) not null unique,
password varchar(30) not null unique
);

-- Order table
-- drop table if exists orders ;
create table orders (
order_id int primary key,
order_status varchar(20) check(order_status in ('queued', 'prepared', 'collected')),
token_no int not null,
placed_time datetime default null,
prepared_time datetime default null, 
collected_time datetime default null,
outlet_id int,
foreign key (outlet_id) references outlet(outlet_id) on delete cascade  
);

INSERT INTO food_token.outlet VALUES
('1', 'aadhya', 'aadhya@gmail.com', '7894561230', 'aadhya'),
('2', '2 degree', '2degree@gmail.com', '9876543210', '2degree');

select * from outlet;


