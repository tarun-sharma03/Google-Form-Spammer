A python script to spam the Google form with fake data. 

usage: python formspam.py [-h] | [-l] link | [-n] number | [-f]

arguments:
-h, --help                      show this help message and exit
-l                              specify the link of the google form(https://docs.google.com/forms/d/{link}/viewform)
-n                              specify the number of forms you want to send
-f                              faker mode on
faker mode: Send mixed data just by specifying the type of data in the input field.
example: python formspam.py -l link -n 100 -f

How to fill entry field:
Step 1: Open the Google form you want to spam.
Step 2: Fill up the form entirely with any value, don't submit yet.
Step 3: Go to inspect.(Right Click>Inspect)
Step 4: Go to Network tab in the drawer.
Step 5: Now submit the form.
Step 6: Open the formResponse and scroll down to Form Data
Step 7: Entry fields are available there in form of entry.{something}
Step 8: Copy entry.{something} and paste in this program one by one.

Where this thing won't work: Forms which require Google login.