# 1, 운영체제
## page 1: OS:
- Everything that isn’t an application or hardware
## OS:
- Software that abstracts hardware into a useful form for applications
- OS's functions: (1) Standard Library (2) Resource Coordinator

## page2 : First Function: Standard Library
Advantages of standard library
- Allow applications to reuse common facilities
- Make different devices look the same
- Provide higher level abstractions




Challenges
- What are the right abstractions?



## page3 : Second Function: Resource Coordinator
Resource: "Anything valuable" 
- (e.g. CPU, memory, disk, network)

Advantages of resource coordinator
- Virtualize resource so multiple users/applications can share
- Protect applications from one another
- Provide efficient and fair access to resources

Challenges
- What mechanisms?
- What policies?
- Abstractions == Combination of mechanisms and policies


## 18 페이지 : Types of OSes
Monolithic kernels 
- Linux, Windows, BSDs, …

UniKernel / Library OS
- SunMOS, Mirage, …

Exokernels
Microkernels
- MINIX
Multi-kernels
- Barrelfish
Lightweight Kernels 
- Catamount, IBM CNK
Co-kernels
- McKernel, Intel mOS

## 19 : Monolithic Kernels
Defacto standard OS design approach
- Linux, Windows, etc
Goal is universal compatibility 
- Support all possible hardware
- Support all possible applications

장점 :Easy to use
- Does everything "good enough"
- Many high level abstractions
단점 : Large and complex
- Size of Linux kernel source code is 850 MB
- Constant security vulnerabilities

## 20 : Unikernel
Link OS to application as a library
- Application and OS are a single entity
- OS Library: 
-- Abstractions to interface directly with hardware
-- Policies to manage isolation in application

Very high performance
- Minimal and highly specialized abstractions
- No context switching
No protection!
- Application runs as the kernel
- Application has control over entire machine

Very low system utilization
- Only one application at a time can run on a machine


## 21 : Unikernel use cases
Supercomputing / HPC
- Historically extreme scale HPC systems have run a single app at a time
-- 1990’s – early 2000’s
- Early OS’s could not scale
-- Unikernels were adopted to "fill the gap"
- Fell out of favor as OSes (Linux) caught up

Cloud (Virtual Machines)
- Virtualization sparked a renaissance in unikernels
-- Performance benefits without the costs
-- Multiple virtualized unikernels can run on a single system

## 22 : Microkernels
Minimalistic kernel
- Provide very few mechanisms
- Basic HW protection/isolation and IPC channels

Higher level abstractions implemented in user space as "servers"
- Clients request functionality from a specific server
- OS as a distributed system (designed by Tannenbaum)

Client-server communicate via message passing
- Performance depends on a very fast message passing mechanism (the most important OS mechanism)


## 23 :Exokernels
A combination of micro- and uni- kernels
- Very small kernel provides basic HW protection
- No OS provided IPC mechanisms

Applications provide own higher level services
- Applications can choose their level of abstraction
- Implement their own services

## 24 : Multi-kernels
Goal: Make microkernels scalable to modern systems
- Modern many-/multi-core systems are basically distributed systems

Distributed Operating System
- Communicate via asynchronous messages 
-- Shared memory doesn’t work in a distributed system
- Replicate state, but use messages to keep it consistent
- Support heterogeneous architectures


