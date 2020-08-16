import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WDQ3NJNFVV\SQLEXPRESS;'
                      'Database=zy38db;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

GET_RESHUM = "exec [dbo].[sp_get_risom] N'{}';"



def select_all_in_sql():
    cursor.execute('SELECT * FROM zy38db.dbo.sender')
    for row in cursor:
        print(row)


def get_reshum(typ):
    cursor.execute(GET_RESHUM.format(typ))
    text = ''
    for row in cursor:
        print(row[0])
        text += row[0]
        text += "\n"
    return text


'''
sql = 'exec [my_database].[dbo].[my_table](?, ?, ?, ?, ?, ?, ?, ?)'
values = (id_, pw, depart, class_, name, birthday, grade, subgrade)

cursor.execute(sql, (values))
'''

# sql2 = 'exec [zy38db].[dbo].[sp_get_risom](?)'
# values = ('עזרה')
#  values = (id_, pw, depart, class_, name, birthday, grade, subgrade)

