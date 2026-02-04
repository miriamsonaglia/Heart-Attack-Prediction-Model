DATA_CONFIG = {
    "China": {
        "file": "heart_attack_china.csv",
        "drop": [
            'Education_Level', 'Employment_Status', 'Air_Pollution_Exposure',
            'Healthcare_Access', 'Rural_or_Urban', 'Region', 'Province',
            'Hospital_Availability', 'TCM_Use', 'Chronic_Kidney_Disease', 'CVD_Risk_Score'
        ],
        "rename": {
            'Patient_ID': 'PatientID', 'Smoking_Status': 'Smoker', 'Cholesterol_Level': 'Cholesterol',
            'Physical_Activity': 'PhysicalActivity', 'Diet_Score': 'HealthyDiet', 'Income_Level': 'IncomeLevel',
            'Blood_Pressure': 'BloodPressure', 'Previous_Heart_Attack': 'PreviousHeartAttack',
            'Family_History_CVD': 'FamilyHistory', 'Stress_Level': 'StressLevel',
            'Alcohol_Consumption': 'AlcoholConsumption', 'Heart_Attack': 'Outcome'
        }
    },
    "United States": {
        "file": "heart_attack_us.csv",
        "drop": [
            'EducationLevel', 'ST_Depression', 'EmploymentStatus', 'MaritalStatus', 'Ethnicity',
            'Medication', 'ChestPainType', 'ECGResults', 'ExerciseInducedAngina', 'Slope',
            'NumberOfMajorVessels', 'Thalassemia', 'StrokeHistory', 'Residence', 'MaxHeartRate', 'HeartRate'
        ],
        "rename": {
            'BMI': 'Obesity', 'Income': 'IncomeLevel', 'Patient_ID': 'PatientID', 'Diet': 'HealthyDiet'
        }
    },
    "India": {
        "file": "heart_attack_india.csv",
        "drop": [
            'State_Name', 'Triglyceride_Level', 'LDL_Level', 'HDL_Level', 'Diastolic_BP',
            'Air_Pollution_Exposure', 'Healthcare_Access', 'Emergency_Response_Time', 'Health_Insurance'
        ],
        "rename": {
            'Patient_ID': 'PatientID', 'Smoking': 'Smoker', 'Alcohol_Consumption': 'AlcoholConsumption',
            'Physical_Activity': 'PhysicalActivity', 'Diet_Score': 'HealthyDiet', 'Cholesterol_Level': 'Cholesterol',
            'Systolic_BP': 'BloodPressure', 'Family_History': 'FamilyHistory', 'Stress_Level': 'StressLevel',
            'Heart_Attack_History': 'PreviousHeartAttack', 'Annual_Income': 'IncomeLevel', 'Heart_Attack_Risk': 'Outcome'
        }
    },
    "Indonesia": {
        "file": "heart_attack_indonesia.csv",
        "drop": [
            'region', 'waist_circumference', 'air_pollution_exposure', 'sleep_hours',
            'blood_pressure_diastolic', 'fasting_blood_sugar', 'cholesterol_hdl', 'cholesterol_ldl',
            'triglycerides', 'EKG_results', 'medication_usage', 'participated_in_free_screening'
        ],
        "rename": {
            'age': 'Age', 'gender': 'Gender', 'income_level': 'IncomeLevel', 'hypertension': 'Hypertension',
            'diabetes': 'Diabetes', 'cholesterol_level': 'Cholesterol', 'obesity': 'Obesity',
            'family_history': 'FamilyHistory', 'smoking_status': 'Smoker', 'alcohol_consumption': 'AlcoholConsumption',
            'physical_activity': 'PhysicalActivity', 'dietary_habits': 'HealthyDiet', 'stress_level': 'StressLevel',
            'blood_pressure_systolic': 'BloodPressure', 'previous_heart_disease': 'PreviousHeartAttack',
            'heart_attack': 'Outcome'
        }
    }
}