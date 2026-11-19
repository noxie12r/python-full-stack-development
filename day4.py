sachink@Sachins-MacBook-Pro ~ % psql --version
zsh: command not found: psql
sachink@Sachins-MacBook-Pro ~ % brew services start postgresql@18
brew services list

zsh: command not found: brew
zsh: command not found: brew
sachink@Sachins-MacBook-Pro ~ % psql postgres

zsh: command not found: psql
sachink@Sachins-MacBook-Pro ~ % echo 'export PATH="/Library/PostgreSQL/18/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

sachink@Sachins-MacBook-Pro ~ % psql -U postgres

Password for user postgres: 
psql (18.7)
Type "help" for help.

postgres=# insert into student (name,age,couse,marks)
postgres-# values
postgres-# );
ERROR:  syntax error at or near ")"
LINE 3: );
        ^
postgres=# insert into student (name,age,couse,marks)
postgres-# 
postgres-# 
postgres-# insert into student (id,name,age,couse,marks)
postgres-# values
postgres-# (11,'aaa',12,'dsa',98),
postgres-# (22,'bbb',13,'dbms',99),
postgres-# (33,'ccc',14,'dsa',97),
postgres-# 
postgres-# (19,'fga',18,'mat',98);
ERROR:  syntax error at or near "insert"
LINE 2: insert into student (id,name,age,couse,marks)
        ^
