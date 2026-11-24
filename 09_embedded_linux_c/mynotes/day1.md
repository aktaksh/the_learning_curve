
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