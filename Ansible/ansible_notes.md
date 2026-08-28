hosts:lall
tasks:
    apt: 
    name : nginx
    state: present

    Ansible - hosts , variables, handlers , modules, tasks

    ansible.cfg

idempotent so repeated taasks re not re executed
Debug -- verbose

copy module 
copy moduel : src dst 
ansible-doc module doc
monitor logs

apt copy service file command
windows errros due to winrm issues


ansible group vars 
check roles tasks main.yaml syntax
dependencies

Role - defined directory structure for a entire solution --
    - roles - defulats main.yaml
    - tasks - main.yaml
    - handlers - main.yaml
    - files - static_files.txt
    - meta - - dependencies if any

Anisble vault - secrets create secrets.yaml
Ansible compliance --
ansivble vault  - audit loggin - security modules - rometheus


Mellanox RDMA - uses phyiscla DMA - nic directly reds from memoery and bypasses kernel
RDMA - kernel bypass


