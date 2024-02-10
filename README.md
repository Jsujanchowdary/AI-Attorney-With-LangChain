# AI ATTORNEY USING LANGCHAIN
### Empowering Legal Research Through AI Unlocking Insights with Ai Attorney

## ABSTRACT
Natural language processing (NLP) and machine learning components are integrated into Streamlit, an AI-powered document chat system. Users can interact with the system through interactive conversations where they can discuss uploaded PDF documents or query a language model that has already been trained. In order to enable intelligent responses and document understanding, the application makes use of OpenAI's language models for text embeddings. When users upload PDFs, the system reads the files and extracts the text. After that, it uses OpenAI's API to create embeddings and breaks the text up into digestible chunks. Because these embeddings are kept in a vector store, retrieving them quickly during user interactions is made possible. An OpenAI chat model handles the conversational part, and a conversation buffer memory keeps track of previous conversations for context-aware replies. Streamlit was used in the design of the user interface to provide a seamless experience. The application has different sections for home, about, news, document search, code explanation, and interactive chat. The concept of AI Attorney presents a novel approach to legal document comprehension, showcasing the potential of sophisticated language models in legal contexts. The system seeks to improve accessibility and comprehension of legal content by providing users with an intelligent, document-centric chat interface.

## INTRODUCTION
The "AI Attorney" project is an innovative investigation into the fields of natural language processing (NLP) and artificial intelligence (AI), with the goal of transforming the comprehension and interaction of legal documents. This creative project combines the power of multiple frameworks and technologies to produce a clever and intuitive AI-powered legal assistant system. The project's main component is the Streamlit framework, a potent instrument for quickly and easily building web applications. The user interface exhibits a high degree of versatility and breadth, as it allows users to easily navigate through various sections such as home, about, code explanation, news, document search, and an engaging "Chat with Me!!" feature.

![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/7f76d244-432a-4c0e-981b-4e14eb2e5517)
The AI Attorney's main objective is to improve legal document accessibility and comprehension through interactive conversations. Either by uploading PDF documents for contextualized conversations or by querying a language model that has already been trained, users can participate in dynamic discussions. The system makes use of advanced text embeddings and OpenAI's language models to comprehend legal language and intelligently respond to user inquiries. One notable feature is the document-centric chat interface, which enables users to converse meaningfully and gain a deeper understanding of the content while also searching through a large corpus of legal documents. By recognizing the potential of AI in legal applications, the project demonstrates a forward-thinking approach and paves the way for a more intelligent and effective legal future.
In addition, the system uses intelligent document processing, chunking and extracting text from uploaded PDFs, utilizing OpenAI's API to create embeddings, and storing them in a vector store for quick retrieval during talks. By combining AI, NLP, and user-centric design, the "AI Attorney" is a step toward changing the legal landscape rather than merely being a tool. This introduction lays the groundwork for an ambitious project that aims to redefine legal information access and comprehension in the digital age, while also showcasing technical prowess.              


## Objectives

The primary objectives of this project are aimed at developing an AI attorney system that excels in comprehending legal documents, providing insightful legal advice, and maintaining an interactive and user-friendly experience. The key goals include:

### Conversational Legal Assistance

- **Conversational User Interface:** Develop a user interface that allows natural language interactions, providing users with information and legal support.
- **Natural Language Inquiries:** Enable users to communicate with the AI Attorney using natural language queries.

### Document Understanding and Analysis

- **Document Processing System:** Establish a robust system for processing legal documents, with a focus on extracting valuable information from PDF files.
- **Algorithmic Comprehension:** Create algorithms capable of comprehending and evaluating legal text to identify pertinent information.

### Real-time Interaction

- **Prompt Legal Advice:** Provide users seeking immediate legal advice with the ability to engage in real-time communication with the AI Attorney.
- **Responsive System:** Develop a system that promptly and accurately responds to user inquiries.

### Multi-Modal Document Support

- **Diverse Document Types:** Extend the system's capabilities to support various legal document formats, including images and scanned documents.
- **Enhanced Document Understanding:** Improve document understanding to handle a broad range of legal content.

