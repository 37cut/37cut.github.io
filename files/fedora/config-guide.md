# fedora netinstall guide

Go to this [page](https://alt.fedoraproject.org/)<br>
Find 'Network Installers' and download.<br>

Here I use minimal install.<br>
If you want to connect to Internet,<br>
you should check **Common NetworkManager Submodules**.

# an example package list

- alacritty
- alsa-firmware
- alsa-sof-firmware
- alsa-utils
- audacity
- bluez
- dbus-x11
- dunst
- feh
- flameshot
- gdouros-symbola-fonts
- gimp
- google-noto-emoji-fonts
- gvfs-archive
- htop
- i3
- ibus
- ibus-libpinyin
- light
- mousepad
- mpv
- NetworkManager-tui
- nodejs
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

## uninstall some pkgs(if exist)
```shell
sudo dnf rm xorg-x11-drv-{amdgpu,armada,ati,nouveau,openchrome,qxl,vmware} \
amd-{gpu,ucode}-firmware nvidia-gpu-firmware xdg-desktop-portal
```

## config shell and account
```shell
chsh -s /usr/bin/zsh
usermod -a -G audio your_account
```

## wallpaper
Config xorg-x11-xdm: `vim /etc/X11/xdm/Xsetup_0`<br>
Write these codes into Xsetup\_0:<br>
```shell
/usr/bin/feh --borderless --no-xinerama --no-menus --no-fehbg --cache-size '16' --window-id ':0' --geometry '3840x2160' --bg-fill '/home/cutt37/.config/i3/Kano.png' &
```

## my configs
[Here](https://cutt37.is-a.dev/files/fedora/config.zip)

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
make .xession executeable: `chmod +x .xsession`<br>
then type this code to keep xdm running: `systemctl set-default graphical.target`

## minbrowser
[Install](https://minbrowser.org/)<br>
```shell
wget -O min-1.33.1-x86\_64.rpm https://github.com/minbrowser/min/releases/download/v1.33.1/min-1.33.1-x86\_64.rpm
```

## wine: Chinese font for wine
See chn\_font.reg under config.zip<br>
Extract it and run `wine regedit chn_font.reg`

## shutdown action after hibernate
Create a file under "/etc/systemd" called "sleep.conf"<br>
Then add these two lines of code:<br>
```shell
[Sleep]
HibernateMode=shutdown
```
And run `sudo systemctl daemon-reload`