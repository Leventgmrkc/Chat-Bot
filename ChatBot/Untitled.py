#!/usr/bin/env python
# coding: utf-8

# # I use two link to get help and the photos that take at the classes.
# 
# ##https://www.harabroke.com/2020/05/how-to-make-chatbot-in-python-using.html
# ##https://sonsuzdesign.blog/2020/12/17/building-a-chatbot-in-python-beginners-guide/
# 
# """ Eliza homework.
# ## I implement lots of regex's but sometihngs went wrong. Some of them are not working.

# In[1]:


import random
print("BOT: What do you want me to call you?")
user_name = input()


# In[2]:


bot_template = "BOT : {0}"
user_template = user_name + " : {0}"


# In[3]:


name = "eliza"
weather = "rainy"
mood = "Happy"
 
 
responses = {
 
"what's your name?": [
   "They call me {0}".format(name),
   "I usually go by {0}".format(name),
   "My name is the {0}".format(name)
],
 
"what's today's weather?": [
    "The weather is {0}".format(weather),
    "It's {0} today".format(weather),
    "Let me check, it looks {0} today".format(weather)
],
    
r"hi|hey|hello": [
    "Hello", "Hey there",
],

 r"i'm (.*) doing good": [
    "Nice to hear that","Alright :)",
],
    
r"(.*) (location|city) ?": [
    "I' m coming from Ankara where is capital of Turkey",
    "We are at the NEIU",
    "This is Chicago baby",
],
    
r"(.*) (sad|sadness)": [
    "Sorry to hear that",
    "Its OK, never mind",
],
    
    
r"(.*) (good|great|fine|happy|joy)": [
    "Nice to hear!",
    "Glad to hear that.",
    "Fantastic!",   
],
    
r"(.*) (mother|mom|sister|brother|father|dad)": [
    "Oowww you have siblings, i just have father!",
    "Hımm, you have strong relationships.",  
],
    
r"(.*) created ?": [
    "Sorry but i can not answer it",
    "Top secret ;)",
],

 
"Are you a robot?": [
    "What do you think?",
    "Maybe yes, maybe no!",
    "Yes, I am a robot with human feelings.",
],
 
"how are you?": [
    "I am feeling {0}".format(mood),
    "{0}! How about you?".format(mood),
    "I am {0}! How about yourself?".format(mood),
],
 
"": [
    "Hey! Are you there?",
    "What do you mean by saying nothing?",
    "Sometimes saying nothing tells a lot :)",
],
 
"default": ["this is a default message"]
 
}


# In[4]:


def respond(message):
   if message in responses:
      bot_message = random.choice(responses[message])
   else:
      bot_message = random.choice(responses["default"])
   return bot_message


# In[5]:


def related(x_text):
   if "name" in x_text:
      y_text = "what's your name?"
   elif "weather" in x_text:
      y_text = "what's today's weather?"
   elif "robot" in x_text:
      y_text = "are you a robot?"
   elif "how are" in x_text:
      y_text = "how are you?"
   elif "siblings" in x_text:
      y_text = "mom" or "mommy" or "sister" or "brother" or "dad" or "daddy"
   else:
      y_text = ""
   return y_text


# In[6]:


def send_message(message):
   print(user_template.format(message))
   response = respond(message)
   print(bot_template.format(response))


# In[ ]:


while 1:
   my_input = input()
   my_input = my_input.lower()
   related_text = related(my_input)
   send_message(related_text)
   if my_input == "bye":
      break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




