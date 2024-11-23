# Fedora netinstall guide

Here I use minimal install.<br>
If you're using laptop,<br>
you should check **Common NetworkManager Submodules**.

Install with: `sudo dnf in`

# Packages

- alacritty
- alsa-utils
- audacity
- bluez
- dbus-x11
- dunst
- flameshot
- gimp
- gvfs-archive
- htop
- i3
- light
- mousepad
- mpv
- NetworkManager-tui
- nodejs
- pcmanfm
- picom
- tlp
- vim-enhanced
- wine
- winetricks \**parameter with: --exclude=kf\\\**
- wqy-zenhei-fonts
- xarchiver
- zsh
- zsh-autosuggestions
- zsh-syntax-highlighting

# Configs

## Refresh the fonts
fc-cache -fv

## Wallpaper on loaded
Config xorg-x11-xdm: `vim /etc/X11/xdm/Xsetup_0`<br>
Write these codes into Xsetup\_0:<br>
```shell
/usr/bin/feh --borderless --no-xinerama --no-menus --no-fehbg --cache-size '16' --window-id ':0' --geometry '3840x2160' --bg-fill '/home/cutt37/.config/i3/Kano.png' &
```

## Add desktop target to Xorg and Xdm
Add .xsession: `touch .xsession && echo i3 > .xsession`<br>
Make .xession executeable: `chmod +x .xsession`

## Uninstall some add-ons
Uninstall some packages I dont need:<br>
xorg-x11-drv-{amdgpu,armada,ati,nouveau,openchrome,qxl,vmware}<br>
amd-{gpu,ucode}-firmware<br>
nvidia-gpu-firmware<br>
Remove with: `sudo dnf rm`

## Config shell, account
```shell
chsh -s /usr/bin/zsh
usermod -a -G audio your_account
```

## Disable selinux
`vim /etc/selinux/config`<br>
Find key 'SELINUX=...'
Replace enforcing to disabled(if available).

## Disable zram
`sudo dnf rm zram-generator-defaults`

## Disable fstrim
`sudo systemctl disable fstrim.timer`

## Minbrowser
[Install](https://minbrowser.org/) minbrowser
