# Terminal emulator :

It is a program that allows us to use the terminal in a graphical way.
<br>
Using Terminal we are able to control our operating system.

# Shell :

It is a command line interface which interprets our commands and tell the os what to do.
<br>
Command prompt is a part of it.

# Linux Terminal Commands

How os knows that where is the file exist :
<br>

```bash
where filename
```

This shows the directory of file.

<br>
Note : whenever we write any commands on the terminal then it's first going to check the $PATH environment variable that does the executable file exists there or not.

<br>
```bash

cat file1.txt | tr a-z A-Z > upper.txt

// Here | means pipe which works like the output from left part and its left will act as input for the command written in right of it.

// Here > means redirection which redirects the output to upper.txt

````
<br>

Note : \(backslash) is used for new line in commands.

<br>

```bash
// To rename a file

mv filename newfile.txt

// Here mv is used to rename a file  but However it is used to move files.

// Note :  while renaming the newfile.txt must not exist in that folder.

// we can also move and rename the file at the same time .

mv file.txt ../file2.txt

// Here file.txt is moved to previous folder and renamed as file2.txt.


````

<br>

```bash

touch folder1/file.txt

// Here file.txt will create  inside folder1.

```

<br>

```bash
du : command used for the disk usage by file of a directory.

```

<br>

```bash
// find the file which is current directory and not in subdirectories :
find . -type f -maxdepth 1


```

<br>

```bash
// delete all the file of type .txt at the same time from the current directory :

find . -type f "*.txt" | -exec rm -rf {} +

// {} all the directory of current folder stored into this placeholder.
// + means all the files in that directory with '.txt' extension.

```

<br>
# File Structure :
There are three types of people who are using your computer :
<br>
1. user : It can be a single person.
<br>
2. Group :   In a group there can be multiple user like sudo which is a group and it typically contains root user and other user having administrative right.

<br>
3. Other
<br>

```bash
// find the files which have all the read write and execute permission:

find . -perm 777

we can use octal number(0-7) while giving the permission to the file.
i.e : 3 = 2 + 1 means write and execute permission

```

<br>

```bash
grep : global regular expression print

// It is used to search for the some text within your file and its case sensitive.

// To search complete word :
grep -w "Mark" file.txt

// here Mark is not a complete word. complete word is Mark Otto.


// To search a word in the current directory .

grep -irwn "Mark" .



```

<br>

```bash
// Regular expression

grep -p "\w" file.txt

// Here '\w' means that all the word(alphabet) in file.txt.

\d = for digit
\d{3} = for digit having 3 character

```

<br>
<br>
```bash

// How to set aliases in bash shell like zprofile in case of zsh.

vim .zprofile

// and then edit it

alias gpom = "git push origin main"

````

<br>

```bash

// we can write multiple commands in a single line by using ';'

git add .; git commit -m "Updated"; git push

````

<br>
<br>
```bash 
In Linux, the id command is used to display information about the user and group IDs associated with a specific user or the current user if no username is provided. It provides details about the UID (User ID), GID (Group ID), and groups the user belongs to.

````

# Stream Editor
The Stream Editor (commonly known as sed) is a powerful text-processing tool in Linux and Unix-based systems. It is used to perform basic and advanced text transformations on a stream of text (e.g., files or input from a pipeline). sed works by reading input line-by-line, applying specified commands, and outputting the result.


# operators
```bash

ping google.com & ping javatpoint.com

& : It is used the first command is running in background and other commands will be executed.
Here a basically a child process is create which is running in background.


echo "first" && echo "Second"

&& : succeding command will be executed only when previous command is executed.



echo "Hello" || echo "world"
|| : succeding command will be executed only when previous command fails.


! : not operator

{} : combination operator

````

# References :

github.com/Kunal-Kushwaha/DevOps-Bootcamp
