# test_jotaiatom.py
"""
Tests for JotaiAtom module.
"""

import unittest
from jotaiatom import JotaiAtom

class TestJotaiAtom(unittest.TestCase):
    """Test cases for JotaiAtom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JotaiAtom()
        self.assertIsInstance(instance, JotaiAtom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JotaiAtom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
