#!/bin/env python2
import sys
import re
import subprocess

bus = sys.argv[1]
probe = sys.argv[2]

output = subprocess.check_output(['sensors', '-u', bus])
match = re.search(r'%s_input:\s(?P<value>\d+.\d+).*' % probe, output)
if match is not None:
    matchdict = match.groupdict()
    print matchdict['value']



