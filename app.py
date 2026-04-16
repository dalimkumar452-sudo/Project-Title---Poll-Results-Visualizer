import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import random

st.set_page_config(page_title='Poll Results', layout='wide')
st.title('📊 Poll Results Visualizer')

def generate_data():
    data = []
    for i in range(100):
        data.append({
            'ID': i,
            'Tech': random.choice(['Python', 'Java', 'Go', 'Rust']),
            'Rating': random.randint(1, 5),
            'Feedback': random.choice(['Great', 'Good', 'Average', 'Nice'])
        })
    return pd.DataFrame(data)

df = generate_data()
st.write('### Live Dashboard Generated Successfully!')
st.bar_chart(df['Tech'].value_counts())
st.dataframe(df)
