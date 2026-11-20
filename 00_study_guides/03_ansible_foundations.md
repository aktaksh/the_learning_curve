# Ansible playbooks, roles and repeatable changes

## Playbooks and idempotence

A play selects inventory hosts and contains tasks. Each task calls a module with arguments. An idempotent module compares the current state with the desired state and avoids unnecessary changes when they already match. Tasks are still evaluated on repeated runs; idempotence does not mean they are never executed again. Arbitrary shell and command tasks need explicit change detection when repeatability matters.

## Corrected package example

```yaml
---
- name: Install nginx on Debian-family lab hosts
  hosts: webservers
  become: true
  tasks:
    - name: Ensure nginx is installed
      ansible.builtin.apt:
        name: nginx
        state: present
        update_cache: true
```

`webservers` must match an inventory group. The apt module applies to Debian-family systems; choose a suitable module for other distributions. Indentation and list markers matter in YAML.

## Validation and troubleshooting

```bash
ansible-playbook -i inventory.ini playbook.yml --syntax-check
ansible-playbook -i inventory.ini playbook.yml --list-hosts
ansible-playbook -i inventory.ini playbook.yml --check --diff
ansible-doc ansible.builtin.copy
```

Syntax checking validates parsing, not connectivity or successful application. Check mode support depends on the module; it is not a universal guarantee of zero side effects. Diff output may expose configuration content. Use verbosity to inspect failures, inventory matching and transport issues. Windows hosts commonly require correctly configured WinRM or another supported connection method.

## Roles, variables and secrets

A role conventionally groups `tasks/main.yml`, `handlers/main.yml`, `defaults/main.yml`, `vars/main.yml`, `files/`, `templates/` and `meta/main.yml`. Handlers respond to task notifications. Group variables configure inventory groups; role defaults provide low-precedence values that can be overridden.

Ansible Vault encrypts secret files or values at rest. It is not an audit-logging or compliance solution by itself. Keep passwords out of source control and review how secrets appear in task output.

## Sources and original notes

- [Ansible module behaviour](https://docs.ansible.com/projects/ansible/latest/module_plugin_guide/modules_intro.html)
- [Check and diff modes](https://docs.ansible.com/projects/ansible/latest/playbooks_checkmode.html)
- [Original Ansible notes](../04_ansible/ansible_notes.md)
