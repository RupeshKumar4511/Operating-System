# Terminal emulator :

It is a program that allows us to use the terminal in a graphical way.
<br>
Using Terminal we are able to control our operating system.

# Shell :

It is a command line interface which interprets our commands and tell the os what to do.
<br>
Command prompt is a part of it.

```bash

// How to check the shell type :
echo $0


```

# Shell Scripting :

shell scrips consists of set of commands to perform a task .
All the commands are executed sequentially .
Some task like file manipulation, program execution, user interaction and automation can be done.
<br>

```bash

#!bin/bash   //This is called shebeng and it is recommended to write not necessary. after this we can write our script.

echo "hello world"


// To execute a script jush write script_file_name.sh


// for Comments :
# This is single line comment 

<<comment  -> In place of comment we can use other words and same word is used in the end to end the comment.

    
Multilines comments here  


comment





// Variables 

var_name=value        // no space between equal to sign

// to store a defined variable into other variable 

var_name = $(hostname)

// to print a variable 

echo $var_name 


// constant variable 
readonly var_name = "Constant Value"


// take input from user 

read varname

or 

read -p "What is your name " name_variable 


// if-else statement 

age = 18 
if[$age -eq 18]
then 
echo "You can vote.."
elif [$age -gt 18]    # -gt means greater than 
echo "You can vote.."
else
echo "You cannot vote.."

fi -> here 'fi' is written to end the if-else statement 

```
<br>

```bash
// Comparison operators :

Operator	Description
-eq	Equal to
-ne	Not equal to
-lt	Less than
-le	Less than or equal to
-gt	Greater than
-ge	Greater than or equal to

```



<br>

```bash  
//check file exist or not 

if [ -d folder_name ] // check folder exist 
if [ ! -d folder_name] // check folder does not exist.

if [ -f file_name ] // check file exist 
if [ ! -f file_name] // check file does not exist.

```
<br>


<br>
```bash 

// switch case 

echo "Enter Your options : "
echo " a = To see the current date"
echo "b = To see the files in the current directory"


read choice 

case $choice in 
    a) date;;
    b) ls;;
    *) echo "Not a valid input";;


esac 

```
<br>
<br>

```bash 

// for loops in shell 

for i in {1..20}
do 
echo "Number is $i"
done

or 


for j in 1 2 3 4 5


or 


for p in Hello Python World 

// each word is takes as one element 



// we can iterate each word of any file 

items = "/home/admin/file.txt"
for i in $(cat $items)
do 
echo $i 
done 


```

<br>
<br>

```bash 
// while loop 
count=0
num=10
while [ $count -le $num ]   // remember the space between while and []
do 
echo "Numbers are $count"
let count++ 
done



while true 
do 
 
# infine loop 

done 




# we can use 'break' and 'continue' statement . 
```

<br>
<br>

```bash 
# until loop : It will execute until the condition is false . 

count=0
num=10
until [ $count -le $num ]
do 
echo "Numbers are $count"
let count++ 
done

```

<br>
<br>

```bash 

# we can use the expression 
a=23
let a++
let a=a*2
echo $a

```

```bash 
# To print the name of script 
echo "Name of the script {0}" 
```

<br>
<br>

```bash 
# function defined and call 

function_name(){
    echo "Hello function"
    
    # set a local variable 
    local first=$1
    local second=$2
    echo $first $second
    }



    # call a function 
    
    function_name 12 30

# we can pass arguments to the functions.



```

<br>
<br>

```bash 
# Bash Variables 
echo $RANDOM => A random integer between 0 and 32767 is generated. 

echo $UID => User id of logged in . 

```

<br>
<br>

```bash 
# if we dont want to print the output of a command on terminal or write a file then we can use 

/dev/null 
```


<br>
<br>

```bash 
# Important commands :

sleep : To create delay between execution . ex : sleep 1s or 1m 

exit : To stop a script at a point . 


exit status $? : It gives the status of previous commands if that was successful. 


# If we want to maintain the logging for your script then we can use logger in our script . 

// we can find the logs under 
/var/logs/messagses

In the script : #logger "Hello world"

It is used for the administrative purpose.



# Debugging 

If we want to debug the script then we can use the commands :

set -x  

It is written after the shebeng.

```





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

# Vim : Inline Editor

Here's a list of essential Vim commands, organized by category:

Basic Navigation
h - Move left
l - Move right
j - Move down
k - Move up
0 - Move to the beginning of the line
^ - Move to the first non-whitespace character of the line
$ - Move to the end of the line
gg - Go to the beginning of the file
G - Go to the end of the file
:n - Go to line n (e.g., :5 goes to line 5)
Ctrl-d - Scroll down half a screen
Ctrl-u - Scroll up half a screen
Modes
i - Insert mode (enter text)
Esc - Exit to normal mode
v - Visual mode (select text)
V - Visual line mode (select entire lines)
Ctrl-v - Visual block mode (select block of text)
R - Replace mode
Editing
x - Delete the character under the cursor
dd - Delete the current line
dw - Delete from the cursor to the end of the word
d$ - Delete from the cursor to the end of the line
u - Undo the last change
Ctrl-r - Redo
p - Paste the last yanked or deleted text after the cursor
P - Paste before the cursor
yy - Yank (copy) the current line
yw - Yank the current word
y$ - Yank from the cursor to the end of the line
Search and Replace
/pattern - Search forward for "pattern"
?pattern - Search backward for "pattern"
n - Repeat the last search in the same direction
N - Repeat the last search in the opposite direction
:%s/old/new/g - Replace all occurrences of "old" with "new" in the file
:n,m s/old/new/g - Replace "old" with "new" from line n to m
File Operations
:w - Save (write) the file
:q - Quit Vim
:wq - Save and quit
:q! - Quit without saving
:e filename - Open a file
:split filename - Open a file in a new horizontal split
:vsplit filename - Open a file in a new vertical split
Window Management
Ctrl-w s - Split window horizontally
Ctrl-w v - Split window vertically
Ctrl-w w - Switch between windows
Ctrl-w q - Close the current window
Buffer Management
:bnext or :bn - Go to the next buffer
:bprev or :bp - Go to the previous buffer
:bd - Close the current buffer
Miscellaneous
. - Repeat the last command
% - Jump to the matching parenthesis, bracket, or brace
:set number - Show line numbers
:set nonumber - Hide line numbers
:set wrap - Enable line wrapping
:set nowrap - Disable line wrapping

# References :

github.com/Kunal-Kushwaha/DevOps-Bootcamp
