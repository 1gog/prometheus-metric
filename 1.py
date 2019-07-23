#!/usr/bin/env python

import subprocess
import sys

a = subprocess.run(["ps", "-heo", "pid,%cpu,%mem", "-q"])
ps -heo pid,%cpu,%mem -q $1
