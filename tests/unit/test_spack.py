# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Test minimal snap."""

import logging
import os
import pathlib
import re
import subprocess
import unittest

logger = logging.getLogger(__name__)


class TestSnap(unittest.TestCase):
    """Unit test Spack snap."""

    @classmethod
    def setUpClass(cls) -> None:
        """Test class setup."""
        subprocess.run(["tox", "-e", "clean"])
        logger.info("Building snap")
        # Go up 3 levels from test file
        os.chdir("/".join(__file__.split("/")[:-3]))
        subprocess.run(["tox", "-e", "snap"])
        # Find generated snap
        cls.SPACK = re.findall(r"(spack.*?snap)", " ".join(os.listdir()))[0]

    def test_build(self):
        """Test snap build status."""
        logger.info(f"Checking for snap {TestSnap.SPACK}...")
        self.assertTrue(pathlib.Path(TestSnap.SPACK).exists())

    def test_install(self):
        """Test snap install status."""
        logger.info(f"Installing spack snap {TestSnap.SPACK}...")
        subprocess.run(["tox", "-e", "install"])
        logger.info("Finished spack snap install!")
        source = subprocess.run(
            ["snap", "list", "spack"], stdout=subprocess.PIPE, text=True
        ).stdout.strip("\n")
        self.assertTrue("spack" in source)

    def test_spack_install(self):
        """Test Spack install."""
        logger.info("Testing Spack install...")
        install = subprocess.run(
            ["spack", "install", "zlib"], stdout=subprocess.PIPE, text=True
        ).stdout.strip("\n")
        self.assertTrue("Successfully installed zlib" in install)
        logger.info("Testing Spack find...")
        find = subprocess.run(
            ["spack", "find", "zlib"], stdout=subprocess.PIPE, text=True
        ).stdout.strip("\n")
        self.assertTrue("zlib@" in find)

    def test_spack_uninstall(self):
        """Test Spack uninstall."""
        logger.info("Testing Spack uninstall...")
        find = subprocess.run(
            ["spack", "uninstall", "zlib"], input="y", stdout=subprocess.PIPE, text=True
        ).stdout.strip("\n")
        self.assertTrue("Successfully uninstalled zlib" in find)
        logger.info("Testing Spack find...")
        find = subprocess.run(
            ["spack", "find", "zlib"], stdout=subprocess.PIPE, text=True
        ).stdout.strip("\n")
        self.assertTrue("No package matches the query: zlib" in find)

    @classmethod
    def tearDownClass(cls) -> None:
        """Test class teardown."""
        subprocess.run(["tox", "-e", "clean"])
