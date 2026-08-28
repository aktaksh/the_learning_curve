// mydevice.cpp

extern "C" {
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/uaccess.h>
#include <linux/init.h>
#include <linux/types.h>
}

#define DEVICE_NAME "mydevice"

class MyDeviceDriver {
public:
    static int open(struct inode *inode, struct file *file)
    {
        printk(KERN_INFO "mydevice: Device opened\n");
        return 0;
    }

    static ssize_t read(struct file *file,
                        char __user *buf,
                        size_t len,
                        loff_t *offset)
    {
        const char msg[] = "Hello User\n";
        size_t msg_len = sizeof(msg);

        /*
         * Prevent repeated reads from returning the same data forever.
         * Without this, cat /dev/mydevice may loop because EOF is never reached.
         */
        if (*offset > 0)
            return 0;

        if (len < msg_len)
            msg_len = len;

        if (copy_to_user(buf, msg, msg_len))
            return -EFAULT;

        *offset += msg_len;

        return msg_len;
    }

    static ssize_t write(struct file *file,
                         const char __user *buf,
                         size_t len,
                         loff_t *offset)
    {
        char kbuf[128];
        size_t copy_len = len;

        if (copy_len >= sizeof(kbuf))
            copy_len = sizeof(kbuf) - 1;

        if (copy_from_user(kbuf, buf, copy_len))
            return -EFAULT;

        kbuf[copy_len] = '\0';

        printk(KERN_INFO "mydevice: Data written from user: %s\n", kbuf);

        return len;
    }

    static int release(struct inode *inode, struct file *file)
    {
        printk(KERN_INFO "mydevice: Device closed\n");
        return 0;
    }
};

static struct file_operations fops = {
    .owner   = THIS_MODULE,
    .open    = MyDeviceDriver::open,
    .read    = MyDeviceDriver::read,
    .write   = MyDeviceDriver::write,
    .release = MyDeviceDriver::release,
};

static int major_number = 0;

static int __init my_init(void)
{
    major_number = register_chrdev(0, DEVICE_NAME, &fops);

    if (major_number < 0) {
        printk(KERN_ERR "mydevice: Failed to register character device\n");
        return major_number;
    }

    printk(KERN_INFO "mydevice: Driver loaded. Major number = %d\n",
           major_number);

    printk(KERN_INFO "mydevice: Create device using:\n");
    printk(KERN_INFO "mydevice: sudo mknod /dev/%s c %d 0\n",
           DEVICE_NAME, major_number);

    return 0;
}

static void __exit my_exit(void)
{
    unregister_chrdev(major_number, DEVICE_NAME);

    printk(KERN_INFO "mydevice: Driver unloaded\n");
}

module_init(my_init);
module_exit(my_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Ankeit");
MODULE_DESCRIPTION("Simple character device driver written with C++-style structure");