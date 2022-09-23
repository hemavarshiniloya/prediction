import streamlit as st
import pickle
pickle_in=open('diamond.pkl','rb')
mond=pickle.load(pickle_in)
a=st.number_input('carat')
b=st.number_input('cut')
c=st.number_input('color')
d=st.number_input('depth')
if st.button('PREDICT'):
  st.success(f'DIAMOND PRICE IS {PRICE}')
