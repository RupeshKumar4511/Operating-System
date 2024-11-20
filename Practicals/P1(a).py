# Write a program where parent and child execute:
# a) Same program, same code.

import multiprocessing


def child_process():
    print("child process executing the same program with same code..")

def parent_process():
    process = multiprocessing.Process(target= child_process)
    process.start()
    process.join()

    print("Parent proces executing the same program with same code..")

if __name__ == "__main__":
   parent_process()