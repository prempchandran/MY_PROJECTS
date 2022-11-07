#this STREAMLIT APP IS CREATED BY PREM CHANDRAN AS A PROJECT FOR SENTIMENT ANALYSIS

import streamlit as st
from transformers import pipeline
# pip install transformers
from textblob import TextBlob # for sentiment analysis
import pandas as pd  
import cleantext




st.title('Sentiment Analyser App')
st.write('created by Prem Chandran' )
st.subheader('This sentiment analysis app can take direct input text, copy and pasted text and CSV files to do a sentiment analysis of the content.')
# st.markdown(' ')
st.caption('Possible applications can for testing polarity in crafting text for student remarks and testimonials to')


st.header('Sentiment Analysis-Model 1')
form = st.form(key='sentiment-form')
user_input = form.text_area('Enter your text')
submit = form.form_submit_button('Submit')

classifier = pipeline("sentiment-analysis")
result = classifier(user_input)[0]
label = result['label']
score = result['score']


if submit:
    classifier = pipeline("sentiment-analysis")
    result = classifier(user_input)[0]
    label = result['label']
    score = result['score']

if label == 'POSITIVE':
    st.success(f'{label} sentiment (score: {score})')
else:
    st.error(f'{label} sentiment (score: {score})')


st.header('Sentiment Analysis-Model 2 ')
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity(between [-1,1], where -1 refers to negative sentiment and +1 refers to positive sentiment): ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity(output that lies within [0,1] and refers to personal opinions and judgments): ', round(blob.sentiment.subjectivity,2))
        
    pre = st.text_input('Clean Text (remove digits, extra white space and stop words): ')
    if pre:
        st.write(cleantext.clean(pre, clean_all= False, extra_spaces=True ,
                stopwords=True ,lowercase=True ,numbers=True , punct=True))
        
with st.expander('Analyze CSV(EXCEL) files'):
    upl = st.file_uploader('Upload file')

    def score(x):
        blob1 = TextBlob(x)
        return blob1.sentiment.polarity
    
#
    def analyze(x):
        if x >= 0.5:
            return 'Positive'
        elif x <= -0.5:
            return 'Negative'
        else:
            return 'Neutral'


#chnage tweets to remarks
#
    if upl:
        df = pd.read_excel(upl)
        del df['Unnamed: 0']
        df['score'] = df['tweets'].apply(score)
        df['analysis'] = df['score'].apply(analyze)
        st.write(df.head(10))

        @st.cache
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv',
        )