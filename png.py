#!/usr/bin/env python

import socket
import sys

try:
    res = socket.gethostbyname(sys.argv[1]);
    print(f"socket.gethostbyname({sys.argv[1]}) : {res}")
except Exception as ex:
    print(f"Failed to resolve {sys.argv[1]}. error: {ex}")
    exit(1)
