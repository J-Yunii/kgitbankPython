create database if not exists member;
commit;
use member;
drop table if exists users;
create table if not exists users(
userid varchar(20) primary key,
userpw varchar(20) not null,
username varchar(20) not null,
userage int,
usermail varchar(20),
useradd varchar(50),
usergender varchar(20),
usertel varchar(20));


insert into users values(
'hong',
'1234',
'홍길동',
23,
'hong@gmail.com',
'부산시 동구 수정동',
'male',
'010-1234-1234');

select * from users;

select version();