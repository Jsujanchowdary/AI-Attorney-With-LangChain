import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from streamlit_option_menu import option_menu
from about import about_page
from home import home_page
from codeexplain import code_page
from news import news_page
from ActsSearch import search_page
from chat import chat_page
import os

api_key = "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"

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    openai_api_key = api_key
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    openai_api_key = api_key
    llm = ChatOpenAI(openai_api_key=openai_api_key)
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="AI Attorney", page_icon=r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\cropped logo.PNG")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None


    st.sidebar.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\cropped logo.PNG", use_column_width=True)
    st.markdown(
    """
        <style>
            @keyframes fadeIn {
                from {
                    opacity: 0;
                    transform: translateY(-10px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            .sidebar .sidebar-content {
                background-color: #f8f9fa;
                box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
                animation: fadeIn 0.5s ease-out;
            }

            .sidebar .sidebar-content .block-container {
                padding: 1em;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar navigation
    navigation = st.sidebar.selectbox("Menu", ["Home", "About","Chat with Me!!", "Chat With Document!!","Search", "Understand Me!!","Todays News"])
    


    if navigation == "Home":
        home_page()
    elif navigation == "About":
        about_page()
    elif navigation == "Understand Me!!":
        code_page()
    elif navigation == "Todays News":
        news_page()
    elif navigation == "Search":
        search_page()
    elif navigation == "Chat with Me!!":
        chat_page()
    elif navigation == "Chat With Document!!":
        st.title("Chat With Document!!")
        st.markdown("Defending Tomorrow with Today's Intelligence: Your AI Attorney for a Smarter Legal Future.")
        st.write("Before Chatting with me first upload the file that you want to Discuss.")
        user_question = st.text_input("Ask a question about your documents:")
        st.sidebar.subheader("Your documents")
        pdf_docs = st.sidebar.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if user_question:
            handle_userinput(user_question)

    # File upload section outside the "Chat" condition
    
    if st.sidebar.button("Process"):
        with st.spinner("Processing"):
            # get pdf text
            raw_text = get_pdf_text(pdf_docs)

            # get the text chunks
            text_chunks = get_text_chunks(raw_text)

            # create vector store
            vectorstore = get_vectorstore(text_chunks)

            # create conversation chain
            st.session_state.conversation = get_conversation_chain(vectorstore)

if __name__ == '__main__':
    main()
