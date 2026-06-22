# Research Resources Catalog

**Project**: Evaluating Chain-of-Thought Prompting Effectiveness Across Mathematical Reasoning Tasks  
**Date**: 2026-06-22

---

## Papers

| # | File | arXiv ID | Authors | Year | Title | Venue | Role |
|---|------|----------|---------|------|-------|-------|------|
| 1 | papers/2201.11903_chain_of_thought.pdf | 2201.11903 | Wei et al. | 2022 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | NeurIPS 2022 | **CORE** — defines the method |
| 2 | papers/2205.11916_least_to_most.pdf | 2205.11916 | Kojima et al. | 2022 | Large Language Models are Zero-Shot Reasoners | NeurIPS 2022 | **CORE** — zero-shot CoT baseline |
| 3 | papers/2203.11171_self_consistency.pdf | 2203.11171 | Wang et al. | 2022 | Self-Consistency Improves Chain of Thought Reasoning | ICLR 2023 | Key extension |
| 4 | papers/2103.03874_math_dataset.pdf | 2103.03874 | Hendrycks et al. | 2021 | Measuring Mathematical Problem Solving With the MATH Dataset | NeurIPS 2021 | Dataset paper |
| 5 | papers/2110.14168_gsm8k.pdf | 2110.14168 | Cobbe et al. | 2021 | Training Verifiers to Solve Math Word Problems | arXiv 2021 | Dataset paper |
| 6 | papers/2211.10435_pal_program_aided.pdf | 2211.10435 | Gao et al. | 2022 | PAL: Program-Aided Language Models | ICML 2023 | Alternative approach |
| 7 | papers/2305.10601_tree_of_thoughts.pdf | 2305.10601 | Yao et al. | 2023 | Tree of Thoughts: Deliberate Problem Solving with LLMs | NeurIPS 2023 | Advanced extension |
| 8 | papers/2205.10625_least_to_most_prompting.pdf | 2205.10625 | Zhou et al. | 2022 | Least-to-Most Prompting Enables Complex Reasoning in LLMs | ICLR 2023 | Decomposition variant |
| 9 | papers/2210.11610_auto_cot.pdf | 2210.11610 | Huang et al. | 2022 | Large Language Models Can Self-Improve | EMNLP 2023 | Self-training with CoT |

### Paper Download Commands
```bash
# Re-download papers if needed
source .venv/bin/activate
python -c "
import requests
papers = [
    ('https://arxiv.org/pdf/2201.11903.pdf', 'papers/2201.11903_chain_of_thought.pdf'),
    ('https://arxiv.org/pdf/2205.11916.pdf', 'papers/2205.11916_least_to_most.pdf'),
    ('https://arxiv.org/pdf/2203.11171.pdf', 'papers/2203.11171_self_consistency.pdf'),
    ('https://arxiv.org/pdf/2103.03874.pdf', 'papers/2103.03874_math_dataset.pdf'),
    ('https://arxiv.org/pdf/2110.14168.pdf', 'papers/2110.14168_gsm8k.pdf'),
    ('https://arxiv.org/pdf/2211.10435.pdf', 'papers/2211.10435_pal_program_aided.pdf'),
    ('https://arxiv.org/pdf/2305.10601.pdf', 'papers/2305.10601_tree_of_thoughts.pdf'),
    ('https://arxiv.org/pdf/2205.10625.pdf', 'papers/2205.10625_least_to_most_prompting.pdf'),
    ('https://arxiv.org/pdf/2210.11610.pdf', 'papers/2210.11610_auto_cot.pdf'),
]
for url, path in papers:
    r = requests.get(url, stream=True, timeout=60)
    open(path, 'wb').write(r.content)
    print(f'Downloaded {path}')
"
```

---

## Datasets

| Dataset | HuggingFace ID | Local Path | Status | Size |
|---------|---------------|------------|--------|------|
| GSM8K | openai/gsm8k | datasets/gsm8k/ | Downloaded | 7,473 train / 1,319 test |
| MATH (algebra) | EleutherAI/hendrycks_math | On-demand | Available | 1,744 train / 1,187 test |
| MATH (counting_and_probability) | EleutherAI/hendrycks_math | On-demand | Available | 771 train / 474 test |
| MATH (geometry) | EleutherAI/hendrycks_math | On-demand | Available | 870 train / 479 test |
| MATH (number_theory) | EleutherAI/hendrycks_math | On-demand | Available | 869 train / 540 test |
| MATH (prealgebra) | EleutherAI/hendrycks_math | On-demand | Available | 1,205 train / 871 test |
| MATH (precalculus) | EleutherAI/hendrycks_math | On-demand | Available | 746 train / 546 test |

**Total MATH test examples across 6 subjects**: 4,097

### Sample Files
- `datasets/gsm8k_samples.json` — 10 GSM8K training examples
- `datasets/math_samples.json` — 30 MATH test examples (5 per subject)

### Re-download Commands
```bash
source .venv/bin/activate

# GSM8K
python datasets/download_gsm8k.py

# MATH (samples only, for inspection)
python datasets/download_math.py
```

