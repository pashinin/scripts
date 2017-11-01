#!/bin/bash

which pip || sudo apt-get install -y python-pip
which ansible || sudo -H pip install ansible -U
which sshd || sudo apt-get -y install ssh

wget -O /tmp/server.yml 'https://raw.githubusercontent.com/pashinin/scripts/master/ubuntu-setup/server.yml'
ansible-playbook /tmp/server.yml
# ansible-playbook -i hosts desktop_as_user.yml -f 10
