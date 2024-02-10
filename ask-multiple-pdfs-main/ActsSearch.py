import streamlit as st
from apiclient.discovery import build

def fetch_google_search_results(query, cx, api_key):
    resource = build("customsearch", 'v1', developerKey=api_key).cse()
    result = resource.list(q=query, cx=cx).execute()
    return result['items']

def search_page():
    # Your Google API key and Custom Search Engine ID
    api_key = "AIzaSyC4xwBIApKA8XJ-gLUKOLO4Ms6a4X0BLIg"
    cx = "807d5be983eda4de8"
    st.header("Search your Acts")

    st.write("Search Results")

    # Input box for search query
    query = st.text_input("Enter your search query:")
        
    if st.button("Search"):
        results = fetch_google_search_results(query, cx, api_key)

        # Display results
        st.header("Search Results:")
        for item in results:
            st.write(f"Title: {item['title']}")
            st.write(f"Link: {item['link']}")
            st.write(f"Snippet: {item['snippet']}")
            if 'cse_image' in item['pagemap']:
                    st.image(item['pagemap']['cse_image'][0]['src'], caption="Image", use_column_width=True)
            st.write("-" * 50)


