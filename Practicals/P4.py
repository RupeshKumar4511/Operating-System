import os
import stat
import time

def file_details(file_path):

    try:
        file_stat = os.stat(file_path)
        file_owner = file_stat.st_uid
        file_access = stat.filemode(file_stat.st_mode)
        access_time = time.ctime(file_stat.st_atime)
        print(f"{file_path}")
        print(f"file_owner : {file_owner}")
        print(f"file_access :  {file_access}")
        print(f"file_access time : {access_time}")

    except FileNotFoundError:
        print("file does not exist")
    except Exception as e:
        print(f"Error : {e} ")

file_path = "./Practicals/Test1.txt"
file_details(file_path)
     