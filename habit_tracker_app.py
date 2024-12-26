import json  # Import the json module for working with JSON data
from datetime import datetime, timedelta  # Import datetime and timedelta to handle dates and times

# Function to get the start of the week (Monday)
def start_of_week(date):
    """Given a date, return the start of that week (Monday)."""
    return date - timedelta(days=date.weekday())  # Subtract days from the given date to get Monday

"""
Class for managing user habits.

This class allows users to manage their habits, including adding, viewing, editing, checking off, and analyzing habits.
It handles the saving and loading of habits from a JSON file.

Attributes:
    habits (list): List of habits loaded from 'habits.json'.

Methods:
    load_habits: Load user-specific habits from the 'habits.json' file.
    save_habits: Save the user's habits to 'habits.json'.
    user_options: Display the options menu for habit management and allow user input.
    add_habit: Add a new habit with details like name, periodicity, and specification.
    show_habits: Display all the user's habits.
    edit_habit: Edit, reset, or remove an existing habit.
    check_off_habit: Mark a habit as completed for the current day and update streaks.
    analyze_habits: Analyze and display information about the user's habits.
    get_period_start: Calculate the start of a period based on the periodicity type.
    prompt_for_frequency: Prompt for the frequency of the habit (e.g., times per week).
"""

class HabitTracker:
    def __init__(self):
        """Initialize the HabitTracker class and load habits."""
        
        # Initialize an empty list to store habits for the user
        self.habits_test = []

        # Load habits from the 'habits.json' file
        self.load_habits()

    def load_habits(self):
        """Load habits for the user."""
        try:
            # Try to open 'habits.json' and load the habits
            with open('habits.json', 'r') as file:
                self.habits_test = json.load(file)
                
                # If the file is empty, initialize with an empty list
                if not self.habits_test:
                    print("No habits found in 'habits.json'.")
                    self.habits_test = []
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn't exist or there's a decoding error, initialize with an empty list
            print("No valid habits file found. Starting with an empty habit list.")
            self.habits_test = []
        except Exception as e:
            print(f"An unexpected error occurred while loading habits: {e}")
            self.habits_test = []  # Initialize with an empty list in case of any error

    def save_habits(self):
        """Save the user's habits to 'habits.json'."""
        try:
            # Open 'habits.json' and save the habits in JSON format
            with open('habits.json', 'w') as file:
                json.dump(self.habits_test, file)
        except Exception as e:
            print(f"An error occurred while saving habits: {e}")

    def user_options(self):
        """Display the user options menu."""
        while True:
            # Display the dashboard menu for the user
            print("\n--- Dashboard ---")
            print("1. Add New Habit")
            print("2. Show Existing Habits")
            print("3. Edit Existing Habit")
            print("4. Habit Analysis")
            print("5. Check Off Habit")
            print("6. Exit\n")

            # Prompt the user to choose an option
            choice = input("Enter your choice (1-6): ")

            # Call the appropriate method based on the user's choice
            if choice == "1":
                self.add_habit()  # Add a new habit
            elif choice == "2":
                self.show_habits()  # Show existing habits
            elif choice == "3":
                self.edit_habit()  # Edit an existing habit
            elif choice == "4":
                self.analyze_habits()  # Analyze the user's habits
            elif choice == "5":
                self.check_off_habit()  # Check off a habit for today
            elif choice == "6":
                # Exit the app and save the user's habits
                print("Exiting...")
                self.save_habits()
                break  # Exit the loop and close the app
            else:
                # Print an error message for invalid input
                print("Invalid choice. Please enter a valid option from the menu.")

    def add_habit(self):
        """Add a new habit for the user."""
        while True:
            # Prompt the user to enter the name of the habit
            habit_name = input("Enter the name of the habit (or enter 0 to cancel): ").strip()
            if habit_name == "0":  # Check if the user wants to cancel
                print("Adding habit canceled.")
                return  # Exit the add_habit method

            # Prompt the user to select the periodicity of the habit
            print("\nChoose the periodicity for this habit:")
            print("1. Daily")
            print("2. Weekly")
            print("3. Monthly")
            print("4. Yearly")
            periodicity_choice = input("Enter your choice (1-4) (or enter 0 to cancel): ").strip()

            if periodicity_choice == "0":  # Check if the user wants to cancel
                print("Adding habit canceled.")
                return  # Exit the add_habit method

            # Initialize the periodicity and display value
            periodicity_display = ""
            periodicity_type = ""

            # Set the periodicity based on user choice
            if periodicity_choice == "1":  # Daily habit
                periodicity_type = "daily"
                periodicity_display = "Daily"
                periodicity = 1  # Default to 1 time per day

            elif periodicity_choice == "2":  # Weekly habit
                periodicity = self.prompt_for_frequency(7, "week")
                periodicity_display = f"Weekly ({periodicity} times)"
                periodicity_type = "weekly"

            elif periodicity_choice == "3":  # Monthly habit
                periodicity = self.prompt_for_frequency(31, "month")
                periodicity_display = f"Monthly ({periodicity} times)"
                periodicity_type = "monthly"

            elif periodicity_choice == "4":  # Yearly habit
                periodicity = self.prompt_for_frequency(365, "year")
                periodicity_display = f"Yearly ({periodicity} times)"
                periodicity_type = "yearly"

            else:
                print("Invalid choice. Please enter a valid number between 1 and 4.")  # Error message for invalid selection
                continue  # Repeat the loop to get a valid input

            # Prompt the user to enter specifications for the habit
            specification = input("Enter the specifications for the habit (e.g., 30 minutes of running) (or enter 0 to cancel): ").strip()
            if specification == "0":  # Check if the user wants to cancel
                print("Adding habit canceled.")
                return  # Exit the add_habit method

            # Create a new habit with the provided details
            habit = {
                'name': habit_name,
                'periodicity': periodicity,
                'periodicity_display': periodicity_display,
                'periodicity_type': periodicity_type,
                'specification': specification,
                'completed_dates': [],
                'current_streak': 0,
                'longest_streak': 0
            }

            # Add the new habit to the list of habits
            self.habits_test.append(habit)

            # Save the updated list of habits to the file
            self.save_habits()

            # Inform the user that the habit has been successfully added
            print(f"Habit '{habit_name}' added.")
            return  # Exit the add_habit method after successful addition

    def show_habits(self):
        """Display all habits with only the name, periodicity, and specification."""
        
        # Check if there are habits to display
        if not self.habits_test:
            print("No habits found.")
            return  # No habits to display

        # Display each habit's name, periodicity, and specification
        for index, habit in enumerate(self.habits_test, start=1):
            periodicity_display = habit.get('periodicity_display', "Not specified")
            print(f"{index}. {habit['name']} ({periodicity_display})")
            print(f"   Specification: {habit['specification']}\n")

    def edit_habit(self):
        """Edit, reset, or remove an existing habit."""
        
        # Display the user's habits to choose from for editing or removal.
        if not self.habits_test:
            print("No habits to edit.")
            return

        # Show available habits to the user
        self.show_habits()

        while True:
            try:
                # Prompt for habit selection by number
                habit_number_input = input("Enter the number of the habit you want to edit or remove (or enter 0 to return to the dashboard): ")
                if habit_number_input == "0":
                    return  # Return to the dashboard if the user chooses 0

                habit_number = int(habit_number_input) - 1  # Adjust for zero-based index

                # Ensure the selection is within valid range
                if 0 <= habit_number < len(self.habits_test):
                    habit = self.habits_test[habit_number]
                    break  # Exit loop once a valid habit is selected
                else:
                    print("Invalid habit number. Please select a valid habit number from the list.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Options for editing, resetting, or removing
        while True:
            print("1. Edit Habit Details")
            print("2. Reset Habit")
            print("3. Remove Habit")
            edit_choice = input("Enter your choice (or enter 0 to return to the dashboard): ")

            if edit_choice == "0":  # Return to dashboard
                return
            elif edit_choice == "1":
                # Edit habit details: name, specification, periodicity type, and frequency
                print("Enter new values (leave blank to keep current value):")
                new_name = input(f"Name ({habit['name']}): ").strip()
                new_specification = input(f"Specification ({habit['specification']}): ").strip()

                # Prompt user to re-select periodicity type
                print("\nChoose the new periodicity for this habit:")
                print("1. Daily")
                print("2. Weekly")
                print("3. Monthly")
                print("4. Yearly")
                periodicity_choice = input("Enter your choice (or leave blank to keep current value): ").strip()

                if periodicity_choice == "1":  # Daily habit
                    habit['periodicity_type'] = "daily"
                    habit['periodicity_display'] = "Daily"
                    habit['periodicity'] = 1  # Default to 1 time per day

                elif periodicity_choice == "2":  # Weekly habit
                    frequency = self.prompt_for_frequency(7, "week")
                    habit['periodicity_type'] = "weekly"
                    habit['periodicity'] = frequency
                    habit['periodicity_display'] = f"Weekly ({frequency} times)"

                elif periodicity_choice == "3":  # Monthly habit
                    frequency = self.prompt_for_frequency(31, "month")
                    habit['periodicity_type'] = "monthly"
                    habit['periodicity'] = frequency
                    habit['periodicity_display'] = f"Monthly ({frequency} times)"

                elif periodicity_choice == "4":  # Yearly habit
                    frequency = self.prompt_for_frequency(365, "year")
                    habit['periodicity_type'] = "yearly"
                    habit['periodicity'] = frequency
                    habit['periodicity_display'] = f"Yearly ({frequency} times)"

                # Update other fields only if new values are provided
                if new_name:
                    habit['name'] = new_name
                if new_specification:
                    habit['specification'] = new_specification

                # Save updated habits to file
                self.save_habits()
                print("Habit updated successfully.")
                break
            elif edit_choice == "2":
                # Reset habit confirmation
                confirm = input("Are you sure you want to reset this habit? This action cannot be undone. (yes/no): ").lower()
                if confirm == "yes":
                    # Clear completions and streaks
                    habit['completed_dates'] = []
                    habit['current_streak'] = 0
                    habit['longest_streak'] = 0
                    self.save_habits()
                    print("Habit reset successfully.")
                else:
                    print("Reset canceled.")
                break
            elif edit_choice == "3":
                # Remove habit confirmation
                confirm = input("Are you sure you want to remove this habit? (yes/no): ").lower()
                if confirm == "yes":
                    self.habits_test.remove(habit)
                    self.save_habits()
                    print("Habit removed successfully.")
                else:
                    print("Removal canceled.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def check_off_habit(self):
        """Check off a habit for today."""
        
        # Display the user's habits to choose from for checking off.
        if not self.habits_test:
            print("No habits to check off.")
            return

        # Display the list of habits for selection
        self.show_habits()

        while True:
            try:
                # Prompt user to select the habit number
                habit_number_input = input("Enter the number of the habit you want to check off (or enter 0 to return to the dashboard): ")
                if habit_number_input == "0":
                    return  # Return to the main dashboard if user chooses 0

                # Adjust for zero-based indexing
                habit_number = int(habit_number_input) - 1

                # Verify habit selection is within the valid range
                if 0 <= habit_number < len(self.habits_test):
                    habit = self.habits_test[habit_number]
                    break  # Exit loop if a valid habit is selected
                else:
                    print("Invalid choice. Please enter a number corresponding to a habit.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Mark today's date as completed for the habit
        today = datetime.today().strftime('%Y-%m-%d')
        if today in habit['completed_dates']:
            print(f"Habit '{habit['name']}' is already checked off for today.")
        else:
            # Add today's date and update streak
            habit['completed_dates'].append(today)
            habit['completed_dates'].sort()  # Keep dates in order
            self.update_streak(habit)  # Update streaks based on completion
        
            # Save changes to 'habits.json'
            self.save_habits()
            print(f"Habit '{habit['name']}' checked off for today.")

    def update_streak(self, habit):
        """Update the current and longest streak for a habit based on completion dates."""

        # Check if there are any completed dates to process
        if not habit['completed_dates']:
            # If no completed dates, set current and longest streak to 0
            habit['current_streak'] = 0
            habit['longest_streak'] = 0
            return  # Exit the function early as there is nothing to process

        # Ensure completed dates are sorted in order
        habit['completed_dates'].sort()

        current_streak = 0  # Start counting streak from zero
        longest_streak = habit['longest_streak']  # Track longest streak

        # Initialize current period
        current_period_start = self.get_period_start(habit['completed_dates'][0], habit['periodicity_type'])
        completed_this_period = 0  # Track completions in current period

        for date_str in habit['completed_dates']:
            current_date = datetime.strptime(date_str, '%Y-%m-%d')
            period_start = self.get_period_start(current_date.strftime('%Y-%m-%d'), habit['periodicity_type'])

            if period_start == current_period_start:
                # If within the current period, increment the completion count
                completed_this_period += 1
            else:
                # Check if completions meet habit's required frequency to keep the streak alive
                if completed_this_period >= habit['periodicity']:
                    current_streak += 1
                    longest_streak = max(longest_streak, current_streak)
                else:
                    # If missed frequency, reset current streak
                    current_streak = 0
                
                # Move to the next period
                current_period_start = period_start
                completed_this_period = 1  # Reset for new period

        # Final check for last period
        if completed_this_period >= habit['periodicity']:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)

        # Update habit streak values
        habit['current_streak'] = current_streak
        habit['longest_streak'] = longest_streak
        self.save_habits()  # Save updated streak values

    def get_period_start(self, date_str, periodicity_type):
        """Get the start date of the period based on the periodicity type."""
        date = datetime.strptime(date_str, '%Y-%m-%d')  # Convert date string to a datetime object
        if periodicity_type == "daily":
            return date  # Daily period starts on the same day
        elif periodicity_type == "weekly":
            return start_of_week(date)  # Weekly period starts at the beginning of the week
        elif periodicity_type == "monthly":
            return date.replace(day=1)  # Monthly period starts on the first day of the month
        elif periodicity_type == "yearly":
            return date.replace(month=1, day=1)  # Yearly period starts on the first day of the year

    def analyze_habits(self):
        """Analyze habits for the user with detailed information."""

        # Check if there are no habits found for the user
        if not self.habits_test:
            print("No habits found.")
            return

        # Print a summary analysis of the user's habits
        print(f"\n--- Habit Analysis ---")

        # Calculate the total number of habits
        total_habits = len(self.habits_test)

        # Calculate the total number of completed instances across all habits
        total_completed = sum(len(habit['completed_dates']) for habit in self.habits_test)

        # Calculate the average current streak across all habits
        average_streak = sum(habit['current_streak'] for habit in self.habits_test) / total_habits if total_habits > 0 else 0

        # Display the total habits, total completed instances, and average current streak
        print(f"Total Habits: {total_habits}")
        print(f"Total Completed Instances: {total_completed}")
        print(f"Average Current Streak: {average_streak:.2f} days")

        # Display detailed analysis for each habit
        for habit in self.habits_test:
            self.update_streak(habit)  # Update streak information
            print(f"\nHabit: {habit['name']}")
            print(f"  Periodicity: {habit['periodicity_display']}")
            print(f"  Specification: {habit['specification']}")
            completed_dates = ', '.join(habit['completed_dates']) if habit['completed_dates'] else "No completions yet"
            print(f"  Completed Dates: {completed_dates}")
            print(f"  Current Streak: {habit['current_streak']} days")
            print(f"  Longest Streak: {habit['longest_streak']} days")

        # End of analysis
        print("\n--- End of Analysis ---")

    def prompt_for_frequency(self, max_frequency, time_unit):
        """
        Prompt the user for the frequency of a habit (e.g., times per week or month).
        The function ensures that the frequency entered is valid.
        """
        while True:
            try:
                # Ask the user for the frequency (e.g., how many times per week or month)
                frequency = int(input(f"How many times per {time_unit}? (1-{max_frequency}): "))
                if 1 <= frequency <= max_frequency:
                    return frequency  # Return the valid frequency
                else:
                    print(f"Please enter a valid number between 1 and {max_frequency}.")
            except ValueError:
                # Handle the case where the input is not a valid integer
                print("Invalid input. Please enter a valid number.")
