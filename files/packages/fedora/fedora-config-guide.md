# Fedora netinstall guide

Here I use minimal install.<br>
If you're using laptop,<br>
it's very important to check **Common NetworkManager Submodules**.

Install with: `sudo dnf in`

## Packages

- alacritty
- alsa-utils
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
- vim-enhanced
- wine
- winetricks \**parameter with: --exclude=kf\\\**<br>
- wqy-zenhei-fonts

fc-cache -fv

- xarchiver
- xorg-x11-\\\* *parameter with: --exclude=xorg-x11-drivers*

Config xorg-x11-xdm: `vim /etc/X11/xdm/Xsetup_0`<br>
Write these codes into Xsetup\_0:<br>
```shell
export HOME=/home/cutt37
/usr/bin/feh --borderless --no-xinerama --no-menus --no-fehbg --cache-size '16' --window-id ':0'  --geometry '3840x2160' --bg-fill '/home/cutt37/.config/i3/Kano.png' &
```

Add .xsession: `touch .xsession && echo i3 > .xsession`<br>
Make .xession executeable: `chmod +x .xsession`


Uninstall some packages I dont need:<br>
xorg-x11-drv-{amdgpu,armada,ati,nouveau,openchrome,qxl,vmware}<br>
Remove with: `sudo dnf rm`

- zsh
- zsh-autosuggestions
- zsh-syntax-highlighting

## Configs

```shell
chsh -s /usr/bin/zsh
usermod -a -G audio your_account
```

Add rpmfusion *free* repos:

```shell
sudo dnf install \
https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
```

Override the default ffmpeg, using ffmpeg from rpmfusion:

`sudo dnf in ffmpeg --allowerasing`

Disable zram

`sudo dnf rm zram-generator-defaults`

[Install](https://minbrowser.org/) minbrowser
