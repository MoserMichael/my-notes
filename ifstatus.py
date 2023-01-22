#!/usr/bin/env python

import sys
import os


status=int(sys.argv[1]);

print(f"Exit status: {status}")

# info from: https://docs.python.org/3/library/os.html

if os.WIFEXITED(status):
    print(f"process exited. with exit status: {os.WEXITSTATUS(status)}\n")

if os.WIFSTOPPED(status):
    print(f"process stopped by delivery of signal. signal number: { os.WSTOPSIG(status) }\n")


if os.WIFSIGNALED(status):
    print(f"process terminated by signal. signal number: { os.WTERMSIG(status) } core dumped: {os.WCOREDUMP(status)}\n")
