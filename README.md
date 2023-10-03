# python_lessons
This repository contains the solutions to the exercises proposed in the Python courses.

- U_python: in this directory are available the codes of both the solved exercises proposed in the Udemy's course "Universidad Python con Frameworks", and other short projects. Some of these projects are described below.


    - 28_project_users_data_layer: in this project, a Data-Access Layer (DAL) was implemented using Python. This DAL was used to access a database managed     through PostgreSQL. The information in the database was contained in a table which consisted of three columns: id_user, username, and password. The         "UserDAO' class was programmed to interact with these columns through CRUD statements. The connection pool, connections, commits, and rollbacks were       managed by the "Connection" and "Cursor_Pool" classes. Finally, users interact with the database from a terminal via both the "list_users.py" script       and the "User" class.
 
    - 76_Django Data-Access Layer: in this project, a Data-Access Layer (DAL) was implemented using Python. This DAL was used to access a database managed through PostgreSQL. The information in the database was contained in a table. A set of classes was programmed to interact with this table through CRUD statements.

    - 84_CRUD_Flask_SQL Customer management system: this system was implemented by combining HTML templates, a web browser and the tools of Django. An alternative version of this project was programmed using Flask. The information of the customers was contained in a table managed through PostgreSQL and CRUD statements.

Tech stack: Python 3.9.6, PostgreSQL 15, Django 4.2.4 and Flask 2.3.3.
