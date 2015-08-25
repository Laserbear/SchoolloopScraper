import requests

username = raw_input("Username:\n")
password = raw_input("Password:\n")
school = raw_input("School specific login URL")

payload = {
    'inUserName': username,
    'inUserPass': password
}

with requests.Session() as s:
    p = s.post(school, data=payload)
    # print the html returned to see if it's a successful login page.
    print p.text

    r = s.get(school) #getting a bad request error here
    print r.text
        
