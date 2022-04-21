import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
modeltraining  = st.container()

with header:
	st.title('Welcome To My Project')

with dataset:
	st.header('Ini Bagian Dataset')
	st.text('Link Download on https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks')

	books_data = pd.read_csv('books.csv',error_bad_lines = False)
	st.write(books_data.head())
	
