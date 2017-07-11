#!/usr/bin/env python

import os
import time

while True:
    try:
        time.sleep(5)
        os.system("echo 'hello'")
    except:
        continue


