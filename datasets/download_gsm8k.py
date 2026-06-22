"""Download GSM8K dataset from HuggingFace."""
from datasets import load_dataset
import json

print("Downloading GSM8K dataset...")
dataset = load_dataset("gsm8k", "main")
dataset.save_to_disk("datasets/gsm8k")

# Save samples
samples = []
for item in list(dataset['train'])[:10]:
    samples.append(item)
with open('datasets/gsm8k_samples.json', 'w') as f:
    json.dump(samples, f, indent=2, default=str)

print(f"GSM8K train: {len(dataset['train'])} examples")
print(f"GSM8K test: {len(dataset['test'])} examples")
print("Saved to datasets/gsm8k/")
print("Sample saved to datasets/gsm8k_samples.json")
