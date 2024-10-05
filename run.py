"""App for students, parents, and teachers to fill surveys and store data."""
import time
import sys
from pyfiglet import Figlet
import gspread
from google.oauth2.service_account import Credentials

# Import question lists from an external module
from questions import student_questions, parent_questions, teacher_questions


reset = "\033[0m"  # Resets color, returns to default color
# Text color codes
red = "\033[31m"  # Red
green = "\033[32m"  # Green
yellow = "\033[33m"  # Yellow
cyan = "\033[36m"  # Cyan
white = "\033[37m"  # White

f = Figlet(font="slant")
copyright = """
    Education Survey.
    https://github.com/swecery/EducationSurvey
    Licensed under GNU GENERAL PUBLIC LICENSE
    Copyright (c) 2023 Ceren Yildiran\n
"""


def get_google_sheet():
    """Define OAuth2.0 scope for Google Sheets and Drive access."""
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]
    # Load credentials from a service account JSON key file (creds.json).
    creds = Credentials.from_service_account_file("creds.json")
    # Authorize the client with the specified scope.
    scoped_creds = creds.with_scopes(scope)
    # Create a Gspread client authorized with the specified credentials.
    gspread_client = gspread.authorize(scoped_creds)
    # Open the Google Sheets spreadsheet by its name ("edusurvey").
    sheet = gspread_client.open("edusurvey")
    # Get a reference to the "Sheet1" worksheet within the spreadsheet.
    sheet1 = sheet.worksheet("Sheet1")

    # Return the reference to the worksheet.
    return sheet1


def save_data(data):
    """Save the given data to Google Sheets."""
    sheet = get_google_sheet()
    # Get the current number of rows
    row_count = len(sheet.get_all_values())
    # Check the maximum row limit
    if row_count >= 1000:
        print("Maximum row limit reached. You may need to create a new sheet.")
        return
    # Calculate the index of the new row
    row_index = row_count + 1
    # Write the data to cells
    for i, value in enumerate(data):
        sheet.update_cell(row_index, i + 1, value)


def show_data():
    """Retrieve and display survey data from Google Sheets."""
    # Ask the user for data and store the result in mydata
    mydata = ask_question()
    # Check if user provided valid data
    if mydata is not None:
        # Save the user's data
        save_data(mydata)
        # Get the Google Sheet
        sheet = get_google_sheet()
        # Retrieve all data from the sheet
        data = sheet.get_all_values()
        # Extract column names (headers) from the data
        column_names = data[0]
        # Display the data in a table format along with the column names
        print_table(data, column_names)


def print_table(data, column_name):
    """Print table headers and rows to the console."""
    # Print the table headers in red color
    print(red + "| {:>10} | {:>10} | {:>10} | {:>10} |".format(*column_name))
    # Print the data rows in white color
    for row in data[1:]:
        formatted_row = []
        for cell in row:
            formatted_cell = "{:>10}".format(cell)
            formatted_row.append(formatted_cell)
        print(white + "| {} | {} | {} | {} |".format(*formatted_row))


def show_loading_animation():
    """
    Display a simple loading animation in the console.

    This function prints 10 dots in a row to simulate a loading animation.
    """
    for _ in range(10):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\n")
    sys.stdout.flush()


def who_are_you():
    """Prompt user for name validation and return it."""
    while True:
        who = input(cyan + "Enter your name (to end the survey press 'q'):")
        # Remove leading and trailing spaces
        who = who.strip()
        if who == "q":
            return who
        # Check the length and content of the input
        elif len(who) >= 3 and len(who) <= 10 and who.isalpha():
            return who
        else:
            error = "Invalid input. Name: 3-10 characters, letters only."
            print(cyan + error + reset)
            print(yellow + "Example: John, Alice" + reset)


def ask_question():
    """Build a function to set user roles and ask questions."""
    while True:
        user_data = []  # Store user data
        try:
            # Prompt the user to choose their role and handle input exceptions
            print(cyan + f.renderText(" Education\n Survey") + reset)
            print(cyan + copyright + reset)
            who = who_are_you()
            if who == "q":
                print("Good Bye!")
                return None
            user_data.append(who)
            question = input(
                cyan
                + "Select your group (to end the survey press 'q')\n"
                + red
                + "1) Student\n"
                + green
                + "2) Parent\n"
                + yellow
                + "3) Teacher\n"
                + reset
                + "Your answer: "
            )
            if question == "q":
                return None
            question = int(question)
        except ValueError:
            # Handle non-integer input gracefully
            print(red + "[!] Please enter a number" + reset)
            continue
        if question == 1:
            result = answer_questions(student_questions)
            if result is None:
                print("Good Bye!")
                return None
            convert = convert_to_percentage(result)
            user_data.extend(["student", result, convert])
            print(
                green
                + "Your score is, "
                + yellow
                + str(result)
                + green
                + "\nThis is your satisfaction percentage, "
                + yellow
                + str(convert_to_percentage(result))
                + "%"
                + reset
            )
            print("Calculating your results ", end="")
            show_loading_animation()
            return user_data
        elif question == 2:
            # If '2' chosen, call 'answer_questions' with parent questions
            result = answer_questions(parent_questions)
            if result is None:
                print("Good Bye!")
                return None
            convert = convert_to_percentage(result)
            user_data.extend(["parent", result, convert])
            print(
                green
                + "Your score is, "
                + yellow
                + str(result)
                + green
                + "\nThis is your satisfaction percentage, "
                + yellow
                + str(convert_to_percentage(result))
                + "%"
                + reset
            )
            print("Calculating your results ", end="")
            show_loading_animation()
            return user_data
        elif question == 3:
            # If '3' chosen, 'answer_questions' with teacher question
            result = answer_questions(teacher_questions)
            if result is None:
                print("Good Bye!")
                return None
            convert = convert_to_percentage(result)
            user_data.extend(["teacher", result, convert])
            print(
                green
                + "Your score is, "
                + yellow
                + str(result)
                + green
                + "\nThis is your satisfaction percentage, "
                + yellow
                + str(convert_to_percentage(result))
                + "%"
                + reset
            )
            print("Calculating your results ", end="")
            show_loading_animation()
            return user_data
        else:
            # Handle invalid input
            print(red + "[!] Please enter the correct number (1/2/3)." + reset)
            print(cyan + "Options:\n1) Student\n2) Parent\n3) Teacher" + reset)
            continue


def answer_questions(questions):
    """Ask and score the provided questions."""
    point = 0  # Initialize the total score
    for q in questions:  # Iterate through each question in the list
        while True:  # Ensure a valid response by starting a loop for the user.
            print(cyan + "Enter your answer between 1 and 5" + reset)
            try:
                answer = input(
                    q + green + "\nAnswer: " + yellow
                )  # Get the user's answer and attempt integer conversion
                if answer == "q":
                    return None
                elif int(answer) <= 0 or int(answer) > 5:
                    err = "Enter 5 to agree, or 1 to disagree."
                    print(red + "[!] Enter a number between 1 and 5." + reset)
                    print(yellow + err + reset)
                    continue  # If not 1-5, show error and restart
                else:
                    point = point + int(answer)  # Add the answer to the total
                    break  # End the loop when a valid answer is obtained
            except ValueError:
                print(
                    red + "[!] Please enter a number." + reset
                )  # Display an error message if the answer is not a number
    return point  # Return the total score


def convert_to_percentage(number):
    """Calculate the percentage value of the given number."""
    percentage = int((number / 10) / 5 * 100)
    return percentage


if __name__ == "__main__":
    # Call the main function to start the program
    show_data()
