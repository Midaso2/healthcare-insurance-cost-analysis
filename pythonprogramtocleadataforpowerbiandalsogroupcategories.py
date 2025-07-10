import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('Star_cleaned_insurance.csv')

# Round charges to 2 decimal places
df['charges'] = df['charges'].round(2)

# Charges bands (interpretable brackets)
def charges_band(val):
    if val < 5000:
        return "<5,000"
    elif val < 10000:
        return "5,000–9,999"
    elif val < 20000:
        return "10,000–19,999"
    elif val < 30000:
        return "20,000–29,999"
    elif val < 50000:
        return "30,000–49,999"
    else:
        return "50,000+"

df['charges_band'] = df['charges'].apply(charges_band)

# BMI category (numeric bands)
def bmi_category(val):
    if val < 18.5:
        return "<18.5"
    elif val < 25:
        return "18.5–24.9"
    elif val < 30:
        return "25–29.9"
    elif val < 35:
        return "30–34.9"
    else:
        return "35+"

df['bmi_category'] = df['bmi'].apply(bmi_category)

# Age group (numeric)
def age_group(val):
    if val < 26:
        return "18–25"
    elif val < 36:
        return "26–35"
    elif val < 46:
        return "36–45"
    elif val < 56:
        return "46–55"
    elif val < 66:
        return "56–65"
    else:
        return "66+"

df['age_group'] = df['age'].apply(age_group)

# Age group (label)
def age_group_label(val):
    if val < 26:
        return "Young Adult"
    elif val < 36:
        return "Adult"
    elif val < 46:
        return "Middle Age"
    elif val < 56:
        return "Senior"
    elif val < 66:
        return "Elder"
    else:
        return "Super Senior"

df['age_group_label'] = df['age'].apply(age_group_label)

# Save to CSV
df.to_csv('powerbigroupeddata.csv', index=False)

print("Enhanced data saved as 'powerbigroupeddata.csv'")
