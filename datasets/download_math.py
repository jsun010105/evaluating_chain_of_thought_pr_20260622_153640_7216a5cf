"""Download MATH dataset from HuggingFace (EleutherAI version)."""
from datasets import load_dataset
import json

subjects = [
    'algebra',
    'counting_and_probability',
    'geometry',
    'intermediate_algebra',
    'number_theory',
    'prealgebra',
    'precalculus',
]

print("Downloading MATH dataset by subject...")
all_samples = []

for subject in subjects:
    try:
        ds = load_dataset('EleutherAI/hendrycks_math', subject)
        print(f"  {subject}: train={len(ds['train'])}, test={len(ds['test'])}")
        # Save 5 samples from test split
        for item in list(ds['test'])[:5]:
            sample = dict(item)
            sample['subject'] = subject
            all_samples.append(sample)
    except Exception as e:
        print(f"  {subject}: failed - {e}")

with open('datasets/math_samples.json', 'w') as f:
    json.dump(all_samples, f, indent=2, default=str)

print(f"\nSaved {len(all_samples)} samples to datasets/math_samples.json")
print("\nTo download the full dataset for a specific subject:")
print("  ds = load_dataset('EleutherAI/hendrycks_math', 'algebra')")
