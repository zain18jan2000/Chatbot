import numpy as np
import string
import nltk
import random
from nltk.stem import WordNetLemmatizer
import tensorflow as tf 
from tensorflow.keras import Sequential 
from datetime import datetime, date
from tensorflow import keras
import json

stop_words = ['is','am','the','a','an','be','are','were',]

text = open('text.json').read()
data = json.loads(text)

lemmatizer = WordNetLemmatizer()
words = []
y = []
patterns =[]
x = []
classes = []
# getting the classes(tags) output and patterns from 'data'
for intent in data['intents']:
    classes.append(intent['tag'])
    for pattern in intent['patterns']:
# applying tokenizer to convert the sentences into a list of words        
        tokens = nltk.word_tokenize(pattern)
# here .extend() is used instead of append() since we don't want to append lists in words 
# but its elements i.e words in 'token'
# here 'tokens' is a list of words
        words.extend(tokens)
        patterns.append(pattern)
        y.append(intent['tag'])

# converting all letters to lower case, applying lemmatization and removing the puctuations
# here 'words' is our vocabulary containing all the words 
words = [lemmatizer.lemmatize(word.lower()) for word  in words if word not in string.punctuation and 
        word not in stop_words]
# converting the list to set to avoid doubling of words in variable 'words'
words = sorted(set(words))
words = list(words)


try:
    model = keras.models.load_model('ZBOT.h5')
except:
    print("The filename ZBOT.h5 not found or the filename has been changed")

 
# applying bag of words techniques to convert user's text in binary
def bagofwords(msg):
    tokens = nltk.word_tokenize(msg)
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token not in string.punctuation and token 
              not in stop_words]
    binary_msg = []
    for word in words:
        binary_msg.append(1) if word in tokens else binary_msg.append(0)
    return np.array(binary_msg)
def prediction(msg):
    message = bagofwords(msg)
    result = model.predict_classes(np.array([message]))
    class_index = list(result)[0] 
    for intent in data['intents']:
        if intent['tag'] == classes[class_index]:
            if classes[class_index] == 'time':
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                response = random.choice(intent['responses']) + current_time
                return response
            elif classes[class_index] == 'date':
                today = date.today()
                current_date = today.strftime("%d/%m/%Y")
                response = random.choice(intent['responses']) + current_date
                return response
            response = random.choice(intent['responses'])
            return response

# to get user input we'll create a window
from tkinter import *
import tkinter as tk
window = tk.Tk()
# detemining how large widow should be and where it should be on  the screen
window.geometry("662x445+220+50")
# this is how to set background color of window
window['background']='white'
# giving title
window.title('ZBOT')
# function to get input from text box and to print that text on other text box
def getinput():
    # getting text
    text = entry.get("1.0", tk.END)
    response =prediction(text)
    # deleting what is written just now when after the button click
    entry.delete(1.0,tk.END)
    # insert the text on other text box at the end
    text_box.config(state = tk.NORMAL)    
    text_box.insert(tk.END,'YOU:   '+text)
    text_box.insert(tk.END,'ZBOT:   ' + response + '\n\n')
    text_box.yview(tk.END)
    text_box.config(state = tk.DISABLED)

text_box = tk.Text(window, bg ="#856ff8", fg = 'white',font=("Verdana",12,'bold')
                  ,height =21,width =58 )
text_box.config(state = tk.DISABLED)
scrollbar = tk.Scrollbar(window, command=text_box.yview)
scrollbar.place(x=645,y=6, height= 435)
# .place() is a geometry manager used to set size of widgets like button, entry box 
text_box.place(x =2,y = 3)
button = tk.Button(window,text ='ENTER', width = 17,height =2,bg ="blue",
                   fg ='white',font=("Verdana",12,'bold'), command = getinput)
button.place(x=450, y=390)
entry = tk.Text(window,height =2,width =40,bg ='yellow',fg = 'blue',font='bold')
entry.place(x = 1, y = 390)
# used to display window
window.mainloop()        
