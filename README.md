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


## 190 : 
The Linux kernel implements two separate priority ranges
The first is the nice value, a number from –20 to +19 with a default of 0
Processes with a lower nice value (higher priority) receive a larger proportion of the system’s processor compared to processes with a higher nice value (lower priority)

Nice values are the standard priority range used in all Unix systems
In other Unix-based systems, such as Mac OS X, the nice value is a control over the absolute timeslice allotted to a process
In Linux, it is a control over the proportion of timeslice


## 191 :
The second range is the real-time priority
The values are configurable, but by default range from 0 to 99, inclusive
Opposite from nice values, higher real-time priority values correspond to a greater priority
All real-time processes are at a higher priority than normal processes

Linux implements real-time priorities in accordance with the relevant Unix standards, specifically POSIX.1b
All modern Unix systems implement a similar scheme


 
 ## 193 :
 The timeslice is the numeric value that represents how long a task can run until it is preempted
The scheduler policy must dictate a default timeslice

Too long timeslice causes to have poor interactive performance,It will no longer feel as if applications are concurrently executed

Too short a timeslice causes significant amounts of processor time to be wasted on the overhead of switching processes

The conflicting goals of I/O-bound versus processor-bound processes arise
I/O-bound processes do not need longer timeslices
Processor-bound processes crave long timeslices 


## 196 :Example scenario

Consider a system with two runnable tasks
(1) text editor, (2) video encoder
The text editor is I/O-bound because it spends nearly all its time waiting for user key presses
When the text editor does receive a key press, the user expects the editor to respond immediately
The video encoder is processor-bound
The encoder spends all its time applying the video codec to the raw data, easily consuming 100% of the processor
The video encoder does not have strong time constraints on when it runs
If it started running now or in half a second, the user would not care
The sooner it finishes the better, but latency is not a primary concern

## 200 : Process Scheduling in Unix Systems
On Unix, the priority is exported to user-space in the form of nice values
This sounds simple, but in practice it leads to several pathological problems
First, mapping nice values onto timeslices requires a decision about what absolute timeslice to allot each nice value
- This leads to suboptimal switching behavior
- For example, let’s assume we assign processes of the default nice value (0) a timeslice of 100 milliseconds and processes at the highest nice value (+19, the lowest priority) a timeslice of 5 milliseconds
- The default-priority process thus receives 20⁄21 (100 out of 105 milliseconds) 
- The low priority process receives 1/21 (5 out of 105 milliseconds)


## 201 : Process Scheduling in Unix Systems
Now, what happens if we run exactly two low priority processes?
We’d expect they each receive 50% of the processor 
But they each enjoy the processor for only 5 milliseconds at a time
5 out of 10 milliseconds each!
That is, instead of context switching twice every 105 milliseconds, we now context switch twice every 10 milliseconds
Conversely, if we have two normal priority processes, each again receives the correct 50% of the processor, but in 100 millisecond increments
Neither of these timeslice allotments are necessarily ideal


## 202 : Process Scheduling in Unix Systems

A second problem concerns relative nice values
Say we have two processes, each a single nice value apart
Let’s assume they are at nice values 0 and 1
This might map to timeslices of 100 and 95 milliseconds
These two values are nearly identical, and thus the difference here between a single nice value is small
Now, instead, let’s assume our two processes are at nice values of 18 and 19
This now maps to timeslices of 10 and 5 milliseconds
The former receiving twice the processor time as the latter!


## 205 : Completely fair scheduling (CFS)
The Completely Fair Scheduler (CFS) is a process scheduler

Merged into the 2.6.23 release of the Linux kernel and is the default scheduler

Maximize overall CPU utilization while also maximizing interactive performance

CFS does not use the old data structures for the runqueues, but it uses a time-ordered red black tree to build a "timeline" of future task execution

In CFS the virtual runtime is expressed and tracked via the per-task
-> p->se.vruntime
-> nanosec-unit

