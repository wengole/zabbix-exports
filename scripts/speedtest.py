#!/bin/env python2
import subprocess
import re
import sys

output = subprocess.check_output(['speedtest-cli', '--simple'])
m = re.search(r'Ping:\s(?P<ping>\d+\.\d+)\sms\s+Download:\s(?P<download>\d+.\d+)\sMbits/s\s+Upload:\s(?P<upload>\d+.\d+)\sMbits/s', output)
if m is not None:
    md = m.groupdict()
    subprocess.call(['zabbix_sender', '-c', '/etc/zabbix/zabbix_agentd.conf', '-z', 'localhost', '-s', 'SAN', '-k', 'speedtest.ping', '-o', md['ping']])
    subprocess.call(['zabbix_sender', '-c', '/etc/zabbix/zabbix_agentd.conf', '-z', 'localhost', '-s', 'SAN', '-k', 'speedtest.upload', '-o', md['upload']])
    subprocess.call(['zabbix_sender', '-c', '/etc/zabbix/zabbix_agentd.conf', '-z', 'localhost', '-s', 'SAN', '-k', 'speedtest.download', '-o', md['download']])

