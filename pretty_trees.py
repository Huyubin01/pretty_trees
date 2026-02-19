import streamlit as st

st.title('SF Trees')
st.write('''This app analyses trees in San Francisco using a dataset kindly provided by SF DPW.''')
col1,col2,col3 = st.columns(3)
with col1:
    st.write('Column 1')
with col2:
    st.write('Column 2')
with col3:
    st.write('Column 3')
    