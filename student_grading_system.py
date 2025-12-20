# Author: Seven Aaliyah Tennyson
# Student ID: A00019091
# Created: 21/10/2025

# This program calculates student grades based on weighted score components and categorises them accordingly.

from datetime import datetime # To handle date of birth inputs and calculate ages
from tabulate import tabulate # To display student data in table format

# Function to calculate overall score based on weighted components
def calculate_overall_score(cw1, cw2, cw3, final_exam): # Multiplies each score by its weight and returns the sum
    overall_score = ((cw1 * 0.10) + (cw2 * 0.20) + (cw3 * 0.30) + (final_exam * 0.40))  
    return overall_score
