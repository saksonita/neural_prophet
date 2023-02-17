import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from PIL import Image
from streamlit_extras.app_logo import add_logo
# from PIL import Image
add_logo("logo.png")

# You can always call this function where ever you want

# st.set_page_config(layout='wide')

## This is File 
# add_logo()
st.title('인공지능 기반 참외 출하량 예측')


# st.text('1. Data학습 : 2015년~현재까지 출하량 데이터를 학습하여 AI예측모형 생성')
# st.text('2. AI예측 : 기준일을 입력하면 이후 1개월간 출하량 예측치를 출력함')
# st.text("주의: 처음 접속시 1., 2. 순서로 실행하고, 2번째부터는 2.만 실행해주세요.")
# st.text("------------ (주)빅데이터랩스 --------------")

st.subheader('This website experiment the performance forcasting between 2 models 1. :blue[Prophet] and  2. :blue[Neural Prophet]')



image = Image.open('models.webp')

st.image(image, caption='About the models')
# df 

st.write('In the "Data 학습 & AI 분석" menu, you may find the information of the data and how the data selected to train. Please be patient on the model training part as the Neural Prophet required sometimes (at least 5 minustes) to fully train. ')


