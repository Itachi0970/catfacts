from urllib.request import urlopen
import json
from time import time, sleep

url = 'https://catfact.ninja/fact'
output = 'catfactoutput.txt'

while True:
	response = urlopen(url)

	data = json.loads(response.read())

	file = open(output, 'a')
	file.write("Fact: " + data['fact'] + "\n")
	file.write("Length: " + str(data['length']) + "\n")
	file.close()
	print(time())
	sleep(60 - time() % 60)