## 25 : Lightweight kernels (LWKs)
Designed specifically for extreme scale HPC
- Large scale supercomputers in the upper ranks of the top 500 (http://www.top500.org)

Large scale, but small world
- Small number of applications
- Small number of application requirements
- Small number of systems

LWKs provide a stripped down OS environment
- Provide the OS features needed and nothing else
-- "Leaky" microkernel
- Will provide functionality in OS when it makes sense

## 26 : Lightweight Co-kernels
Fact: Programmers are lazy
- Everyone just wants to use Linux
- LWKs lack many Linux features (i.e. shells)
Co-kernels couple an LWK and a FWK (Linux) on the same machine
- Missing features in LWK can be provided by Linux
- Machine can be managed via Linux
- Applications can be launched onto an LWK partition
Best of both worlds
- Functionality of Linux
- Performance of an LWK for HPC Apps
- Non-interference between the two partitions


## 28 : Hypervisors/VMMs
A Virtual Machine is a software version of the hardware state of a computer system
- An operating system running within a virtual machine is called a guest operating system

## 29 : Virtual Machine Monitors (VMMs)
Virtual Machines run an OS as an application
- Implements hardware interface in software

Ways to build a VMM (Type 1 vs Type 2)
- Type 2: VMs run as apps in a native OS
-- VMWare Player, KVM, VirtualBox
- Type 1: Hypervisor is the native OS
-- No native apps, everything runs in a VM
-- Xen, VMWare ES


## 32 : What a happens when a program runs?
A running program executes instructions.
1. The processor fetches an instruction from memory.
2. Decode: Figure out which instruction this is
3. Execute: i.e., add two numbers, access memory, check a condition, jump to function, and so forth.
4. The processor moves on to the next instruction and so on.

## 33 : Operating System (OS)
Responsible for
- Making it easy to run programs
- Allowing programs to share memory
- Enabling programs to interact with devices

OS is in charge of making sure the system operates correctly and efficiently.

## 34 : Virtualization
The OS takes a physical resource and transforms it into a virtual form of itself.
- - Physical resource: Processor, Memory, Disk …
- The virtual form is more general, powerful and easy-to-use.
- Sometimes, we refer to the OS as a virtual machine.


## 35 : System call
System call allows user to tell the OS what to do.
- The OS provides some interface (APIs, standard library).
- A typical OS exports a few hundred system calls.
- - Run programs
- - Access memory
- - Access devices

## 36 : The OS is a resource manager.
The OS manage resources such as CPU, memory and disk.
The OS allows
- Many programs to run  Sharing the CPU
- Many programs to concurrently access their own instructions and data  Sharing memory
- Many programs to access devices  Sharing disks


## 37 : Virtualizing the CPU
The system has a very large number of virtual CPUs.
- Turning a single CPU into a seemingly infinite number of CPUs.
- Allowing many programs to seemingly run at once                                                   
- --  Virtualizing the CPU

## 41 : Virtualizing Memory
The physical memory is an array of bytes.
A program keeps all of its data structures in memory.
- Read memory (load):
- -Specify an address to be able to access the data
- Write memory (store):
- - Specify the data to be written to the given address



## 44 :Virtualizing Memory (Cont.)
The output of the program mem.c
- The newly allocated memory is at address 00200000.
- It updates the value and prints out the result.


## 45 : Virtualizing Memory (Cont.)
Each process accesses its own private virtual address space.
- The OS maps address space onto the physical memory.
- A memory reference within one running program does not affect the address space of other processes.
- Physical memory is a shared resource, managed by the OS.


## 46 : The problem of Concurrency
The OS is juggling many things at once, first running one process, then another, and so forth.

Modern multi-threaded programs also exhibit the concurrency problem.


## 48 : Concurrency Example (Cont.)
The main program creates two threads.
- Thread: a function running within the same memory space. Each thread start running in a routine called worker().
- worker(): increments a counter

## 49 : Concurrency Example (Cont.)
loops determines how many times each of the two workers will increment the shared counter in a loop.
loops: 1000.

loops: 100000.


## 50 : Why is this happening?
Increment a shared counter  take three instructions.
1, Load the value of the counter from memory into register.
2, Increment it
3. Store it back into memory

These three instructions do not execute atomically.  Problem of concurrency happen.


## 51 : Persistence
Devices such as DRAM store values in a volatile.
Hardware and software are needed to store data persistently.
- Hardware: I/O device such as a hard drive, solid-state drives(SSDs)
- Software:
- - File system manages the disk.
- -File system is responsible for storing any files the user creates.


## 52 :Persistence (Cont.)
open(), write(), and close() system calls are routed to the part of OS called the file system, which handles the requests
Create a file (/tmp/file) that contains the string "hello world"


## 53 :Persistence (Cont.)
What OS does in order to write to disk?
- Figure out where on disk this new data will reside
- Issue I/O requests to the underlying storage device

File system handles system crashes during write.
- Journaling or copy-on-write
- Carefully ordering writes to disk




## 54 : Design Goals
Build up abstraction
- Make the system convenient and easy to use.

Provide high performance
- Minimize the overhead of the OS.
- OS must strive to provide virtualization without excessive overhead.

Protection between applications
- Isolation: Bad behavior of one does not harm other and the OS itself.


## 55 : Design Goals (Cont.)
High degree of reliability
- The OS must also run non-stop.

Other issues
- Energy-efficiency
- Security
- Mobility


## 56 : What does OS deal with
CPU
- Execute code with data


Memory
- Read and write code and data


Storage
- Persistently store the code and data











# 2번째 PPT

## 2 : How to provide the illusion of many CPUs?
CPU virtualizing
- The OS can promote the illusion that many virtual CPUs exist.
- Time sharing: Running one process, then stopping it and running another

## 3 :A Process
A process is a running program.


Comprising of a process:
- Memory (address space)
- -Instructions
- -Data section
- Registers
- -Program counter
- -Stack pointer


## 4 : Process API
These APIs are available on any modern OS.
Create
- Create a new process to run a program
Destroy
- Halt a runaway process
Wait
- Wait for a process to stop running
Miscellaneous Control
- Some kind of method to suspend a process and then resume it
Status
- Get some status info about a process


## 5 : Process Creation
1, Load a program code into memory, into the address space of the process.
- Programs initially reside on disk in executable format.
- OS perform the loading process lazily.
  -> Loading pieces of code or data only as they are needed during program execution.

2, The program’s run-time stack is allocated.
- Use the stack for local variables, function parameters, and return address.
- Initialize the stack with arguments  argc and the argv array of main() function


## 6 : Process Creation (Cont.)
3, The program’s heap is created.
- Used for explicitly requested dynamically allocated data.
- Program request such space by calling malloc()and free it by calling free().

4, The OS do some other initialization tasks.
- Input/output (I/O) setup
- - Each process by default has three open file descriptors.
- - Standard input, output and error

5,Start the program running at the entry point, namely main().
- The OS transfers control of the CPU to the newly-created process.


## 7 :
Loading:
Takes on-disk program
and reads it into the address space of process


## 9 : Process States
A process can be one of three states.
Running
- A process is running on a processor.
Ready
- A process is ready to run but for some reason the OS has chosen not to run it at this given moment.
Blocked
- A process has performed some kind of operation.
- When a process initiates an I/O request to a disk, it becomes blocked and thus some other process can use the processor.

## 10 : Data structures
The OS has some key data structures that track various relevant pieces of information.
- Process list
- -Ready processes
- -Blocked processes
- - Current running process
- Register context

Process Control Block (PCB)
- A C-structure that contains information about each process.


## 15 : The fork() System Call
Create a new process
- The newly-created process has its own copy of the address space, registers, and PC.

## 23 : CPU registers and instructions
x86 is a CISC architecture with hundreds of instructions defined
General instruction categories
- General Purpose instructions
- Floating-Point instructions
- Program Flow-related instructions
Hardware-related instructions
- Simple x86 instructions:
- MOV	  AX, BX

- ADD	  AX, CX


## 24 : CPU registers and instructions
A number of the x86 instructions have multiple variants. 
Here are a few variants of the MOV and ADD instructions as examples:

MOV    SI, 7000h		; move immediate to register
MOV    BX, AX			; move ax register to bx register
MOV    BX, [SI]			; move memory data to register
MOV    [SI], BX			; move register data to memory
ADD    AX, BX			; register to register add
ADD    AX, [BX]		; memory to register add 
ADD    [BX], AX		; register to memory add
ADD    AX, 20			; immediate to register add


## 25 : CPU registers and instructions
A small sampling of the general-purpose and floating-point x86 instructions are shown below:


## 26 : CPU registers and instructions
Here is a small subset of the x86 instructions related to program flow:
JMP
JNZ
LOOP
CALL
RET
INT
IRET


## 28 : CPU registers and instructions
General-Purpose Registers (GPRs)


## 29 : CPU registers and instructions
CPU registers and instructions

## 30 : CPU registers and instructions

## 33 : CPU registers and instructions
Sized Operations with GPRs

8-bit Operations                
ADD    AX, BX
ADD    AX, R8W
ADD    R9W, R8W

64-bit Operations
ADD    RAX, RBX
ADD    RAX, R8
ADD    RAX, RAX

16-bit Operations
ADD    AL, BL
ADD    AL, AH
ADD    R8B, AL
ADD    R8B, AH

32-bit Operations
ADD    EAX, EBX
ADD    EAX, R8D
ADD    R9W, EAX

## 35 : CPU registers and instructions
Little Endian – the least significant byte goes in the littlest address
mov    esi, 4000h
mov    ax, 1234h
mov    [esi], ax

## 36 : Single Instruction Multiple Data (Simd)
x87 FPU Register Set
- The MMX registers are the same physical registers as the x87 registers
- MMX instructions perform the same operation on multiple pieces of data packed into registers
- - SIMD operations
- -Targeted at multimedia and communication applications
Only supports integer operations


## 37 : Single Instruction Multiple Data (Simd)
PADDSB
- Packed Add Bytes
- Signed, Saturating
PADDUSB
- Packed Add Bytes
- Unsigned, Saturating



## 49 : real mode
All x86-based processors start in Real Mode when reset
- 16-bit operating environments with 20-bit of address space
Memory address space is divided into segments
- 64kB in size
- Base address in on any 16-byte boundary in the 20-bit address space
- Multiple segments can be active at a time
- -CS – Code Segment
- -SS – Stack Segment
- -DS – Data Segment (Default)
- -ES, FS, and GS – additional data segments
- No concepts of paging or virtual memory
- No protection – any program has free access to all of memory and can directly access I/O ports


## 50 : Segmented memory in real mode
There can be six active segments of memory at a time
- Each segment register defines an active segment
The segment registers hold the upper 16-bit of the 20-bit base address of the segment

## 52 : protected mode
Protected Mode was implemented to handle the problems that exist with a multitasking environment
- Providing memory protection across applications
- Managing I/O transactions from a central entity (OS)
- Controlling access to OS resources and tools
- Verifying an application’s request to disable/enable interrupt
Protected Mode introduced several new topics to handle the above issues
- Segment Descriptors
- Task Switching
- Software Privilege Levels
- Virtual Memory and Paging
- I nterrupt Descriptors


# 53 : Privileged Instructions
Some instructions can only be executed at the highest privilege level (ring 0)
- because they could affect the state of some shared resource
Examples: 
- CLI
- STI
- INVLPG
- WBINVD
- MOV (Control/Debug Register N)
- RDMSR
- WRMSR


# 54 : Protected Mode
In Protected Mode, OS can assign attributes and access right to each segment
- Base address
- Size of segment
- Privilege Level
- Read/Write permissions
- Mode of operation
- -16-bit, 32-bit, or 64-bit
Each segment has an 8-byte descriptor for attributes
- All defined segment descriptors are held in either Global Descriptor Table (GDT) or Local Descriptor Table (LDT)
- The descriptor tables live in memory and are managed by OS

## 55 : Virtual-8086 Mode
Virtual-8086 Mode enables Real Mode applications to run efficiently under the Protected Mode
Virtual-8086 Mode emulates the Real Mode environment
- 16-bit operating environment
- 20-bit address space
It enables the processor to watch for operations that would be disruptive in a multitasking environment
- e.g., enabling/disabling interrupt handling
- It triggers an exception if a disruptive operation is attempted allowing the OS to handle the event


## 56 : System Management Mode (SMM)
System Management Mode (SMM) is used to handle system-specific activities
- Power management, security, platform management
This mode can only be entered by receiving a System Management Interrupt (SMI)
When entering SMM, the processor automatically saves the state of the machine and enters a state that is transparent to the OS
- Operates in a special region called SMRAM

## 57 : Long Mode (IA-32e mode)
Long Mode is comprised of 2 sub-modes
- 64-bit Mode
- Compatibility Mode
Must be enabled by a 64-bit capable OS
Provides the ability for 64-bit applications, as well as existing 32-bit and 16-bit Protected Mode applications to be run in this mode
Provides a very low latency transition between a 32-bit environments (Compatibility Mode) and a 64-bit environment (64-bit Mode)
Implements the x86-64 extensions
- Intel 64, AMD64, and x64


## 58 :64-bit Mode
64-bit Mode is a sub-mode of Long Mode, which runs native 64-bit applications
- Allows software to support larger address space
- -Provides the ability to support up to a 64-bit virtual address space
- - -Modern x86-64 based processors implement a 48-bit virtual address space
- -Enables the processor to support up to a 52-bit physical address space
- - -Modern x86-64 based processors implement a 40- or 48-bit physical address space
Removes a lot of the antique legacy mechanisms not used by modern software
- Segmentation and hardware task switching


## 59 :Compatibility Mode
A sub-mode of Long Mode, which runs binary compatible 16- and 32-bit Protected Mode applications under 64-bit system software
To an application, Compatibility Mode looks just like Legacy Protected Mode
- 32-bit virtual address space
- 8 General-purpose registers (GPRs)
- GPRs are 32-bit wide
All system software semantics are still 64-bit
Interrupt and Exception handling cause the processor to transit into 64-bit Mode








## 63 : The elf binary format
file hello
file hello.o
readelf -h hello
readelf -h hello.o
readelf -l hello
readelf -l hello.o
readelf -S hello
readelf -S hello.o
nm hello.o
nm hello


readelf -r hello.o
readelf -s hello
readelf -d hello
objdump -d hello.o -M intel
objdump -d hello -M intel



## 64 : Procedure call
The stack is a memory area at the end of the address space of a process
- It grows from top to bottom when elements are pushed on to it
- It is used to provide memory for the local variables of the function
- It also supports parameter-passing when functions are invoked
- If nested procedures are called, the stack grows from top to bottom and accepts new activation records that hold all data needed for one procedure
- The activation record of the procedure currently executing is delimited at the top by the frame pointer and at the bottom by the stack pointer




## 65 : Procedure call
Two stack manipulation commands
- Push places a value on the stack and decrements the stack pointer by the number of bytes in memory required by the value
- -The end of the stack is moved down to lower addresses
- Pop removes a value from the stack and increments the value of the stack pointer accordingly
- -The end of the stack is moved up




## 66: Procedure call
To invoke and exit functions, the following two commands are provided – they automatically manipulate the stack
- call pushes the current value of the instruction pointer onto the stack and branches to the start address of the function to be called
- return pops the bottom value from the stack and branches to the specified address
- -Procedures must be implemented so that return is the last command and the address placed on the stack by call is at the bottom





## 67 : Procedure call
A procedure call therefore consists of the following two steps
1, Build a parameter list in the stack
- The first argument to be passed to the called function is placed last on the stack
- This makes it possible to pass a varying number of arguments that can be popped from the stack one after the other
2, Invoke call, which causes the current value of the instruction pointer (pointing to the instruction that follows call) to be pushed onto the stack and delegates code flow to the invoked function






## 68 : Procedure call
The procedure called is responsible for managing the frame pointer and performs the following steps
1, The previous frame pointer is pushed onto the stack, thus moving the stack pointer down
2, The frame pointer is assigned the current value of the stack pointer and now marks the start of the stack area for the function to be executed
3, The code of the function is executed
4, When the function terminates, the stored frame pointer is at the bottom of the stack
- Its value is popped from the stack and saved in the frame pointer that now again points to the start of the stack area of the previous function 
- The return address saved when the function was called is now located at the bottom end of the stack
5, Invoking return causes the return address to be popped from the stack
- The processor branches to the return address, thus returning the code flow to the calling function





## 71 : Stack overflow protection
-fno-stack-protector
- No protection code is included for stack smashing attacks.
-fstack-protector
- Emit extra code to check for buffer overflows, such as stack smashing attacks. 
- This is done by adding a guard variable to functions with vulnerable objects. 
- This includes functions that call alloca(), and functions with buffers larger than 8 bytes.
-fstack-protector-all 
- Like -fstack-protector except that all functions are protected.





## 74 : Software Privilege Levels
Level 0 - highest privilege level
- For OS kernel
Level 1 - second highest privilege level
- For OS Services and high-privileged device drivers
- Could be used for debuggers
Level 2 - third highest privilege level
- For lower-privileged device driver
Level 3 - lowest privilege level
- For application programs





## 75 : Privilege (protection) Rings
The x86 systems use privilege levels, the mechanism whereby the OS and CPU conspire to restrict what user-mode programs can do
- 0 (most privileged) to 3 (least privileged)
- For memory, I/O ports, machine instructions



## 76 : Privilege (protection) Rings
About 15 instructions are restricted by the CPU to ring 0
- These instructions can subvert the protection mechanism
- An attempt to run them outside of ring 0 causes a general-protection exception
CPU keeps track of the current privilege level, which involves the segment selectors, e.g.,:
- Requested Privilege Level (RPL)
- Current Privilege Level (CPL)




## 78 : Privilege (protection) Rings
Keep in mind that the CPU privilege level has nothing to do with OS users
- Whether you’re root, administrator, guest, or a regular user, it does not matter
- All user code runs in ring 3, all kernel code runs in ring 0
- -regardless of the OS users on whose behalf the code operates
 Due to restricted access to memory and I/O ports, user mode can do almost nothing to the outside world without calling the kernel
- All of the data structures that control such things – memory, open files, etc. – cannot be touched directly by user code 





## 79 : Privilege (protection) Rings
The CPU protects memory at two crucial points:
- When a segment selector is loaded
- When a page of memory is accessed with a linear address
When a data segment selector is being loaded, the check below takes place:





## 80 : Privilege (protection) Rings
Useful memory protection is done in the paging unit when a linear address is converted into a physical address
Each memory page is a block of bytes described by a page table entry containing two fields related to protection:
- Supervisor flag
- Read/write flag
The supervisor flag is the primary x86 memory protection mechanism used by kernels
- When it is on, the page cannot be accessed from ring 3




## 81 : Privilege (protection) Rings
While the read/write flag isn’t as important for enforcing privilege, it’s still useful
- When a process is loaded, pages storing binary images (code) are marked as read only, thereby catching some pointer errors if a program attempts to write to these pages
- This flag is also used to implement copy on write when a process is forked in Unix
- Upon forking, the parent’s pages are marked read only and shared with the forked child
- If either process attempts to write to the page, the processor triggers a fault and the kernel knows to duplicate the page and mark it read/write for the writing process




## 82 : System calls in detail
Every interaction with the outside world is mediated by the kernel through system calls
- If an application saves a file, writes to the terminal, or opens a TCP connection, the kernel is involved
- These system calls are function calls from an application into the kernel




## 86 : System calls in detail
It all starts with a call to the C library’s getpid(), which is a wrapper for the system call

Once the wrapper has done its initial work it’s time to jump into the kernel

The mechanics of this transition vary by processor architecture

In Intel processors, arguments and the syscall number are loaded into registers, then an instruction is executed to put the CPU in privileged mode and immediately transfer
control to a global syscall entry point within the kernel

The kernel then uses the syscall number as an index into sys_call_table, an array of function pointers to each syscall implementation
https://thevivekpandey.github.io/posts/2017-09-25-linux-system-calls.html




## 88 : How to efficiently virtualize the CPU with control?
The OS needs to share the physical CPU by time sharing.
Issue
- Performance: How can we implement virtualization without adding excessive overhead to the system?
- Control: How can we run processes efficiently while retaining control over the CPU?


## 90 : Problem 1: Restricted Operation
What if a process wishes to perform some kind of restricted operation such as …
- Issuing an I/O request to a disk
- Gaining access to more system resources such as CPU or memory

Solution: Using protected control transfer
- User mode: Applications do not have full access to hardware resources.
- Kernel mode: The OS has access to the full resources of the machine






## 91 : System Call
Allow the kernel to carefully expose certain key pieces of functionality to user program, such as …
- Accessing the file system
- Creating and destroying processes
- Communicating with other processes
- Allocating more memory




## 92 : System Call (Cont.)
Trap instruction
- Jump into the kernel
- Raise the privilege level to kernel mode

Return-from-trap instruction
- Return into the calling user program
- Reduce the privilege level back to user mode




## 95 : interrupt service routine (ISR)
An interrupt is an event that causes the currently executing code to be effectively paused while the event is serviced.
There are two main categories of interrupts:
- Hardware interrupts 
- -Asynchronous
- Software interrupts 
- -Synchronous





## 96 : Hardware Interrupts
External interrupts from a IO devices, chipset components or other processors
Local interrupts
- Thermal sensor, performance monitor counter interrupts, etc.
Special case interrupts:
- NMI: Non-Maskable Interrupt
- SMI: System Management Interrupt







## 97 :Hardware Interrupts
Most hardware interrupts go through an interrupt controller (e.g. Local APIC) before being delivered to the target core.
- NMIs and SMIs are not handled by an interrupt controller. 
- -These are delivered directly to the target core.
Software running on one core can program that core’s local APIC to fire an interrupt targeting another core (or set of cores)
- Commonly referred to as IPIs (Inter-Processor Interrupts)





## 98 :Software interrupts
Interrupts may also occur via dedicated software instructions. 
Each time an interrupt instruction (INT xx) is executed by the processor, the xx value (an 8-bit operand) causes the CPU to run the requested interrupt service routine.
INT 21h for various DOS services
DOS read, write, write string, terminate program, etc.
INT 80h (x86) and syscall (x86_64) for system calls
Software interrupts do NOT interact with any interrupt controller (e.g. Local APIC). 
These are handled entirely within the core executing the instruction.






## 99 : Processor Exceptions
An exception is typically an unexpected internal event and generally occurs when the CPU executes an instruction requiring additional attention
Some exceptions are error conditions, some are not:
- Integer divide by zero attempt (an error exception)
- Page fault
- -when attempting to access a memory address that isn't present in DRAM
- Stack overflow, etc.
Exceptions do NOT interact with any interrupt controller (e.g. Local APIC).
- These are handled entirely within the core that detected the exception.






## 100 :interrupt service routine (ISR)

Each unique interrupt and exception is represented by a vectors (aka interrupt vector).
- CPU uses the vector to locate and execute the appropriate handler, also referred to as the interrupt service routine (ISR)

The x86 architecture supports an 8-bit interrupt vector (0 –255) 
- In multi-processor/core systems, there can be more than 256 unique interrupts. 
- Each logical processor supports 256 vectors.





## 102 : interrupt service routine (ISR)
Upon entering an ISR, the processor automatically saves info about the state of the interrupted program:

SS, SP, Flags, CS, IP, etc.



## 103 : Non-maskable interrupt (NMI)
A computer processor interrupt that cannot be ignored by standard interrupt masking techniques in the system
- When response time is critical or when an interrupt should never be disabled during normal system operation
- Typically used to signal attention for non-recoverable hardware errors
These errors include
- Non-recoverable internal system chipset errors
- Corruption in system memory such as parity and ECC errors
- Data corruption detected on system and peripheral busses
From users
- Hardware and software debugging interfaces
- System reset buttons



## 105 :Problem 2: Switching Between Processes
How can the OS regain control of the CPU so that it can switch between processes?
- A cooperative Approach: Wait for system calls
- A non-cooperative Approach: The OS takes control




## 106 : A cooperative Approach: Wait for system calls
Processes periodically give up the CPU by making system calls such as yield.
- The OS decides to run some other task.
- Application also transfer control to the OS when they do something illegal.
- -Divide by zero
- -Try to access memory that it shouldn’t be able to access

- Ex) Early versions of the Macintosh OS, The old Xerox Alto system

