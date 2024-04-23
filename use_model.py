from common import get_openai_client

client = get_openai_client()
completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-0125:personal::xxx",
  messages=[
    {"role": "system", "content": "你一个人工智能法律助理"},
    {"role": "user", "content": "举一个例子，不构成资敌罪的情况"}
  ]
)
print(completion.choices)