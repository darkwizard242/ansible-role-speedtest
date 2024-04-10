[![build-test](https://github.com/darkwizard242/ansible-role-speedtest/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-speedtest/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-speedtest/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-speedtest/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/51713?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/51713?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/51713?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-speedtest&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-speedtest) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-speedtest&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-speedtest) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-speedtest&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-speedtest) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-speedtest&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-speedtest) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-speedtest?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-speedtest?color=orange&style=flat-square)

# Ansible Role: speedtest

Role to install (_by default_) [Ookla's Speedtest CLI](https://www.speedtest.net/apps/cli) package or uninstall (_if passed as var_) on Debian based systems and EL based systems. Speedtest CLI can be used for internet connection measurement.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
speedtest_app: speedtest
speedtest_app_desired_state: present

# Debian family based
speedtest_debian_pre_reqs:
  - apt-transport-https
  - dirmngr
  - gnupg1
speedtest_debian_pre_reqs_desired_state: present
speedtest_repo_debian_gpg_key: https://packagecloud.io/ookla/speedtest-cli/gpgkey
speedtest_repo_debian: "deb https://packagecloud.io/ookla/speedtest-cli/{{ ansible_distribution | lower }}/ {{ ansible_lsb['codename'] }} main"
speedtest_repo_debian_filename: "{{ speedtest_app }}"
speedtest_repo_debian_keyring_filename: "{{ speedtest_app }}.gpg"
speedtest_repo_debian_keyid: C525F88FCF3A7E56CE2CF59131EB3981E723ACAA
speedtest_repo_debian_desired_state: present

# EL family based
speedtest_repo_el_name: ookla_speedtest-cli
speedtest_repo_el_description: ookla_speedtest-cli
speedtest_repo_el_baseurl: "https://packagecloud.io/ookla/speedtest-cli/el/{{ ansible_distribution_major_version }}/$basearch"
speedtest_repo_el_gpgcheck: no
speedtest_repo_el_gpgkey: https://packagecloud.io/ookla/speedtest-cli/gpgkey
speedtest_repo_el_filename: "{{ speedtest_app }}"
speedtest_repo_el_state: present
speedtest_repo_el_enabled: yes
speedtest_repo_el_filename_owner: root
speedtest_repo_el_filename_group: root
speedtest_repo_el_filename_mode: '0644'
```

### Variables table:

Variable                                | Description
--------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
speedtest_app                           | Name of speedtest application package require to be installed i.e. `speedtest`
speedtest_app_desired_state             | State of the speedtest_app package. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
speedtest_debian_pre_reqs               | Speedtest recommends the installation of both these packages on Debian family systems and as such, they are considered pre-requisites.
speedtest_debian_pre_reqs_desired_state | Desired state for Speedtest pre-requisite apps on Debian family systems.
speedtest_repo_debian_gpg_key           | Speedtest GPG key url required on Debian family systems
speedtest_repo_debian                   | Speedtest repo URL for Debain family systems.
speedtest_repo_debain_filename          | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems.
speedtest_repo_debian_keyring_filename  | Name of the gpg file that will be stored at `/etc/apt/trusted.gpg.d/' on Debian based systems. Should end in `.gpg`
speedtest_repo_debian_keyid             | Key ID to import to ensure it hasn't changed. Download the key and use `gpg --show-keys <keyfile>` to determine the ID.
speedtest_repo_debian_desired_state     | `present` indicates creating the repository file if it doesn't exist on Debian based systems. Alternative is `absent` (not recommended as it will prevent from installation of **speedtest** package).
speedtest_repo_el_name                  | Repository name for Speedtest on EL based systems.
speedtest_repo_el_description           | Description to be added in EL based repository file for Speedtest.
speedtest_repo_el_baseurl               | Repository baseurl for Speedtest on EL based systems.
speedtest_repo_el_gpgcheck              | Boolean for whether to perform gpg check against Speedtest repository on EL based systems.
speedtest_repo_el_gpgkey                | GPG key for Speedtest repository.
speedtest_repo_el_state                 | `present` indicates creating the repository file if it doesn't exist on EL based systems. Alternative is absent (not recommended as it will prevent from installation of speedtest packages).
speedtest_repo_el_enabled               | Boolean to set so that Speedtest repository is enabled on EL based systems.
speedtest_repo_el_filename              | File path for the speedtest repository to be saved as on EL based systems.
speedtest_repo_el_filename_owner        | Owner of /etc/yum.repos.d/speedtest.repo on EL based systems.
speedtest_repo_el_filename_group        | Group of /etc/yum.repos.d/speedtest.repo on EL based systems.
speedtest_repo_el_filename_mode         | Mode of /etc/yum.repos.d/speedtest.repo on EL based systems.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **speedtest** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.speedtest
```

For customizing behavior of role (i.e. installing latest verion of **speedtest**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.speedtest
  vars:
    speedtest_apps_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **speedtest** packages) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.speedtest
  vars:
    speedtest_apps_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-speedtest/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
