# Fedora installation guide

Go to this [page](https://alt.fedoraproject.org/)<br>

I will use i3 desktop<br>

# Configs

## things to add
- 7zip-standalone
- alacritty
- audacity
- dbus-x11
- dunst
- feh
- gimp
- gvfs-archive
- htop
- i3
- ibus
- ibus-pinyin
- langpacks-en
- light
- mousepad
- mpv
- NetworkManager-tui
- pcmanfm
- picom
- tlp
- vim-enhanced
- xarchiver
- xorg-x11-server-Xorg
- xorg-x11-xdm
- zsh
- zsh-autosuggestions
- zsh-syntax-highlighting

## things to remove
- firefox
- gnome-abrt
- nano
- xfce4-terminal
- amd-gpu-firmware
- nvidia-gpu-firmware
- amd-ucode-firmware
- tiwilink-firmware
- qcom-wwan-firmware
- nxpwireless-firmware
- mt7xxx-firmware
- libertas-firmware
- brcmfmac-firmware
- atheros-firmware
- lightdm (be careful with this one)

## set default shell
`chsh -s /usr/bin/zsh`

## dnf config
Edit /etc/dnf/dnf.conf<br>
- `max_parellel_downloads=1`
- `install_weak_deps=False`
- `exclude=flameshot`

## pipewire -\> pulseaudio
```shell
sudo dnf rm pipewire\*
sudo dnf in pulseaudio
```

## my configs
Download [here](https://cutt37.is-a.dev/files/fedora/config-files.zip)<br>
- .Xresources                   -> $HOME<br>
- .zshrc                        -> $HOME<br>
- alacritty.toml                -> $HOME/.config/alacritty<br>
- config                        -> $HOME/.config/i3<br>
- dunstrc                       -> $HOME/.config/dunst<br>
- 50-mouse-acceleration.conf    -> /usr/share/X11/xorg.conf.d<br>
- 20-intel.conf                 -> /etc/X11/xorg.conf.d<br>
- environment                   -> /etc - <b>This could be a backup. Please edit /etc/profile instead</b><br>
- vimrc                         -> /etc<br>
- i3status.conf                 -> /etc<br>
- tlp.conf                      -> /etc<br>
- picom.conf                    -> /etc/xdg<br>
- systemd/logind.conf           -> /etc/systemd<br>
- systemd/sleep.conf            -> /etc/systemd<br>
- xdm/Xresources                -> /etc/X11/xdm<br>
- xdm/Xsetup\_0                 -> /etc/X11/xdm

## disable selinux
`vim /etc/selinux/config`<br>
Find key 'SELINUX=...'<br>
Replace enforcing to disabled(if available).

## disable zram
`sudo dnf rm zram-generator`

## unused services
```shell
sudo systemctl disable fstrim.timer
sudo systemctl disable sshd
sudo systemctl disable avahi-daemon
sudo systemctl disable avahi-daemon.socket
```

## mask services
```shell
sudo systemctl mask NetworkManager-wait-online
sudo systemctl mask tpm2.target
```

## edit xorg-x11-xdm
Edit .xsession:
- `touch .xsession && echo i3 > .xsession`<br>
Make .xsession executeable: `chmod +x .xsession`<br>
Then type this code to keep xdm running: `systemctl set-default graphical.target`

## regen the grub file
`sudo grub2-mkconfig -o /boot/grub2/grub.cfg`

## minbrowser
`curl -L https://github.com/minbrowser/min/releases/download/v1.30.0/min-1.30.0-x86_64.rpm > min-1.30.0-x86_64.rpm`

## flameshot
```shell
sudo dnf in qt5-{qtbase,qttools},qt5-qtbase-gui
curl -L https://github.com/flameshot-org/flameshot/releases/download/v0.5.1/flameshot_0.5.1-fedora27-x86_64.rpm > flameshot_0.5.1-fedora27-x86_64.rpm
```

# Notes

## remove unused repos
Repository path: /etc/yum.repos.d<br>
Remove within `rm` command

## system upgrade
```shell
sudo dnf upgrade --refresh
sudo dnf system-upgrade download --releasever=XX
sudo dnf system-upgrade reboot
```

## update rescue kernel
```shell
sudo rm /boot/*rescue*
sudo kernel-install add "$(uname -r)" "/lib/modules/$(uname -r)/vmlinuz"
```

## remove old kernel
`sudo dnf remove $(dnf repoquery --installonly --latest-limit=-1)`