---

## Code Repositories

| Repository | Local Path | Source URL | Purpose |
|-----------|-----------|------------|---------|
| GSM8K Official | code/grade-school-math | https://github.com/openai/grade-school-math | Dataset files, evaluation utilities |
| MATH Official | code/hendrycks-math | https://github.com/hendrycks/math | Dataset structure reference, evaluation code |
| Zero-Shot CoT | code/zero_shot_cot | https://github.com/kojima-takeshi188/zero_shot_cot | Reference implementation for CoT evaluation |

### Re-clone Commands
```bash
git clone https://github.com/openai/grade-school-math code/grade-school-math
git clone https://github.com/hendrycks/math code/hendrycks-math
git clone https://github.com/kojima-takeshi188/zero_shot_cot code/zero_shot_cot
```

---

## Key Quantitative Results from Literature

### GSM8K Benchmark (direct vs. CoT)

| Model | Direct Prompting | Few-Shot CoT | Gain (pp) | Source |
|-------|-----------------|--------------|-----------|--------|
| GPT-3 175B | ~16% | ~46% | ~30 | Wei 2022 |
| PaLM 540B | 18% | 57% | 39 | Wei 2022 |
| InstructGPT (text-davinci-002) | 10.4% (0-shot) | 40.7% (0-shot CoT) | 30.3 | Kojima 2022 |
| PaLM 540B + Self-Consistency | — | ~74% | — | Wang 2022 |
| Codex + PAL | — | ~72% | — | Gao 2022 |
| PaLM 540B + Self-Improve | — | ~82% | — | Huang 2022 |

### MATH Benchmark Baselines

| Model | Accuracy | Source |
|-------|----------|--------|
| GPT-2 (fine-tuned) | 4.2% | Hendrycks 2021 |
| GPT-3 (fine-tuned) | 6.9% | Hendrycks 2021 |
| GPT-3 (few-shot CoT) | ~5-10% | Various |
| GPT-4 | ~42% | Yao 2023 |
| GPT-4 + complex CoT | ~52-68% | Later work |

---

## Python Environment

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Installed packages
uv pip install pypdf requests arxiv httpx datasets
```

Key packages:
- `pypdf` — PDF reading and chunking
- `requests` — HTTP downloads
- `arxiv` — arXiv paper search API
- `httpx` — Async HTTP (for paper-finder service)
- `datasets` — HuggingFace datasets

---

## Useful Code Snippets

### Answer Extraction (GSM8K)
```python
import re

def extract_gsm8k_answer(completion: str) -> str | None:
    """Extract numeric answer from GSM8K-style completion."""
    if "####" in completion:
        return completion.split("####")[-1].strip().replace(",", "")
    # Fallback: find last number in response
    numbers = re.findall(r'-?\d+(?:\.\d+)?', completion)
    return numbers[-1] if numbers else None

def check_gsm8k_correct(prediction: str, ground_truth: str) -> bool:
    pred = extract_gsm8k_answer(prediction)
    truth = extract_gsm8k_answer(ground_truth)
    if pred is None or truth is None:
        return False
    try:
        return abs(float(pred.replace(",", "")) - float(truth.replace(",", ""))) < 1e-6
    except ValueError:
        return pred == truth
```

### Answer Extraction (MATH)
```python
import re

def extract_math_answer(completion: str) -> str | None:
    """Extract boxed answer from MATH-style completion."""
    matches = re.findall(r'\\boxed\{([^}]+)\}', completion)
    return matches[-1] if matches else None
```

### GSM8K Loading
```python
from datasets import load_dataset

gsm8k = load_dataset("openai/gsm8k", "main")
test_set = gsm8k["test"]  # 1,319 examples
# Each example: {"question": str, "answer": str}
```

### MATH Loading (stratified by difficulty)
```python
from datasets import load_dataset

# Load a specific subject
algebra = load_dataset("EleutherAI/hendrycks_math", "algebra")
test = algebra["test"]  # 1,187 examples
# Filter by difficulty level
easy = [x for x in test if x["level"] == "Level 1"]
hard = [x for x in test if x["level"] == "Level 5"]
```

---

## CoT Prompt Templates

### Few-Shot CoT Template (GSM8K)
```python
FEW_SHOT_COT_EXAMPLES = [
    {
        "question": "Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?",
        "answer": "Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is #### 11"
    },
    # ... 7 more examples from the Wei et al. paper
]

def format_few_shot_cot(question: str, examples: list) -> str:
    prompt = ""
    for ex in examples:
        prompt += f"Q: {ex['question']}\nA: {ex['answer']}\n\n"
    prompt += f"Q: {question}\nA:"
    return prompt
```

### Zero-Shot CoT Template
```python
def format_zero_shot_cot(question: str) -> str:
    return f"Q: {question}\nA: Let's think step by step."
```

### Direct Prompting Template
```python
def format_direct(question: str) -> str:
    return f"Q: {question}\nA:"
```
