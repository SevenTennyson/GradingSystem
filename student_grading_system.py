# Author: Seven Aaliyah Tennyson
# Student ID: A00019091
# Created: 21/10/2025

# This program calculates student grades based on weighted score components and categorises them accordingly.

from datetime import datetime
datetime.now() # Get the current date and time
# print(datetime.now()) # Print the current date and time

from pdb import main # To handle date of birth inputs and calculate ages
from tabulate import tabulate # To display student data in table format

# Sample data to demonstrate tabulate functionality
data = [
    ["Alice", 24, "Engineer"],
    ["Bob", 30, "Data Scientist"],
    ["Charlie", 28, "Teacher"]
]

# Creating a table with headers and a grid format
table = tabulate(
    data, 
    headers=["Name", "Age", "Profession"], 
    tablefmt="pipe" # "pipe", "grid", "fancy_grid", etc.
)

# print(table)


# Function to calculate overall score based on weighted components
def calculate_overall_score(cw1, cw2, cw3, final_exam): # Multiplies each score by its weight and returns the sum
    overall_score = ((cw1 * 0.10) + (cw2 * 0.20) + (cw3 * 0.30) + (final_exam * 0.40))  
    return overall_score

# Function rounds the overall score to the nearest whole number for categorisation
def round_to_category(overall_score):
    categories = [
        (100, 100),    # Gold Standard
        (82, 92),      # Upper First
        (72, 78),      # First
        (62, 68),      # Upper Second
        (52, 58),      # Lower Second
        (42, 48),      # Third
        (32, 38),      # Condonable Fail
        (5, 25),       # Fail
        (0, 0)         # No Submission
    ]

    for min_score, max_score in categories:
        if min_score <= overall_score <= max_score:
            return f"{min_score}-{max_score}"

    return "Unclassified"

print(round_to_category(68.5))  # Example test

# Example: Testing the function test_score = calculate_overall_score(85, 90, 78, 88)
test_score = calculate_overall_score(85, 90, 78, 88)
# print("Overall Score:", test_score)

# Function to determine grade category based on overall score
def determine_grade_category(overall_score): # Returns the grade category as a string
    if overall_score == 100:
        return "Gold Standard"
    elif 82 <= overall_score <= 92:
        return "Upper First"
    elif 72 <= overall_score <= 78:
        return "First"
    elif 62 <= overall_score <= 68:
        return "Upper Second"
    elif 52 <= overall_score <= 58:
        return "Lower Second"
    elif 42 <= overall_score <= 48:
        return "Third"
    elif 32 <= overall_score <= 38:
        return "Condonable Fail"
    elif 5 <= overall_score <= 25:
        return "Fail"
    elif overall_score == 0:
        return "No Submission"
    else:
        return "Unclassified"
    
print(determine_grade_category(68.5))  # Example test
        
        
'''
The main function collects up to 3 student data entries, 
stores them in a list 'students[]' and displays the results in a table
'''
def main(name, dob, age, cw1, cw2, cw3, final_exam):
# Introduction message
    print("=========================================")
    print("Welcome to the Student Grading System")
    print("=========================================")
    print("Please enter the details for up to 3 students.")
    print()
    
    '''
    students = []  # List to store student data entries
    id = input("Enter student's ID: ")
    name = input("Enter student's name: ")
    dob = input("Enter student's date of birth (YYYY-MM-DD): ")
    cw1 = float(input("Enter score for Coursework 1 (out of 100): "))
    cw2 = float(input("Enter score for Coursework 2 (out of 100): "))
    cw3 = float(input("Enter score for Coursework 3 (out of 100): "))
    final_exam = float(input("Enter score for Final Exam (out of 100): "))
    '''
main("John Doe", "2000-01-01", 24, 85, 90, 78, 88)