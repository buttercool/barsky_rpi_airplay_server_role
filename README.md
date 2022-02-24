# barsky_rpi_airplay_server_role
Barsky RPi Airplay Server Ansible Role
## Install
- Copy this whole directory (the parent directory of this README.txt and it's contents) into you Ansible roles directory.
- Adjust the contents of the roles 'files' directory to reflext the hostnames of your RPi's. TL;DR edit every instance of 'mbox-common' or 'mbox-bedrooms' in the file names.
- Adjust the contents of the roles 'tasks' main.yml file and replace every instance of 'mbox-common' or 'mbox-bedrooms' with your own names (this should be consistent with the names you changed for the files as well)
- Adjust your *asound.conf files to reflect what you are naming each L/R channel and any combined outputs (like ALL).
- Adjust the shairport-sync*.conf files to reflect your Airplay Zone naming, also change output names to match your *asound.conf files, finally define a connection password if you want.

## Reference Role Directory Structure and Contents
~~~
~/ansible/roles/barsky_rpi_airplay_server# tree
.
├── files
│   ├── barsky-volume-api.service
│   ├── mbox-bedrooms-asound.conf
│   ├── mbox-bedrooms-shairport-sync.conf
│   ├── mbox-bedrooms-shairport-syncAllBedrooms.conf
│   ├── mbox-bedrooms-shairport-syncKidsBedroom.conf
│   ├── mbox-common-asound.conf
│   ├── mbox-common-shairport-sync.conf
│   ├── mbox-common-shairport-syncAll.conf
│   ├── shairport-sync.service (NOT in use currently)
│   ├── shairport-sync@.service
│   └── volume-api.py
├── handlers
│   └── main.yml
└── tasks
    └── main.yml
~~~
