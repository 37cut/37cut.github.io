# Fedora Linux
https://alt.fedoraproject.org

### Packages
https://cutt37.is-a.dev/files/fedora/src/1.md

### File configs
https://cutt37.is-a.dev/files/fedora/src/2.md

### Package manager
https://cutt37.is-a.dev/files/fedora/src/3.md

### Sound server
https://cutt37.is-a.dev/files/fedora/src/4.md

### Display manager
https://cutt37.is-a.dev/files/fedora/src/5.md

### Arc graphics
https://cutt37.is-a.dev/files/fedora/src/6.md

### set-default shell
`chsh -s /usr/bin/zsh`

### flameshot
```shell
sudo dnf in qt5-{qtbase,qttools} qt5-qtbase-gui
curl -L https://github.com/flameshot-org/flameshot/releases/download/v0.5.1/flameshot_0.5.1-fedora27-x86_64.rpm > flameshot_0.5.1-fedora27-x86_64.rpm
sudo rpm -i flameshot_0.5.1-fedora27-x86_64.rpm
```

### disable selinux
Edit /etc/selinux/config<br>
Find 'SELINUX=...' then replace 'enforcing' to 'disabled'.

`sudo grubby --update-kernel ALL --args selinux=0`

### disable \`default dirs
Edit $HOME/.config/user-dirs.dirs<br>
Remove the text inside the quotes.

### disable watchdog
Create /etc/modprobe.d/blacklist.conf<br>
Find your wdt via `lsmod`

Then add `blacklist your_module` into the file

### unused services
```shell
sudo systemctl disable avahi-daemon
sudo systemctl disable avahi-daemon.socket
```

### mask services
```shell
sudo systemctl mask sshd
sudo systemctl mask wsdd
sudo systemctl mask NetworkManager-wait-online.service
sudo systemctl mask NetworkManager-dispatcher.service
```

### chromium
Go to ___chrome://flags___

Search ___gemini___ and disable every options include gemini keyword<br>
Search ___optimization guide on device___ and disable it

To prevent chrome download ai models into this folder -> ___$HOME/.config/chromium/OptGuideOnDeviceModel___ <br>
You could make this folder inmutable:<br>
`sudo chattr +i $HOME/.config/chromium/OptGuideOnDeviceModel/`

## Notes

### system upgrade
```shell
sudo dnf upgrade --refresh
sudo dnf system-upgrade download --releasever=XX
sudo dnf system-upgrade reboot
```

### update rescue kernel
```shell
sudo rm /boot/*rescue*
sudo kernel-install add "$(uname -r)" "/lib/modules/$(uname -r)/vmlinuz"
```

### remove old kernel
`sudo dnf remove $(dnf repoquery --installonly --latest-limit=-1)`
