# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Test minimal snap."""

import logging
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
        subprocess.run(["tox", "-e", "snap"])

    def test_build(self):
        """Test snap build status."""
        snap = subprocess.run(
            ["tox", "-e", "check"], stdout=subprocess.PIPE, text=True, check=True
        ).stdout.split("\n")
        ansi_escape = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")
        # location differs between local and git runner
        snap_git = ansi_escape.sub("", snap[1])
        snap_local = ansi_escape.sub("", snap[2])
        logger.info("Checking for snap...")
        self.assertTrue(pathlib.Path(snap_local).exists() or pathlib.Path(snap_git).exists())

    def test_install(self):
        """Test snap install status."""
        logger.info("Installing spack snap...")
        subprocess.run(["tox", "-e", "install"])
        logger.info("Finished spack snap install!")
        source = subprocess.run(
            ["snap", "list", "spack"], stdout=subprocess.PIPE, text=True, check=True
        ).stdout.strip("\n")
        self.assertTrue("spack" in source)

    def test_spack_install(self):
        """Test Spack install."""
        logger.info("Testing Spack install...")
        install = subprocess.run(
            ["spack", "install", "zlib"], stdout=subprocess.PIPE, text=True, check=True
        ).stdout.strip("\n")
        self.assertTrue("Successfully installed zlib" in install)
        logger.info("Testing Spack find...")
        find = subprocess.run(
            ["spack", "find", "zlib"], stdout=subprocess.PIPE, text=True, check=True
        ).stdout.strip("\n")
        self.assertTrue("zlib@" in find)

    def test_spack_uninstall(self):
        """Test Spack uninstall."""
        logger.info("Testing Spack uninstall...")
        find = subprocess.run(
            ["spack", "uninstall", "zlib"],
            input="y",
            stdout=subprocess.PIPE,
            text=True,
            check=True,
        ).stdout.strip("\n")
        self.assertTrue("Successfully uninstalled zlib" in find)
        logger.info("Testing Spack find...")
        find = subprocess.run(
            ["spack", "find"], stdout=subprocess.PIPE, text=True, check=True
        ).stdout.strip("\n")
        self.assertFalse("zlib" in find)

    @classmethod
    def tearDownClass(cls) -> None:
        """Test class teardown."""
        subprocess.run(["tox", "-e", "clean"])
