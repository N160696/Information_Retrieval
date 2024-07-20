# import streamlit as st
# from src.helper import get_pdf_text, get_conversational_chain, get_text_chunks, get_vector_store
# # import time


# def user_input(user_question):
#     response = st.session_state.conversation({'question': user_question})
#     st.session_state.chatHistory = response['chat_history']
#     for i, message in enumerate(st.session_state.chatHistory):
#         if i % 2 == 0:
#             st.write("User:", message.content)
#         else:
#             st.write("Reply:", message.content)



# def main():
#     st.set_page_config("Information Retrieval")
#     st.header("Information-Retrieval-system")
#     user_question= st.text_input("Ask a Question from the PDF files")

#     if "conversation" not in st.session_state:
#         st.session_state.conversation = None
    
#     if "chatHistory" not in st.session_state:
#         st.session_state.chatHistory = None
    
#     if user_question:
#         user_input(user_question)




#     with st.sidebar:
#         st.title("Menu:")
#         pdf_docs = st.file_uploader("Upload your PDF files and click on the submit & Process Button", accept_multiple_files=True)
#         if st.button("Submit & Process"):
#             with st.spinner("Processing...."):
#                 raw_text= get_pdf_text(pdf_docs)
#                 text_chunks= get_text_chunks(raw_text)
#                 vector_store= get_vector_store(text_chunks)
#                 st.session_state.conversation =get_conversational_chain(vector_store)

#                 # time.sleep(2)

#                 st.success("Done")


# if __name__ == "__main__":
#     main()


import streamlit as st
from src.helper import get_pdf_text, get_conversational_chain, get_text_chunks, get_vector_store

def user_input(user_question):
    if st.session_state.conversation:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chatHistory = response['chat_history']
        for i, message in enumerate(st.session_state.chatHistory):
            if i % 2 == 0:
                st.write("User:", message.content)
            else:
                st.write("Reply:", message.content)
    else:
        st.write("Please upload and process PDF files first.")

def main():
    st.set_page_config("Information Retrieval")
    st.header("Information-Retrieval-system")
    user_question = st.text_input("Ask a Question from the PDF files")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    
    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files and click on the submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            if pdf_docs:
                with st.spinner("Processing...."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    vector_store = get_vector_store(text_chunks)
                    st.session_state.conversation = get_conversational_chain(vector_store)
                    st.success("Done")
            else:
                st.write("Please upload PDF files.")

if __name__ == "__main__":
    main()
