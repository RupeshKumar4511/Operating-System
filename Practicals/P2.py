# Write a program where parent and child execute:
# b) Same program, different code.

import multiprocessing


def child_task():
    print("child process executing the same program with same code..")

def parent_task ():
    print("parent process executing the same program with same code..")

        