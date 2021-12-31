# Chatbot

Chatbots are software applications that use artificial intelligence & natural language processing to understand what a human wants, and guides them to their desired outcome with as little work for the end user as possible. 

Unlike Generative based Chatbots, This chatbot is trained on predefined input patterns and responses. Hence it is a Retrieval based Chatbot. The Retrieval based Chatbots are widely used in the industry to make goal-oriented chatbots where we can customize the tone and flow of the chatbot to drive our customers with the best experience.

This repository contains following 4 files in 'Retrieval based Chatbots' folder,<br><br>
**text.json**. This file contains predefined input patterns and responses in dictionary structure of python. Our chatbot is trained on these input patterns and responses.<br/>
**zbot-checkpoint.ipynb**. This file is for building and training the model for chatbot. <br>
**zbot.py**. This file contains code for text processing, text encoding and creating a window which acts as an interface between user and our chatbot. <br/>
**zbot.h5**. This is trained model of chatbot. Although it is trained on the pre-defined chats in text.json, it can also be used for other predefined chats, but for that the model will have to be retrained.  

<h2>GUI INTERFACE</h2><br>

![chatbot](https://user-images.githubusercontent.com/82854685/140954852-cb6b00b5-9e8d-4260-96d0-438a607e8466.JPG)
