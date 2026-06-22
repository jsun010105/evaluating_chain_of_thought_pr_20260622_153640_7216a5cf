# Papers

This directory contains PDFs of key papers for the CoT prompting research project.

## Downloaded Papers

| File | arXiv ID | Authors | Year | Title | Venue |
|------|----------|---------|------|-------|-------|
| 2201.11903_chain_of_thought.pdf | 2201.11903 | Wei et al. | 2022 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | NeurIPS 2022 |
| 2205.11916_least_to_most.pdf | 2205.11916 | Kojima et al. | 2022 | Large Language Models are Zero-Shot Reasoners | NeurIPS 2022 |
| 2203.11171_self_consistency.pdf | 2203.11171 | Wang et al. | 2022 | Self-Consistency Improves Chain of Thought Reasoning in Language Models | ICLR 2023 |
| 2103.03874_math_dataset.pdf | 2103.03874 | Hendrycks et al. | 2021 | Measuring Mathematical Problem Solving With the MATH Dataset | NeurIPS 2021 |
| 2110.14168_gsm8k.pdf | 2110.14168 | Cobbe et al. | 2021 | Training Verifiers to Solve Math Word Problems | arXiv 2021 |
| 2211.10435_pal_program_aided.pdf | 2211.10435 | Gao et al. | 2022 | PAL: Program-Aided Language Models | ICML 2023 |
| 2305.10601_tree_of_thoughts.pdf | 2305.10601 | Yao et al. | 2023 | Tree of Thoughts: Deliberate Problem Solving with Large Language Models | NeurIPS 2023 |
| 2205.10625_least_to_most_prompting.pdf | 2205.10625 | Zhou et al. | 2022 | Least-to-Most Prompting Enables Complex Reasoning in Large Language Models | ICLR 2023 |
| 2210.11610_auto_cot.pdf | 2210.11610 | Huang et al. | 2022 | Large Language Models Can Self-Improve | EMNLP 2023 |

## Paper Summaries

### 1. Chain-of-Thought Prompting (Wei et al., 2022) — CORE PAPER
- **Relevance**: Directly introduces the CoT prompting technique central to our experiment
- **Key Finding**: CoT with PaLM 540B achieves 57% on GSM8K, vs 18% for standard prompting (PaLM 540B standard)
- **Method**: Few-shot prompting with step-by-step reasoning exemplars
- **Datasets**: GSM8K, SVAMP, AQuA, ASDiv, MultiArith, CommonsenseQA, StrategyQA, BIG-bench symbolic tasks
- **Key Result**: Emergent ability — CoT only helps for models >100B parameters

### 2. Zero-Shot Reasoners (Kojima et al., 2022) — CORE PAPER
- **Relevance**: Introduces zero-shot CoT ("Let's think step by step"), crucial baseline for our study
- **Key Finding**: Simple trigger phrase achieves 40.7% on GSM8K (up from 10.4% zero-shot), 78.7% on MultiArith (from 17.7%)
- **Method**: Zero-shot CoT with a single universal prompt template "Let's think step by step"
- **Models Tested**: InstructGPT (text-davinci-002), PaLM 540B
- **Datasets**: MultiArith, GSM8K, AQuA-RAT, SVAMP, CommonsenseQA, StrategyQA, Date Understanding, Tracking Shuffled Objects

### 3. Self-Consistency (Wang et al., 2022)
- **Relevance**: Major improvement over greedy CoT decoding, important baseline/extension for our study
- **Key Finding**: Self-consistency boosts CoT with +17.9% on GSM8K, +11.0% on SVAMP, +12.2% on AQuA
- **Method**: Sample multiple reasoning paths via temperature sampling, take majority vote answer
- **Datasets**: GSM8K, SVAMP, AQuA, StrategyQA, ARC-challenge

### 4. MATH Dataset (Hendrycks et al., 2021)
- **Relevance**: One of our two primary evaluation datasets; covers competition-level math
- **Key Finding**: Even very large models struggle (accuracy <10% for most models at time of publication)
- **Dataset**: 12,500 competition math problems across 7 subjects (Algebra, Geometry, Number Theory, etc.) at 5 difficulty levels
- **Subjects**: Algebra, Counting & Probability, Geometry, Intermediate Algebra, Number Theory, Prealgebra, Precalculus

### 5. GSM8K / Training Verifiers (Cobbe et al., 2021)
- **Relevance**: Introduces GSM8K, our primary evaluation dataset
- **Key Finding**: Grade school math is hard for LLMs; verifier-based approach substantially improves performance
- **Dataset**: 8,500 grade school math problems (7,473 train, 1,319 test), requiring 2-8 reasoning steps
- **Focus**: Multi-step arithmetic word problems requiring elementary operations

### 6. PAL: Program-Aided Language Models (Gao et al., 2022)
- **Relevance**: Important alternative to natural-language CoT; shows code as intermediate reasoning beats pure text CoT
- **Key Finding**: PAL surpasses PaLM-540B chain-of-thought by absolute 15% on GSM8K using only CODEX
- **Method**: LLM generates Python code as reasoning steps, Python interpreter executes
- **Datasets**: 13 tasks including GSM8K, BIG-Bench Hard, MATH

### 7. Tree of Thoughts (Yao et al., 2023)
- **Relevance**: Extends CoT to tree-based search; provides upper bound for prompting-based reasoning
- **Key Finding**: GPT-4 with ToT achieves 74% on Game of 24, vs. 4% with standard CoT
- **Method**: Maintains a tree of coherent reasoning "thoughts", uses LM to evaluate candidates, BFS/DFS search
- **Tasks**: Game of 24, Creative Writing, Mini Crosswords

### 8. Least-to-Most Prompting (Zhou et al., 2022)
- **Relevance**: Key extension of CoT for harder-than-exemplar generalization
- **Key Finding**: GPT-3 code-davinci-002 solves SCAN in any split (99%+) vs. 16% for CoT
- **Method**: Decompose problem into subproblems, solve sequentially with previous answers in context
- **Datasets**: SCAN (compositional generalization), AQuA (algebra), GSM8K (math word problems)

### 9. LLMs Can Self-Improve (Huang et al., 2022)
- **Relevance**: Shows CoT enables self-improvement without fine-tuning labels; methodology relevant to our study
- **Key Finding**: Self-generated CoT + fine-tuning improves PaLM 540B from 74.4% to 82.1% on GSM8K
- **Method**: Use CoT+self-consistency to generate high-confidence rationale-augmented answers, then fine-tune
- **Datasets**: GSM8K, DROP, OpenBookQA, NLI
