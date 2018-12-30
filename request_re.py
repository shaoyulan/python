import re,requests
Re = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+')
url = 'https://www.grantthornton.tw/meet-our-people/'
html = requests.get(url)
emails = Re.findall(html.text)
for email in emails:
	print(email)

# ok 
