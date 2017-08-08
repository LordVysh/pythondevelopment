from collections import ChainMap
default_connection = {'host': 'localhost', 'port': 80210}
connection = {'port': 90210}
conn = ChainMap(connection, default_connection)
print(conn['port'])
print(conn['host'])
print(conn.maps)
conn['host'] = 'irascent.com'
print(conn.maps)
del conn['port']
print(conn.maps)
print(conn['port'])
print(dict(conn))
