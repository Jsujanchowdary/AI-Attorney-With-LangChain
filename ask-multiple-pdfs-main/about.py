import streamlit as st
import time

def fade_in_animation(element, duration=0.5):
    st.markdown(
        f"""
        <style>
            @keyframes fade-in {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            {element} {{
                animation: fade-in {duration}s ease-in-out;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

def about_page():
    st.title("About AI Attorney")
    st.subheader("Empowering Legal Excellence Through AI")
    col1, col2 = st.columns(2)
    with col2:
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\ailogo.png")
    with col1:
        st.text(" ")
        st.text(" ")
        st.write("At AI Attorney, we are at the forefront of the legal technology revolution. Our mission is to empower legal professionals with cutting-edge AI solutions that redefine the practice of law. With a relentless commitment to innovation, we have developed a suite of services designed to enhance the legal industry's efficiency, accuracy, and client service. Here's what sets us apart:")
    st.write(" Expertise: Our team combines legal expertise with AI prowess to create solutions that truly understand the intricacies of the law.")
    st.write(" Innovation: We constantly push boundaries, developing custom AI tools that adapt to the ever-changing legal landscape.")
    st.write(" Efficiency: AI Attorney's solutions streamline legal processes, allowing you to focus on what matters most – your clients.")
    st.write(" Accuracy: Our AI algorithms deliver unparalleled precision in legal research, analysis, and document review.")
    st.write(" Client-Centric: We prioritize your success, aiming to elevate your practice to new heights while ensuring your clients receive top-notch service.")
    st.write("Join AI Attorney on the journey to redefine legal excellence in the digital age.")
    st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\about.png")

    st.header("Product Features")
    st.markdown("AI Attorney stands as a pioneering force in the legal technology landscape, harnessing the power of Artificial Intelligence (AI) and Natural Language Processing (NLP) techniques to revolutionize legal research. Here are the key features that set AI Attorney apart")
    col1, col2 = st.columns(2)
    with col2:
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\img-1.png")
    with col1:
        st.subheader("Cutting-Edge NLP Technology")
        st.markdown(
            """
            - Utilizes advanced NLP algorithms for precise legal document analysis.
            - Ensures accurate keyword extraction, improving the relevance of search results.
            - Integrates the powerful Natural Language Toolkit (NLTK) library for robust language processing.
            - Enhances legal research efficiency with AI-driven language understanding.
            """
        )

    with col1:    
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\img-2.png")

    with col2:
        st.subheader("Scenario-Based Search")
        st.markdown(
            """
            - Empowers users to input specific legal scenarios for tailored research.
            - Aligns research outcomes with real-world legal situations.
            - Provides contextually relevant legal articles and sections.
            - Streamlines the process of finding pertinent legal information.
            """
        )

    with col2:
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\img-3.png")
    with col1:
        st.subheader("PDF File Analysis")
        st.markdown(
            """
            - Accelerates legal research by analyzing and interpreting case PDF files.
            - Intelligently identifies act names and relevant sections within uploaded documents.
            - Significantly reduces manual effort in reviewing case materials.
            - Enhances productivity for legal experts dealing with extensive case files.
            """
        )

    with col1:
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\img-4.png")
    with col2:
        st.subheader("Keyword Extraction Expertise")
        st.markdown(
            """
            - Meticulously crafted keyword extraction process for precision and relevance.
            - Guarantees contextually accurate and meaningful search results.
            - Improves the overall effectiveness of legal research.
            - Minimizes irrelevant content, saving users valuable time.
            """
        )

    with col2:
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\img-3.png")
    with col1:
        st.subheader("Adaptive Learning")
        st.markdown(
            """
            - Continuously refines keyword extraction based on user interactions.
            - Adapts to evolving legal language and terminology.
            - Ensures ongoing improvement in search accuracy.
            - Customizes results to match the evolving needs of legal professionals.
            """
        )

    with col1:
        st.image(r"..\ask-multiple-pdfs-main\ask-multiple-pdfs-main\images\img-1.png")
    with col2:
        st.subheader("Multilingual Text Translation")
        st.markdown(
            """
            - Breaks language barriers by providing multilingual text translation.
            - Expands accessibility for legal professionals working in diverse linguistic contexts.
            - Enables seamless research in international legal scenarios.
            - Enhances collaboration and understanding in global legal environments.
            """
        )

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






 
 