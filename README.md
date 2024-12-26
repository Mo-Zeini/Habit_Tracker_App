# Habit Tracker App

## Overview
The Habit Tracker app is a Python-based application designed to help users build, monitor, and analyze their habits effectively. It provides features for adding, editing, and tracking habits with detailed analytics to improve user productivity and consistency. This app is ideal for individuals looking to develop better habits and maintain a streak-based tracking system.

## Features

- Add new habits with specific details (name, periodicity, specifications)
- View all existing habits
- Edit, reset, or remove habits
- Check off habits as completed
- Analyze habits with insights on streaks and completion rates
- Save and load habits automatically using a JSON file

## Requirements

- Python 3.7 or later
- `json` module (standard library)
- `datetime` module (standard library)

## File Structure

The Habit Tracker app consists of the following files:

1. **`habit_tracker_app.py`**: Contains the core logic for managing habits. Includes classes and methods for adding, editing, tracking, and analyzing habits.

2. **`main.py`**: Serves as the entry point for the application. Initializes the `HabitTracker` class and provides the user interface for managing habits.

3. **`habits.json`**: A JSON file that stores all user habit data persistently. Automatically created and updated by the app.

4. **`test.py`**: Contains unit tests for validating the functionality of the app. Tests features such as adding habits, editing habits, checking off habits, and analyzing data.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Mo-Zeini/Habit_Tracker_App.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Habit_Tracker_App
   ```
3. Run the application:
   ```bash
   python main.py
   ```
4. Follow the on-screen menu to:
    - Add a new habit.
    - View existing habits.
    - Edit, reset, or remove habits.
    - Check off habits as completed.
    - Analyze your habits.

### Example

Upon running the application, you will see the following options:

```
--- Dashboard ---
1. Add New Habit
2. Show Existing Habits
3. Edit Existing Habit
4. Habit Analysis
5. Check Off Habit
6. Exit
```

Select an option to perform the desired actions. The app will guide you through each process with clear prompts.

## Habit JSON File Structure

The app saves habits in a `habits.json` file. Each habit has the following structure:

```json
{
    "name": "Habit Name",
    "periodicity": <frequency>,
    "periodicity_display": "Display Periodicity",
    "periodicity_type": "daily|weekly|monthly|yearly",
    "specification": "Habit details",
    "completed_dates": ["YYYY-MM-DD", ...],
    "current_streak": <current streak>,
    "longest_streak": <longest streak>
}
```

### Example

```json
[
    {
        "name": "Morning Exercise",
        "periodicity": 1,
        "periodicity_display": "Daily",
        "periodicity_type": "daily",
        "specification": "30 minutes of yoga or jogging",
        "completed_dates": ["2024-11-04", "2024-11-05"],
        "current_streak": 2,
        "longest_streak": 2
    }
]
```

## Testing

The app includes a test suite located in `test.py`. This suite uses Python's `unittest` framework to validate core functionalities. To run the tests:

```bash
python -m unittest test.py
```

### Features Tested
- Adding a habit
- Viewing habits
- Editing or resetting a habit
- Checking off a habit
- Analyzing habits for streaks and completion rates

## Enhancements

### Future Improvements
- Add a graphical user interface (GUI) for improved user experience.
- Add visual analytics for habit performance.

### Current Limitations
- The app operates through a command-line interface only.
- All data is stored locally in a JSON file.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Mo-Zeini/Habit_Tracker_App/blob/main/LICENSE.txt) file for details.

## Author

- [Mohamed Elzeini](https://github.com/Mo-Zeini)

## Acknowledgements

- This app was developed as part of a project assigned by IU International University of Applied Sciences for the Bachelor of Applied Artificial Intelligence program.

