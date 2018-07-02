import mysql.connector

try :
    with open('file.txt','r+') as fp:
        for line in fp:
            print(line)
            
            cnx = mysql.connector.connect(user='abc', password='1234',host='120.110.7.27',database='smarttimersocket')
            cursor = cnx.cursor()
            cursor.execute(line)
            cnx.commit()
            cursor.close()
            cnx.close()
        fp.close
        f = open('file.txt','w+')
        f.close
    with open('recored.txt','r+') as rep:
        for line in rep:
            print(line)
            cnx = mysql.connector.connect(user='abc', password='1234',host='120.110.7.27',database='smarttimersocket')
            cursor = cnx.cursor()
            cursor.execute(line)
            cnx.commit()
            cursor.close()
            cnx.close()
        rep.close
        ref = open('recored.txt','w+')
        ref.close
except (IOError, TypeError) as e:
    print ("IOError TypeError:"+str(e))
except Exception as e:
    print("Error:"+str(e))
finally :
    print("Finall")
