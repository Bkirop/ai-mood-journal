import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import warnings
# Suppress only specific warnings if needed (example: FutureWarning from pandas)
warnings.filterwarnings('ignore', category=FutureWarning)

# Set style for better visualizations
plt.style.use('default')
sns.set_palette("husl")

print("="*60)
print("COMPREHENSIVE DATA ANALYSIS: IRIS DATASET")
print("="*60)

# ==========================================
# TASK 1: LOAD AND EXPLORE THE DATASET
# ==========================================

print("\n" + "="*40)
print("TASK 1: LOAD AND EXPLORE THE DATASET")
print("="*40)

try:
    # Load the Iris dataset
    iris_data = load_iris()
    
    # Create a DataFrame
    df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)
    
    # Also create a time column for line chart (simulated dates)
    dates = pd.date_range(start='2023-01-01', periods=len(df), freq='D')
    df['date'] = dates
    
    print("✅ Dataset loaded successfully!")
    print(f"Dataset shape: {df.shape}")
    
    # Display first few rows
    print("\n1. First 5 rows of the dataset:")
    print("-" * 50)
    print(df.head())
    
    # Explore the structure
    print("\n2. Dataset structure and data types:")
    print("-" * 50)
    print("Data types:")
    print(df.dtypes)
    
    print(f"\nDataset Info:")
    print(f"- Number of rows: {len(df)}")
    print(f"- Number of columns: {len(df.columns)}")
    print(f"- Memory usage: {df.memory_usage(deep=True).sum()} bytes")
    
    # Check for missing values
    print("\n3. Missing values check:")
    print("-" * 50)
    missing_values = df.isnull().sum()
    print("Missing values per column:")
    for col, missing in missing_values.items():
        print(f"  {col}: {missing}")
    
    if missing_values.sum() == 0:
        print("✅ No missing values found - dataset is clean!")
    else:
        print("⚠️  Missing values detected - cleaning required")
        # Clean missing values (fill with median for numerical, mode for categorical)
        for col in df.columns:
            if df[col].dtype in ['int64', 'float64']:
                df[col].fillna(df[col].median(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)
        print("✅ Missing values cleaned!")

except Exception as e:
    print(f"❌ Error loading dataset: {str(e)}")
    exit()

# ==========================================
# TASK 2: BASIC DATA ANALYSIS
# ==========================================

print("\n" + "="*40)
print("TASK 2: BASIC DATA ANALYSIS")
print("="*40)

# Basic statistics
print("\n1. Basic statistics of numerical columns:")
print("-" * 50)
numerical_cols = df.select_dtypes(include=[np.number]).columns
print(df[numerical_cols].describe().round(3))

# Group analysis
print("\n2. Grouping analysis by species:")
print("-" * 50)
species_analysis = df.groupby('species')[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']].agg({
    'sepal length (cm)': ['mean', 'std'],
    'sepal width (cm)': ['mean', 'std'],
    'petal length (cm)': ['mean', 'std'],
    'petal width (cm)': ['mean', 'std']
}).round(3)

print("Mean and Standard Deviation by Species:")
print(species_analysis)

# Additional insights
print("\n3. Key findings and patterns:")
print("-" * 50)
print("📊 ANALYSIS INSIGHTS:")
print(f"• Total samples: {len(df)}")
print(f"• Number of species: {df['species'].nunique()}")
print(f"• Samples per species: {df['species'].value_counts().to_dict()}")

# Find correlations
correlations = df[numerical_cols[:-1]].corr()
# Unstack, sort, and remove self-correlations for clarity
corr_pairs = correlations.unstack()