-- Schema for example to-do app

-- Projects - it os high level operations, how do with
create table project (
	name        text primary key,
	description text,
	deadline    date
);

-- Problems - it is steps, how be need complete
-- for complicated project
create table task (
	id           integer primary key autoincrement not null,
	priority     integer default 1,
	details text,
	status text,
	deadline date,
	completed_on date,
	project text not null references project(name)
);
