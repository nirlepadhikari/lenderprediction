import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .viewerBadge_link__1S137 {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.sidebar.slider("Client's Age",18,80)
st.sidebar.selectbox("Application Type",["Sole","Sws","Joint"])
st.sidebar.number_input("Comprehensive Score")
st.sidebar.number_input("Veda Score 1.1")
st.sidebar.radio("Current Payday Loans?",["Yes","No"])
YoN= st.sidebar.radio("Payday Lender Enquiries?",["Yes","No"])
if YoN:
  st.sidebar.date_input("Date")
st.sidebar.selectbox("Residence Type",["Renting","Bording","Own","Mortgage"])
st.sidebar.number_input("Time in curent residence(months)")
st.sidebar.number_input("Time in previous residence(months)")
st.sidebar.selectbox("Current employment Status",["Full Time","Part Time","Casual","Mortgage"])
st.sidebar.number_input("Current employment duration (months)")
st.sidebar.selectbox("Previous employment Status",["Full Time","Part Time","Casual","Mortgage"])
st.sidebar.number_input("Previous employment duration (months)")
AdverseOrDefaults= st.sidebar.radio("Adverse Or Defaults?",["Yes","No"])
if AdverseOrDefaults=="Yes":
  st.sidebar.date_input("Input Date")
  st.sidebar.number_input("Amount")
st.sidebar.number_input("Asset Age(year)")
st.sidebar.number_input("Book Value")
st.header("Artificial Intelligence Lender Prediction")
st.markdown("<img src='https://editor.analyticsvidhya.com/uploads/70332https___specials-images.forbesimg.com_dam_imageserve_966248982_960x0.jpg' style='max-height:300px; max-width=300px;'></img>",unsafe_allow_html=True)



