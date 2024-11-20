# Write a program where parent and child execute:
# b) Same program, different code.

import multiprocessing

def parent_task():
    print("Parent executing with its own code.")

def child_task():
    print("Child executing with its own code.")

if __name__ == "__main__":
    print("Parent executing same program with different code.")

    # Create a child process
    child_process = multiprocessing.Process(target=child_task)
    child_process.start()
    child_process.join()  

    
    parent_task()

        