# Fedora netinstall guide

Here I use minimal install.<br>
If you're using laptop,<br>
it's very important to check **Common NetworkManager Submodules**.<br>

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

If slim not loaded on startup, try this:<br>
`sudo systemctl disable multi-user.target`

- bluez
- chromium
- dbus-x11
- dunst
- flameshot
- gimp
- htop
- light
- mousepad
- mpv
- nodejs
- pcmanfm
- vim-enhanced
- wine
- winetricks \**parameter with: --exclude=kf\\\**<br>
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

Override the default ffmpeg, using ffmpeg from rpmfusion:

`sudo dnf in ffmpeg --allowerasing`
