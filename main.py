import os
import openai


def tog(c):
  if c.lower() in ['a','e','i','o','u', 'á','é','í','ó','ú']:
     return c
  elif c in ['h', 'H']:
    return '' 
  elif c.islower():
    return 'g'
  elif c.isupper():
    return 'G'
  return c

def translate(text):
  return "".join([tog(c) for c in text])

openai.api_key = os.environ.get('OPEN_AI_API_KEY')
messages = [ {"role": "system", "content":
                        "You are a intelligent assistant."} ]
while True:
   message = input("User : ")
   if message:
      messages.append({"role": "user", "content": message})
      chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
      reply = chat.choices[0].message.content
      print(f"ChatGereGere: {translate(reply)}\n\n")
      print(f"Traducción: {reply}\n\n")
      messages.append({"role": "assistant", "content": reply})


