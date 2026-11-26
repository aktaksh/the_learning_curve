# Embedded Linux and C — Quick Notes

Short refresher notes distilled from the three tutorials in `Docs/` and the existing study notes. The tutorials cover Linux/C foundations; board-specific cross-compilation, device-tree and driver build steps must follow the target vendor's toolchain and ABI documentation.

## 1. C build and types

- Build path: source → preprocessor → compiler → assembler → linker → executable.
- In a hosted C program, `main` is the normal entry point.
- `#include` brings in declarations from headers; it does not link a library. `math.h` is a header; on many Linux toolchains, math functions also need `-lm` at link time.
- `.a` is a static archive; `.so` is a shared library. `ldd <trusted-binary>` shows dynamic dependencies; `readelf -d <binary>` inspects ELF dynamic entries.
- Use `size_t` for sizes/indexes, `ssize_t` for signed I/O results, and `<stdint.h>` fixed-width types when representation matters. Type sizes vary by ABI.
- Common format specifiers: `%d` int, `%u` unsigned int, `%ld` long, `%zu` size_t, `%p` pointer (pass `(void *)p`).

```bash
gcc -std=c11 -Wall -Wextra -Wpedantic -g main.c -o app
./app
```

## 2. Pointers, memory and ownership

- A pointer stores an address; `&x` gets an address and `*p` dereferences a valid pointer. A pointer is not itself “in the heap.”
- Stack: automatic local storage, usually limited, released when the function returns. Heap: dynamically allocated storage with explicit lifetime.
- `malloc` returns `NULL` on failure; `calloc` also zero-initializes; `realloc` may move the allocation; `free` releases it. Give each allocation one clear owner and free it once.
- Check pointers before use; avoid uninitialized, null, dangling, out-of-bounds and use-after-free accesses.
- `memset` fills bytes with one byte value. It is not a constructor and does not initialize complex objects by field semantics.
- Arrays are contiguous and C does not bounds-check them. Strings are `char` arrays terminated by `\0`; use bounded input such as `fgets`.
- `fgets` is a C standard-library function, not a system call. `strtol` converts a string to `long`; check the end pointer and range for invalid input.
- `fflush(stdout)` pushes buffered C output to the stream; output can otherwise remain buffered, especially when redirected.
- `struct` fields may have ABI-dependent padding. Do not serialize raw structures as a portable wire format. Use explicit fields, widths and byte order.
- Bitwise masks manipulate flags; prefer unsigned types and validate shift widths. Little-endian stores the low byte first; big-endian stores the high byte first.

## 3. C structure and debugging

- Functions receive arguments by value. Pass a pointer to let a function modify a caller-owned object; use a double pointer when it must replace the caller's pointer.
- A function pointer stores a function address and supports callbacks and operation tables.
- A linked list links nodes with pointers; nodes need not be contiguous. Insertion can be cheap at a known position; lookup is linear.
- `errno` is meaningful after an API reports failure. Save/read it then; use `perror` or `strerror` for a description.
- Undefined behavior includes out-of-bounds access, invalid pointers, use-after-free and signed overflow. Compiler warnings, GDB and sanitizers help expose defects.

```bash
gcc -Wall -Wextra -g -O0 app.c -o app
gdb ./app
strace -f ./app
```

## 4. Linux architecture and boot

- Linux is the kernel; a distribution combines it with user-space libraries, utilities, services and package management.
- Typical request path: application → C library/API → system call → kernel subsystem → driver → device. A system call is a controlled user-to-kernel entry; the kernel handles privileged operations.
- Kernel responsibilities include scheduling, virtual memory, filesystems/VFS, networking, device drivers, interrupts and hardware access.
- Typical boot: UEFI → bootloader (often GRUB) → kernel + initramfs → root filesystem → PID 1 (often systemd) → services/login.
- Drivers may be built into the kernel or loaded as modules. Devices may appear as character devices, block devices, network interfaces or virtual/pseudo devices.
- Ubuntu/Debian commonly use `apt`/`.deb`; RHEL-family systems commonly use `dnf`/RPM. `*-dev` or `*-devel` packages provide development headers and link-time files. RPM `.spec` files describe how an RPM package is built.

## 5. File I/O and system calls

- A file descriptor is a small integer handle. Standard input/output/error are usually 0/1/2.
- Buffered stdio uses `FILE *` functions such as `fopen`, `fgets`, `fprintf`, `fread`, `fwrite`, `fflush` and `fclose`.
- POSIX I/O uses descriptors: `open`, `read`, `write`, `lseek`, `fsync`, `ioctl`, `close`.
- `read`: positive bytes read, `0` means EOF, `-1` means error. Reads and writes may complete partially; loop until done and handle `EINTR` where appropriate.
- `lseek` changes the offset of a seekable descriptor. `fsync` requests that file data/metadata be committed to storage; it does not make every storage device immune to failure.
- `fcntl` gets/sets descriptor flags and related controls. `ioctl` is a device/subsystem-specific control interface.
- `pipe2` creates a pipe; `shmget` obtains a System V shared-memory segment; semaphores coordinate access. A mutex provides exclusive ownership; a semaphore is counter-based.
- Always check return values and close/free resources on error paths. Use a clear cleanup path when a function acquires multiple resources.

