create table tovar(

	naim varchar(450) not null,

	opt numeric(10,2),

	rozn int,

	opisanie varchar(350),

	art int identity primary key,

	kolichestvo varchar (1000),

	id int foreign key references postav(id)

	)