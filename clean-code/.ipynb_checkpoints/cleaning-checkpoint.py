import pandas as pd
import numpy as np

def clean(df, country_name):
    """
    Applica trasformazioni di valore e ottimizzazione dei tipi.
    """
    df = df.copy()

    # --- 1. TRASFORMAZIONI SEMANTICHE ---
    if country_name == "China":
        df['Smoker'] = df['Smoker'].map({'Smoker': True, 'Non-Smoker': False})
        df['PhysicalActivity'] = df['PhysicalActivity'].map({"High": True, "Medium": True, "Low": False})
        df['HealthyDiet'] = df['HealthyDiet'].map({"Healthy": True, "Moderate": True, "Poor": False})
        bool_cols = ['Hypertension', 'Diabetes', 'Obesity', 'AlcoholConsumption', 'FamilyHistory', 'PreviousHeartAttack', 'Outcome']
        for col in bool_cols:
            if col in df.columns: df[col] = df[col].map({'Yes': True, 'No': False})

    elif country_name == "United States":
        df['Cholesterol'] = pd.cut(df['Cholesterol'], bins=[-float('inf'), 200, 240, float('inf')], labels=['Low', 'Normal', 'High'], right=False)
        df['StressLevel'] = pd.cut(df['StressLevel'], bins=[0, 3, 7, 11], labels=['Low', 'Medium', 'High'], right=False)
        df['IncomeLevel'] = pd.cut(df['IncomeLevel'], bins=[0, 60000, 100000, float("inf")], labels=["Low", "Middle", "High"], right=False)
        df['Obesity'] = df['Obesity'] >= 30
        df['PhysicalActivity'] = df['PhysicalActivity'] > 2
        df['AlcoholConsumption'] = df['AlcoholConsumption'] > 2
        df['HealthyDiet'] = df['HealthyDiet'].map({"Healthy": True, "Moderate": True, "Unhealthy": False})
        df['Outcome'] = df['Outcome'].map({'Heart Attack': True, 'No Heart Attack': False})

    elif country_name == "India":
        df['HealthyDiet'] = df['HealthyDiet'] > 4
        df['Cholesterol'] = pd.cut(df['Cholesterol'], bins=[-float('inf'), 200, 240, float('inf')], labels=['Low', 'Normal', 'High'], right=False)
        df['StressLevel'] = pd.cut(df['StressLevel'], bins=[0, 3, 7, 11], labels=['Low', 'Medium', 'High'], right=False)
        df['IncomeLevel'] = pd.cut(df['IncomeLevel'], bins=[0, 300000, 1000000, float('inf')], labels=["Low", "Middle", "High"], right=False)

    elif country_name == "Indonesia":
        df['Smoker'] = df['Smoker'].map({'Past': True, 'Current': True, 'Never': False})
        df['AlcoholConsumption'] = df['AlcoholConsumption'].map({'Moderate': True, 'High': True, 'None': False}).fillna(False)
        df['PhysicalActivity'] = df['PhysicalActivity'].map({'Low': False, 'Moderate': True, 'High': True})
        df['Diabetes'] = df['Diabetes'].map({'Healthy': False, 'Unhealthy': True})
        df['Cholesterol'] = pd.cut(df['Cholesterol'], bins=[-float('inf'), 200, 240, float('inf')], labels=['Low', 'Normal', 'High'], right=False)

    # --- 2. OTTIMIZZAZIONE TIPI (Casting) ---
    if 'Age' in df.columns: df['Age'] = df['Age'].astype('int16')
    if 'BloodPressure' in df.columns: df['BloodPressure'] = df['BloodPressure'].astype('int16')

    cat_cols = ['Gender', 'Cholesterol', 'StressLevel', 'IncomeLevel', 'State']
    for col in cat_cols:
        if col in df.columns: df[col] = df[col].astype('category')

    bool_cols = ['Smoker', 'Hypertension', 'Diabetes', 'Obesity', 'PhysicalActivity',
                 'HealthyDiet', 'AlcoholConsumption', 'FamilyHistory', 'PreviousHeartAttack', 'Outcome']
    for col in bool_cols:
        if col in df.columns: df[col] = df[col].fillna(False).astype('bool')

    return df