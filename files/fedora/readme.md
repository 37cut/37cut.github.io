# Fedora

Go to this [page](https://alt.fedoraproject.org/)

I will use i3 desktop

## Configs

### things to add
- 7zip-standalone ___;and type this command `sudo ln -s /usr/libexec/7zip/7z.so /bin/7z.so`___
- alacritty
- alsa-plugins-pulseaudio
- audacity
- dbus-x11
- dunst
- feh
- gimp
- gvfs-archive
- htop
- i3
- ibus
- ibus-pinyin ___;I recommended reinstall ibus___
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

### things to remove
___;know your device first!!___
- abrt
- firefox
- gnome-abrt
- gnome-disk-utility
- ibus-{anthy,chewing,m17n,hangul,table}
- nano
- pavucontrol
- plymouth
- setroubleshoot
- xorg-x11-drv-{intel,amdgpu,ati,nouveau,openchrome,qxl,vmware}
- xfce4-terminal
- zram-generator
- {amd,nvidia}-gpu-firmware
- {amd-ucode,mt7xxx}-firmware
- {atheros,brcmfmac,libertas,nxpwireless,qcom-wwan,tiwilink}-firmware
- cirrus-audio-firmware
- lightdm ___;beware this___

### my configs
Download [here](https://cutt37.is-a.dev/files/fedora/files.cutt37)
- .Xresources                   -> $HOME
- .zshrc                        -> $HOME
- alacritty.toml                -> $HOME/.config/alacritty
- config                        -> $HOME/.config/i3
- dunstrc                       -> $HOME/.config/dunst
- mimeapps.list                 -> /usr/share/applications
- 50-mouse-acceleration.conf    -> /usr/share/X11/xorg.conf.d
- environment                   -> /etc ___;Partial ENV keys does not function properly. I suggest edit /etc/profile instead___
- vimrc                         -> /etc
- i3status.conf                 -> /etc
- tlp.conf                      -> /etc
- picom.conf                    -> /etc/xdg
- xdm/xdm-config                -> /etc/X11/xdm
- xdm/Xresources                -> /etc/X11/xdm
- xdm/Xsetup                    -> /etc/X11/xdm

## Settings

### disable tpm2
Go to your bios and then disable it.

### zsh as default shell
`chsh -s /usr/bin/zsh`

### dnf
Edit /etc/dnf/dnf.conf
- `max_parellel_downloads=1`
- `install_weak_deps=False`
- `exclude=flameshot`

### pipewire -\> pulseaudio
```shell
sudo dnf rm pipewire\*
sudo dnf in pulseaudio
```

### force every sound goes through pulseaudio
Add these line to /etc/asound.conf:
```shell
pcm.!default {
    type pulse
}

ctl.!default {
    type pulse
}
```

### force PostMixer channel off
Go to this folder: <u>/usr/share/alsa/ucm2</u>

Find the folder matched your sound devices,<br>
`sudo vim /usr/share/alsa/ucm2/Intel/sof-hda-dsp/HiFi-sof.conf` for example

Find the line: ___cset "name='${var:PostMixerAnalogPlaybackDrcSwitch ${var:\_\_drcswitch}"___ <br>
Then change the value: ___${var:\_\_drcswitch}___ to ___off___

### disable selinux
`vim /etc/selinux/config`
Find key 'SELINUX=...'<br>
Replace enforcing to disabled(if available).

### disable `default dirs
Edit $HOME/.config/user-dirs.dirs<br>
Remove the text inside the double quotes.

### unused services
```shell
sudo systemctl disable fstrim.timer
sudo systemctl disable sshd
sudo systemctl disable avahi-daemon
sudo systemctl disable avahi-daemon.socket
```

### mask services
```shell
sudo systemctl mask NetworkManager-wait-online
sudo systemctl mask NetworkManager-dispatcher.service
```

### xorg-x11-xdm
Create .xsession: `touch .xsession && echo i3 > .xsession`<br>
Make .xsession executeable: `chmod +x .xsession`<br>
Then type this command to activate xdm on next startup: `systemctl set-default graphical.target`

and finally enable xdm.service

### minbrowser
`curl -L https://github.com/minbrowser/min/releases/download/v1.35.5/min-1.35.5-x86_64.rpm > min-1.35.5-x86_64.rpm`

### flameshot
```shell
sudo dnf in qt5-{qtbase,qttools} qt5-qtbase-gui
curl -L https://github.com/flameshot-org/flameshot/releases/download/v0.5.1/flameshot_0.5.1-fedora27-x86_64.rpm > flameshot_0.5.1-fedora27-x86_64.rpm
```

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
