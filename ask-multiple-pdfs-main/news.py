import streamlit as st
import requests
import pycountry


def news_page():
    st.title("News")
    
    
    
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey=757271b3c2c5422388ffb027ce0f0f90"

    r = requests.get(url)
    r = r.json()
    articles = r['articles']
    for article in articles:
        st.header(article['title'])
        st.write(article['publishedAt'])
        if article['author']:
            st.write(article['author'])
        st.write(article['source']['name'])
        if article['urlToImage']:
            st.image(article["urlToImage"])
        st.write(article['description'])
        if article["url"]:
            st.write(article['url'])

