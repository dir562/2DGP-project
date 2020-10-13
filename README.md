# 1, 운영체제
## page 1: OS:
Everything that isn’t an application or hardware
## OS:
Software that abstracts hardware into a useful form for applications
OS's functions: (1) Standard Library (2) Resource Coordinator

## page2 : First Function: Standard Library
Advantages of standard library
Allow applications to reuse common facilities
Make different devices look the same
Provide higher level abstractions




Challenges
What are the right abstractions?



## page3 : Second Function: Resource Coordinator
Resource: "Anything valuable" 
(e.g. CPU, memory, disk, network)

Advantages of resource coordinator
Virtualize resource so multiple users/applications can share
Protect applications from one another
Provide efficient and fair access to resources

Challenges
What mechanisms?
What policies?
Abstractions == Combination of mechanisms and policies


## 184 page : Linux Multiprocessor Schedulers
O(1)
A Priority-based scheduler
Use Multiple queues
Change a process’s priority over time
Schedule those with highest priority
Interactivity is a particular focus

Completely Fair Scheduler (CFS)
Deterministic proportional-share approach
Multiple queues


## 185 page
BF Scheduler (BFS)
A single queue approach
Proportional-share
Based on Earliest Eligible Virtual Deadline First (EEVDF)



# 2번째 PPT

## 179 page
With round robin, the system might produce a schedule that looks like this:

## 180page Load Imbalance issue of MQMS
After job C in Q0 finishes:
A gets twice as much CPU as B and D.

After job A in Q0 finishes:
CPU0 will be left idle!


## 181page How to deal with load imbalance?
The answer is to move jobs (Migration).
Example:
The OS moves one of B or D to CPU 0



## 186페이지 : I/O-Bound VS. Processor-Bound Processes
Processes can be classified as either I/O-bound or processor-bound 
The former is characterized as a process that spends much of its time submitting and waiting on I/O requests
Consequently, such a process is runnable for only short durations, because it eventually blocks waiting on more I/O
Any type of blockable resource, such as keyboard input or network I/O, and not just disk I/O
Most graphical user interface (GUI) applications are I/O-bound, even if they never read from or write to the disk
They spend most of their time waiting on user interaction via the keyboard and mouse

## 188 페이지 : I/O-Bound VS. Processor-Bound Processes
The scheduling policy must satisfy two conflicting goals
Fast process response time (low latency)
Maximal system utilization (high throughput)

Linux, aiming to provide good interactive response and desktop performance,
optimizes for process response (low latency), thus favoring I/O-bound processes over processor-bound processors

## 189 페이지 : Process Priority
A common type of scheduling algorithm is priority-based scheduling
The goal is to rank processes based on their worth and need
Both the user and the system can set a process’s priority to influence the scheduling behavior
Processes with a higher priority run before those with a lower priority
Processes with the same priority are scheduled round-robin
On some systems, processes with a higher priority also receive a longer timeslice
The runnable process with timeslice remaining and the highest priority always runs


