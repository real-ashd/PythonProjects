#Install the module mysql with cmd 'pip3 install mysql-connector-python'
import mysql.connector

con= mysql.connector.connect(
user='ardit700_student',
password='ardit700_student',
host='108.167.140.122',
database='ardit700_pm1database'
)

cursor = con.cursor()

print("Dictionary using mysql database by @real_ashd\n")
q=0
while q!='q':
    word = input('Enter Word : ')
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'"% word)
    results = cursor.fetchall()
    if results:
        for result in results:
            print(result[1])
    else:
        print("No word found!")
    print('------------------------------------------------------------------')
    q=input("\nEnter q to quit the program or press any other key to search another word : ")
    q=q.lower()