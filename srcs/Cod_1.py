import ast # for parsing and manipulation of abstract syntax trees (AST)
import time # to measure code execution time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os

start_time=time.time()
# Function to count the number of angles per entry in the column 'ang'.
def count_angles(angle_string):# The count_angles function is applied to each element of the 'ang' column of the DataFrame. If the data has 𝑛 rows, then applying this function to the entire column has a total complexity of 𝑂(𝑛).
    try:
        # We convert the string to a list using ast.literal_eval and count the sublists (angles).
        angle_list = ast.literal_eval(angle_string.replace("\n", ","))# The complexity is O(m) where m is the length of the string (Tx sources)..
        return len(angle_list)  # The complexity is O(1)
    except:
        # If there is an error in the conversion, we return 0
        return 0
# Applying count_angles to each row has a total complexity of 𝑂(𝑛⋅𝑚).
# We apply the function to count the angles
data['angle_count'] = data['ang'].apply(count_angles)

# Separate data into groups based on the number of angles (more than one).
grouped_data = {n: data[data['angle_count'] == n] for n in range(1, 6)} # Filtering a DataFrame in pandas has a complexity of 𝑂(𝑛), since it checks each row to see if it meets the filtering criteria. Since this is done 5 times, the complexity here is 𝑂(5𝑛)=𝑂(𝑛).

# We delete the column 'angle_count' before saving the data
for n in grouped_data: # For a cycle that goes through all the rows of the database we have a complexity O(n)
    grouped_data[n].drop(columns=['angle_count'], inplace=True)

# Save each group in a CSV file
for n in range(1, 6): # For a cycle that goes through all the rows of the database we have a complexity O(n). There are 5 groups, so the complexity is 𝑂(5𝑛)=𝑂(𝑛).
    filename = f'music_data_{n}_angles.csv'
    grouped_data[n].to_csv(filename, index=False)
# Total Complexity
#  Adding all the parts, the total complexity of the code is: 𝑂(𝑛⋅𝑚)+𝑂(𝑛)+𝑂(𝑛)+𝑂(𝑛)+𝑂(𝑛)=𝑂(𝑛⋅𝑚)
end_time=time.time()
final= end_time - start_time
print( f'\n Time: {(final)*1000} ms')