import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

header = st.container()
dataset = st.container()
features = st.container()
modeltraining  = st.container()

with header:
	st.title('Data Science Project 1 : Goodreads Simple EDA')
	st.text('By Mohamad Ikhsan Zulfadly')

with dataset:
	st.header('Dataset Metadata')
	st.text('Link Download on https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks')

	books_data = pd.read_csv('books.csv',error_bad_lines = False)
	st.write(books_data.head())

	count_row = len(books_data)
	st.text('Jumlah Data Buku : ' + str(count_row))
with features:
	st.header('Data Exploratory')

	st.subheader("Ini Merupakan Grafik Persebaran Buku Berdasarkan Bahasa Yang Digunakan")
	dist_lang = pd.DataFrame(books_data['language_code'].value_counts())
	st.bar_chart(dist_lang)
	st.text('Dari Grafik diatas dapat disimpulkan rata-rata buku yang tersedia dalam data set')
	st.text('adalah buku-buku berbahasa inggris.')

	##Seaborn
	fig = plt.figure(figsize=(5,5))
	
	sns.kdeplot(books_data["average_rating"])

	plt.title("Rata-Rata Sebaran Rating Buku")

	st.pyplot(fig)

	most_books = books_data.groupby('authors')['title'].count().reset_index().sort_values('title',ascending = False).head(10).set_index('authors')
	
	fig = plt.figure(figsize=(5,5))
	ax  = sns.barplot(most_books['title'],most_books.index, palette='flare')
	ax.set_title("Top 10 Authors with most books")
	ax.set_xlabel("Total number of books")
	for i in ax.patches:
		ax.text(i.get_width()+.3, i.get_y()+0.5, str(round(i.get_width())),fontsize = 10,color = 'k')

	st.pyplot(fig)

	books_data['publication_year'] = books_data['publication_date'].str[-4:]

	most_book_publisher = books_data.groupby('publisher')['title'].count().reset_index().sort_values('title',ascending = False).head(10)

	df_heatmap = books_data[books_data['publisher'].isin(most_book_publisher.reset_index()['publisher'].tolist())]

	df_heatmap = df_heatmap[df_heatmap['publication_year'].isin(['2003','2004','2005','2006','2007'])]	

	df_heatmap = df_heatmap.groupby(['publisher','publication_year']).agg({'average_rating':np.mean}).reset_index()

	df_heatmap = df_heatmap.pivot('publisher','publication_year', 'average_rating')

	fig, ax= plt.subplots(figsize=(10,5))

	sns.heatmap(ax=ax, data=df_heatmap)
	ax.set_title('Heatmap Penjualan Publisher Per Tahun')

	st.pyplot(fig)