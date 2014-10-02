#!/bin/env python2
import sys
import requests

apikey = sys.argv[1]
subject =sys.argv[2]
message = sys.argv[3]

params = {
    'apikey': apikey,
    'application': 'Zabbix',
    'event': subject,
    'description': message,
    'priority': 0,
}
r = requests.post('https://www.notifymyandroid.com/publicapi/notify')

print subject
print message
print r.status_code