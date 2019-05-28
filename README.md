Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

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
 
 
License
-------

GPLv3

Author Information
------------------

Jeremie CUADRADO <redbeard28>