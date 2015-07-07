from sa_common import session, engine


def some_db_operations():
    result = engine.execute('SELECT COUNT(*) FROM test')
    print list(result)


with session.begin_nested():
    some_db_operations()
