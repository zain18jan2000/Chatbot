import numpy as np
import string
import nltk
import random
from nltk.stem import WordNetLemmatizer
import tensorflow as tf 
from tensorflow.keras import Sequential 
from datetime import datetime, date
from tensorflow import keras

stop_words = ['is','am','the','a','an','be','are','were',]

data = {"intents": [
             {"tag": "greeting",
              "patterns": ["Hello", "How are you?", "Hi there", "Hi", "Whats up",'hey'],
              "responses": ["Howdy Partner!", "Hello", "How are you doing?", "Greetings!",
                            "How do you do?"],
             },
             {"tag": "age",
              "patterns": ["how old are you?", "when is your birthday?", "when was you born?",'what is your date of birth?','your birth date'],
              "responses": [ "I was born in 2021", 
                            "My birthday is January 3rd and I was born in 2021","03/01/2021"]
             },
             {"tag": "state",
              "patterns": ["what are you doing this weekend?",
"do you want to hang out some time?", "what are your plans for this week"],
              "responses": ["I am available all week", "I don't have any plans", "I am not busy"]
             },
             {"tag": "name",
              "patterns": ["what's your name?", "what are you called?", "who are you?",],
              "responses": ["My name is zbot", "I'm zbot", "zbot",'call me zbot']
             },

             {"tag": "goodbye",
              "patterns": [ "bye", "g2g", "see ya", "adios", "cya"],
              "responses": ["It was nice speaking to you", "See you later", "Speak soon!"]
             },
             {"tag":'intro',
              "patterns": ['tell me about your self','introduce yourself','i would like to know about you',
                          'i want to about you'],
              'responses': ['i am a chatbot that is all you should know','i am a chatbot and i was programmed by a programmer']
             },
             { 'tag':"intelligence",
                 "patterns": ['you are intelligent','you seems to be intelligent','you are wise',
                              'you are smart','you know you are smart'],
              'responses': ['am I? thanks','thanks','I know']
             },
             {"tag":'abuse',
     'patterns': ['you are stupid','you are trash','you are as bad as hell','get lost','you are bad',
                'you are dump','you seems like garbage','shutup','go away','idiot'],
     'responses': ['you know donot have mannners','shutup','same to you','you made me angry',
                  'mind your language']},
    
    {'tag':"stupidity",
     'patterns':['you are stupid','you are not intelligent','you are not smart','stupid',
                 'you are lazy','you are not replying properly',"I didn't ask that",
                 "that's not my answer","why are you not replying"],
     'responses': ['I am not smart enough to reply always accurately', 
                  'I am not trained to reply each and every response']
    },
    {
     'tag': 'undefined',
      'patterns':['oh i see','i know','i see','so that is the problem','haha','hahaha','hahahaha','oh',
                 'yeah i know','it is fine',"It's fine"],
     'responses':[' '] 
    },
     { 'tag':' joke',
    'patterns': ['tell me a joke','do you know any joke?'],
     'responses': ['elephant is scared of mouse','why did mushroom go to party? Because he is fungi',
    "what do you call fake speghetti? an inpasta" ]
    },
     {
    'tag':'thankful',
     'patterns': ['thank you','thanks','thanks for that','thankyou'],    
     'responses': ["you're welcome",'welcome','no need']
     },
    { 'tag':"creater",
     'patterns': ['who programmed you ?','who created you','who made you',
                 'what is name of person who created you','who is Zain','who create you?'],
     'responses':['Zain programmed me','I was programmed by Zain','his name is Zain, he is a student']
                 },
    {
        'tag':'change name',
        'patterns':['i will call you bot', 'you are robot from now', 'can I call you bot?'],
        'responses':['you are not allowed to changed my name','you cannot changed my name']
    },
    {
        'tag': 'username',
        'patterns':['my name is zain','my name is laiba','i am zain','you can call me Hamza',
                    'you know my name is x','what is my name'],
        'responses':['I am not smart enough to remember your name',"I cannot remember any one's name"]
    },
    {
        'tag': 'time',
        'patterns':['what time is it?','tell me the time',' can you tell me the current time',
                    'show me the time'],
        'responses':["","current time is "]},
    {
        'tag':'creater info',
        'patterns': ['in which institution does zain study?','what does zain do'],
        'responses': ['My creater Zain studies in NED university, he is an electronic engineering student']
    },
    {'tag':'creater info',
        'patterns': ['where do you live','where is your residence?'],
        'responses': ['I love to in electronic devices','I live in computer',
                      "Well, It's a difficult question, you can say my residence is in computer"]
    },
    {'tag':'date',
        'patterns': ['what is the  date today',"what's the date today ?","tell me the date",'date'
                    ,'tell me the current date','can you tell me the date',"today's date ?"],
     'responses': ["","current date is "]
    }
     ]}

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

# converting to lower case, applyging lemmatization removing the puctuations
# here 'words' is our vocabulary containing all the words 
words = [lemmatizer.lemmatize(word.lower()) for word  in words if word not in string.punctuation and 
        word not in stop_words]
# converting the list to set to avoid doubling of words in in 'words'
words = sorted(set(words))
words = list(words)


try:
    model = keras.models.load_model('ZBOT.h5')
except:
    print("The filename ZBOT.h5 not found or the filename has been changed")

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

# to get user input in  multiples lines
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