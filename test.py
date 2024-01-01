# import os
import openai
key="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"
openai.api_key = key

content = "hello"
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": content}
  ]
)

chat_response = completion.choices[0].message.content
print(f'ChatGPT: {chat_response}')