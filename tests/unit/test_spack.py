# Copyright 2023 Canonical Ltd.
# See LICENSE file for licensing details.

"""Test minimal snap."""

import logging
import os
import pathlib
import re
import shlex
import subprocess
import unittest

logger = logging.getLogger(__name__)


class TestSnap(unittest.TestCase):
    """Unit test Spack snap."""

    @classmethod
    def setUpClass(cls) -> None:
        """Test class setup."""
        subprocess.run(shlex.split("tox -e clean"))
        logger.info("Building snap")
        # Go up 3 levels from test file
        os.chdir("/".join(__file__.split("/")[:-3]))
        subprocess.run(shlex.split("tox -e snap"))
        # Find generated snap
        cls.SPACK = re.findall(r"(spack.*?snap)", " ".join(os.listdir()))[0]

    @classmethod
    def tearDownClass(cls) -> None:
        """Test class teardown."""
        subprocess.run(shlex.split("tox -e clean"))

    def test_build(self):
        """Test snap build status."""
        logger.info(f"Checking for snap {TestSnap.SPACK}...")
        self.assertTrue(pathlib.Path(TestSnap.SPACK).exists())

    def test_install(self):
        """Test snap install status."""
        logger.info(f"Installing spack snap {TestSnap.SPACK}...")
        subprocess.run(shlex.split("tox -e install"))
        logger.info("Finished spack snap install!")
        source = subprocess.run(
            shlex.split("snap list spack"), stdout=subprocess.PIPE, text=True
        ).stdout.strip("\n")
        self.assertTrue("spack" in source)
