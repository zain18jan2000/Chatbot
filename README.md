# Chatbot

Chatbots are software applications that use artificial intelligence & natural language processing to understand what a human wants, and guides them to their desired outcome with as little work for the end user as possible. 

Unlike Generative based Chatbots, This chatbot is trained on predefined input patterns and responses. Hence it is a Retrieval based Chatbot. The Retrieval based Chatbots are widely used in the industry to make goal-oriented chatbots where we can customize the tone and flow of the chatbot to drive our customers with the best experience.

This repository contains following 3 files in 'Retrieval based Chatbots' folder,<br/>
**text.json**. This file contains predefined input patterns and responses in dictionary structure of python. Our chatbot is trained on these input patterns and responses.<br/>
**zbot.py**. This file contains code for text processing, text encoding and creating a window which acts as an interface between user and our chatbot. <br/>
**zbot.h5**. This is trained model of chatbot. Although it is trained on the pre-defined chats in text.json, it can also be used for other predefined chats, but for that the model will have to be retrained.  

<h2>GUI INTERFACE</h2><br>
![chatbot](https://user-images.githubusercontent.com/82854685/140953741-9fb49d61-8dd9-4e67-b7c3-5cc6c5083cf1.JPG)
