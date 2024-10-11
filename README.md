# Operating-System

Operating System is a system software which manages hardware and software resources of the computer system.It acts as interface between user and hardware resources. OS works on System Calls.

# Primary Goal :
1) Convenience 
<br>

2) Throughput : It is the no of execution executed per unit time.
<br>

Note : At present Linux has best throughput as compared to other os.


# Functionality Of OS :
1. Resource Management: (hardware management like managing cpu)
<br>

2. Process Management: (cpu scheduling)
<br>

3. Storage Management :(File System )
<br>

4. Memory Management : (RAM , multitasking)
<br>

5. Security and Privacy : (Admin Password)


# Types of Operating System :
1. Batch Os : In this os , similar types of jobs were batched together and executed in time.The system put all of the jobs in a queue on the basis of first come first serve and then executes the jobs one by one.
<br>

Note : Each process needs two types of system time: CPU time and IO time.
<br>
Note : Program on execution is called as process.

2. Multiprogramming os : In this os , there are n no of instructions are stored in RAM and when the first process is either completed or go for I/O then in this conditions cpu goes to proeces another instructions.   

<br>

3. Multiprocessing Os :  There are more than one processors present in the system which can execute more than one process at the same time
<br>

4. Multitasking Os : It allows a user to perform more than one computer task at the same time. In this Os, CPU provides some amount of time to each process present in RAM. It is more responsive towards process.like server.
<br>

5. Network Os : An Operating system, which includes software and associated protocols to communicate with other computers and share their resources to each other via a network conveniently . Clusterd os is an example of this type of system (in this os , several devices are connect to same local network for execution process.)
<br>

6. Real Time Os : In Real-Time Systems, each job carries a certain deadline within which the job is supposed to be completed, otherwise, the huge loss will be there, or even if the result is produced, it will be completely useless. It is of two types :
(I) Soft RTOS : like online transaction (instruction within a deadline)
(II) Hard RTOS : like missile system (instruction may some delay)
(III) Firm RTOS : like ticket reservation (the output will changes if process is completed after the deadline )
<br>

7. Distributed OS : The Distributed Operating system is not installed on a single machine, it is divided into parts, and these parts are loaded on different machines. A part of the distributed Operating system is installed on each machine to make their communication possible.


<br>

# Process management in os :

# Attributes of a process :

# Process States :

# Process Schedular :

# Process Queues :

# Time related to Queues :

Completion Time : The time at which a particular process is completed.
<br>


# CPU Scheduling :
why do we need cpu Scheduling :
<br>
In some cases like when a process has more burst time then other process will starve.

# CPU scheduling Algorithm: 

1. First come first serve

<br>

2. Shortest Job First:
<br>

3. Shortest Remaining time first:
<br>

4. Round Robin :

<br>

5. Priority based Algorithm :
<br>

6. Highest Response Ratio time next:

# Software Solution to prevent race condition:

Race conditions occurs when multiple process using same system varibles at the same time .
<br>
1 <b>Lock Variable :</b>
<br>
Porperties that needs to be satisfied for the solution of race condition:
<br>
Mutual Exclusion : Not satisfied in all condition
<br>
Progress :satisfied
<br>
Bounded Waiting : satisfied


<br>
2 <b>Test Set Lock Mechanism</b>
<br>
Properties:
<br>
Mutual Exclusion :satisfied
<br>
Progress : satisfied
<br>
Bounded Waiting : not satisfied
<br>

```bash
// Pseudocode
lock = false;
while(test_set(lock)):
// critical section
lock = false // exit secion


def function(target):
    temp = target
    lock = true
    return temp

```


3.<b>Turn Variable Approach :</b>
<br>
For two process
<br>
Mutual Exclusion : satisfied
<br>
we can check mutual exclusion is satisfied by checking the multiple process enters into the critical section.

<br>
Progress : not satisfied in all condition because spin lock is caused.
<br>
We can check the Progress conditions by altering the process to enter into the critcal sections (if there are two process then intially allows the first process to enter into cs and then check if intially second process enters into the cs then does first blocks the first process or not).
<br>

Bounded Waiting : satisfied (It means that everytime only one process is not executing).
<br>
We can check the Bounded waiting conditions by ensuring that any process should not wait more than a max-limit.
This can be checked by allowing the same process to enter into the cs twice after IO.
<br>

4.<b>Interested Variable Mechanism :</b>
<br>
For two process
<br>
Mutual Exclusion : satisfied
<br>
Progress : satisfied
<br>
Bounded Waiting : not satisfied  because dead lock is caused.