A process gets stuck in an infinite loop. 
 Reboot the machine




## 107 : A Non-Cooperative Approach: OS Takes Control
A timer interrupt
- During the boot sequence, the OS start the timer.
- The timer raise an interrupt every so many milliseconds.
- When the interrupt is raised :
- -The currently running process is halted.
- -Save enough of the state of the program
- -A pre-configured interrupt handler in the OS runs.

A timer interrupt gives OS the ability to 

run again on a CPU.





## 108 : System Timers
Intel 8253/8254 - Programmable Interval Timers (PITs)
- Timer 0 (System Timing): 1.1932 MHz
- Timer 1 (DRAM Refresh): 1.1932 MHz
- Timer 2 (General Use and Speaker): 1.1932 MHz
- Timer 3 (Watchdog Timer): 298.3 KHz
- Timer 4 (Not Implemented)
- Timer 5 (CPU Speed Control)
Newer motherboards also include a counter through
- Advanced Configuration and Power Interface (ACPI)
- Local Advanced Programmable Interrupt Controller (Local APIC)
- High Precision Event Timer
The CPU itself also provides the Time Stamp Counter (TSC)


## 109 : Saving and Restoring Context
Scheduler makes a decision:
- Whether to continue running the current process, or switch to a different one.
- If the decision is made to switch, the OS executes context switch.