### User-Friendly Experience

- **Intuitive Interface:** Design an easy-to-use and intuitive interface to facilitate smooth communication between users and the AI Attorney.
- **Usability and Accessibility:** Prioritize usability and accessibility for users with varying levels of legal expertise.

### Integration of News and Updates

- **Legal News Feature:** Incorporate a feature that provides users with relevant legal news and updates.
- **Knowledge Base Enhancement:** Regularly update the AI Attorney's knowledge base with the latest legal information to keep users informed.

## Background and Literature Survey

Although AI technologies have shown they can speed up the work of lawyers by handling routine tasks and technical tasks, they are not yet capable of completely replacing legal specialists (Deltsova, 2020) [1]. This idea offers a solid and condensed basis for assessing developments in the application of AI in the legal field. Legal practitioners can use this perspective to evaluate the impact of AI on legal practice and the achievement of desired results, while academics studying the role of AI in legal reasoning can use it to track progress (Eliot, 2020) [2]. It is argued that investigating AI within the context of law will play a crucial role in encouraging the creation of AI systems that support human welfare, underscoring the increased importance of this intersection (Verheij, 2020) [3]. Simultaneously, it is acknowledged that artificial intelligence has the potential to serve as a crucial "assistant" to legal professionals, providing a way to improve the effectiveness and caliber of legal services provided (Vasiliev & Pechatnova, 2020) [4].

![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/e071d290-61d6-424f-ba1c-cdc8ab9a9e72)

The literature has proposed a number of novel keyword extraction methods, demonstrating developments in this area. In order to improve news retrospective event detection accuracy and efficiency, Li et al. introduced a Chinese news document keyword extraction method based on tf/idf with multiple strategies [5]. This method outperformed baseline methods. Wang and Ning proposed a TF-IDF method that combines context and semantic classification to address problems with keyword extraction [6]. When compared to conventional TF-IDF and TextRank methods, improved TextRank algorithms for keyword extraction showed superior generality and accuracy [7]. Additionally, a newer version of TextRank was created for extracting keywords from text streams. It offers notable speed improvements and is useful for research projects [8]. The efficiency of keyword extraction was found to be improved by the combination of Named Entity Recognition (NER) and RAKE [9]. Additionally, domAIn-specific adaptations like RAKEB showed improved keyword extraction performance in the case of Bengali language [10]. The traditional TextRank algorithm was also improved by a cutting-edge method that combined keyword extraction with text network analysis.
![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/6957d9ac-1981-4f72-a0ea-339e9d8c923c)

## Proposed System

The following block diagram shows the system architecture of this project.
![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/2dc143aa-be1c-40dc-8688-e13c33e65dc5)
LangChain is an open-source framework that helps developers create applications using large language models (LLMs). It provides a standard interface for chains, integrations with other tools, and end-to-end chains for common applications. 
LangChain's use cases include: 
- Document analysis and summarization
- Chatbots
- Code analysis

LangChain is data-aware and agentic, allowing connections with various data sources for personalized experiences. Agents can be used to control the flow of a chain and to make decisions about which tasks to perform. 
LangChain simplifies development by providing: Standardized interfaces, Prompt management, External integrations.

## Working Methodology

The AI Attorney project makes use of a sidebar navigation system and Streamlit-based user interface to provide users with a variety of features like code understanding, information exploration, AI-driven document interaction, search capabilities, and access to the most recent news. Processing PDF documents and allowing users to ask legal questions about the content is the main function of the project. Through the sidebar, users can upload multiple PDFs. This initiates a processing mechanism that uses OpenAI's GPT-based embeddings stored in an FAISS vector store, to vectorize the documents and extract text from them. It also segments the documents into manageable chunks. A ChatGPT model integrated into a Conversational Retrieval Chain facilitates the conversational aspect, and chat history is stored in a buffer memory. With distinct pages for home, about, code explanation, news, search, and AI-based chatting with both general and document-specific questions, the user interface offers a seamless experience.