5.<b>Paterson Solution :</b>
<br>
For two process
<br>
Mutual Exclusion : satisfied
<br>
Progress : satisfied
<br>
Bounded Waiting : satisfied

# Hardware solution to prevent race conditions :
Semaphore: It is an integer variable which is used in mutual exclusive manner by various concurrent cooperative proeces in order to achieve synchronization  or we can say it  is used to prevent race condition.

<br>
There are two types of Semaphore :
<br>
1.Binary Semaphore :

```bash
// wait or down or p function  or we can say entry section pseudocode

p(semaphore s){
if(s.value == 1 ){
   disable_interrupts();  // Prevent preemption or interrupts
   s.value = 0;
}
else
{
    // block this process and place this in suspend list
    sleep();

}
 enable_interrupts();   // Re-enable interrupts
}


// up or signal or v function or we can say that exit section pseudocode
v(sempahore s){ 
if(suspend list is empty){
   s.value = 1 ;
}
else{
   // select a process from suspend list.
   wakeUp();
}

}
```


<br>
Note : In binary semaphores, the checking and setting of the semaphore value are atomic operations. This ensures that mutual exclusion is preserved, and race conditions are avoided.In some systems, semaphores are managed by the operating system kernel, which ensures atomicity via interrupt disabling or through the use of spinlocks or mutexes. The OS guarantees that a semaphore's wait() (or P()) and signal() (or V()) operations are performed without interruption, ensuring that the semaphore value cannot be changed by other processes during these operations.


<br>
When it is implemented at user level then checking and setting the semaphore value should be atomic.
<br>
2. Counting Semaphore :
semaphore can be any integer value.

# DeadLock :
It is a situation where no process got blocked and no process proceeds. All process are continuously waiting for infinite time.

# DeadLock Handling strategies :
# 1. Deadlock Ignorance :
# 2. Deadlock Prevention: 
<br>
In deadlock Prevention we need to false any of four conditions from (Mutual exclusion, Hold and Wait , No preemption,circular wait.)
<br>
1. Mutual Exclusion : To make it false we have to make all resources are sharable .But there some resources which are not sharable like printer,tapeDrive etc because these resources cannot shared by more than process ar a time.
<br>
2. Hold and Wait :
To make it false when a process comes we provide all the resources what the process is demanding. But practically it is not possible because if we provide all resources to a single process then all other process will continuously waiting.
<br>

3. No preemption : 
To make it false we need to preempt a process from a cylic wait to prevent deadlock. This is not a good approach at all since if we take a resource away which is being used by the process then all the work which it has done till now can become inconsistent.

<br>
Remember that when we take resource from a process the process will go again in the ready queue.
<br>
Consider a printer is being used by any process. If we take the printer away from that process and assign it to some other process then all the data which has been printed can become inconsistent and ineffective and also the fact that the process can't start printing again from where it has left which causes performance inefficiency.

<br>

4. Circular wait :
To violate circular wait, we can assign a priority number to each of the resource. A process can't request for a lesser priority resource. This ensures that not a single process can request a resource which is being utilized by some other process and no cycle will be formed.
<br>
Among all the methods, violating Circular wait is the only approach that can be implemented practically.

# Deadlock Avoidance 
RGA , Banker's algorithms 

# Deadlock Detection and Recovery 

# System Calls :
A system call in an operating system (OS) is a mechanism that allows a user-space program to request a service or resource from the kernel, which operates in a more privileged mode. These services include tasks like file handling, memory management, process control, networking, and device I/O.

<br>
<b>User Mode vs. Kernel Mode:</b>
<br>
In a modern OS, applications run in user mode with limited access to hardware and system resources, while the kernel runs in kernel mode with full access to those resources. A system call transitions the program from user mode to kernel mode.

# Types of System calls :
File management: It is used to handle files.
examples are : open(), read(), write(), createFile() , close()
<br>

Device Management : It is used to take the previleges for the use of system devices like printer.
examples are : read() , write(), Reposition(),ioctl() etc. Here ioctl means input-output control.

<br>
Process management: It is used to direct the process. one example is like to load a process to a main memory. 
exmaples are : fork(), exec(), exit(), wait()
<br>
 
Information Maintenance : It is used to get the information about the process (we can say metadata).
Examples are : getPId(),attributes,get system time and data.

<br>

Communication related : It is used for the intercommunication process.
examples are :  pipe(),create/delete connection etc

<br>
There are also some Protection and Security related system calls.


