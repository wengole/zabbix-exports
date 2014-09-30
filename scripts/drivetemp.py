#!/bin/env python2
import sys
import subprocess
import re

device = sys.argv[1]
output = subprocess.check_output(['nc', 'localhost', '7634'])
match = re.search(r'%s\|(?P<serial>[a-zA-Z0-9_-]+)\|(?P<temp>\w+)\|(?P<unit>\w+).*' % device, output)
if match is not None:
    matchdict = match.groupdict()
print matchdict['temp']