The application's visually appealing layout, which makes use of CSS styling to improve the sidebar's appearance, complements its user-centric design. The code makes use of different modules for different functionalities, such as vectorization, conversational AI interactions, and text extraction from PDFs. A responsive interface and obvious navigation options make it easier for users to move between the application's various sections. The approach captures the complexity of the project by combining general conversational AI and document-centric AI features into a unified and intuitive Streamlit application.

## Get Pdf Text Flow Diagram
![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/f93ac1ba-3ffe-48e5-8f8e-767523ef4964)

## Web Diagram
![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/dc3da018-a815-4c72-8839-7d426925568a)

## WEB PAGES

### Home Page
![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/6e361528-e258-4e15-8380-205e642ccbb0)

### About Page
![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/4346fba2-2637-4915-a0df-fc8484a31905)

### Chat With Me!! Page
![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/42fa1e5c-e07e-4248-bdbe-efa611bbc266)

### Chat With Document!! Page
![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/17b7234d-e579-434a-8d9d-c809330e8766)

### Search Page
![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/ab35cea9-d556-4bd4-8a84-acc41e36df2b)

### Understand Me!! Page
![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/e84d9de0-ed9c-4dce-890d-2645d07da3b2)

### Today’s News Page
![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/2cb9cdf4-607e-4764-a8fb-9ef5aa1d2b22)

## RESULTS AND DISCUSSIONS

**a.	Result From Chat With Me!!**
- User: What is IPC Section 307?
- Bot Output:
- ![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/ad6c0e96-b8e6-4ed9-8fc8-a6a84ab06fcb)
  
**b. Result From Chat With Document!!**
First user has Uploaded the Document called Acts
- User: what Indian Acts and Sections are applicable for Scenario: A person fires a gun at another with the intent to kill but misses the target.
- ![image](https://github.com/Jsujanchowdary/AI-Attorney-Using-LangChain/assets/91127394/ee0b5522-f810-44ef-8f03-7a5b6e372221)
- Bot Output: The relevant Indian Act in this scenario would be the Indian Penal Code (IPC). The specific sections that would apply are:
  Section 307: Attempt to murder - This section deals with the act of attempting to commit murder. It states that whoever does any act with the intention of causing the death of another person, but the act does not result in the death of that person, shall be punished with imprisonment for a term which may extend to life imprisonment or for a term which may extend to ten years, and shall also be liable to fine.
  Additionally, depending on the circumstances, other relevant sections of the IPC may also apply, such as:

  Section 34: Acts done by several persons in furtherance of common intention - This section deals with situations where a criminal act is done by several individuals in furtherance of a common intention. It states that when a criminal act is done by several persons, each person is liable for the act as if he/she had done it alone.

  Section 120B: Criminal conspiracy - This section deals with the offense of criminal conspiracy, which is an agreement between two or more persons to commit a criminal act. It states that whoever is a party to a criminal conspiracy to commit an offense punishable with death, imprisonment for life, or rigorous imprisonment for a term of two years or upwards, shall be punished in the same manner as if he/she had actually committed the offense.

## CONCLUSION AND FUTURE WORK

To sum up, the AI Attorney project's development and execution represent a major advancement toward the creation of a more sophisticated and approachable legal assistance system. The incorporation of OpenAI models, specifically the ChatOpenAI model, has shown encouraging results in comprehending and reacting to user inquiries, creating a stimulating and educational atmosphere. The document processing feature is very effective at retrieving data from uploaded PDFs, which makes legal documents easier for users to access and use. The project successfully validates the potential of advanced natural language processing in the legal domain by offering a conversational interface for legal inquiries.

There are numerous opportunities for further improvements and modifications in the future. The ChatOpenAI model's contextual understanding and responsiveness can be further improved by increasing the amount of training data available to it. Furthermore, investigating domain-specific embeddings and customized training strategies may improve the model's accuracy for legal jargon and nuance. Expanding the scope of document formats handled and increasing the precision of text extraction are potential areas of future development for the document processing module. Assuring the AI Attorney's applicability and accuracy in a variety of legal scenarios would require working with legal experts to customize the system for particular use cases. Iterative updates and constant user feedback will be essential for improving and developing the system, which will ultimately contribute to the ongoing development of AI in the legal sector.


