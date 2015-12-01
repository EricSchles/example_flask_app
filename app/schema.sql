drop table if exists ip_logger;
    create table Data (
    id integer primary key autoincrement,
    data text not null,
    timestamp text not null
);