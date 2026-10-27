"""Checks for the educational form examples; these do not test the web UI."""

import unittest
from . import assignment_window as assignment
from . import commitment_window as commitment


class WindowExamples(unittest.TestCase):
    def test_invalid_commitment_does_not_save(self):
        items = []
        window = commitment.open_window("2026-10-26")
        commitment.change_field(window, "title", "Practice")
        commitment.change_field(window, "end", "15:00")
        self.assertFalse(commitment.save_window(window, items))
        self.assertEqual(items, [])
        self.assertTrue(window["errors"])

    def test_overlap_warns_and_edit_replaces(self):
        items = []
        first = commitment.open_window("2026-10-26")
        commitment.change_field(first, "title", "Practice")
        self.assertTrue(commitment.save_window(first, items))
        second = commitment.open_window("2026-10-26")
        commitment.change_field(second, "title", "Commute")
        self.assertTrue(commitment.save_window(second, items))
        self.assertEqual(second["warnings"], ["Overlaps Practice"])
        edit = commitment.open_window("2026-10-26", items[0])
        commitment.change_field(edit, "title", "Team practice")
        self.assertEqual(items[0]["title"], "Practice")
        self.assertTrue(commitment.save_window(edit, items))
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]["title"], "Team practice")

    def test_assignment_save_cancel_and_validation(self):
        items = []
        window = assignment.open_window("2026-10-26")
        assignment.change_field(window, "title", "Algebra")
        assignment.change_field(window, "minutes", "45.5")
        self.assertFalse(assignment.save_window(window, items))
        assignment.change_field(window, "minutes", "60")
        self.assertTrue(assignment.save_window(window, items))
        self.assertEqual(items[0]["minutes"], 60)
        edit = assignment.open_window("2026-10-26", items[0])
        assignment.change_field(edit, "title", "Different title")
        assignment.cancel_window(edit)
        self.assertEqual(items[0]["title"], "Algebra")
        self.assertFalse(assignment.save_window(edit, items))

    def test_new_window_cannot_delete_an_unrelated_item(self):
        items = [{"title": "Old example without an ID"}]
        self.assertFalse(assignment.delete_item(assignment.open_window("2026-10-26"), items))
        self.assertFalse(commitment.delete_item(commitment.open_window("2026-10-26"), items))
        self.assertEqual(len(items), 1)


if __name__ == "__main__":
    unittest.main()
