import streamlit as st
import pandas as pd
import numpy as np
from sklearn import preprocessing
import joblib
from PIL import Image

image = Image.open('godread.jpg')
st.image(image)

st.title('Predict average rating the books')
rating_count = st.number_input('Enter total rating votes', step=100, value=100)
num_pages = st.number_input('Enter number of pages', min_value=49, max_value=1500, step=10)
authors = st.text_input('Enter author name', placeholder='Agatha Christie')
language = st.selectbox(
    'Select the language in which it is written',
    ('spa', 'en-US', 'eng', 'fre')
)

if st.button('Submit'):
  book_model = joblib.load('good_read_model.pkl')
  book_dict = {
      'ratings_count': [rating_count],
      'num_pages': [num_pages],
      'authors': [authors],
      'en-US': [0],
    	'eng':  [0],
      'fre': [0],
      'spa': [0]
      }
  
  book = pd.DataFrame(data=book_dict)
  
  if language == 'spa':
    book_dict['spa'] = 1
  elif language == 'en-US':
    book_dict['en-US'] = 1
  elif language == 'eng':
    book_dict['eng'] = 1
  elif language == 'fre':
    book_dict['fre'] = 1

  le = preprocessing.LabelEncoder()
  book.loc[:, 'authors'] = le.fit_transform(book['authors'])

  prediction = np.around(book_model.predict(book), 2)
  st.write(f'The average rating is {float(prediction)}')
