CREATE DATABASE IF NOT EXISTS unlucky;
USE unlucky;

CREATE TABLE IF NOT EXISTS accounts (
	idAccount int(11) NOT NULL AUTO_INCREMENT,
  	username varchar(100) NOT NULL,
  	email varchar(50) NOT NULL,
    PRIMARY KEY (idAccount)
);

create table commentDB (
id int auto_increment,
username varchar(50) NOT NULL,
content varchar(255) not null,
now_date varchar(20),
PRIMARY KEY (id)
);