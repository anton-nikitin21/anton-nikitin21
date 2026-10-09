create table OTZOV(

LOGIN_CLIENT nvarchar(100) not null,

grade int not null check (grade >= 0 and grade <= 5),

ARTICLES int foreign key references PRODUCTS (ARTICLES),

comment nvarchar(2000),

)