## 110 : Context Switch
A low-level piece of assembly code
- Save a few register values for the current process onto its kernel stack
- General purpose registers
- -PC
- -Kernel stack pointer
- Restore a few for the soon-to-be-executing process from its kernel stack
- Switch to the kernel stack for the soon-to-be-executing process 


## 114 : 병행성이 걱정?
What happens if, during interrupt or trap handling, another interrupt occurs?

OS handles these situations:

Disable interrupts during interrupt processing

Use a number of sophisticate locking schemes to protect concurrent access to internal data structures.



## 123 : Events that Cause a Task Switch
The CS portion of a Far Call/Far jump branch target address selects TSS descriptor in GDT

The CS portion of a Far Call/Far jump selects Task Gate descriptor in the GDT or LDT

INT nn where nn selects a Task Gate in IDT

Hardware interrupt selects a Task Gate in IDT

Software exception selects a Task Gate in IDT

IRET execution when Eflags[NT] bit set







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

## 206 : Completely fair scheduling (CFS)
Each process then runs for a "timeslice" proportional to its weight divided by the total weight of all runnable threads

To calculate the actual timeslice, CFS sets a target for its approximation of the "infinitely small" scheduling duration
 -This target is called the targeted latency
 
 
 ## 208 : Completely fair scheduling (CFS)
  Assume the targeted latency is 20 milliseconds and we have 2 runnable tasks at the same priority
