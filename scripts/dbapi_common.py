from MySQLdb import connect

conn = connect('localhost', user='test', passwd='test', db='test')

def cursor():
    return conn.cursor()
