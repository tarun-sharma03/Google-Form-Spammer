import sys
import http.client
from faker import Faker

fake=Faker()

def post(link,num,faker):
	form_entry=['']
	form_entry_data=['']
	payload="------WebKitFormBoundary7MA4YWxkTrZu0gW"

	if (faker==0):
		choice='y'
		while(choice=='y'):
			print("Enter form data entry: ")
			form_entry.append(raw_input())
			print("Enter the value:	")
			form_entry_data.append(raw_input())
			print("Add more entries?(y/N)")
			choice=raw_input()
		for i in range(len(form_entry)):
			if(i==0):
				continue
			payload+="\r\nContent-Disposition: form-data; name=\""+str(form_entry[i])+"\"\r\n\r\n"+str(form_entry_data[i])+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW"
		
	

	elif (faker==1):
		choice='y'
		while(choice=='y'):
			print("Enter form data entry: ")
			form_entry.append(raw_input())
			print("Choose the type of value:	\n(name,number,email,address,none)")
			form_entry_data.append(faker_input(raw_input()))
			print("Add more entries?(y/N)")
			choice=raw_input()
		for i in range(len(form_entry)):
			if(i==0):
				continue
			payload+="\r\nContent-Disposition: form-data; name=\""+str(form_entry[i])+"\"\r\n\r\n"+str(form_entry_data[i])+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW"
	payload+="--"
	conn = http.client.HTTPSConnection("docs.google.com")

	headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'postman-token': "f7281180-f919-b589-709a-a77457e89d08"
    }
	print("Sending")
	for x in range (num):
		conn.request("POST", "/forms/u/0/d/e/"+link+"/formResponse", payload, headers)
		res = conn.getresponse()
		data = res.read()
		print('.')

	if(len(data)>100):
		print('Successful!')
	else:
		print('ERROR!!')	


def faker_input(type):
	if(type=="name"):
		name=fake.name()
		print(name)
		return fake.name()
	else:
		print("Enter the value:	")
		return raw_input()
	

argument=sys.argv
faker=0
link='wrong input'
num=0
help_flag=0

def help():
	faker=0

for i in range(len(argument)):
	if(argument[i]=='-h' or argument[i]=='--help'):
		help()
		help_flag=1
		break
	if(argument[i]=='-l'):
		i=i+1
		link=argument[i]
	if(argument[i]=='-n'):
		i=i+1
		num=int(argument[i])
	if(argument[i]=='-f'):
		faker=1

if(help_flag==0):
	post(link,num,faker)


	
