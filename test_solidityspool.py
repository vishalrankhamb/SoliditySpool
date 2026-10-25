# test_solidityspool.py
"""
Tests for SoliditySpool module.
"""

import unittest
from solidityspool import SoliditySpool

class TestSoliditySpool(unittest.TestCase):
    """Test cases for SoliditySpool class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = SoliditySpool()
        self.assertIsInstance(instance, SoliditySpool)

    def test_run_method(self):
        """Test the run method."""
        instance = SoliditySpool()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
