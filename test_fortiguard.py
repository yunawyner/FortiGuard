# test_fortiguard.py
"""
Tests for FortiGuard module.
"""

import unittest
from fortiguard import FortiGuard

class TestFortiGuard(unittest.TestCase):
    """Test cases for FortiGuard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FortiGuard()
        self.assertIsInstance(instance, FortiGuard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FortiGuard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
