# Type or Loose It Study Helper App

## Overview

The **Type or Loose It Study Helper App** is a desktop application built with Tkinter in Python. It serves as a study aid by allowing users to type text into a text entry field. The application continuously monitors user input and clears the text if no new input is detected within 5 seconds.

## Features

- **User Input Monitoring**: Tracks user input and updates the last input time on each key press.
- **Automatic Clearing**: Clears the text entry field if no input is detected for 5 seconds.
- **Image Display**: Displays a sample image in the left frame.
- **Quit Button**: Provides a button to exit the application.

## Code Explanation
- **Window Creation: Sets up the main window and frames.
- **Image Handling: Attempts to load and display an image.
- **Text Entry: Provides a text area for user input.
- **Input Monitoring: Uses a timer to check input and clear text if necessary.
- **Event Binding: Updates the last input time on key presses.
- **Quit Functionality: Allows the user to close the application.
