#!/usr/bin/python3
"""
Test file for the console
"""

import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import console
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """Class for testing the console"""

    @classmethod
    def setUpClass(cls):
        """Setup for the test"""
        cls.consol = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """At the end of the test, tear it down"""
        del cls.consol

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'Fix Pep8')

    def test_docstrings_in_console(self):
        """Checking for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        # Add more docstring checks as needed

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """Test quit command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """Test create command input"""
        # Add create command tests

    def test_show(self):
        """Test show command input"""
        # Add show command tests

    def test_destroy(self):
        """Test destroy command input"""
        # Add destroy command tests

    def test_all(self):
        """Test all command input"""
        # Add all command tests

    def test_update(self):
        """Test update command input"""
        # Add update command tests

    def test_z_all(self):
        """Test alternate all command input"""
        # Add alternate all command tests

    def test_z_count(self):
        """Test count command input"""
        # Add count command tests

    def test_z_show(self):
        """Test alternate show command input"""
        # Add alternate show command tests

    def test_destroy(self):
        """Test alternate destroy command input"""
        # Add alternate destroy command tests

    def test_update(self):
        """Test alternate update command input"""
        # Add alternate update command tests

    def test_custom_command(self):
        """Test custom command in the console"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("custom_command argument1 argument2")
            self.assertEqual("Expected output for the custom command", f.getvalue())


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None, "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1, "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None, "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1, "HBNBCommand class needs a docstring")


if __name__ == "__main__":
    unittest.main()

