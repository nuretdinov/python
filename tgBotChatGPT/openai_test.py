from openai import OpenAI
import os

client = OpenAI(
   # api_key=os.environ.get(".env"),
)

question = 'can you tell a few interesting subtopics in topic football'
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": question}
  ]
)

print(completion.choices[0].message)