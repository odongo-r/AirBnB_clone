import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up the test environment before each test."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up the test environment after each test."""
        pass

    @patch('sys.stdout', new=StringIO())
    def test_quit_command(self):
        """Test quit command."""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    @patch('sys.stdout', new=StringIO())
    def test_EOF_command(self):
        """Test EOF command."""
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    @patch('sys.stdout', new=StringIO())
    def test_create_command(self):
        """Test create command."""
        with patch('sys.stdin', StringIO('y\n')):
            self.console.onecmd("create BaseModel")

    @patch('sys.stdout', new=StringIO())
    def test_show_command(self):
        """Test show command."""
        with patch('sys.stdin', StringIO('y\n')):
            self.console.onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertNotEqual(f.getvalue(), "")

    @patch('sys.stdout', new=StringIO())
    def test_destroy_command(self):
        """Test destroy command."""
        with patch('sys.stdin', StringIO('y\n')):
            self.console.onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertNotEqual(f.getvalue(), "")

    @patch('sys.stdout', new=StringIO())
    def test_all_command(self):
        """Test all command."""
        with patch('sys.stdin', StringIO('y\n')):
            self.console.onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertNotEqual(f.getvalue(), "")

    @patch('sys.stdout', new=StringIO())
    def test_update_command(self):
        """Test update command."""
        with patch('sys.stdin', StringIO('y\n')):
            self.console.onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 123 name 'test_name'")
            self.assertNotEqual(f.getvalue(), "")

    @patch('sys.stdout', new=StringIO())
    def test_count_command(self):
        """Test count command."""
        with patch('sys.stdin', StringIO('y\n')):
            self.console.onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            self.assertNotEqual(f.getvalue(), "")

    @patch('sys.stdout', new=StringIO())
    def test_update_from_dict_command(self):
        """Test update from dict command."""
        with patch('sys.stdin', StringIO('y\n')):
            self.console.onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update_from_dict BaseModel 123 {'name': 'test_name'}")
            self.assertNotEqual(f.getvalue(), "")


if __name__ == '__main__':
    unittest.main()

