# Datasets

This directory contains downloaded datasets and scripts for the CoT prompting research project.

## Overview

| Dataset | Source | Size (Train) | Size (Test) | Task Type | Difficulty |
|---------|--------|--------------|-------------|-----------|------------|
| GSM8K | openai/grade-school-math | 7,473 | 1,319 | Grade school math word problems | Medium (2-8 steps) |
| MATH | EleutherAI/hendrycks_math | ~7,500 (combined) | ~4,097 (combined) | Competition mathematics | Hard (5 difficulty levels) |

---

## GSM8K Dataset

### Description
Grade School Math 8K (GSM8K) is a dataset of 8,500 high-quality, linguistically diverse grade school math word problems created by human problem writers. Problems require 2-8 reasoning steps using basic arithmetic operations (+, -, *, /).

### Statistics
- **Train**: 7,473 examples
- **Test**: 1,319 examples
- **Problem type**: Word problems requiring multi-step arithmetic reasoning
- **Difficulty**: Solvable by a bright middle school student
- **Format**: Each answer ends with `#### <numeric_answer>`

### Download Instructions
```python
from datasets import load_dataset

# Option 1: From HuggingFace (recommended)
dataset = load_dataset("openai/gsm8k", "main")
# train: 7473, test: 1319

# Option 2: From the official GitHub repo
# git clone https://github.com/openai/grade-school-math
# Data at: grade-school-math/grade_school_math/data/train.jsonl
#           grade-school-math/grade_school_math/data/test.jsonl
```

### Files
- `datasets/gsm8k/` — HuggingFace arrow format (gitignored, must re-download)
- `datasets/gsm8k_samples.json` — 10 sample problems for inspection
- `datasets/download_gsm8k.py` — Download script

### Sample Data Preview
```json
{
  "question": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?",
  "answer": "Natalia sold 48/2 = <<48/2=24>>24 clips in May.\nNatalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.\n#### 72"
}
```

### Evaluation Metric
Exact match on the numeric final answer extracted after `####`.

---

## MATH Dataset

### Description
MATH is a dataset of 12,500 challenging competition mathematics problems across 7 subjects and 5 difficulty levels. Problems span from pre-algebra to competition math (AMC, AIME, etc.). Each problem has a full step-by-step solution.

### Statistics
- **Total problems**: 12,500 (7,500 train + 5,000 test, approximate)
- **Subjects** (with test counts from EleutherAI version):
  - Algebra: 1,187 test examples
  - Counting & Probability: 474 test examples
  - Geometry: 479 test examples
  - Number Theory: 540 test examples
  - Prealgebra: 871 test examples
  - Precalculus: 546 test examples
  - Intermediate Algebra: (train-only in some versions)
- **Difficulty Levels**: 1 (easiest) to 5 (hardest)
- **Format**: LaTeX math expressions, multi-step solutions

### Download Instructions
```python
from datasets import load_dataset

# Via HuggingFace (EleutherAI version, per subject)
subjects = ['algebra', 'counting_and_probability', 'geometry',
            'intermediate_algebra', 'number_theory', 'prealgebra', 'precalculus']

for subject in subjects:
    ds = load_dataset('EleutherAI/hendrycks_math', subject)
    # ds['train'], ds['test']

# Alternative: qwedsacf/competition_math (full combined dataset)
# git clone from HF Hub (see hendrycks-math repo README)
```

### Files
- `datasets/math_samples.json` — 5 samples per subject (30 total) for inspection
- `datasets/download_math.py` — Download script

### Sample Data Preview
```json
{
  "problem": "What is the value of $x$ if $x=\\frac{2009^2-2009}{2009}$?",
  "level": "Level 1",
  "type": "Algebra",
  "solution": "We have \\begin{align*} x &= \\frac{2009^2 - 2009}{2009} \\\\ &= \\frac{2009(2009-1)}{2009} \\\\ &= 2009-1 \\\\ &= \\boxed{2008}. \\end{align*}",
  "subject": "algebra"
}
```

### Evaluation Metric
Exact match on the boxed final answer (\\boxed{...} in LaTeX). Note: symbolic matching is needed for equivalent forms (e.g., 1/2 vs 0.5 vs \\frac{1}{2}).

---

## Usage in Experiments

For our CoT evaluation experiment:

1. **Primary benchmark**: GSM8K test set (1,319 problems) — well-suited for comparing direct vs. CoT prompting
2. **Difficulty stratification**: MATH dataset by level 1-5 — enables testing hypothesis that CoT gains increase with harder problems
3. **Recommended test size per subject**: 50-100 problems from GSM8K test, 20-50 from each MATH difficulty level

### Recommended evaluation subsets
```python
# GSM8K - use full test set (1,319 problems, ~manageable with API)
# MATH - stratify by difficulty
math_easy = dataset.filter(lambda x: x['level'] == 'Level 1')    # ~200 problems
math_hard = dataset.filter(lambda x: x['level'] == 'Level 5')    # ~200 problems
```
