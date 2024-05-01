# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="microsoft/Phi-3-mini-128k-instruct", trust_remote_code=True)

text = "Tell me a story about horses."
r = pipe(text)

print(r)