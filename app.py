import streamlit as st
import cv2
import os
from PIL import Image
from qa_funcs import generate_answer, extract_text_txt, extract_text_pdf, extract_text_docx

st.set_page_config(
    page_title="Q&A",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
)

top_image = Image.open('static/top.png')
bottom_image = Image.open('static/bottom.png')
main_image = Image.open('static/main_banner.png')


upload_path = "uploads/"
download_path = "downloads/"

st.sidebar.image(top_image,use_column_width='auto')
format_type = st.sidebar.selectbox('Apply Q&A for? 🎯',["Plain Text","Documents"])
st.sidebar.image(bottom_image,use_column_width='auto')

st.image(main_image,use_column_width='auto')
st.title("📄 Q&A System 🗣")

if format_type == "Plain Text":
    text = st.text_area("Enter your text here: 🎯", height=300)
    ques_text = st.text_area("Enter your Question: 🙋",height=50)
    if st.button("Run"):
        if ques_text is not None and text is not None and ques_text != "" and text != "":
            with st.spinner(f"Getting your Answer... 💫"):
                ans = generate_answer(text,ques_text)
                st.markdown("Here's the answer 🗣")
                st.balloons()
                st.success('✅ '+ans)
        elif (ques_text is None or ques_text == "") and (text is not None or text != ""):
            st.warning('⚠ Please enter your question! 😯')
        elif (ques_text is not None or ques_text != "") and (text is None or text == "" ):
            st.warning('⚠ Please enter your plain text! 😯')
        else:
            st.warning('⚠ Text fields missing! 😯')

if format_type == "Documents":
    st.info('Supports all popular document formats 📄 - TXT, PDF, DOCX 😉')
    uploaded_file = st.file_uploader("Upload Document 📃", type=["txt","pdf","docx"])
    if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())
        if uploaded_file.name.endswith('.txt') or uploaded_file.name.endswith('.TXT'):
            with st.spinner(f"Working... 💫"):
                uploaded_txt_file = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                downloaded_txt_file = os.path.abspath(os.path.join(download_path,str("processed_"+uploaded_file.name)))
                txt = extract_text_txt(uploaded_txt_file,downloaded_txt_file)

        if uploaded_file.name.endswith('.pdf') or uploaded_file.name.endswith('.PDF'):
            with st.spinner(f"Working... 💫"):
                uploaded_pdf_file = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                txt = extract_text_pdf(uploaded_pdf_file)

        if uploaded_file.name.endswith('.docx') or uploaded_file.name.endswith('.DOCX'):
            with st.spinner(f"Working... 💫"):
                uploaded_docx_file = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                txt = extract_text_docx(uploaded_docx_file)

    else:
        st.warning('⚠ Please upload your document 😯')

    ques_text = st.text_area("Enter your Question: 🙋",height=50)
    if st.button("Run"):
        if (ques_text is not None and ques_text != ""):
            with st.spinner(f"Getting your Answer... 💫"):
                    ans = generate_answer(str(txt),ques_text)
                    st.markdown("Here's the answer 🗣")
                    st.balloons()
                    st.success('✅ '+ans)
        else:
            st.warning('⚠ Please enter your question! 😯')