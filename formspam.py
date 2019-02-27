import sys
import http.client
from faker import Faker

fake=Faker()
fake_IN=Faker('hi_IN')

def post(link,num,faker):
	form_entry=['']
	form_entry_data=['']
	payload="------WebKitFormBoundary7MA4YWxkTrZu0gW"

	if (faker==0):
		choice='y'
		while(choice=='y'):
			print("Enter form data entry: ")
			form_entry.append(input())
			print("Enter the value:	")
			form_entry_data.append(input())
			print("Add more entries?(y/N)")
			choice=input()
		for i in range(len(form_entry)):
			if(i==0):
				continue
			payload+="\r\nContent-Disposition: form-data; name=\""+str(form_entry[i])+"\"\r\n\r\n"+str(form_entry_data[i])+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW"
		conn = http.client.HTTPSConnection("docs.google.com")
		
		payload+="--"

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
		
	

	elif (faker==1):
		choice='y'
		while(choice=='y'):
			print("Enter form data entry: ")
			form_entry.append(input())
			print("Choose the type of value:	\n(name,number,email,word,sentence,or enter the value)")
			form_entry_data.append(input())
			print("Add more entries?(y/N)")
			choice=input()
		
		conn = http.client.HTTPSConnection("docs.google.com")

		headers = {
	    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
	    'cache-control': "no-cache",
	    'postman-token': "f7281180-f919-b589-709a-a77457e89d08"
	    }
		print("Sending")
		for x in range (num):
			payload_ls="------WebKitFormBoundary7MA4YWxkTrZu0gW"
			for i in range(len(form_entry)):
				if(i==0):
					continue
				payload_ls+="\r\nContent-Disposition: form-data; name=\""+str(form_entry[i])+"\"\r\n\r\n"+str(faker_input(form_entry_data[i]))+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW"
			payload_ls+="--"
			print(payload_ls)
			conn.request("POST", "/forms/u/0/d/e/"+link+"/formResponse", payload_ls, headers)
			res = conn.getresponse()
			data = res.read()
			print('.')

		if(len(data)>100):
			print('Successful!')
		else:
			print('ERROR!!')

	
def help():
	print("usage: python formspam.py [-h] | [-l] link | [-n] number | [-f]")
	print("")
	print("arguments:")
	print("-h, --help			show this help message and exit")
	print("-l				specify the link of the google form(https://docs.google.com/forms/d/<link>/viewform)")
	print("-n				specify the number of forms you want to send")
	print("-f				faker mode on")
	print("faker mode: Send mixed data just by specifying the type of data in the input field.")
	print("example: python formspam.py -l link -n 100 -f")
	print("")
	print("How to fill entry field:")
	print("Step 1: Open the Google form you want to spam.")
	print("Step 2: Fill up the form entirely with any value, don't submit yet.")
	print("Step 3: Go to inspect.(Right Click>Inspect)")
	print("Step 4: Go to Network tab in the drawer.")
	print("Step 5: Now submit the form.")
	print("Step 6: Open the formResponse and scroll down to Form Data")
	print("Step 7: Entry fields are available there in form of entry.<something>")
	print("Step 8: Copy entry.<something> and paste in this program one by one.")


def faker_input(type):
	if(type=="name"):
		return fake.name()
	if(type=="number"):
		return fake.msisdn()
	if(type=="word"):
		return fake.word()
	if(type=="sentence"):
		return fake.sentence()
	if(type=="email"):
		return fake.email()
	else:
		return type
	

argument=sys.argv
faker=0
link='wrong input'
num=0
help_flag=0
faker=0

for i in range(len(argument)):
	if(argument[i]=='-h' or argument[i]=='--help'):
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


if(num==0 and help_flag==0):
	print("usage: python formspam.py [-h] [-l | -n | -f]")

elif(help_flag==1):
	help()

else:
	post(link,num,faker)
