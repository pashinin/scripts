#!/bin/bash

which pip || sudo apt-get install -y python-pip
which ansible || sudo -H pip install ansible -U
# apt-get ... ansible  # too old in repos

which sshd || sudo apt-get -y install ssh

# [ -f /root/.ssh/authorized_keys ] || (sudo mkdir /root/.ssh && sudo touch /root/.ssh/authorized_keys && sed -i '`cat ~/.ssh/id_rsa.pub`' /root/.ssh/authorized_keys)

# ansible-galaxy install -r requirements.yml

# ansible all -m ping
# ansible-playbook -i hosts desktop.yml --user root -f 10
# ansible-playbook -i hosts desktop.yml -f 10 --ask-become-pass
# ansible-playbook -i hosts desktop_as_user.yml -f 10

# TODO: should check that "python" is available
# python3.6 setup.py
