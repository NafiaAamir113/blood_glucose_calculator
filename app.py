import streamlit as st

# Function to calculate estimated HbA1c
def calculate_hba1c(average_glucose):
    # Conversion formula for HbA1c (DCCT formula)
    hba1c = (average_glucose + 46.7) / 28.7
    return hba1c

# Function to provide health advice
def health_advice(glucose_level):
    if glucose_level < 70:
        return "Your blood glucose is low (Hypoglycemia). Please consume fast-acting sugar and consult your healthcare provider."
    elif 70 <= glucose_level <= 99:
        return "Your blood glucose is in the normal range. Maintain a balanced diet and regular exercise."
    elif 100 <= glucose_level <= 125:
        return "Your blood glucose is in the prediabetic range. Consider lifestyle changes like healthy eating and regular physical activity."
    else:
        return "Your blood glucose is high (Hyperglycemia). Consult your healthcare provider for proper management."

# Main Streamlit App
def main():
    st.title("🩸 Blood Glucose Level & HbA1c Calculator")
    st.write("Track your blood glucose levels, get personalized health advice, and estimate your HbA1c levels.")

    # User input for glucose level
    st.header("📋 Input Your Details")
    glucose_level = st.number_input("Enter your blood glucose level (mg/dL):", min_value=0, step=1, format="%d")
    average_glucose = st.number_input("Enter your average glucose level (mg/dL) for HbA1c estimation:", min_value=0, step=1, format="%d")

    # Calculate and display health advice
    if st.button("Get Health Advice"):
        advice = health_advice(glucose_level)
        st.success(f"💡 **Health Advice:** {advice}")

    # Calculate and display estimated HbA1c
    if st.button("Calculate HbA1c"):
        if average_glucose > 0:
            estimated_hba1c = calculate_hba1c(average_glucose)
            st.success(f"🧮 **Estimated HbA1c:** {estimated_hba1c:.2f}%")
        else:
            st.warning("Please enter a valid average glucose level for HbA1c estimation.")

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center;">
            <p>Made with ❤️ by ME</p>
            <p>For informational purposes only. Always consult your healthcare provider for medical advice.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()


