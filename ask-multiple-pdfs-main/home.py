# home.py
import streamlit as st
import os
import numpy as np
import pandas as pd
def home_page():
    st.title("AI Attorney")
    st.markdown("Transforming the Legal Industry with AI")
    st.caption("AI Attorney is a cutting-edge legal technology firm revolutionizing the legal industry with advanced artificial intelligence solutions. We provide clients with efficient, accurate, and cost-effective legal services, powered by state-of-the-art AI algorithms and expert legal insights, ensuring seamless and precise legal support.")
    st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\AiLaw.jpeg")

    st.markdown(
    "AI Attorney is at the forefront of revolutionizing the legal industry by harnessing the power of artificial intelligence. "
    "Our commitment is to provide innovative and efficient solutions that transform traditional legal processes. "
    "With cutting-edge AI algorithms and expert legal insights, we strive to deliver accurate and cost-effective legal services to our clients."
    )

    st.markdown(
        "Our team of dedicated professionals is passionate about leveraging technology to address the complexities of the legal landscape. "
        "We believe in the seamless integration of AI into legal workflows, empowering legal professionals and organizations to work smarter and achieve better outcomes."
    )

    st.markdown(
        "At AI Attorney, we constantly push the boundaries of what AI can achieve in the legal domain. Our mission is to redefine how legal services are delivered, making them more accessible, precise, and adaptable to the evolving needs of our clients."
    )

    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")

    st.header("OBJECTIVE")
    col1, col2 = st.columns(2)
    with col1:
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\law 2.png")
    with col2:
        st.write("""The objective of this presentation is to demonstrate the groundbreaking 
                capabilities and significant contributions of Ai Attorney, an advanced AI powered system, in revolutionizing legal research. Through its utilization of 
                cutting-edge Natural Language Processing (NLP) algorithms, Ai Attorney offers 
                users precise and pertinent legal materials based on input scenarios or case PDF 
                files. This presentation aims to highlight the system's meticulous keyword 
                extraction process, its ability to swiftly analyze and recognize relevant legal 
                sections within uploaded case files, and its ongoing enhancement through user 
                interactions. The presentation seeks to underscore how Ai Attorney substantially 
                improves the efficiency and accuracy of legal research, outperforming 
                conventional tools.""")


    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.header("Motivation: Revolutionizing Legal Assistance with AI")
    st.write("""Welcome to AI Attorney, where cutting-edge artificial intelligence meets legal documentation!
        Our motivation stems from a deep commitment to making legal processes more accessible, efficient, 
        and user-friendly. Here's why AI Attorney is poised to revolutionize the legal assistance landscape:""")
    
    st.markdown("""

        ### Bridging the Gap
        Legal documents can be complex and intimidating, often creating a significant barrier 
        between individuals and their understanding of legal matters. AI Attorney bridges this gap by 
        providing an intuitive platform where users can ask questions about their documents in plain language.

        ### Empowering Users
        We believe that everyone has the right to comprehend and engage with legal documents that concern them.
        AI Attorney empowers users by offering a conversational interface, enabling them to seek clarification, 
        explanations, and guidance on legal jargon, contracts, and other legal texts.

        ### Enhancing Efficiency
        Traditional legal processes can be time-consuming. AI Attorney streamlines the document review 
        and understanding process, offering quick and accurate responses to user queries. This efficiency 
        ensures that users can make informed decisions promptly.

        ### Leveraging Advanced AI Technology
        AI Attorney leverages state-of-the-art natural language processing and conversational AI models. 
        Our technology can understand and respond to a wide range of legal questions, providing users with 
        valuable insights and information.

        ### Continuous Improvement
        We are committed to constant improvement. AI Attorney's AI models learn and adapt over time, 
        ensuring that the platform evolves to meet the diverse and dynamic needs of its users.

        Explore AI Attorney and experience the future of legal assistance – where technology meets 
        accessibility, empowering individuals to navigate legal complexities with confidence.

        Remember, AI Attorney is here to assist, simplify, and make legal matters more understandable for everyone.
    """)

    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")

    st.subheader("Team Members")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\udit sir.jpg")
        st.subheader("Prof.Udit Narayana Kar")
        st.write("`Senior Assistant Professor Grade 1 at VIT-AP University`")
    
    with col2:
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\sujan.jpg")
        st.subheader("JUJJAVARAPU SUJAN CHOWDARY")
        st.write("`CSE (Spec. in Artificial Intelligence)`")

    with col3:
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\eswar.jpg")
        st.subheader("RAJA ESWARA VENKATA SAI")
        st.write("`CSE (Spec. in Artificial Intelligence)`")

    with col1:
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\rupa.png")
        st.subheader("KARAKA RUPASREE")
        st.write("`CSE (Spec. in Artificial Intelligence)`")

    with col2:
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\sreeven.png")
        st.subheader("NAGI REDDY SREEVEN REDDY")
        st.write("`CSE (Spec. in Artificial Intelligence)`")

    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")

    
    st.subheader("Current Location")

    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [16.4942796, 80.5007368],
    columns=['lat', 'lon'])

    st.map(df)


    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")


    st.header(":mailbox: Get In Touch With Me!")
    contact_form = """
    <form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css(r"..\ask-multiple-pdfs-main\style\style.css")



