import pprint

import pymysql
cnx = pymysql.connect(user='axv6458', password='Terrorblade91+',
                          host='acadmysqldb001p.uta.edu',
                          database='axv6458')
cursor = cnx.cursor()
if cursor:
    print("successsfully connected")

def insert_useracc():
        x = input("enter username:")
        y = input("enter phone:")
        z = input("rolename:")

        query = ("insert into User_Acc (username, phone, RoleName) values (%s,%s,%s);")
        data = (x, y, z)

        cursor.execute(query, data)

        print("database updated")

        cnx.commit()

# insert_useracc()

def retrieve_useracc():

        query = ("select * from User_Acc;")

        cursor.execute(query)
        columns = cursor.description
        result = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
        print("--------------User Accounts-------------")
        for x in result:
            print(x)



        cnx.commit()

# retrieve_useracc()

def insert_role():
        x = input("enter rolename:")
        y = input("enter role description:")


        query = ("insert into User_Roles values (%s,%s);")
        data = (x, y)
        cursor.execute(query, data)

        print("database updated")

        cnx.commit()
# insert_role()

def retrieve_roles():

        query = ("select * from User_Roles;")

        cursor.execute(query)
        columns = cursor.description
        result = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
        print("--------------Roles-------------")
        for x in result:
            print(x)


        cnx.commit()
# retrieve_roles()

def retrieve_tables():

        query = ("select * from Tables;")

        cursor.execute(query)
        columns = cursor.description
        result = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
        print("--------------Tables-------------")
        for x in result:
            for y in x:
                if y == 'UserID':

                    print('%s' % x.get('UserID'), 'is owener of table ', x)

        # pprint.pprint(result)



        cnx.commit()
# retrieve_tables()

def insert_tables():
            x = input("enter  new table name:")
            y = input("enter role userID(this will be the owener of the table):")
            z = input("enter role name(which already exist)")


            query = ("insert into Tables values (%s,%s, %s);")
            data = (x, y, z)
            cursor.execute(query, data)

            print("database updated")

            cnx.commit()
# insert_tables()

def insert_privilages():
    x = input("enter select privilege (yes/or)")
    y = input("enter update privilege (yes/or)")
    z = input("enter delete privilege (yes/or)")
    p = input("enter create tab privilege (yes/or)")
    q = input("enter for which userID these privileges apply")
    if x == 'yes' and y == 'yes' and z == 'yes' and p == 'yes':
        r = 'dev'
    if x == 'yes' and y == 'no' and z == 'no' and p == 'yes':
        r = 'admin'
    if x == 'no' and y == 'no' and z == 'no' and p == 'no':
        r = 'client'

    print("if all privilages are granted the privilage is taken as account privilage else relation privilage")

    query = ("insert into Privilages values (%s,%s, %s, %s, %s, %s);")
    data = (x, y, z, p, q, r)
    cursor.execute(query, data)

    print("database updated")

    cnx.commit()
# insert_privilages()

def retrieve_privilages():

        query = ("select * from Privilages;")

        cursor.execute(query)
        columns = cursor.description
        result = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
        print("--------------Privilages-------------")
        for x in result:
            print(x)
        cnx.commit()

# retrieve_privilages()
while True:
    print("1: view UserAcc \n2: view roles \n3: view privilages \n4: view tables \n5: insert into UserAcc \n6: insert into roles \n7: insert into privilages \n8: insert into tables \n 9:exit loop")
    a = int(input("enter option:"))

    if a == 1:
        retrieve_useracc()
    elif a == 2:
        retrieve_roles()
    elif a == 3:
        retrieve_privilages()
    elif a == 4:
        retrieve_tables()
    elif a == 5:
        insert_useracc()
    elif a == 6:
        insert_role()
    elif a == 7:
        insert_privilages()
    elif a == 8:
        insert_tables()
    else:
        break

#3.5
print("3.5")
query = ("select * from User_Acc, User_Roles where RoleName = Role_Name order by UserId;")
cursor.execute(query)
columns = cursor.description
result = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]

for x in result:
            print(x)
cnx.commit()
#3.6
query = ("select * from Account_Privileges, User_Roles where Rolename = Role_Name")
cursor.execute(query)
columns = cursor.description
result = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
print("\n\n\n3.6")
for x in result:
            print(x)
cnx.commit()
#3.7
query = ("select * from Relation_privilages A, User_Roles U, Tables T where A.Rolename = U.Role_Name and U.Role_Name = T.Rolename")
cursor.execute(query)
columns = cursor.description
result = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
print("\n\n\n3.7")
for x in result:
            print(x)
cnx.commit()
#3.8
query = ("select * from Privilages where RoleNmae = 'dev'")
cursor.execute(query)
columns = cursor.description
result = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
print("\n\n\n3.8a")
for x in result:
            print(x)
cnx.commit()

query = ("select * from Privilages where UserID = 5")
cursor.execute(query)
columns = cursor.description
result = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
print("\n\n\n3.8b")
for x in result:
            print(x)
cnx.commit()
query = ("select * from Privilages")
cursor.execute(query)
columns = cursor.description
result = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
print("\n\n\n3.8c")

for x in result:
            print(x)
cnx.commit()