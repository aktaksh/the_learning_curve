# Ansible — quick refresher

## Building blocks
A play targets inventory hosts. Tasks invoke modules; variables supply configuration. Handlers run when notified by changed tasks. ansible.cfg controls settings.

Idempotent modules evaluate the desired state on repeated runs and avoid unnecessary changes. Tasks still run; command/shell tasks are not automatically idempotent.

## Valid playbook example
```yaml
---
- name: Install nginx on Debian-family hosts
  hosts: webservers
  become: true
  tasks:
    - name: Ensure nginx is installed
      ansible.builtin.apt:
        name: nginx
        state: present
```

Use an inventory group named webservers. apt is for Debian-family systems; use a suitable module on RHEL.

## Roles and variables
- tasks/main.yml: role tasks.
- handlers/main.yml: notified actions.
- defaults/main.yml: overridable defaults.
- vars/main.yml: role variables.
- files/ and templates/: static and rendered content.
- meta/main.yml: metadata and dependencies.
- group_vars/: configuration for inventory groups.

## Checks and troubleshooting
```bash
ansible-playbook -i inventory.ini playbook.yml --syntax-check
ansible-playbook -i inventory.ini playbook.yml --list-hosts
ansible-playbook -i inventory.ini playbook.yml --check --diff
ansible-doc ansible.builtin.copy
```

Syntax checks do not prove remote connectivity. Check-mode support varies by module; diff output may reveal secrets. Use verbosity to inspect inventory, authentication and transport failures. Windows targets commonly use WinRM.

## Secrets and scope
Ansible Vault encrypts values/files at rest; it does not provide compliance or audit logging by itself. Modules such as copy, template, file, service and package manage different resource types.

RDMA is a separate networking topic: supported NICs can access registered memory through DMA. It is not an Ansible feature.

References: [Modules](https://docs.ansible.com/projects/ansible/latest/module_plugin_guide/modules_intro.html), [Check mode](https://docs.ansible.com/projects/ansible/latest/playbooks_checkmode.html).
