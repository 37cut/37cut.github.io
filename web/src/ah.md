# System maintainence

### system upgrade
sudo dnf upgrade --refresh<br>
sudo dnf system-upgrade download --releasever=XX<br>
sudo dnf system-upgrade reboot

### update rescue kernel
sudo rm /boot/*rescue*<br>
sudo kernel-install add "$(uname -r)" "/lib/modules/$(uname -r)/vmlinuz"

### remove old kernel
sudo dnf remove $(dnf repoquery --installonly --latest-limit=-1)
