#!/usr/bin/env.python3

import requests 

start, end = 0, 100

for num in range(start, end + 1):
	if num % 2 != 0:
		api_key = num
		html = requests.get(f'http://10.10.69.122:8000/api/{api_key}')
		new = html.text
		if 'error' not in new:
			print(new)
