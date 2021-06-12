#DictionaryWithMySqlv1.1
#Install the module mysql with cmd 'pip3 install mysql-connector-python'
import mysql.connector
from difflib import get_close_matches

con= mysql.connector.connect(
user='ardit700_student',
password='ardit700_student',
host='108.167.140.122',
database='ardit700_pm1database'
)

cursor = con.cursor()
print("Dictionary using mysql database version 1.1 by @real_ashd")
def getAllWords():
	query=cursor.execute("SELECT Expression FROM Dictionary")
	data = cursor.fetchall()
	datalist = []
	for t in data:
		for x in t:
			datalist.append(x)
	return datalist

# print(getAllWords())
def checkWord(w):
	data = getAllWords()
	if w in data:
		cursor.execute('SELECT * FROM Dictionary WHERE Expression="%s"'% w)
		return cursor.fetchall()
	elif len(get_close_matches(w,data)) > 0:     #Checking the closest match of the word entered
		yn = input("Did you mean %s instead?\nEnter Y if yes or N if No: " % get_close_matches(w, data)[0])
		if yn.lower() == 'y':
			cursor.execute('SELECT * FROM Dictionary WHERE Expression="%s"'% get_close_matches(w, data)[0])
			print("The definition of",get_close_matches(w, data)[0],"is:")
			return cursor.fetchall()
		elif yn.lower() == 'n':
			return "The word doesn\'t exist. Please double check it."
		else:
			return "Invalid input. Please try again."
	else:
		return "The word doesn\'t exist. Please double check it."
q=0
while q!='q':
	word = input('Enter Word : ')
	results=checkWord(word)


	if type(results) != list:
		print(results)
	else:
		if results:
			for result in results:
				print(result[1])
		else:
			print("No word found!")
	print('------------------------------------------------------------------')

	
	q=input("\nEnter q to quit the program or press any other key to search another word : ")
	q=q.lower()