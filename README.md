# 📄  Question_Answering_System
A simple Q&amp;A webapp to process text built using RoBerTa Model from Huggingface Transformers 🤗.

## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Simply run the command: 
```
streamlit run app.py
```
3. Navigate to http://localhost:8501 in your web-browser.
4. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading documents, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```

## Results:
1. Perform Q&A on random text on the fly!

2. Upload your document ***(supports PDFs, Word Files, Text files)*** and perform Q&A:
