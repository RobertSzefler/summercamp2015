Task 0: Look around
-------------------

Log in to the freshly created mysql database using the command-line `mysql` utility::

    mysql -u test --password=test test

Take a look at how the database is organized. You can start with listing all tables:

    SHOW TABLES;

For each table, you can obtain information about its structure using::

    EXPLAIN table_name;

(the short form), or::

    SHOW CREATE TABLE table_name;

(for the full `CREATE TABLE` statement - includes foreign key information etc).


Task 2: Lone persons
--------------------

Write a `SELECT` query that lists the names of persons that don't have friends.

Tips:

- SQL `SUM` operator might come in handy


Task 3: ?
---------

TODO
