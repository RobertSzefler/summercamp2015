The SQLAlchemy kata
===================


Task 0: Look around
-------------------

Take a look at the SQLAlchemy example_ provided.

.. _example: https://github.com/RobertSzefler/summercamp2015/blob/master/examples/sa_example.py


Task 1: Models
--------------

Write SQLAlchemy model definitions for the two remaining tables in the database. Test
your code with some simple queries, for example::

    print(session.query(Model).count())

You don't need to implement foreign keys at this moment.


Task 2: Defriendizer
--------------------

Write a python script that, for two person names specified on the command line as arguments,
will make them non-friends. This time do it SQLAlchemy-style :)

Tips:

- to delete some rows, just call ``.delete()`` on a query set.
- you need to make sure that either the connection is made in the autocommit mode,
  or you add an explicit commit after the delete operation; otherwise it will be
  rolled back and no change will be applied to the database


Task 3: Get creative
--------------------
