import openai
openai.api_key='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'
messages=[{"role":"system","content": "You are an intelligent assistant"}]
while True:
  message=input("User: ")
  if message:
    messages.append(
        {"role":"user","content": message
    })
    chat=openai.ChatCompletion.create(
        model='gpt-3.5-turbo', messages=messages, temperature=0.5
    )
    reply=chat.choices[0].message.content
    print(f"CHATBOT: {reply}")
    messages.append(
        {"role":"assistant","content": reply})