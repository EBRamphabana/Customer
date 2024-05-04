import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, ttest_ind
import streamlit as st

# Define function to calculate correlation and plot BMI vs Glucose
def plot_bmi_glucose(df):
    # Null and Alternative Hypotheses
    H0 = "There is no correlation between BMI and Glucose levels."
    H1 = "There is a correlation between BMI and Glucose levels."

    # Calculate correlation
    correlation_coefficient, p_value = pearsonr(df['BMI'], df['Glucose'])

    # Plot
    plt.figure(figsize=(8, 6))
    sns.regplot(data=df, x='BMI', y='Glucose')
    plt.title('Scatter Plot of BMI vs Glucose Levels')
    plt.xlabel('BMI')
    plt.ylabel('Glucose Levels')

    # Statistical test
    alpha = 0.05
    if p_value < alpha:
        conclusion = "We fail to reject the null hypothesis."
    else:
        conclusion = "We reject the null hypothesis."

    # Conclusion
    st.write("Null Hypothesis (H0):", H0)
    st.write("Alternative Hypothesis (H1):", H1)
    st.write("Correlation Coefficient:", correlation_coefficient)
    st.write("p-value:", p_value)
    st.write("Conclusion:", conclusion)

    st.pyplot(plt)

# Define function to calculate correlation and plot BMI vs Cholesterol
def plot_bmi_cholesterol(df):
    # Null and Alternative Hypotheses
    H0 = "There is no correlation between BMI and Cholesterol levels."
    H1 = "There is a correlation between BMI and Cholesterol levels."

    # Calculate correlation
    correlation_coefficient, p_value = pearsonr(df['BMI'], df['CHL'])

    # Plot
    plt.figure(figsize=(8, 6))
    sns.regplot(data=df, x='BMI', y='CHL')
    plt.title('Scatter Plot of BMI vs Cholesterol Levels')
    plt.xlabel('BMI')
    plt.ylabel('Cholesterol Levels')

    # Statistical test
    alpha = 0.05
    if p_value < alpha:
        conclusion = "We fail to reject the null hypothesis."
    else:
        conclusion = "We reject the null hypothesis."

    # Conclusion
    st.write("Null Hypothesis (H0):", H0)
    st.write("Alternative Hypothesis (H1):", H1)
    st.write("Correlation Coefficient:", correlation_coefficient)
    st.write("p-value:", p_value)
    st.write("Conclusion:", conclusion)

    st.pyplot(plt)

# Define function to calculate correlation and plot BMI vs Blood Pressure
def plot_bmi_blood_pressure(df):
    # Null and Alternative Hypotheses
    H0 = "There is no correlation between BMI and Blood Pressure."
    H1 = "There is a correlation between BMI and Blood Pressure."

    # Calculate correlation
    correlation_coefficient_sbp, p_value_sbp = pearsonr(df['BMI'], df['SBP'])
    correlation_coefficient_dbp, p_value_dbp = pearsonr(df['BMI'], df['DBP'])

    # Plot
    plt.figure(figsize=(12, 6))

    # Scatter plot for Systolic Blood Pressure
    plt.subplot(1, 2, 1)
    sns.regplot(data=df, x='BMI', y='SBP')
    plt.title('BMI vs Systolic Blood Pressure')
    plt.xlabel('BMI')
    plt.ylabel('Systolic Blood Pressure')

    # Scatter plot for Diastolic Blood Pressure
    plt.subplot(1, 2, 2)
    sns.regplot(data=df, x='BMI', y='DBP')
    plt.title('BMI vs Diastolic Blood Pressure')
    plt.xlabel('BMI')
    plt.ylabel('Diastolic Blood Pressure')

    plt.tight_layout()

    # Statistical test
    alpha = 0.05
    if p_value_sbp < alpha or p_value_dbp < alpha:
        conclusion = "We fail to reject the null hypothesis."
    else:
        conclusion = "We reject the null hypothesis."

    # Conclusion
    st.write("Null Hypothesis (H0):", H0)
    st.write("Alternative Hypothesis (H1):", H1)
    st.write("Correlation Coefficient (SBP):", correlation_coefficient_sbp)
    st.write("p-value (SBP):", p_value_sbp)
    st.write("Correlation Coefficient (DBP):", correlation_coefficient_dbp)
    st.write("p-value (DBP):", p_value_dbp)
    st.write("Conclusion:", conclusion)

    st.pyplot(plt)

# Main function
def main():
    # Load data from Excel file
   
    file_path = "C:/Users/202101775/Downloads/codsoft_project/data.xlsx"
    df = pd.read_excel(file_path)

    # Streamlit app
    st.title("Health Analysis Dashboard")

    # Define tabs
    tabs = ["Home", "BMI vs Glucose", "BMI vs Cholesterol", "BMI vs Blood Pressure"]
    page = st.sidebar.radio("Navigation", tabs)

    # Home tab
    if page == "Home":
        st.write("Welcome to the Health Analysis Dashboard!")
        st.write("This dashboard analyzes the relationships between BMI and various health parameters such as Glucose levels, Cholesterol levels, and Blood Pressure.")
        st.write("Use the tabs on the left to navigate between different visualizations.")

    # BMI vs Glucose tab
    elif page == "BMI vs Glucose":
        st.header("BMI vs Glucose Levels")
        plot_bmi_glucose(df)
        st.write("Conclusion: Based on the correlation coefficient of -0.1908 and a p-value of 0.5974, we fail to reject the null hypothesis. This suggests that there is insufficient evidence to conclude a significant correlation between BMI and Glucose levels. Further analysis with a larger sample size may be necessary to draw stronger conclusions.")

    # BMI vs Cholesterol tab
    elif page == "BMI vs Cholesterol":
        st.header("BMI vs Cholesterol Levels")
        plot_bmi_cholesterol(df)
        st.write("Conclusion: With a correlation coefficient of -0.5739 and a p-value of 0.0828, we fail to reject the null hypothesis. This indicates that there is not enough evidence to support a significant correlation between BMI and Cholesterol levels. However, it's worth noting that the correlation coefficient suggests a moderately strong negative correlation, which could be explored further with additional data points.")

    # BMI vs Blood Pressure tab
    elif page == "BMI vs Blood Pressure":
        st.header("BMI vs Blood Pressure")
        plot_bmi_blood_pressure(df)
        st.write("Conclusion: The correlation coefficients for both Systolic Blood Pressure (SBP) and Diastolic Blood Pressure (DBP) are 0.0388 and 0.0956, respectively, with p-values of 0.9153 and 0.7929. These values indicate a lack of significant correlation between BMI and either SBP or DBP. Thus, we fail to reject the null hypothesis. It appears that BMI is not strongly associated with variations in blood pressure within this sample. Further investigation with a larger and more diverse dataset could provide additional insights.")

# Run the app
if __name__ == "__main__":
    main()


