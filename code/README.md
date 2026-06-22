# Code Repositories

This directory contains cloned repositories relevant to the CoT prompting research project.

## Repositories

### 1. grade-school-math (GSM8K Official)
- **Source**: https://github.com/openai/grade-school-math
- **Authors**: OpenAI (Cobbe et al.)
- **Purpose**: Official repository for the GSM8K dataset and evaluation code
- **Status**: Archive (code as-is, no updates expected)

#### Contents
- `grade_school_math/data/train.jsonl` — 7,473 training problems
- `grade_school_math/data/test.jsonl` — 1,319 test problems
- `grade_school_math/data/train_socratic.jsonl` — Training data with Socratic subquestions
- `grade_school_math/data/test_socratic.jsonl` — Test data with Socratic subquestions
- `grade_school_math/data/example_model_solutions.jsonl` — Solutions from 6B and 175B GPT-3 models
- `calculator.py` — Calculator annotation sampling implementation
- `dataset.py` — Dataset loading utilities; `is_correct()` for answer checking

#### Key Usage
```python
# Load dataset
import json
with open('code/grade-school-math/grade_school_math/data/test.jsonl') as f:
    test_data = [json.loads(line) for line in f]

# Check answer correctness
from grade_school_math.dataset import is_correct
# Answer format: ends with "#### <number>"
```

#### Answer Format
Answers use `####` separator: `"Some reasoning steps.\n#### 42"`
Final answer extraction: `answer.split("####")[-1].strip()`

---

### 2. hendrycks-math (MATH Dataset Official)
- **Source**: https://github.com/hendrycks/math
- **Authors**: Hendrycks et al. (UC Berkeley)
- **Purpose**: Official repository for the MATH competition math dataset and evaluation utilities

#### Contents
- `modeling/` — Baseline model code
- `setup.py` — Package setup
- Evaluation utilities for the MATH dataset

#### Key Usage
```python
# Dataset available at HuggingFace
from datasets import load_dataset
ds = load_dataset('EleutherAI/hendrycks_math', 'algebra')

# Answer format: LaTeX boxed answer, e.g., \boxed{42}
# Evaluation: exact string match on boxed content
```

#### Notes
- Problems use LaTeX for math formatting
- 5 difficulty levels (Level 1 easiest, Level 5 hardest)
- 7 subject areas
- Evaluation requires symbolic equivalence checking for full accuracy

---

### 3. zero_shot_cot (Zero-Shot Reasoners)
- **Source**: https://github.com/kojima-takeshi188/zero_shot_cot
- **Authors**: Kojima et al. (University of Tokyo)
- **Purpose**: Official implementation of "Large Language Models are Zero-Shot Reasoners" (NeurIPS 2022)

#### Contents
- `main.py` — Main evaluation script
- `utils.py` — Utility functions for prompting and evaluation
- `dataset/` — Dataset loading code
- `log/` — Example experiment logs

#### Key Usage
```bash
export OPENAI_API_KEY=<your-key>

# Zero-shot CoT (our proposal)
python main.py --method=zero_shot_cot --model=gpt3-xl --dataset=gsm8k

# Zero-shot baseline
python main.py --method=zero_shot --model=gpt3-xl --dataset=gsm8k

# Few-shot CoT
python main.py --method=few_shot_cot --model=gpt3-xl --dataset=gsm8k

# Few-shot baseline
python main.py --method=few_shot --model=gpt3-xl --dataset=gsm8k
```

#### Supported Datasets
MultiArith, GSM8K, AQuA-RAT, SingleEq, AddSub, MultiArith, StrategyQA, CommonsenseQA, Date Understanding, Tracking Shuffled Objects

#### Notes
- Uses OpenAI API (InstructGPT models: gpt3, gpt3-medium, gpt3-large, gpt3-xl)
- Rate limit: ≤60 API calls/minute (set `api_time_interval=1.0`)
- `limit_dataset_size=10` for budget-conscious testing

---

## Relevance to Our Experiment

| Repository | Use in Experiment |
|-----------|-------------------|
| grade-school-math | Load GSM8K test set; use `is_correct()` for answer checking |
| hendrycks-math | Reference for MATH dataset format and evaluation methodology |
| zero_shot_cot | Reference implementation for zero-shot vs. few-shot CoT comparison; adapt `utils.py` |
