# Spack Snap
This repository contains the packaging metadata for creating a snap of Spack.  For more information on snaps, visit [snapcraft.io](https://snapcraft.io/). 

## Installing the Snap
The snap can be installed directly from the Snap Store.  Follow the link in the badge below for more information.
<br>

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/spack)


## Building the Snap
The steps outlined below are based on the assumption that you are building the snap with the latest LTS of Ubuntu.  If you are using another version of Ubuntu or another operating system, the process may be different.

### Clone Repository
```bash
git clone git@github.com:dvdgomez/spack-snap.git
cd spack-snap
```
### Installing and Configuring Prerequisites
```bash
sudo snap install snapcraft
sudo snap install lxd
sudo lxd init --auto
```
### Packing and Installing the Snap
```bash
snapcraft pack
sudo snap install ./spack*.charm --dangerous --classic
```
## How to Use the Snap
```bash
# Install a package
spack install <package_name>

# Uninstall a package
spack uninstall <package_name>
```

For more on usage, see [Usage](https://spack.readthedocs.io/en/latest/basic_usage.html) for more information.
## License
The Spack Snap is free software, distributed under the Apache Software License, version 2.0. See [LICENSE](https://github.com/dvdgomez/spack-snap/blob/main/LICENSE) for more information.
