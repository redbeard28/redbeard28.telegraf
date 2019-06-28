import os
import pytest

import testinfra.utils.ansible_runner
# https://github.com/ansible/molecule/issues/2083

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# We need to search for key words in files
@pytest.mark.parametrize('file, content', [
  ("/etc/telegraf/telegraf.conf", "global"),
  ("/etc/telegraf/telegraf.d/system.conf", "inputs.cpu")
])

def test_files(host, file, content):
    file = host.file(file)
    assert file.exists
    assert file.contains(content)

# Function to get ansible vars from defaults and vars folders
@pytest.fixture
def get_vars(host):
    defaults_files = "file=../../defaults/main.yml name=role_defaults"
    vars_files = "file=../../vars/main.yml name=role_vars"

    ansible_vars = host.ansible(
        "include_vars",
        defaults_files)["ansible_facts"]["role_defaults"]

    ansible_vars.update(host.ansible(
        "include_vars",
        vars_files)["ansible_facts"]["role_vars"])
    print(ansible_vars)
    return ansible_vars

# Verify if user telegraf exist
def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("telegraf")

# Verify if group telegraf exist
def test_group_file(host):
    group = host.file("/etc/group")
    assert group.contains("telegraf")
    #assert group.contains == get_vars['base_telegraf_group']

# Verify if telegraf.conf exist with the good user/group
def test_telegraf_conf_file(host):
    config = host.file('/etc/telegraf/telegraf.conf')
    assert config.exists
    assert config.user == "telegraf"
    assert config.group == "telegraf"

# Verify if system.conf exist with the good user/group
def test_system_inputs_file(host,get_vars):
    config_dir_path = get_vars['base_telegraf_config_basedir']
    config = host.file(config_dir_path + '/telegraf.d/system.conf')
    assert config.exists
    # assert config.user == 'telegraf'
    # assert config.group == 'telegraf'
    assert config.user == get_vars['base_telegraf_user']
    assert config.group == get_vars['base_telegraf_group']


# Verify if metrics file exist with the good user/group
def test_telegraf_metrics_file(host,get_vars):
    config = host.file(get_vars['base_telegraf_dir_metrics'] + '/' + get_vars['base_telegraf_file_metrics'])
    assert config.exists
    assert config.user == 'telegraf'
    assert config.group == 'telegraf'

# Verify if package for telegraf is installed and running
def test_telegraf_is_installed(host):
    telegraf = host.package("telegraf")
    assert telegraf.is_installed

# Verify if service for telegraf is installed and running
def test_telegraf_running_and_enabled(host):
    srv_telegraf = host.service("telegraf")
#    assert srv_telegraf.is_running
    assert srv_telegraf.is_enabled


def check_ansible_play(host):
    """
    Verify that a package is installed using Ansible
    package module
    """
    assert not host.ansible("package", "name=telegraf state=present")["changed"]