- Each will run for 10 milliseconds before preempting the other
- If we have 4 tasks at the same priority, each will run for 5 milliseconds
- If there are 20 tasks, each will run for 1 millisecond

As the number of runnable tasks approaches infinity, the assigned timeslice approaches zero

As this will eventually result in unacceptable switching costs, CFS imposes a floor on the timeslice assigned to each process
- This floor is called the minimum granularity
- By default it is 1 millisecond
- Thus, even as the number of runnable processes approaches infinity, each will run for at least 1 millisecond


## 209 : Completely fair scheduling (CFS)
Now, let’s again consider the case of two runnable processes with dissimilar nice values
- One with the default nice value (0)
- One with a nice value of 5

These nice values have dissimilar weights and thus our two processes receive different proportions of the processor’s time
- he weights work out to about a 1⁄3 penalty for the nice-5 process
- If our target latency is again 20 milliseconds, our two processes will receive 15 and 5 milliseconds each of processor time, respectively

What would be the allotted timeslices?
- Again 15 and 5 milliseconds each!
- Absolute nice values no longer affect scheduling decisions
- Only relative values affect the proportion of processor time allotted


## 212 :CFS implementation
CFS's task picking logic is based on this p->se.vruntime value
- It always tries to run the task with the smallest p->se.vruntime value (i.e., the task which executed least so far)
- The left most node of the scheduling red-black tree is chosen and sent for execution

 If the process completes execution, it is removed from the system and scheduling tree
 If the process reaches its maximum execution time or is otherwise stopped it is reinserted into the scheduling tree based on its new spent execution time
The new left-most node will then be selected from the tree, repeating the iteration

