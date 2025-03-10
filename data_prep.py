import pandas as pd
import numpy as np
from pathlib import Path

def load_and_clean_data():
    # Read the Excel file
    input_path = Path('../dataset/raw/Practice Question.xlsx')
    df = pd.read_excel(input_path)
    
    # Display initial information about the dataset
    print("Initial Dataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Basic cleaning steps
    # 1. Remove duplicates if any
    df = df.drop_duplicates()
    
    # 2. Handle missing values
    # Fill numeric columns with median
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
    
    # Fill categorical columns with mode
    categorical_columns = df.select_dtypes(include=['object']).columns
    df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])
    
    # 3. Convert data types if needed
    # Add specific type conversions based on your columns
    
    print("\nDataset Info After Cleaning:")
    print(df.info())
    
    return df

if __name__ == "__main__":
    cleaned_data = load_and_clean_data()
    
    # Create processed directory if it doesn't exist
    output_dir = Path('../dataset/processed')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save cleaned dataset
    output_path = output_dir / 'cleaned_data.csv'
    cleaned_data.to_csv(output_path, index=False)
    print(f"\nCleaned data saved to {output_path}")