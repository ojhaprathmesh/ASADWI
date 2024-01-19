import joblib
import pandas as pd

inp_place = 'Patna'


def water_quality_check(model_file_path, csv_file_path, place=inp_place):
    wq_model = joblib.load(model_file_path)
    # Read the Excel file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Filter the DataFrame based on the place name
    result_df = df[df['District'] == place]

    # Check if result_df is empty
    if not result_df.empty:
        # Extract relevant raw_data from the result DataFrame
        input_data = result_df[['pH', 'EC in μS/cm', 'HCO3', 'Cl', 'TH', 'Ca', 'Mg', 'Na', 'K']]

        # Make predictions using the loaded model
        predictions = wq_model.predict(input_data)

        if predictions[-1] > 150:
            return "Water Not Fit For Drinking"
        else:
            return "Safe Water"

    else:
        return "No raw_data found for the specified place!"


def geology_check(model_file_path, excel_file_path, place=inp_place):
    geo_model = joblib.load(model_file_path)
    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_file_path)

    # Filter the DataFrame based on the place name
    result_df = df[df['District'] == place]

    # Check if result_df is empty
    if not result_df.empty:
        # Extract relevant raw_data from the result DataFrame
        input_data = result_df[['LaDeg', 'LaMin', 'LaSec', 'LoDeg', 'LoMin', 'LoSec', 'Elevation', 'Lining', 'MP', 'Dia']]

        # Make predictions using the loaded model
        predictions = geo_model.predict(input_data)

        # Display predictions
        return f"{round(predictions[-1],4)} meters"

    else:
        return "No raw_data found for the specified place!"


def lithology(model_file_path, excel_file_path, place=inp_place):
    litho_model = joblib.load(model_file_path)
    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_file_path)

    # Extract relevant raw_data from the result DataFrame
    input_data = df[['From', 'To', 'Thickness']]

    # Make predictions using the loaded model
    predictions = litho_model.predict(input_data)

    value = predictions[-1]
    if value <= 1:
        return "Clay And Kankar"
    elif value <= 2:
        return "Fine Sand With Clay"
    elif value <= 3:
        return "Fine Sand"
    elif value <= 4:
        return "Fine To Medium Sand"
    elif value <= 5:
        return "Coarse To Very Coarse Sand"
    elif value <= 6:
        return "Coarse Sand"
    elif value <= 7:
        return "Sandy Clay"
    elif value <= 8:
        return "Clay"
    elif value <= 9:
        return "Medium Sand"
    elif value <= 10:
        return "Gravel"

    if value <= 3.5:
        return "Digging Manually Possible"
    elif value <= 7:
        return "Digging With JCB"
    elif value <= 10:
        return "Digging With Drill"