postgres=# create table student_card(
postgres(# card_id serial primary key,
postgres(# card_number varchar(50),
postgres(# id int unique references student(id)
postgres(# );
ERROR:  relation "student" does not exist
postgres=# create table student(
postgres(# id serial primary key,
postgres(# name varchar(100),
postgres(# age int,
postgres(# course varchar(50),
postgres(# mark int );
CREATE TABLE
postgres=# \dl
      Large objects
 ID | Owner | Description 
----+-------+-------------
(0 rows)

postgres=# \dt
           List of tables
 Schema |  Name   | Type  |  Owner   
--------+---------+-------+----------
 public | student | table | postgres
(1 row)

postgres=# insert into student(name,age,course,marks,id)
postgres-# values
postgres-# ('Rahul',21,'BCA',85,1),
postgres-# ('Priya',22,'CSE',89,2),
postgres-# ('Uday',23,'BCA',98,3),
postgres-# ('Sachin',24,'MCA'78,4);
ERROR:  syntax error at or near "78"
LINE 6: ('Sachin',24,'MCA'78,4);
                          ^
postgres=# insert into student(name,age,course,marks,id)
values
('Rahul',21,'BCA',85,1),
('Priya',22,'CSE',89,2),
('Uday',23,'BCA',98,3),
('Sachin',24,'MCA',78,4);
ERROR:  column "marks" of relation "student" does not exist
LINE 1: insert into student(name,age,course,marks,id)
                                            ^
postgres=# 
postgres=# insert into student(name,age,course,marks,id)
postgres-# values
postgres-# ('Rahul',21,'BCA',85,1),
postgres-# ('Priya',22,'CSE',89,2),
postgres-# ('Uday',23,'BCA',98,3),
postgres-# ('Sachin',24,'MCA'78,4);
ERROR:  syntax error at or near "78"
LINE 6: ('Sachin',24,'MCA'78,4);
                          ^
postgres=# insert into student(name,age,course,marks,id)
postgres-# values
postgres-# ('Rahul',21,'BCA',85,1),
postgres-# ('Priya',22,'CSE',89,2),
postgres-# ('Uday',23,'BCA',98,3),
postgres-# ('Sachin',24,'MCA',78,4);
ERROR:  column "marks" of relation "student" does not exist
LINE 1: insert into student(name,age,course,marks,id)
                                            ^
postgres=# create a table departent(
postgres(# department_id serial primary key,
postgres(# department_name archar(100) );
ERROR:  syntax error at or near "a"
LINE 1: create a table departent(
               ^
postgres=# create table department(
postgres(# department_id serial primary key,
postgres(# department_name archar(100) );
ERROR:  type "archar" does not exist
LINE 3: department_name archar(100) );
                        ^
postgres=# create table department(
postgres(# department_id serial primary key,
postgres(# department_name varchar(100) );
CREATE TABLE
postgres=# 
postgres=# insert into  departments (departments_name)
postgres-# values
postgres-# ('CSE'),
postgres-# ('AI')
postgres-# ('AE'),
postgres-# ('AI'),
postgres-# ('EC'),
postgres-# ('ME');
ERROR:  syntax error at or near "("
LINE 5: ('AE'),
        ^
postgres=# insert into  departments (departments_name)
postgres-# values
postgres-# ('CSE'),
postgres-# ('AI'),
postgres-# ('AE'),
postgres-# ('EC'),
postgres-# ('ME');
ERROR:  relation "departments" does not exist
LINE 1: insert into  departments (departments_name)
                     ^
postgres=# insert into  department (departments_name)
postgres-# ('CSE'),
postgres-#  ('AI'),
postgres-# ('AE'),
postgres-# ('EC'),
postgres-#  ('ME');
ERROR:  syntax error at or near "'CSE'"
LINE 2: ('CSE'),
         ^
postgres=# insert into  department (departments_name)
postgres-# values
postgres-# ('CSE'),
postgres-# ('AI'),
postgres-# ('AE'),
postgres-# ('EC'),
postgres-# ('ME');
ERROR:  column "departments_name" of relation "department" does not exist
LINE 1: insert into  department (departments_name)
                                 ^
postgres=# insert into  departments (department_name)
postgres-# values
postgres-# ('CSE'),
postgres-# ('AI'),
postgres-# ('AE'),
postgres-# ('EC'),
postgres-# ('ME');
ERROR:  relation "departments" does not exist
LINE 1: insert into  departments (department_name)
                     ^
postgres=# insert into  department (department_name)
postgres-# values
postgres-# ('CSE'),
postgres-# ('AI'),
postgres-# ('AE'),
postgres-# ('EC'),
postgres-# ('ME');
INSERT 0 5
postgres=# select * from departments
postgres-# ;
ERROR:  relation "departments" does not exist
LINE 1: select * from departments
                      ^
postgres=# select * from departments;
ERROR:  relation "departments" does not exist
LINE 1: select * from departments;
                      ^
postgres=# select * from department;
 department_id | department_name 
---------------+-----------------
             1 | CSE
             2 | AI
             3 | AE
             4 | EC
             5 | ME
(5 rows)

postgres=# create table employee(
postgres(# employee_id serial primary key,
postgres(# employee_name varchar(100),
postgres(# employee_salary int,
postgres(# department_id int references department(department_id);
postgres(# ;
postgres(# );
ERROR:  syntax error at or near ";"
LINE 5: department_id int references department(department_id);
                                                              ^
postgres=# 
postgres=# create table employee(
postgres(# employee_id serial primary key,
postgres(# employee_name varchar(100),
postgres(# employee_salary int,
postgres(# department_id int references department(department_id)
postgres(# );
CREATE TABLE
postgres=# insert into employee (employee_name,employee_salary,department_id)
postgres-# ;
ERROR:  syntax error at or near ";"
LINE 2: ;
        ^
postgres=# insert into employee (employee_name,employee_salary,department_id);
ERROR:  syntax error at or near ";"
LINE 1: ...into employee (employee_name,employee_salary,department_id);
                                                                      ^
postgres=# insert into employee (employee_name,employee_salary,department_id)
postgres-# values
postgres-# ('sac',30000,1),
postgres-# 
postgres-# ('noc',40000,2),
postgres-# 
postgres-# ('roc',50000,3);
INSERT 0 3
postgres=# select * from emloyee;
ERROR:  relation "emloyee" does not exist
LINE 1: select * from emloyee;
                      ^
postgres=# select * from employee;
 employee_id | employee_name | employee_salary | department_id 
-------------+---------------+-----------------+---------------
           1 | sac           |           30000 |             1
           2 | noc           |           40000 |             2
           3 | roc           |           50000 |             3
(3 rows)

postgres=# 
postgres=# 
postgres=# 
