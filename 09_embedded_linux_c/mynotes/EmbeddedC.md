### 
Vmstat 1,3 
Malloc create memory 
Stack vs heap 
*p —>pointer goes in heap 
If !p - terror -malloc - then return 1

Memset
Memset - constructor —> initialiser 
%ld - long intitger
%d 
%u - unsigned integer
Flush flush putput to terminal
free(p)

C convert main.c - preprocessor - compiler - assmebler - linker
assembler translater 
linker - links to library like math.h
static and dynamic kibrary  - linker and  extension so 
dynamic library lib.so

### List of lnked library ---
ldd find
	linux-vdso.so.1 (0x0000f9370321c000)
	libselinux.so.1 => /usr/lib/aarch64-linux-gnu/libselinux.so.1 (0x0000f93703130000)
	libm.so.6 => /usr/lib/aarch64-linux-gnu/libm.so.6 (0x0000f93703060000)
	libc.so.6 => /usr/lib/aarch64-linux-gnu/libc.so.6 (0x0000f93702e90000)
	/lib/ld-linux-aarch64.so.1 (0x0000f937031e0000)
	libpcre2-8.so.0 => /usr/lib/aarch64-linux-gnu/libpcre2-8.so.0 (0x0000f93702dd0000)
fireball@fireball:/usr/bin$ 

copy find cmd in linux from one to another machine.
rpm specs file which have list of librares
 in ubunutu the dev.libraries
yum, dnf


in program of  C - 
main is the starting point.
python , bash , perl is sequential  and its interpretor and not a language. 
int main(void) -- > integer
varibalei s placeholder
python needs no datatype
### Advanced data types -
 %zu - size_t 
%u insigned integer

- fgets is system call. - input as string and converts to number
- strtol - string to line

Linux forcefull clear cache
vmstat -s -S M

system call - open read wrote. lsseek close fsync
if fd == -1 then file failed to open

Linux os full tutorial - html. chapter 12 
Acknowledge via TCP 
kernel nftable - packet filtering
### iptables - 
rule. - acept drop 
chain - input chain or output chain forward chain
ipsec - 
ebtable. - ether bridge tables
daemon andsevice are same but daemon does not have the capability to write to tty

cat /proc/pid/fd
strace - ptrace - 
#Linux C

Kernel rooting job iand tcp ip stack is bypassed
kernel space - scheduler - VFS - memory mgmt - devic driver
system call interface - 
can save few microsecs

DPDK - DPDK directly in the user space Nic to user space. context switch polling method not interrupts.
lock mechanism - ring buffer buffer space - lockless method by creating a ring buffer in dpdk
consumer and producer 
Ring buffer - 
in socket buffer - linked list
perror
fcntl - file control
close(fd)
ioctl 
pipe2 shmget
semaphore -- sync variable and resources like alock mechanism how multiple threads work
offset - the location eg : Hello then cursor is at en do hello is offset
Any file operation needs  open  read write write lseek(change the offset).
fsync - file sync
linked list does nto need contiguous memory
malloc will return -1 if the contigous fails
for(;;). -- infinte loop or while 1




RDMA - 

onload - 













