<div align="center">

<img src="./assets/spack-logo.svg" width="200" height="200" alt="Spack logo">
<br>

# Spack

A [snap](https://snapcraft.io/about) package for [Spack](https://spack.io/about/) - a flexible package manager and development tool for supercomputers.

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/spack)

</div>

> __Note:__ The Spack snap is currently only available within the edge channel on the Snap Store as the initial call for testing window is open.
> Interested in testing this new snap package? See the [Spack snap call-for-testing thread](https://forum.snapcraft.io/t/call-for-testing-spack-0-20-2/37272)
> on the Snapcraft forum. Please report all this issues and/or suggestions on call-for-testing thread.

## Features

Spack is a package manager and development tool for supercomputers. Spack supports
installing 7000+ packages and supports several different build systems and compiler
backends. Packages installed using Spack peacefully coexist with other packages
installed using the distribution package manager. Spack uses `RPATH` to link
dependencies rather than `LD_LIBRARY_PATH`; there is no need to worry about conflicting
libraries messing with binary executables. Each install is unique and will not break
other existing installations on your host system.

## Usage

This section provides a brief overview of how to use the Spack snap on your system.
For more in-depth information on how to use Spack on your system, see the 
[Spack Usage](https://spack.readthedocs.io/en/latest/basic_usage.html) section in
Spack's official upstream documentation.

#### Installing Spack using snap

```shell
sudo snap install spack --edge --classic
```

#### Installing packages

```shell
# Install compilers on your system.
sudo apt update
sudo apt install gcc g++ gfortran make

# Load compiler configuration into Spack.
spack compiler find

# Install a package.
sudo spack install <package_name>

# Uninstall a package.
sudo spack uninstall <package_name>
```

#### Installing packages in `/home/<user>` rather than in `/opt/spack/*`

```shell
# Create .spack in your home directory.
mkdir -p ~/.spack

# Set local configuration file in place.
cat << EOF > ~/.spack/config.yaml
config:
  install_tree: $user/.spack/opt/spack
  license_dir: $user/.spack/etc/spack/licenses
  source_cache: $user/.spack/var/spack
  environments_root: $user/.spack/env
EOF

# Install packages as you normally would.
spack install <package_name>
```

#### Enabling shell support

```shell
# On bash/zsh/sh/etc.
. /etc/spack/shell/setup-env.sh

# On csh/tcsh.
source /etc/spack/shell/setup-env.csh

# On fish.
source /etc/spack/shell/setup-env.fish

# Load your packages.
spack load <package_name>
```

## Building the Spack snap

Want to build and test the Spack snap locally without pulling from the Snap Store? 
Use the following commands to build and install the Spack snap on your system. These
instructions assume that you are running on a Linux distribution that supports 
installing snap packages. Please see [this page](https://snapcraft.io/docs/installing-snapd) 
for a list of Linux distributions that support using snap packages.

#### Clone Repository

```shell
git clone git@github.com:canonical/spack-snap.git
cd spack-snap
```

#### Installing and Configuring Prerequisites

```shell
sudo snap install lxd
sudo lxd init --minimal
sudo snap install snapcraft --classic
```

#### Packing and Installing the Snap

```shell
snapcraft
sudo snap install ./spack*.charm --dangerous --classic
```

## License

This project is part of Spack. Spack is distributed under the terms of both the 
MIT license and the Apache License (Version 2.0). Users may choose either license, 
at their option.

All new contributions must be made under both the MIT and Apache-2.0 licenses.

See [LICENSE-MIT](./LICENSE-MIT), [LICENSE-APACHE](./LICENSE-APACHE), 
and [COPYRIGHT](./COPYRIGHT) for details.

SPDX-License-Identifier: (Apache-2.0 OR MIT)
