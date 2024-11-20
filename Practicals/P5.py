import shutil
def copy_files(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File {source} copied to {destination} file")
    except IOError as e:
        print(f"Error {e}")
source_file ="C://Users//admin//Desktop//Operating-System//Practicals//Test1.txt"
destination_file = "C://Users//admin//Desktop//Operating-System//Practicals//Test2.txt"

copy_files(source_file, destination_file)