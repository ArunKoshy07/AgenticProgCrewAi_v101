# pip install openai
# key = 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

from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
