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






