Task 0: Look around
-------------------

Log in to the freshly created mysql database using the command-line `mysql` utility::

    mysql -u test --password=test test

Take a look at how the database is organized. You can start with listing all tables::

    SHOW TABLES;

For each table, you can obtain information about its structure using::

    EXPLAIN table_name;

(the short form), or::

    SHOW CREATE TABLE table_name;

(for the full `CREATE TABLE` statement - includes foreign key information etc).

You can then take a look at the simple template for writing solutions to the exercises.
It just contains some boiler plate code to connect with the db etc. It's here_.

.. _here: https://github.com/RobertSzefler/summercamp2015/blob/master/dbapi_kata_template.py

Task 1: Lone persons
--------------------

Write a python script that lists the names of persons that don't have friends, in
alphabetic order.

Tips:

- ``UNION`` is your friend
- a subquery is OK
- maybe use a ``LEFT JOIN`` as an alternative?


Task 2: Account statistics
--------------------------

Write a python script that lists the names of persons that have below-average
account balances, together with their balances.

Tips:

- you will need a ``JOIN``
- average is just ``AVG`` :)


Task 3: FOAF 
------------

Write a python script that, for a person name specified on the command line as the
sole argument, will find the richest person between friends-of-a-friend of that
specified person.

Tips:

- sometimes you just need more than one ``JOIN``
- for simplicity you can assume that the "friends" relation is one way only, ie that
  you find a person's friends by select rows from the ``friends`` table with a match on
  ``person1_id`` only


Task 4: Defriendizer
--------------------

Write a python script that, for two person names specified on the command line as
arguments, will make them non-friends.
