# -*- coding: utf-8 -*-

import requests
i=0;

while(1):
	url = 'https://docs.google.com/forms/d/e/1FAIpQLSfqr5KTf9VZ4zOh3OjwmWUuoM3Qsh96SNuPOuElzJSfQHl-Qw/formResponse'

	form_data = {
		'entry.1129185899'	:	'Sim',
		'entry.1742382206'	:	'R$00,00 - R$50,00',
		'entry.1716037067'	:	'SMS',
		'entry.1981569101'	:	'Televisão',
		'entry.2070244210'	:	'Nunca',
		'entry.1361771801'	:	'Sim'
		}
		
	user_agent ={
		'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSfqr5KTf9VZ4zOh3OjwmWUuoM3Qsh96SNuPOuElzJSfQHl-Qw/viewform',
		'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"
		}
		
	r = requests.post(url, data=form_data, headers=user_agent)
	i=i+1
	
	print('%s - Total Count = %i' %(r, i))
