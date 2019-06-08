Role Name
=========

A brief description of the role goes here.

Requirements
------------

This repository holds an `Ansible <http://www.ansible.com/home>`_ role
that is installable using ``ansible-galaxy``.  This role contains
tasks used to install and set up a telegraf minimal install for:

    - debian (tested OK)
    - centos (tested OK)
    - redhat (not yet tested)
    - windows (dev in progress...)


Contributing
------------

If you think you've found a bug or are interested in contributing to
this project check out `redbeard28.telegraf on Github
<https://github.com/redbeard28/redbeard28.telegraf>`_.

Installation
------------

Create an ``ansible.cfg`` file in your project directory to tell
Ansible where to install your roles 

````yaml
[defaults]
roles_path = roles:external_roles
vault_password_file = vault/.vault_password
host_key_checking = False
log_path = tmp/ansible.log
local_tmp = tmp/.ansible/tmp
retry_files_enabled = True
retry_files_save_path = tmp/.ansible/ansible-retry
force_color = 1
forks = 50
callback_whitelist = profile_tasks
timeout = 30
[ssh_connection]
ssh_args = -i ~/.ssh/id_rsa -o ControlMaster=auto -o ControlPersist=30m
control_path = ~/.ssh/ansible-%%r@%%h:%%p
scp_if_ssh = True
[privilege_escalation]
become=true
````



Role Variables
--------------
```yaml

http_proxy: ''

base_telegraf_user: 'telegraf'
base_telegraf_group: 'telegraf'
base_telegraf_service_name: 'telegraf'
base_telegraf_dir_metrics: '/var/log/telegraf'
base_telegraf_file_metrics: 'metrics.log'
base_telegraf_metric_interval: '60s'
base_telegraf_logrotate_file: '/etc/logrotate.d/telegraf'
base_telegraf_debug_mode: 'false'
```

````yaml
base_telegraf_ansible_message: "Managed by ansible. This file was modified {{ ansible_date_time.weekday }} {{ ansible_date_time.day }}/{{ ansible_date_time.month }}/{{ ansible_date_time.year }} at {{ ansible_date_time.time }}"
base_telegraf_config_basedir: '/etc/telegraf'
base_telegraf_config_extradir: "{{ base_telegraf_config_basedir }}/telegraf.d"
base_telegraf_dir_base: '/etc/telegraf'
base_telegraf_dir_logs: "{{ base_telegraf_dir_base }}/logs"
base_telegraf_file_logs: 'telegraf.log'
base_telegraf_python_package_prefix: 'python35'
base_telegraf_python_version: '3.5'
base_telegraf_python_package:
  - "{{ base_telegraf_python_package_prefix }}"
  - "{{ base_telegraf_python_package_prefix }}-pip"
base_telegraf_pip_modules:
  - 'setuptools'
  - 'pyyaml'
base_telegraf_rotate_day: 7

base_telegraf_debian_python_package_prefix: 'python3.5'
base_telegraf_debian_python_version: '3'
base_telegraf_debian_python_package:
  - "{{ base_telegraf_debian_python_package_prefix }}"
  - "python{{ base_telegraf_debian_python_version }}-pip"
````

----

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

````yaml

- name: "Deploy telegraf"
  hosts: all
  become: yes
  vars_files:
    - secrets/secrets.yml
  roles:
    - { role: roles/redbeard28.telegraf, tags: [redbeard28.telegraf] }
````
 
Molecule Framework
-------------
Please see (molecule documentation)[https://molecule.readthedocs.io/en/stable/configuration.html]

```yaml
driver:
  name: docker
platforms:
  - name: instance
    hostname: instance
    image: image_name:tag
    dockerfile: Dockerfile.j2
    pull: True|False
    pre_build_image: True|False
    registry:
      url: registry.example.com
      credentials:
        username: $USERNAME
        password: $PASSWORD
        email: user@example.com
    override_command: True|False
    command: sleep infinity
    pid_mode: host
    privileged: True|False
    security_opts:
      - seccomp=unconfined
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:ro
    tmpfs:
      - /tmp
      - /run
    capabilities:
      - SYS_ADMIN
    exposed_ports:
      - 53/udp
      - 53/tcp
    published_ports:
      - 0.0.0.0:8053:53/udp
      - 0.0.0.0:8053:53/tcp
    ulimits:
      - nofile:262144:262144
    dns_servers:
      - 8.8.8.8
    networks:
      - name: foo
      - name: bar
    network_mode: host
    purge_networks: true
    docker_host: tcp://localhost:12376
    env:
      FOO: bar
    restart_policy: on-failure
    restart_retries: 1
    buildargs:
        http_proxy: http://proxy.example.com:8080/
```
 
License
-------

GPLv3

Author Information
------------------

Jeremie CUADRADO <redbeard28>