## 6. Processes and memory

- A program is executable bytes on disk; a process is a running instance with a PID, virtual address space, open descriptors, credentials and scheduling state.
- Threads share much of a process's address space and resources, but have their own execution state and stacks.
- `fork()` creates a child that initially shares pages copy-on-write. Parent and child continue after the call with different return values.
- `exec*()` replaces the current process image; it normally keeps the PID and does not create a new process. It returns only if execution fails.
- Children inherit many process attributes, including open descriptors, unless close-on-exec or other rules change them.
- The parent uses `wait()`/`waitpid()` to collect child status. A zombie has exited but has not been reaped; an orphan's parent exited first.
- `exit()` flushes stdio and runs `atexit` handlers. `_exit()` terminates immediately without those user-space cleanups; it is commonly used after failed `exec` in a child.
- Common `ps` states: `R` running/runnable, `S` interruptible sleep, `D` uninterruptible sleep, `T` stopped/traced, `Z` zombie.
- `SIGTERM` can be handled; `SIGKILL` cannot be caught or ignored.
- Virtual address space is not the same as resident RAM. Heap/stack diagrams are conceptual; ASLR, ABI and mappings change actual addresses.

```text
/proc/<PID>/fd/     process file-descriptor links
ps -o pid,ppid,stat,comm -p <PID>
strace -f -e trace=process,openat,read,write,close <command>
```

## 7. Linux operations and troubleshooting

| Need | Commands |
|---|---|
| Kernel and distribution | `uname -r`; `cat /etc/os-release` |
| Devices and modules | `lsblk`; `lspci -k`; `lsmod`; `modinfo <module>` |
| Network links/routes/sockets | `ip link`; `ip route`; `ss -lntup` |
| Processes | `ps`; `top -H`; `pidstat` |
| Memory | `free -h`; `vmstat 1 3`; `cat /proc/meminfo` |
| Storage | `df -h`; `df -i`; `iostat -xz 1` |
| Services and logs | `systemctl status <unit>`; `systemctl --failed`; `journalctl -u <unit>`; `journalctl -k` |
| File descriptors and syscalls | `ls -l /proc/<PID>/fd`; `strace -p <PID>` |
| Dynamic libraries | `ldd <trusted-binary>`; `readelf -d <binary>` |

- `vmstat 1 3` samples system activity; its first row is generally a since-boot average, followed by interval samples.
- `find` locates files on the local filesystem. Use `scp` over SSH to copy files between machines.
- Diagnose high CPU by finding the PID/thread and inspecting its work/state; diagnose memory by comparing RSS and trends; diagnose disk pressure with capacity, inode and I/O-latency checks.
- Linux uses memory for cache; cache is generally reclaimable. Do not force-clear caches as a routine memory fix.
- A service is managed background work; `systemd` manages units and `journalctl` reads the system journal. Unit names/log files differ by distribution.
- Permissions use owner/group/mode; privileged access should be limited. RHEL-family systems often use SELinux; Ubuntu commonly uses AppArmor.

## 8. Networking and packet filtering

- Applications use sockets. The normal Linux packet path goes through the kernel networking stack, routing/filter rules and the NIC driver.
- `nftables` is the modern Linux packet-filtering framework; `iptables` commands may be a compatibility interface depending on distribution; `ebtables` historically filters Ethernet bridge traffic.
- A firewall rule gives an action (for example accept/drop) within a chain/hook. Confirm the active backend and ruleset before troubleshooting.

## 9. Low-latency and IPC reminders

- DPDK poll-mode drivers let user-space applications access NIC RX/TX rings and poll queues instead of relying on per-packet interrupts. Polling can reduce path overhead but consumes dedicated CPU; pinning, queue ownership and NUMA placement matter.
- OpenOnload is a user-space networking acceleration option for supported NICs/applications; behavior depends on platform and configuration.
- RDMA supports remote memory operations with reduced CPU involvement versus conventional message copies; NIC, fabric, access model and application must all support it.
- A ring buffer is a circular producer/consumer queue. Lock-free behavior depends on the design and ownership rules; it is not automatic.
- A kernel socket buffer is kernel networking memory, not the same thing as an application ring buffer.

## 10. Quick review path

1. Compile a small C program with warnings enabled.
2. Trace its system calls with `strace`.
3. Follow its file descriptors and process state with `/proc`, `ps` and `waitpid` examples.
4. Inspect the target Linux device, driver, interface and service logs before changing configuration.
5. For embedded targets, verify CPU architecture, ABI, sysroot, libc and vendor-supported kernel/toolchain versions.

## References

- [C foundations for Linux system programming](../Docs/c_foundations_for_linux_system_programming.html)
- [Linux operating-system tutorial](../Docs/linux_operating_system_complete_tutorial.html)
- [Linux system calls and process fundamentals](../Docs/linux_system_calls_process_fundamentals.html)
- [Linux man-pages](https://man7.org/linux/man-pages/)
- [Linux kernel documentation](https://docs.kernel.org/)
- [DPDK Poll Mode Drivers](https://doc.dpdk.org/guides/prog_guide/ethdev/ethdev.html)
