create schema if not exists sorteo;

use sorteo;

drop table if exists users;

create table if not exists users (
	id INT(11) unsigned auto_increment not null,
    nombre varchar(5) not null,
    pass varchar(45) not null,
    created_at timestamp not null default CURRENT_TIMESTAMP,
    updated_at timestamp not null default current_timestamp on update current_timestamp,
    deleted_at timestamp null default null,
    primary key(id)
);

drop table if exists semanas;

create table if not exists semanas (
		id int(11) unsigned auto_increment not null,
        fechaInicio date not null,
        fechaFin date not null,
        estado_id int(1) not null,
        created_at timestamp not null default CURRENT_TIMESTAMP,
		updated_at timestamp not null default current_timestamp on update current_timestamp,
        deleted_at timestamp null default null,
        primary key(id)
);

drop table if exists premios;

create table if not exists premios (
	id int(11) unsigned auto_increment not null,
    semana_id int(11) unsigned not null,
	fecha date not null,
    numero int(11) unsigned not null,
    color varchar(1) not null,
    descripcion varchar(100) default '',
    obsequiado datetime default null,
    created_at timestamp not null default CURRENT_TIMESTAMP,
    updated_at timestamp not null default current_timestamp on update current_timestamp,
    deleted_at timestamp null default null,
    primary key(id)
);

drop table if exists pulsaciones;

create table if not exists pulsaciones (
	id int(11) unsigned auto_increment not null,
    dia date not null,
    pulsacion int(11) unsigned not null,
    premio_id int(11) unsigned default null,
    created_at timestamp not null default CURRENT_TIMESTAMP,
    updated_at timestamp not null default current_timestamp on update current_timestamp,
    primary key(id)
);

drop table if exists parametros;

create table if not exists parametros (
	id int(10) unsigned auto_increment not null,
    `password` varchar(255) default null,
    puerto varchar(50) default null,
    primary key(id)
);

