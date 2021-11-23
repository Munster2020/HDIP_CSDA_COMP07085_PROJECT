use datarep;

mysql> CREATE TABLE dvds(
    -> id int AUTO_INCREMENT PRIMARY KEY,
    -> title varchar(250),
    -> director varchar(250),
    -> genre varchar(250),
    -> price int
    -> );