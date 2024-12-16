import os
import pandas as pd
import plotly.express as px

# Define the path to the folder containing your data files
folder_path = r"C:\Users\asus\Downloads\archive\cleaned_dataset"


# Initialize an empty DataFrame to combine all relevant data
combined_data = pd.DataFrame()

# Load all CSV files and combine them
for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):
        file_path = os.path.join(folder_path, file_name)
        temp_data = pd.read_csv(file_path)
        combined_data = pd.concat([combined_data, temp_data], ignore_index=True)

# Inspect the combined dataset
print(combined_data.head())
print(combined_data.columns)

# Filter columns of interest (Cycle, Battery_impedance, Re, Rct)
# Adjust the column names based on your dataset
filtered_data = combined_data[['test_id', 'Re', 'Rct']]



# Drop rows with missing values (if any)
filtered_data = filtered_data.dropna()

# Plot 1: Battery Impedance vs. Cycle
fig1 = px.line(filtered_data,
               x='test_id',
               y='Re',
               title='Electrolyte Resistance (Re) over Test Cycles',
               labels={'test_id': 'Cycle Number', 'Re': 'Impedance (Ohms)'})
fig2 = px.line(filtered_data,
               x='test_id',
               y='Rct',
               title='Charge Transfer Resistance (Rct) over Test Cycles',
               labels={'test_id': 'Cycle Number', 'Rct': 'Impedance (Ohms)'})

# Show the plots
fig1.show()
fig2.show()

# Plot 3: Rct (Charge Transfer Resistance) vs. Cycle
fig3 = px.line(filtered_data, x='Cycle', y='Rct',
               title='Charge Transfer Resistance (Rct) vs. Aging Cycles',
               labels={'Cycle': 'Cycle Number', 'Rct': 'Resistance (Ohms)'})
fig3.show()

# Combined Plot: Battery Impedance, Re, Rct vs. Cycle
melted_data = filtered_data.melt(id_vars='Cycle',
                                 value_vars=['Battery_impedance', 'Re', 'Rct'],
                                 var_name='Parameter', value_name='Value')

fig4 = px.line(melted_data, x='Cycle', y='Value', color='Parameter',
               title='Battery Parameters vs. Aging Cycles',
               labels={'Cycle': 'Cycle Number', 'Value': 'Resistance (Ohms)'})
fig4.show()
