import os
import pandas as pd

# Input and output folder paths
input_folder = r"D:\3_2_AD\SecureIoT-NLP\data"
output_folder = r"D:\3_2_AD\SecureIoT-NLP\data\processed"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Function to process a single file
def process_file(file_path, output_path):
    # Load the data
    data = pd.read_csv(file_path, delim_whitespace=True, header=None)

    # Separate sensor states and labels
    sensor_data = data.iloc[:, :-2]
    labels = data.iloc[:, -2:]

    # Add is_active column
    sensor_data = sensor_data.copy()
    sensor_data['is_active'] = sensor_data.sum(axis=1)

    # Filter active rows
    filtered_data = sensor_data[sensor_data['is_active'] > 0].drop(columns=['is_active'])
    filtered_data = pd.concat([filtered_data, labels.reset_index(drop=True)], axis=1)

    # Save the processed file
    filtered_data.to_csv(output_path, index=False)

# Process all files in House A and House B
for house in ["House_A", "House_B"]:
    house_folder = os.path.join(input_folder, house)
    for file_name in os.listdir(house_folder):
        if file_name.endswith(".txt"):  # Process only .txt files
            input_file = os.path.join(house_folder, file_name)
            output_file = os.path.join(output_folder, f"{house}_{file_name.replace('.txt', '.csv')}")
            process_file(input_file, output_file)
            print(f"Processed: {input_file} -> {output_file}")
