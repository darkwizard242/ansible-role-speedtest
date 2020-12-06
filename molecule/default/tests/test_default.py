import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = "speedtest"
PACKAGE_BINARY = "/usr/bin/speedtest"
REPO_DEBIAN_FILE = "/etc/apt/sources.list.d/speedtest.list"
REPO_EL_FILE = "/etc/yum.repos.d/speedtest.repo"


def test_speedtest_package_installed(host):
    """
    Tests if speedtest is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_speedtest_binary_exists(host):
    """
    Tests if speedtest binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_speedtest_binary_file(host):
    """
    Tests if speedtest binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_speedtest_binary_which(host):
    """
    Tests the output to confirm speedtest's binary location.
    """
    assert host.check_output('which speedtest') == PACKAGE_BINARY


def test_trivy_repo_exists(host):
    """
    Tests if speedtest repo file exists.
    """
    assert host.file(REPO_DEBIAN_FILE).exists or \
        host.file(REPO_EL_FILE).exists


def test_trivy_repo_file(host):
    """
    Tests if speedtest repo file is file type.
    """
    assert host.file(REPO_DEBIAN_FILE).is_file or \
        host.file(REPO_EL_FILE).is_file
