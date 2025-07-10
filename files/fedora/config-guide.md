# fedora netinstall guide

Go to this [page](https://alt.fedoraproject.org/)<br>
Find 'Network Installers' and download.<br>

Here I use minimal install.<br>
If you have a card which is wireless,<br>
then you should check **Common NetworkManager Submodules** this option.

# an example package list
- alacritty
- alsa-firmware
- alsa-sof-firmware
- alsa-utils
- audacity
- bleachbit
- bluez
- dbus-x11
- dunst
- feh
- flameshot
- gdouros-symbola-fonts
- gimp
- gvfs-archive
- htop
- i3
- ibus
- ibus-libpinyin
- light
- mousepad
- mpv
- NetworkManager-tui
- pcmanfm
- picom
- tlp
- vim-enhanced
- wqy-zenhei-fonts
- xarchiver
- xorg-x11-server-Xorg
- xorg-x11-xdm
- zsh
- zsh-autosuggestions
- zsh-syntax-highlighting

# configs

## refresh the fonts
```shell
fc-cache -fv
sudo fc-cache -fv
```

## uninstall some pkgs(if you need that, dont follow this)
```shell
sudo dnf rm xorg-x11-drv-{amdgpu,armada,ati,nouveau,openchrome,qxl,vmware} \
amd-{gpu,ucode}-firmware nvidia-gpu-firmware xdg-desktop-portal

sudo dnf rm {atheros,brcmfmac,cirrus-audio,mt7xxx,nxpwireless,tiwilink}-firmware
```

## config shell and account
```shell
chsh -s /usr/bin/zsh
usermod -a -G audio your_account
```

## dnf config
Edit /etc/dnf/dnf.conf<br>
Add `max_parellel_downloads=1` to it

## my configs
Download [here](https://cutt37.is-a.dev/files/fedora/config.zip)<br>
- .zshrc                        -> /home/account<br>
- alacritty.toml                -> /home/account/.config/alacritty<br>
- config                        -> /home/account/.config/i3<br>
- dunstrc                       -> /home/account/.config/dunst<br>
- 50-mouse-acceleration.conf    -> /usr/share/X11/xorg.conf.d<br>
- environment                   -> /etc<br>
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

## disable fstrim
`sudo systemctl disable fstrim.timer`

## mask tpm
```shell
sudo systemctl mask tpm2.target
```

## enable services
```shell
sudo systemctl enable xdm
sudo systemctl enable tlp
```

## about xorg-x11-xdm
Add .xsession: `touch .xsession && echo i3 > .xsession`<br>
make .xsession executeable: `chmod +x .xsession`<br>
then type this code to keep xdm running: `systemctl set-default graphical.target`

## minbrowser
[Install](https://minbrowser.org/)<br>
```shell
wget -O min-1.33.1-x86\_64.rpm https://github.com/minbrowser/min/releases/download/v1.33.1/min-1.33.1-x86\_64.rpm
```

# notes

## remove unused repos
Repository path: /etc/yum.repos.d
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
