import pandas as pd
import numpy as np

def load_data(file_path):
    """Step 1: Data Ingestion"""
    try:
        df = pd.read_csv(file_path)
        print("✅ Data Ingested Successfully")
        return df
    except FileNotFoundError:
        print("❌ Error: File not found. Please check the path.")
        return None

def transform_data(df):
    """Step 2: Data Transformation & Feature Engineering"""
    # 1. Temporal Normalization
    df['Record Date'] = pd.to_datetime(df['Record Date'], dayfirst=True)
    
    # 2. Payment Synthesis (Engineering Total Ridership)
    df['Total_Ridership'] = (df['Total Smart Cards'] + 
                             df['Total Tokens'] + 
                             df['Total QR'] + 
                             df['Total NCMC'] + 
                             df['Group Ticket'])
    
    # 3. Categorical Mapping
    df['Day_Name'] = df['Record Date'].dt.day_name()
    df['Is_Weekend'] = df['Record Date'].dt.dayofweek > 4
    
    print("✅ Transformation & Feature Engineering Complete")
    return df

def generate_insights(df):
    """Step 3: Analytical Processing"""
    avg_ridership = df['Total_Ridership'].mean()
    weekend_drop = df[df['Is_Weekend']==True]['Total_Ridership'].mean()
    
    print(f"--- 📊 Quick Report ---")
    print(f"Average Daily Ridership: {int(avg_ridership)}")
    print(f"Weekend Ridership Average: {int(weekend_drop)}")
    print("-----------------------")

if __name__ == "__main__":
    # Path to your data (Update this for your local environment)
    DATA_PATH = "data/NammaMetro_Ridership_Dataset.csv"
    
    # Run the Pipeline
    raw_data = load_data(DATA_PATH)
    if raw_data is not None:
        clean_data = transform_data(raw_data)
        generate_insights(clean_data)
        
        # Save the processed data for Power BI or further analysis
        clean_data.to_csv("data/processed_ridership.csv", index=False)
        print("✅ Clean dataset saved to data/processed_ridership.csv")
