import os
import argparse


PACKAGES = {
    "core-utils": {
        # "linux-lts419": "aur",
        #"linux-zen": "aur",
        #"vulkan-intel": "pacman",
        #"lib32-vulkan-intel": "pacman",
        # "pulseaudio": "pacman",
        #"pulseaudio-bluetooth": "pacman",
        #"intel-gpu-tools": "pacman",
        # "intel-compute-runtime": "pacman",
        # "intel-opencl": "aur",
        # "level-zero-loader": "pacman",
        # "gcc8": "aur",  # for cuda
        # "cuda-10.1": "aur",
        # "cudnn7-cuda10.1": "aur",
        "pipewire": "pacman",
        "qt5-tools": "pacman"
        # "pipewire-alsa": "pacman",
        # "pipewire-pulse": "pacman",
        # "pipewire-jack": "pacman",
    },
    "security": {
        "gnome-keyring": "pacman",
        "seahorse": "pacman",
        "tor": "pacman",
        "torsocks": "pacman",
        "firejail": "pacman",
        # "strace": "pacman",
        "gocryptfs": "pacman",
        # "tunnelbear": "aur",
        #"bitwarden-bin": "aur"
    },
    "media": {
        "pix": "aur",
        "gimp": "pacman",
        "lollypop": "pacman",
        "flameshot": "pacman",
        "transmission-qt": "pacman",
        "google-chrome": "aur",
        "sublime-text-3": "aur",
        "tor-browser": "aur",
        "dropbox": "aur",
        "spotify": "aur",
    },
    "social": {
        "telegram-desktop": "pacman",
        "discord": "pacman",
        "steam": "pacman"
    },
    "development": {
        "dbeaver": "pacman",
        "gitkraken": "aur",
        "clion-jre": "aur",
        "clion-gdb": "aur",
        "clion": "aur",
        "docker": "pacman",
        # "minikube": "pacman",
        # "kubectl": "pacman",
        # "kubelet": "pacman",
        "rust": "pacman",
        "go": "pacman",
        "cmake": "pacman",
    },
    "development-python": {
        "python37": "aur",
        "python38": "aur",
        "pycharm-community-edition": "pacman",
    },
    "development-java": {
        "jre11-openjdk": "pacman",
        "jdk11-openjdk": "pacman",
        "jre14-openjdk": "pacman",
        "jdk14-openjdk": "pacman",
        "intellij-idea-ultimate-edition": "aur",
    },
    "development-micro": {
        #"kicad": "pacman",
        #"kicad-library": "pacman",
    	#"arduino-avr-core": "pacman",
        #"arduino": "aur",
        #"arduino-pro-ide": "aur",
        #"platformio": "aur",
        #"esp-idf": "aur",
        #"xtensa-esp32-elf-gcc-bin": "aur"
    },
    "personalization": {
        "latte-dock-git": "aur",
        "lolcat": "pacman",
        "fish": "pacman",
        "plasma5-applets-window-buttons": "aur",
        "plasma5-applets-window-title": "aur",
        "plasma5-applets-eventcalendar": "aur",
        "buddhasay": "aur",
        "ulauncher": "aur",
        "kwin-scripts-parachute": "aur",
        "materia-kde": "pacman",
        "kvantum-theme-materia": "pacman",
        "sddm-sugar-light": "aur",
        "sddm-sugar-dark": "aur",
        "sddm-sugar-candy-git": "aur",
        "lightly-qt": "aur",
    },
    "backup": {
        "timeshift": "aur",
        # "btrbk": "aur",
    },
    "remote": {
        "parsec-bin": "aur",
        "anydesk-bin": "aur",
        "krdc": "pacman",
        "krfb": "pacman",
    },
    "touchpad-gestures": {
        #"touchegg": "aur.laptop"
        # "ruby-fusuma": "aur.laptop",
        # "ruby-fusuma-plugin-keypress": "aur.laptop"
    },
    "office": {
        "onlyoffice-bin": "aur",
        "ttf-times-new-roman": "aur",
        "otf-xits": "aur",
        "kile": "pacman",
        "texlive-most": "pacman",
        "texlive-langcyrillic": "pacman",
        "aspell-en": "pacman",
        "aspell-ru": "pacman",
    },
    "utils": {
        "xdotool": "pacman",
        "gutenprint": "pacman",
        "ttf-opensans": "pacman",
        "grub-customizer": "pacman",
        "gparted": "pacman",
        "zip": "pacman",
        "unzip": "pacman",
        "etcher-bin": "aur",
        "inotify-tools": "pacman",
        "graphviz": "pacman",
        "wine": "pacman",
        "appmenu-gtk-module": "pacman",
        # "imagemagick": "pacman",
        # "kdialog": "pacman",
        "gotop": "aur",
        "trezor-suite-appimage": "aur",
        "ksysguard-gpu": "aur",
        # "plasma-systemmonitor": "pacman",
        "sshfs": "pacman",
        # "kio-fuse": "pacman",
        "tlp": "pacman",
        "powertop": "pacman",
        "logiops": "aur",
        "barrier-bin": "aur",
    }
}


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Package installer")
	parser.add_argument("-l", "--laptop", action="store_true")
	parser.add_argument("-p", "--pacman", action="store_true")
	parser.add_argument("-a", "--aur", action="store_true")

	args = parser.parse_args()

	pacman_packages = []
	aur_packages = []

	for category in PACKAGES:
		for package, src in PACKAGES[category].items():
			if src.startswith("pacman"):
				if ".laptop" in src and args.laptop:
					pacman_packages.append(package)
				elif ".laptop" not in src:
					pacman_packages.append(package)

			elif src.startswith("aur"):
				if ".laptop" in src and args.laptop:
					aur_packages.append(package)
				elif ".laptop" not in src:
					aur_packages.append(package)

	if args.pacman:
		print("Installing pacman packages")
		os.system(f"sudo pacman -Sy --noconfirm --needed {' '.join(pacman_packages)}")

	if args.aur:
		print("Installing aur packages")
		os.system(f"yay -S --needed --noconfirm --batchinstall --noredownload --norebuild {' '.join(aur_packages)}")

