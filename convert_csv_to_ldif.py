from ldap3 import Connection, STRATEGY_LDIF_PRODUCER, MODIFY_ADD, MODIFY_REPLACE, MODIFY_DELETE
import csv
__author__ = 'jacopo'

with open("ldap.csv", 'r', ) as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_ALL)
    for row in reader:
        connection = Connection(server=None, client_strategy=STRATEGY_LDIF_PRODUCER)
	#Il metodo add() inserisce in "connection.response" un file .ldif         
        connection.add("cn="+row[1]+",ou=People,dc=bho,dc=it","person" ,{'objectClass':'inetOrgPerson','o':row[0],'sn':row[1],'cn':row[1], 'description':row[2], 'telephoneNumber': row[3], 'fax': row[4], 'mail': row[5]})
        stampa = connection.response
        print(str(stampa))
        print("\n")
f.close()
