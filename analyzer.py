from langchain_community.llms import HuggingFaceEndpoint
from langchain_huggingface import ChatHuggingFace
import streamlit as st 
from pypdf import PdfReader
import docx
import os 

#pass apikey 
token  = os.getenv('HuggingFaceHub_API_Token') 

#title
st.title("AI Resume Analyzer")
st.write("Upload your resume and get personalized suggestions")
#take input from user
file_uploaded = st.file_uploader("Upload Your File:",type=['doc','pdf','txt'])

#extract text from file
def extract_text(file):
    file_type = file.name.split('.')[-1].lower()

    text = ""

    # PDF
    if file_type == "pdf":
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()

    # DOCX
    elif file_type == "docx":
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text

    # TXT
    elif file_type == "txt":
        text = file.read().decode("utf-8")

    else:
        return "Unsupported file type ❌"

    return text

if file_uploaded:
    #calling function
    extracted_text = extract_text(file_uploaded)
    description  = st.text_input("Paste Description:")
    if description:
        
        prompt  = f"""Role: Act as you are a expert in Application Tracking System.
                    Analyze following resume content againest  description.
                 return   key insights in the form of paragraphs  for the following things :
                    1-ATS score[1-100]
                    2-Missing keywords
                    3-Strong suggestions
                    4-Any improvements
                 Resume_content:{extracted_text}
                 description : {description}
                 """
         #Accessing   llm model           
        llm  =HuggingFaceEndpoint(repo_id = "openai/gpt-oss-120b",
        task='text-generation',max_new_tokens =5000)
        model = ChatHuggingFace(llm = llm)
        #final answer 
        result  =model.invoke(prompt)
        st.write("Analyzing")
        st.text_area("Here Is Answer",result.content,height=1000)
    
        st.write("Modify changes in your resume and then apply to job")







