import streamlit as st
import joblib 
import pandas as pd

model = joblib.load('SVM_model.pkl')
scaler = joblib.load('scaler.pkl')
columns = joblib.load('columnsl.pkl')

st.title('loan status pridiction by ADNAN ')
st.markdown('provide following details')

dep = st.slider('Number Of Dependents ' ,0,5,2)

edu = st.selectbox('Education',['Graduated','Not Graduated'])

emp = st.selectbox('Self Employed',['Yes','No'])

inc = st.number_input(
    "enter yearly income",
    min_value=0,
    max_value=100000000,
    value=25
)
lon = st.number_input(
    "Enter loan amount",
    min_value=0,
    max_value=100000000,
    value=25
)

term = st.slider('loan term ' ,0,20,2)

cbil = st.number_input(
    "Enter credit card score ",
    min_value=0,
    max_value=10000,
    value=25
)
res  = st.number_input(
    "Enter residential assets value ",
    min_value=0,
    max_value=10000000000,
    value=25
)
com  = st.number_input(
    "Enter commersial  assets value ",
    min_value=0,
    max_value=10000000000,
    value=25
)
lux  = st.number_input(
    "Enter luxury assets value ",
    min_value=0,
    max_value=10000000000,
    value=25
)
bank  = st.number_input(
    "Enter bank assets value ",
    min_value=0,
    max_value=10000000000,
    value=25
)
if st.button('check approval'):
    raw = raw = {
    'no_of_dependents': dep,
    'education': 1 if edu == 'Graduated' else 0,
    'self_employed': 1 if emp == 'Yes' else 0,
    'income_annum': inc,
    'loan_amount': lon,
    'loan_term': term,
    'cibil_score': cbil,
    'residential_assets_value': res,
    'commercial_assets_value': com,
    'luxury_assets_value': lux,
    'bank_asset_value': bank
}
    df = pd.DataFrame([raw])
    for col in columns:
        if col not in df.columns:
            df[col] = 0
    df = df[columns]
    scaled  = scaler.transform(df)
    prediction = model.predict(scaled)[0]
    if prediction == 1:
        st.success('loan will be approve')
    else:
        st.error('loan might not approve')






