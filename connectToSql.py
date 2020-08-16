import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WDQ3NJNFVV\SQLEXPRESS;'
                      'Database=zy38db;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM zy38db.dbo.sender')

for row in cursor:
    print(row)

'''
sql = 'exec [my_database].[dbo].[my_table](?, ?, ?, ?, ?, ?, ?, ?)'
values = (id_, pw, depart, class_, name, birthday, grade, subgrade)

cursor.execute(sql, (values))
'''

sql = 'exec [zy38db].[dbo].[sp_get_risom]'
#  values = (id_, pw, depart, class_, name, birthday, grade, subgrade)

print(cursor.execute(sql))