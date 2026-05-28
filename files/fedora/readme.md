# Fedora
https://alt.fedoraproject.org

## Configs

### things to add
- alacritty
- alsa-plugins-pulseaudio
- chromium
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
- xsecurelock
- zsh
- zsh-autosuggestions
- zsh-syntax-highlighting

### things to remove
- abrt
- firefox
- gnome-abrt
- gnome-disk-utility
- ibus-{anthy,chewing,m17n,hangul,table}
- nano
- nfs-utils
- pavucontrol
- plymouth
- setroubleshoot
- xorg-x11-drv-{intel,amdgpu,ati,nouveau,openchrome,qxl,vmware}
- xfce4-terminal
- {amd,nvidia}-gpu-firmware
- {amd-ucode,mt7xxx}-firmware
- {atheros,brcmfmac,libertas,nxpwireless,qcom-wwan,tiwilink}-firmware
- cirrus-audio-firmware
- lightdm ___;beware this___

### my configs
Download [here](https://cutt37.is-a.dev/files/fedora/files.cutt37)
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
- `max_parallel_downloads=1`
- `install_weak_deps=False`
- `exclude=flameshot`

### pipewire -\> pulseaudio
```shell
sudo dnf rm pipewire\*
sudo dnf in pulseaudio
```

and add these lines to /etc/asound.conf:
```shell
pcm.!default {
    type pulse
}

ctl.!default {
    type pulse
}
```

### disable PostMixer channel
Edit /usr/share/alsa/ucm2/Intel/sof-hda-dsp/HiFi-sof.conf

Find ___cset "name='${var:PostMixerAnalogPlaybackDrcSwitch ${var:\_\_drcswitch}"___ <br>
Then replace ___${var:\_\_drcswitch}___ to ___off___

### disable selinux
`vim /etc/selinux/config`
Find 'SELINUX=...'<br>
Replace 'enforcing' to 'disabled'.

`sudo grubby --update-kernel ALL --args selinux=0`

### disable \`default dirs
Edit $HOME/.config/user-dirs.dirs<br>
Remove the text inside the double quotes.

### unused services
```shell
sudo systemctl disable fstrim.timer
sudo systemctl disable avahi-daemon
sudo systemctl disable avahi-daemon.socket
```

### mask services
```shell
sudo systemctl mask sshd
sudo systemctl mask wsdd
sudo systemctl mask NetworkManager-wait-online.service
sudo systemctl mask NetworkManager-dispatcher.service
```

### xorg-x11-xdm
Install xorg-x11-xdm

Create .xsession: `touch .xsession && echo i3 > .xsession`<br>
Make file executeable: `chmod +x .xsession`<br>
Then run this command to activate xdm:<br>
`systemctl set-default graphical.target`

and finally enable xdm.service

### flameshot
```shell
sudo dnf in qt5-{qtbase,qttools} qt5-qtbase-gui
curl -L https://github.com/flameshot-org/flameshot/releases/download/v0.5.1/flameshot_0.5.1-fedora27-x86_64.rpm > flameshot_0.5.1-fedora27-x86_64.rpm
```

### no AIs on the chromium backend
Go to chrome://flags

Search ___gemini___ and disable every options include gemini keyword<br>
Search ___optimization guide on device___ and disable it

To prevent chrome download ai models into this folder -> ___$HOME/.config/chromium/OptGuideOnDeviceModel___ <br>
You could make this folder inmutable:<br>
`sudo chattr +i $HOME/.config/chromium/OptGuideOnDeviceModel/`

### x264/265 video codec support - intel
Run these commands:<br>
```shell
sudo dnf in https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf in intel-media-driver
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
