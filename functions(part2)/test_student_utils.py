import unittest
from student_utils import calculate_average, get_highest_score, get_lowest_score

class TestStudentUtils(unittest.TestCase):
    """Tests for student_utils functions."""

    def test_calculate_average(self):
        """Test that the average is calculated correctly."""
        self.assertEqual(calculate_average([90, 80, 70]), 80.0)

    def test_get_highest_score(self):
        """Test that the highest score is found."""
        self.assertEqual(get_highest_score([90, 80, 70]), 90)

    def test_get_lowest_score(self):
        """Test that the lowest score is found."""
        self.assertEqual(get_lowest_score([90, 80, 70]), 70)

if __name__ == "__main__":
    unittest.main(exit=False)
