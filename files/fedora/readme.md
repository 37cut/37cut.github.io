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

### Other settings
https://cutt37.is-a.dev/files/fedora/src/7.md

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
