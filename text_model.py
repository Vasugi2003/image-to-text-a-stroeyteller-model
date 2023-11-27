from dotenv import find_dotenv, load_dotenv
from transformers import pipeline 
import requests
import json
import logging
import streamlit as st
requests.verify = False

load_dotenv(find_dotenv()) #access huggingface token
log = logging.getLogger("text_model.py")
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class Models:
    def __init__(self):
        self.api_token = "your api key"
        self.model_id = "openai-gpt" 
    def img2text(self,url):
        image_to_text = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
        text = image_to_text(url)
        log.info("image to text model running")
        return text[0]['generated_text']

    def story(self,payload):
        payload  = json.dumps(payload)
        headers = {"Authorization": f"Bearer {self.api_token}"}
        url = f"https://api-inference.huggingface.co/models/{self.model_id}"
        response = requests.post(url, headers=headers, data=payload)
        log.info("story model running")
        return response.json()[0]['generated_text']
    
    status_bar = st.progress(0,text="progress will be shown here")
    def chain(self,payload,num=0):
        if num == 50:
            self.status_bar.progress(100,text="story generated!!")
            return payload
        
        response = self.story(payload)
        percent = int(((num+1)/50) * 100)
        self.status_bar.progress(percent,text="generating story for you!!")
        return self.chain(response,num+1)


    

    

if __name__ == "__main__":

    model = Models()
    response = model.chain(model.img2text("image.jpg"))
    print(response)
