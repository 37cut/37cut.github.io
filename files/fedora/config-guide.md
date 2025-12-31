# Fedora installation guide

Go to this [page](https://alt.fedoraproject.org/)<br>

I will use i3 desktop<br>

## Configs

### things to add
- 7zip-standalone
- alacritty
- alsa-plugins-pulse
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

### things to remove
- firefox
- gnome-abrt
- gnome-disk-utility
- nano
- xorg-x11-drv-intel
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
- cirrus-audio-firmware
- lightdm (be careful with this one)

### my configs
Download [here](https://cutt37.is-a.dev/files/fedora/config-files.cutt37)<br>
- .Xresources                   -> $HOME
- .zshrc                        -> $HOME
- alacritty.toml                -> $HOME/.config/alacritty
- config                        -> $HOME/.config/i3
- dunstrc                       -> $HOME/.config/dunst
- 50-mouse-acceleration.conf    -> /usr/share/X11/xorg.conf.d
- 20-intel.conf                 -> /etc/X11/xorg.conf.d
- environment                   -> /etc - <b>This could be a backup. Please edit /etc/profile instead</b>
- vimrc                         -> /etc
- i3status.conf                 -> /etc
- tlp.conf                      -> /etc
- picom.conf                    -> /etc/xdg
- systemd/logind.conf           -> /etc/systemd
- xdm/xdm-config                -> /etc/X11/xdm
- xdm/Xresources                -> /etc/X11/xdm
- xdm/Xsetup                    -> /etc/X11/xdm

## Settings

### disable tpm2
Go to your bios then disable it.

### set default shell
`chsh -s /usr/bin/zsh`

### dnf config
Edit /etc/dnf/dnf.conf<br>
- `max_parellel_downloads=1`
- `install_weak_deps=False`
- `exclude=flameshot`

### pipewire -\> pulseaudio
```shell
sudo dnf rm pipewire\*
sudo dnf in pulseaudio
```

### enable software mixing manually
Add these line to /etc/asound:<br>
```shell
pcm.!default {
    type pulse
}

ctl.!default {
    type pulse
}
```

### disable zram
`sudo dnf rm zram-generator`

### disable selinux
`vim /etc/selinux/config`<br>
Find key 'SELINUX=...'<br>
Replace enforcing to disabled(if available).

### disable `download folder
Edit $HOME/.config/user-dirs.dirs<br>
Remove the text after $HOME/

### disable PostMixer channel
Take a look at this folder: <u>/usr/share/alsa/ucm2</u><br>
`sudo vim /usr/share/alsa/ucm2/Intel/sof-hda-dsp/HiFi-sof.conf` For example<br><br>

Find sth called: <b>If.endpoint_with_drc</b><br>
Go to True -\> EnableSequence<br><br>

Find the line: <b>cset "name='${var:PostMixerAnalogPlaybackDrcSwitch ${var:__drcswitch}"</b><br>
Then change the value: <b>${var:__drcswitch}</b> to <b>off</b>

### unused services
```shell
sudo systemctl disable fstrim.timer
sudo systemctl disable sshd
sudo systemctl disable avahi-daemon
sudo systemctl disable avahi-daemon.socket
```

### mask services
`sudo systemctl mask NetworkManager-wait-online`

### edit xorg-x11-xdm
Edit .xsession:
- `touch .xsession && echo i3 > .xsession`<br>
Make .xsession executeable: `chmod +x .xsession`<br>
Then type this code to keep xdm running: `systemctl set-default graphical.target`

### regen the grub file
`sudo grub2-mkconfig -o /boot/grub2/grub.cfg`

### minbrowser
`curl -L https://github.com/minbrowser/min/releases/download/v1.28.1/min-1.28.1-x86_64.rpm > min-1.28.1-x86_64.rpm`

### flameshot
```shell
sudo dnf in qt5-{qtbase,qttools},qt5-qtbase-gui
curl -L https://github.com/flameshot-org/flameshot/releases/download/v0.5.1/flameshot_0.5.1-fedora27-x86_64.rpm > flameshot_0.5.1-fedora27-x86_64.rpm
```

## Notes

### remove unused repos
Repository path: /etc/yum.repos.d<br>
Remove within `rm` command

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
