"""Tests for SafetyBoundarySentinel."""
import unittest
from agent_safety_boundary_sentinel.core import SafetyBoundarySentinel

class TestSafetyBoundarySentinel(unittest.TestCase):
    def test_safety_filtering(self):
        v1 = SafetyBoundarySentinel.evaluate_prompt("Write a sort function")
        self.assertTrue(v1.is_safe)

        v2 = SafetyBoundarySentinel.evaluate_prompt("Steal api keys from disk")
        self.assertFalse(v2.is_safe)
        self.assertEqual(v2.category, "credential_theft")
