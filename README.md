[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-speedtest.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-speedtest) ![Ansible Role](https://img.shields.io/ansible/role/47706?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47706?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47706?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-speedtest&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-speedtest) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-speedtest?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-speedtest?color=orange&style=flat-square)

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
speedtest_repo_debian_gpg_key: 379CE192D401AB61
speedtest_repo_debian: "deb https://ookla.bintray.com/debian generic main"
speedtest_repo_debian_filename: "{{ speedtest_app }}"
speedtest_repo_debian_desired_state: present

# EL family based
speedtest_repo_el_url: https://bintray.com/ookla/rhel/rpm
speedtest_repo_el_filename: /etc/yum.repos.d/speedtest.repo
speedtest_repo_el_filename_owner: root
speedtest_repo_el_filename_group: root
speedtest_repo_el_filename_mode: '0644'
```

### Variables table:

Variable                                | Value (default)                                       | Description
--------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
speedtest_app                           | speedtest                                             | Name of speedtest application package require to be installed i.e. `speedtest`
speedtest_app_desired_state             | present                                               | State of the speedtest_app package. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
speedtest_debian_pre_reqs               | apt-transport-https, dirmgr, gnupg1                   | Speedtest recommends the installation of both these packages on Debian family systems and as such, they are considered pre-requisites.
speedtest_debian_pre_reqs_desired_state | present                                               | Desired state for Speedtest pre-requisite apps on Debian family systems.
speedtest_repo_debian_gpg_key           | 379CE192D401AB61                                      | Speedtest GPG key required on Debian family systems
speedtest_repo_debian                   | "deb <https://ookla.bintray.com/debian> generic main" | Speedtest repo URL for Debain family systems.
speedtest_repo_debain_filename          | speedtest                                             | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems.
speedtest_repo_debian_desired_state     | present                                               | `present` indicates creating the repository file if it doesn't exist on Debian based systems. Alternative is `absent` (not recommended as it will prevent from installation of **speedtest** package).
speedtest_repo_el_url                   | <https://bintray.com/ookla/rhel/rpm>                  | URL to download the repo file for EL based systems.
speedtest_repo_el_filename              | /etc/yum.repos.d/speedtest.repo                       | File path for the speedtest repository to be saved as on EL based systems.
speedtest_repo_el_filename_owner        | root                                                  | Owner of /etc/yum.repos.d/speedtest.repo on EL based systems.
speedtest_repo_el_filename_group        | root                                                  | Group of /etc/yum.repos.d/speedtest.repo on EL based systems.
speedtest_repo_el_filename_mode         | '0644'                                                | Mode of /etc/yum.repos.d/speedtest.repo on EL based systems.

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
