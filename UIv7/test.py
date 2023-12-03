import pandas as pd

# Read the CSV file into a DataFrame
file_path = "messages.csv"
df = pd.read_csv(file_path)

# Replace 'your_column_name' with the actual name of the column you want to convert
column_name = "1111111111111111"

# Convert the specified column to a NumPy array
column_array = df[column_name].values

# Now, column_array contains the values of the specified column as a NumPy array
print(column_array)
