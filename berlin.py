import streamlit as st
import pandas as pd
import geopandas as gpd

st.title("Berlin Business Dashboard")

@st.cache
def load_data():
   data = pd.read_csv('berlinplan.csv', encoding='utf-8',
   error_bad_lines=False) 
   data['district'] = data['BEZIRK']
   return data.set_index('BEZIRK')

data = load_data()


districts = st.sidebar.multiselect(
    "Choose districts", list(set(data.district)), ["Mitte",'Spandau']
)

new_df = data[data['district'].isin(districts)]
if st.checkbox('Show raw data'):
   st.write(new_df)# Create distplot with custom bin_size
    
st.vega_lite_chart(new_df, {
     'width': 'container',
     'height': 600,
     'width': 600,
     'mark':'circle',
     'tooltip': True,
     'encoding':{
        'x':{
           'field':'activity',
           'type': 'quantitative'
         },
        'y':{
           'field':'habitants',
           'type':'quantitative'
          },
        'size':{
           'field':'surface',
           'type':'quantitative'
          },
        'color':{
           'field':'district',
           'type':'nominal'}
         }
       })






#district  = st.sidebar.multiselect("District", data['BEZIRKSREG'].unique())
#if district:
 #   data = data[data.BEZIRKSREG.isin(district)]