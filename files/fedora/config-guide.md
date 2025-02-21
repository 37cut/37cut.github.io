# Fedora netinstall guide

Go to this [page](https://alt.fedoraproject.org/)<br>
Find 'Network Installers' and download.<br>

Here I use minimal install.<br>
If you want to connect to Internet,<br>
you should check **Common NetworkManager Submodules**.

# Packages to download(for me)

- alacritty
- alsa-utils
- audacity
- bluez
- dbus-x11
- dunst
- feh
- flameshot
- gdouros-symbola-fonts
- gimp
- gnome-boxes
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

# Configs

## Refresh the fonts
```shell
fc-cache -fv
sudo fc-cache -fv
```

## Uninstall some add-ons(if exist)
```shell
sudo dnf rm xorg-x11-drv-{amdgpu,armada,ati,nouveau,openchrome,qxl,vmware} \
amd-{gpu,ucode}-firmware nvidia-gpu-firmware xdg-desktop-portal
```

## Config shell, account
```shell
chsh -s /usr/bin/zsh
usermod -a -G audio your_account
```

## Wallpaper on loaded
Config xorg-x11-xdm: `vim /etc/X11/xdm/Xsetup_0`<br>
Write these codes into Xsetup\_0:<br>
```shell
/usr/bin/feh --borderless --no-xinerama --no-menus --no-fehbg --cache-size '16' --window-id ':0' --geometry '3840x2160' --bg-fill '/home/cutt37/.config/i3/Kano.png' &
```

## Disable selinux
`vim /etc/selinux/config`<br>
Find key 'SELINUX=...'
Replace enforcing to disabled(if available).

## Disable zram
`sudo dnf rm zram-generator`

## Disable fstrim
`sudo systemctl disable fstrim.timer`

## Enable services
```shell
sudo systemctl enable xdm
sudo systemctl enable tlp
```

## About xorg-x11-xdm
Add .xsession: `touch .xsession && echo i3 > .xsession`<br>
make .xession executeable: `chmod +x .xsession`
then type this code to keep xdm running: `systemctl set-default graphical.target`

## Minbrowser
[Install](https://minbrowser.org/) minbrowser or using wget instead
wget -O min-1.33.1-x86\_64.rpm https://github.com/minbrowser/min/releases/download/v1.33.1/min-1.33.1-x86\_64.rpm

## wine中文字体: Chinese font for wine
See chn\_font.reg under config.zip
Extract and execute:
`wine regedit chn_font.reg`
