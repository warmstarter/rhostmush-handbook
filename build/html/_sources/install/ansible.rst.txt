.. _install-ansible:
.. index:: Ansible - Install, Install - Ansible

====================================
Installing using an ansible playbook
====================================

To begin, you will run the following command in a directory that will house your game::

   git clone https://github.com/RhostMUSH/trunk Rhost

You may also just run the yml file and ansible (ansible-playbook) to install your RhostMUSH engine::

   wget https://raw.githubusercontent.com/RhostMUSH/trunk/master/rhostinstall.yml
   ansible-playbook rhostinstall.yml
