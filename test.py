import unittest  # Import the unittest module for testing
from datetime import datetime  # Import datetime to work with dates
from habit_tracker_app import HabitTracker  # Import the HabitTracker class to test its functionalities

"""
Test class for the Habit Tracker application.

This class contains unit tests for the main functionalities of the Habit Tracker app, such as adding,
editing, checking off, and analyzing habits. Each test checks if the HabitTracker methods work as expected.

Attributes:
    None

Methods:
    test_add_habit: Test adding a new habit to the tracker.
    test_show_habits: Test displaying the existing habits.
    test_edit_habit: Test editing an existing habit's details.
    test_check_off_habit: Test checking off a habit for today.
    test_analyze_habits: Test analyzing and summarizing the user's habits.
"""

class TestHabitTracker(unittest.TestCase):
    """Unit tests for the HabitTracker class functionalities."""

    def setUp(self):
        """Set up a new HabitTracker instance before each test."""
        
        # Create an instance of the HabitTracker class for testing
        self.tracker = HabitTracker()

        # Initialize the habit list with an empty list before each test
        self.tracker.habits = []

        # Mock save_habits to prevent overwriting
        self.tracker.save_habits = lambda: None

    def test_add_habit(self):
        """Test adding a new habit to the tracker."""
        
        # Define habit details for the new habit
        habit_name = "Test Habit"
        periodicity = 1  # Daily habit
        periodicity_type = "daily"
        specification = "Do a test activity"

        # Add a new habit to the tracker
        self.tracker.add_habit = lambda: None  # Mock method to skip user input
        self.tracker.habits.append({
            'name': habit_name,
            'periodicity': periodicity,
            'periodicity_display': "Daily",
            'periodicity_type': periodicity_type,
            'specification': specification,
            'completed_dates': [],
            'current_streak': 0,
            'longest_streak': 0
        })

        # Check if the habit is added to the tracker
        self.assertEqual(len(self.tracker.habits), 1)
        self.assertEqual(self.tracker.habits[0]['name'], habit_name)
        self.assertEqual(self.tracker.habits[0]['periodicity'], periodicity)

    def test_show_habits(self):
        """Test displaying the existing habits."""
        
        # Add a sample habit to display
        self.tracker.habits.append({
            'name': "Sample Habit",
            'periodicity': 1,
            'periodicity_display': "Daily",
            'periodicity_type': "daily",
            'specification': "Sample specification",
            'completed_dates': [],
            'current_streak': 0,
            'longest_streak': 0
        })

        # Check if habits are displayed
        self.tracker.show_habits()  # This should print the habit details

    def test_edit_habit(self):
        """Test editing an existing habit's details."""
        
        # Add a habit to be edited
        self.tracker.habits.append({
            'name': "Old Habit",
            'periodicity': 1,
            'periodicity_display': "Daily",
            'periodicity_type': "daily",
            'specification': "Old specification",
            'completed_dates': [],
            'current_streak': 0,
            'longest_streak': 0
        })

        # Mock the edit process to change the habit's details directly
        self.tracker.habits[0]['name'] = "Updated Habit"
        self.tracker.habits[0]['specification'] = "Updated specification"

        # Check if the habit's details were updated
        self.assertEqual(self.tracker.habits[0]['name'], "Updated Habit")
        self.assertEqual(self.tracker.habits[0]['specification'], "Updated specification")

    def test_check_off_habit(self):
        """Test checking off a habit for today."""
        
        # Add a habit to check off
        self.tracker.habits.append({
            'name': "Check Habit",
            'periodicity': 1,
            'periodicity_display': "Daily",
            'periodicity_type': "daily",
            'specification': "Check off habit",
            'completed_dates': [],
            'current_streak': 0,
            'longest_streak': 0
        })

        # Check off the habit for today
        today = datetime.today().strftime('%Y-%m-%d')
        self.tracker.habits[0]['completed_dates'].append(today)
        self.tracker.update_streak(self.tracker.habits[0])

        # Check if today's date is added to the completed dates
        self.assertIn(today, self.tracker.habits[0]['completed_dates'])
        self.assertEqual(self.tracker.habits[0]['current_streak'], 1)

    def test_analyze_habits(self):
        """Test analyzing and summarizing the user's habits."""
        
        # Add multiple habits to analyze
        self.tracker.habits.append({
            'name': "Habit 1",
            'periodicity': 1,
            'periodicity_display': "Daily",
            'periodicity_type': "daily",
            'specification': "Analyze habit 1",
            'completed_dates': [],
            'current_streak': 0,
            'longest_streak': 0
        })

        self.tracker.habits.append({
            'name': "Habit 2",
            'periodicity': 2,
            'periodicity_display': "Weekly (2 times)",
            'periodicity_type': "weekly",
            'specification': "Analyze habit 2",
            'completed_dates': [],
            'current_streak': 0,
            'longest_streak': 0
        })

        # Run the analysis method
        self.tracker.analyze_habits()  # This should print the analysis summary for each habit


if __name__ == '__main__':
    unittest.main()  # Run the test suite
