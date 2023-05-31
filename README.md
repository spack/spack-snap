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
sudo snap install ./spack*.charm --dangerous
```
## How to Use the Snap
Currently the snap can be used for installing and loading packages.

```bash
# Install a package
spack install <package_name>

# Uninstall a package
spack uninstall <package_name>
```

### Modules

For every package that Spack installs it also provides a module file which can be used with Lmod.

```bash
# Install lmod - may need additional specifiers like %gcc@11.3.0
spack install lmod

# Put lmod in path
. $(spack location -i lmod)/lmod/lmod/init/bash

# Should match the snap shell environment
snap run --shell spack; env | grep MODULEPATH

# Show modules available
module avail

# Load a module
module load <module from module avail output>

# Show modules loaded
module list
```

For more on Spack usage, see [Spack Usage](https://spack.readthedocs.io/en/latest/basic_usage.html) for more information.
For more on lmod usage, see [Lmod Usage](https://lmod.readthedocs.io/en/latest/010_user.html) for more information.
## Limitations
Currently shell support is not supported with the Spack snap. Therefore, instead of `spack load <package_name>` the shell type has to be specified in the load flag as seen below, ie --sh. This is true for other commands that rely on shell support. It is recommended to instead use modules with the Spack snap instead.

```bash
# Load a package
eval `spack load --sh <package_name>`
```
## License
The Spack Snap is free software, distributed under the Apache Software License, version 2.0. See [LICENSE](https://github.com/dvdgomez/spack-snap/blob/main/LICENSE) for more information.
