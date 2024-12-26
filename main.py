from habit_tracker_app import HabitTracker  # Import the HabitTracker class to manage the habit tracking functionality.

"""
Main class for running the Habit Tracker application.

This class initializes the habit tracking functionality for a normal user without authentication. 
It provides an interface for users to manage their habits once they open the app.

Attributes:
    None

Methods:
    run_habit_tracker: Initiate the habit tracking application by creating an instance of the HabitTracker class.
    It provides functionality for managing habits without any authentication process.
"""

def run_habit_tracker():
    """Run the habit tracking application."""

    # Create an instance of the HabitTracker class to manage habits
    tracker = HabitTracker()

    # Call the method to show the user dashboard
    tracker.user_options()

if __name__ == "__main__":
    run_habit_tracker()  # Start the application
