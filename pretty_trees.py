import streamlit as st

st.title('SF Trees')
st.write('''This app analyses trees in San Francisco using a dataset kindly provided by SF DPW.''')

#让用户输入决定列宽度
first_width = st.number_input('First Width',min_value=1,value=1)
second_width = st.number_input('Second Width',min_value=1,value=1)
third_width = st.number_input('Third Width',min_value=1,value=1)
col1,col2,col3 = st.columns((first_width,second_width,third_width))
with col1:
    st.write('First column')
with col2:
    st.write('second column')
with col3:
    st.write('third column')
#上面代码的简易写法,用with语句更整洁，更易于理解和调试 
# col1.write('Column 1')
# col2.write('Column 2')
# col3.write('Column 3')  
#三种列宽度设置，它们都产生了相同的列宽度
#option1
# col1,col2,col3 = st.columns((1,1,1))
# #option2
# col1,col2,col3 = st.columns((10,10,10))
# #option3
# col1,col2,col3 = st.columns(3)