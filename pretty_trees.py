import streamlit as st
import pandas as pd
import          .express as px
#设为宽格式
st.set_page_config(layout = 'wide')

st.title('SF Trees')
st.write('''This app analyses trees in San Francisco using a dataset kindly provided by SF DPW.''')

trees_df = pd.read_csv('trees.csv')
today = pd.to_datetime('today')
trees_df['date'] = pd.to_datetime(trees_df['date'])
trees_df['age'] = (today - trees_df['date']).dt.days
unique_caretakers = trees_df['caretaker'].unique()
#按树木所有者分类
owners = st.sidebar.multiselect('Tree Owner Filter',trees_df['caretaker'].unique())
if owners:
    trees_df = trees_df[trees_df['caretaker'].isin(owners)]
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

col1,col2 = st.columns(2)
with col1:
    fig = px.histogram(trees_df,x=trees_df['dbh'],title='Tree Width')
    st.plotly_chart(fig)
with col2:
    fig = px.histogram(trees_df,x=trees_df['age'],title='Tree Age')
    st.plotly_chart(fig)
st.write('Trees by Location')
trees_df = trees_df.dropna(subset=['longitude','latitude'])
trees_df = trees_df.sample(n=1000,replace=True)
st.map(trees_df)

#让用户输入决定列宽度
# first_width = st.number_input('First Width',min_value=1,value=1)
# second_width = st.number_input('Second Width',min_value=1,value=1)
# third_width = st.number_input('Third Width',min_value=1,value=1)
# col1,col2,col3 = st.columns((first_width,second_width,third_width))
#三种列宽度设置，它们都产生了相同的列宽度
#option1
# col1,col2,col3 = st.columns((1,1,1))
# #option2
# col1,col2,col3 = st.columns((10,10,10))
# #option3，列之间有大间隙
# col1,col2,col3 = st.columns(3,gap = 'large')
# with col1:
#     #如果让图不再与列的末端对齐
#     st.line_chart(df_dbh_grouped,use_container_width = False)
# with col2:
#     st.bar_chart(df_dbh_grouped)
# with col3:
#     st.area_chart(df_dbh_grouped)
#上面代码的简易写法,用with语句更整洁，更易于理解和调试 
# col1.write('Column 1')
# col2.write('Column 2')
# col3.write('Column 3')  
#使用标签
# tab1,tab2,tab3 = st.tabs(['Line Chart','Bar Chart','Area Chart'])
# with tab1:
#     st.line_chart(df_dbh_grouped)
# with tab2:
#     st.bar_chart(df_dbh_grouped)
# with tab3:
#     st.area_chart(df_dbh_grouped)