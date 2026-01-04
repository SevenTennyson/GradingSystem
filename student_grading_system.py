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


# This function rounds the overall score to the nearest whole number for categorisation
def round_to_category(score): # score is the grade to be categorised
    categories = [
        (0, "No Submission"),
        (5, "Fail"),
        (15, "Fail"),
        (25, "Fail"),
        (32, "Condonable Fail"),
        (35, "Condonable Fail"),
        (38, "Condonable Fail"),
        (42, "Third"),
        (45, "Third"),
        (48, "Third"),
        (52, "Lower Second"),
        (55, "Lower Second"),
        (58, "Lower Second"),
        (62, "Upper Second"),
        (65, "Upper Second"),
        (68, "Upper Second"),
        (72, "First"),
        (75, "First"),
        (78, "First"),
        (82, "Upper First"),
        (85, "Upper First"),
        (92, "Upper First"),
        (100, "Gold Standard")
    ]
    
    if score == 100:
        return (100, "Gold Standard")
    if score == 0:
        return (0, "No Submission")
    if score < 0 or score > 100:
        return "Unclassified"
    
    nearest_lower = None
    nearest_upper = None
    
    for mark, category in categories:
        if mark <= score:
            nearest_lower = (mark, category)
        elif mark >= score and nearest_upper is None:
            nearest_upper = (mark, category)
            break
        
    if nearest_upper is None:
        return nearest_lower
    
    lower_distance = score - nearest_lower[0]
    upper_distance = nearest_upper[0] - score
    
    # Determine which is closer
    if lower_distance < upper_distance:
        return nearest_lower
    elif upper_distance < lower_distance:
        return nearest_upper
    else:
        # If equidistant, round up
        return nearest_upper
    
    
    '''
    for min_score, max_score in categories:
        if min_score <= score <= max_score:
            return f"{min_score}-{max_score}"
        

    return "Unclassified"
    '''

result = round_to_category(68.5)  # Example test
print("result: ", result)

# Example: Testing the function test_score = calculate_overall_score(85, 90, 78, 88)
test_score = calculate_overall_score(85, 90, 78, 88)
print("Overall Score:", test_score)

        
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


# Saving student data to .txt file
# Cleaner code
with open("student_data.txt", "a") as file:
    file.write(f"{student_name}, {student_id}, {overall_grade}, {category}\n")

# Open the file in read mode
with open("student_data.txt", "r") as file:
    for line in file:
        # Remove any extra newline characters
        line = line.strip()
        print(line)
        return "Student information saved to student_data.txt"