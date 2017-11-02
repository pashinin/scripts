#!/bin/bash

which pip || sudo apt-get install -y python-pip
which ansible || sudo -H pip install ansible -U
which sshd || sudo apt-get -y install ssh

cd /tmp
[ -d scripts ] || git clone https://github.com/pashinin/scripts.git
[ ! -d scripts ] || (cd scripts; git pull)
cd scripts/ubuntu-setup

# curl -o hosts https://raw.githubusercontent.com/pashinin/scripts/master/ubuntu-setup/hosts
# curl -o server.yml https://raw.githubusercontent.com/pashinin/scripts/master/ubuntu-setup/server.yml
ansible-playbook -i hosts server.yml
# ansible-playbook -i hosts desktop_as_user.yml -f 10
