# Fedora config

Install with: `sudo dnf in`<br>

## Packages

- NetworkManager-tui
- alacritty
- i3
- gvfs-archive
- xorg-x11-\\\* *parameter with: --exclude=xorg-x11-{xdm},xorg-x11-drivers*

Uninstall some packages I dont need:<br>
Remove with: `sudo dnf rm`<br>

xorg-x11-drv-{amdgpu,armada,ati,nouveau,openchrome,qxl,vmware}

- picom
- slim
- chromium
- pcmanfm
- vim-enhanced
- wine
- light
- dbus-x11
- winetricks \**parameter with: --exclude=kf\\\**<br>
- mousepad
- nodejs
- dunst
- gimp
- flameshot
- mpv
- bluez
- xarchiver
- zsh
- zsh-autosuggestions
- zsh-syntax-highlighting

## Files

- background.png

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

Override the default ffmpeg, install from rpmfusion.

`sudo dnf in ffmpeg --allowerasing`
