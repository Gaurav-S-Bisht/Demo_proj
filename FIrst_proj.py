import streamlit as st
st.balloons()
st.title("Hello this is my first Page")
st.write("Welcome to the app creation module.....")
st.text_input('Enter your name:-')
st.number_input('Enter your marks...:-')
x=st.radio('Are you a a working professional',options=['Yes','No'])
if x=='Yes':
    st.write('You can choose weekend Batch')
else:
    st.write('You can choose Weekdays Batch')

st.sidebar.markdown('Test Result')
y=st.sidebar.checkbox('Are you looking for another advance industrial training experience')

if y==1:
    st.sidebar.write('You can freely contact with our counsellors for further enquiry')