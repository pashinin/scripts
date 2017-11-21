To clone this repo to `/tmp/scripts/`, update and run provision:

On server:

    bash <(wget -q https://raw.githubusercontent.com/pashinin/scripts/master/ubuntu-setup/server.sh -O -)



## From repo folder

This will run `ansible-playbook ...` on all 3 machines:

    make provision
