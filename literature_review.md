# Literature Review: Chain-of-Thought Prompting for Mathematical Reasoning

**Project**: Evaluating Chain-of-Thought Prompting Effectiveness Across Mathematical Reasoning Tasks  
**Date**: 2026-06-22  
**Hypothesis**: CoT prompting improves LLM performance on multi-step mathematical reasoning by 15-30% compared to direct prompting, with larger gains on harder problems; effect consistent across model families but varying by problem complexity.

---

## 1. Research Area Overview

Chain-of-thought (CoT) prompting has emerged as one of the most impactful techniques in large language model (LLM) research since 2022. The core idea is simple: rather than asking a model to produce a final answer directly, the prompt includes intermediate reasoning steps that guide the model through multi-step problem solving. This mirrors how humans solve complex problems — by breaking them down into tractable subgoals and working through them sequentially.

### Historical Timeline

- **Pre-2022**: LLMs struggle on arithmetic and reasoning tasks; scaling alone insufficient
- **Jan 2022**: Wei et al. (arXiv:2201.11903) formally introduce CoT prompting; show massive gains emerge at ~100B+ parameter scale
- **May 2022**: Kojima et al. (arXiv:2205.11916) discover zero-shot CoT ("Let's think step by step") — no exemplars needed
- **May 2022**: Zhou et al. (arXiv:2205.10625) introduce Least-to-Most prompting for harder-than-exemplar generalization
- **Mar 2022**: Wang et al. (arXiv:2203.11171) propose Self-Consistency — sampling multiple reasoning paths improves accuracy further
- **Oct 2022**: Huang et al. (arXiv:2210.11610) show LLMs can self-improve using CoT-generated rationales
- **Nov 2022**: Gao et al. (arXiv:2211.10435) introduce PAL — using code instead of natural language as the reasoning chain
- **May 2023**: Yao et al. (arXiv:2305.10601) propose Tree of Thoughts — generalizing CoT to tree-based search

### Current State (2026)
CoT prompting is now considered a standard technique in LLM deployment. Modern frontier models (GPT-4, Claude 3+, Gemini Ultra) incorporate CoT reasoning by default in many settings. The field has moved toward: (1) automated CoT generation, (2) code-integrated reasoning (PAL-style), (3) process reward models to verify reasoning steps, and (4) inference-time scaling (repeated sampling).

---

## 2. Key Papers

### Paper 1: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
**Citation**: Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., Zhou, D. (2022). NeurIPS 2022. arXiv:2201.11903

**Contribution**: 
Introduces chain-of-thought prompting as a formal method where few-shot exemplars include intermediate reasoning steps. Demonstrates that this emergent capability scales: CoT only significantly helps models with ~100B+ parameters.

**Methodology**:
- Few-shot prompting with 8 question-answer pairs where answers include step-by-step reasoning
- Three test models: GPT-3 (175B), PaLM (540B), LaMDA (137B)
- Compared: standard prompting vs. CoT prompting

**Key Results**:
| Dataset | Model | Standard Prompting | CoT Prompting | Gain |
|---------|-------|-------------------|---------------|------|
| GSM8K | PaLM 540B | 18% | 57% | +39pp |
| GSM8K | GPT-3 175B | ~16% | 46% | ~+30pp |
| SVAMP | PaLM 540B | ~74% | ~88% | ~+14pp |
| AQuA | PaLM 540B | ~23% | ~35% | ~+12pp |

**Relevance to our study**: Directly motivates our hypothesis. Establishes that 15-30% gains are plausible for GSM8K-level tasks; larger gains (~39pp) observed for hardest benchmarks at largest scale.

**Datasets used**: GSM8K, SVAMP, AQuA, ASDiv, MultiArith, CommonsenseQA, StrategyQA, Last Letter, Coin Flip, Date Understanding, Tracking Shuffled Objects

---

### Paper 2: Large Language Models are Zero-Shot Reasoners
**Citation**: Kojima, T., Gu, S.S., Reid, M., Matsuo, Y., Iwasawa, Y. (2022). NeurIPS 2022. arXiv:2205.11916

**Contribution**:
Discovers that the simple prompt addition "Let's think step by step" before answers dramatically improves LLM reasoning — without any hand-crafted few-shot examples. Establishes zero-shot CoT as the strongest zero-shot baseline.

**Methodology**:
- Two-stage prompting: (1) trigger "Let's think step by step" to elicit reasoning; (2) extract answer from generated reasoning
- Models: InstructGPT (text-davinci-002, ~175B), PaLM 540B
- Compared: zero-shot direct vs. zero-shot CoT

**Key Results**:
| Dataset | Zero-Shot Direct | Zero-Shot CoT | Gain |
|---------|-----------------|---------------|------|
| MultiArith | 17.7% | 78.7% | +61pp |
| GSM8K | 10.4% | 40.7% | +30.3pp |
| AQuA-RAT | 22.4% | 33.5% | +11.1pp |
| SVAMP | 58.8% | 62.1% | +3.3pp |

**Relevance to our study**: Establishes the zero-shot CoT baseline for our experiment; shows gains vary significantly by task difficulty and type.

---

### Paper 3: Self-Consistency Improves Chain of Thought Reasoning in Language Models
**Citation**: Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., Zhou, D. (2022). ICLR 2023. arXiv:2203.11171

**Contribution**:
Introduces self-consistency: instead of greedy decoding of CoT, sample multiple diverse reasoning paths and take the majority vote answer. The intuition is that correct answers are reached by many different valid reasoning paths, while incorrect answers are more idiosyncratic.

**Methodology**:
- Sample 40 reasoning chains (temperature > 0)
- Marginalize over sampled paths by majority voting on final answers
- Applied on top of any CoT method

**Key Results**:
| Dataset | CoT (greedy) | CoT + Self-Consistency | Gain |
|---------|-------------|----------------------|------|
| GSM8K | ~56% | ~74% | +17.9pp |
| SVAMP | ~79% | ~90% | +11pp |
| AQuA | ~35% | ~47% | +12.2pp |
| StrategyQA | ~73% | ~79% | +6.4pp |

**Relevance to our study**: Self-consistency is an important extension baseline. If our experiment includes self-consistency, we should expect an additional 10-18pp boost on top of standard CoT. Establishes ceiling for greedy CoT.

---

### Paper 4: Measuring Mathematical Problem Solving With the MATH Dataset
**Citation**: Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart, S., Tang, E., Song, D., Steinhardt, J. (2021). NeurIPS 2021. arXiv:2103.03874

**Contribution**:
Introduces the MATH dataset — 12,500 competition math problems (AMC, AIME, etc.) across 7 subjects and 5 difficulty levels. Establishes that scaling alone cannot solve competition math.

**Methodology**:
- Evaluated multiple models (GPT-2, GPT-3, etc.) on MATH
- Baseline: few-shot prompting with step-by-step solutions
- Also contributed AMPS pretraining dataset (23GB of Khan Academy + Mathematica problems)

**Key Results**:
- Even best models at publication scored <10% on MATH
- Performance stratified clearly by difficulty level: Level 1 ~25-40%, Level 5 <5%
- Mathematical problem solving requires understanding beyond pattern matching

**Dataset structure**:
- 7 subjects: Algebra, Counting & Probability, Geometry, Intermediate Algebra, Number Theory, Prealgebra, Precalculus
- 5 difficulty levels: Level 1 (easiest) to Level 5 (hardest)
- Answers in LaTeX \\boxed{} format

**Relevance to our study**: Primary dataset for testing difficulty-stratified hypothesis. The 5 difficulty levels provide natural stratification to test if CoT gains increase with problem difficulty.

---

### Paper 5: Training Verifiers to Solve Math Word Problems (GSM8K)
**Citation**: Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C., Schulman, J. (2021). arXiv:2110.14168

**Contribution**:
Introduces GSM8K — 8,500 grade school math word problems. Proposes using verifiers (trained outcome reward models) to select correct solutions from generated candidates.

**Methodology**:
- Human-written problems requiring 2-8 steps
- Verifier (ORM) trained to score generated solutions
- Evaluated GPT-3 (6B and 175B) variants

**Key Results**:
- GPT-3 175B fine-tuned: ~33% on GSM8K
- GPT-3 175B + verifier: ~55% on GSM8K (prior SOTA at paper publication)
- PaLM 540B + CoT: 57% (first to exceed verifier approach without fine-tuning)

**Dataset details**:
- Train: 7,473 problems
- Test: 1,319 problems
- Solutions use `####` to mark final answer
- Calculator annotations: `<<2+3=5>>`

**Relevance to our study**: Defines our primary evaluation benchmark and establishes the historical baseline for direct prompting vs. CoT comparisons.

---

### Paper 6: PAL: Program-Aided Language Models
**Citation**: Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang, Y., Callan, J., Neubig, G. (2022). ICML 2023. arXiv:2211.10435

**Contribution**:
Introduces PAL — using Python code as the intermediate reasoning "chain" instead of natural language. The LLM generates executable code; a Python interpreter handles computation. Eliminates arithmetic errors in CoT.

**Methodology**:
- LLM (Codex) prompted to generate Python programs given problem description
- Python interpreter executes code to obtain the answer
- Evaluated on 13 tasks across mathematical, symbolic, and algorithmic reasoning

**Key Results**:
- PAL with Codex surpasses PaLM-540B CoT by absolute 15% on GSM8K
- Eliminates a major source of CoT failures: arithmetic errors in text generation

**Relevance to our study**: Important alternative paradigm. If our experiment includes code-capable models, PAL represents an upper bound for code-based CoT. Demonstrates that text-CoT arithmetic errors are a significant limitation.

---

### Paper 7: Tree of Thoughts: Deliberate Problem Solving with Large Language Models
**Citation**: Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T.L., Cao, Y., Narasimhan, K. (2023). NeurIPS 2023. arXiv:2305.10601

**Contribution**:
Generalizes CoT from a single chain to a tree of "thoughts" (coherent text units). Uses BFS or DFS with LM-based evaluation to explore multiple reasoning paths and backtrack.

**Methodology**:
- Decompose problems into thoughts (intermediate reasoning units)
- Use LLM to generate and evaluate candidate thoughts
- BFS/DFS search over thought tree
- Applied to: Game of 24, Creative Writing, Mini Crosswords

**Key Results**:
- Game of 24: GPT-4 standard CoT: 4%; GPT-4 ToT: 74%
- Shows significant improvement on problems requiring exploration and backtracking

**Relevance to our study**: Establishes the theoretical upper bound for reasoning quality. ToT is expensive (many API calls) but motivates our hypothesis that harder problems benefit more from structured reasoning.

---

### Paper 8: Least-to-Most Prompting Enables Complex Reasoning in Large Language Models
**Citation**: Zhou, D., Scharli, N., Hou, L., Wei, J., Scales, N., Wang, X., Schuurmans, D., Cui, C., Bousquet, O., Le, Q., Chi, E. (2022). ICLR 2023. arXiv:2205.10625

**Contribution**:
Introduces least-to-most prompting: (1) decompose a problem into simpler subproblems; (2) solve them sequentially, using previous answers as context. Enables generalization to problems harder than training exemplars.

**Methodology**:
- Stage 1: "To solve [problem], we need to first solve:" — decompose into subproblems
- Stage 2: Solve each subproblem with previous solutions in context
- Evaluated on SCAN (compositional generalization), AQuA (math), GSM8K

**Key Results**:
- SCAN with GPT-3 code-davinci-002: CoT 16% vs. Least-to-Most 99%+
- AQuA: 60.1% (least-to-most) vs 51.9% (CoT 8-shot)
- GSM8K: comparable to standard CoT

**Relevance to our study**: Motivates our difficulty-stratification hypothesis — if harder problems require decomposition, least-to-most should help more on hard problems. Provides an alternative CoT variant to include as a condition.

---

### Paper 9: Large Language Models Can Self-Improve
**Citation**: Huang, J., Gu, S.S., Hou, L., Wu, Y., Wang, X., Yu, H., Han, J. (2022). EMNLP 2023. arXiv:2210.11610

**Contribution**:
Shows that LLMs can self-improve without labeled data by generating high-confidence CoT rationale-augmented answers and fine-tuning on them. Uses CoT + self-consistency to filter for reliable self-generated training data.

**Methodology**:
- Generate 32 diverse CoT solutions per problem (self-consistency)
- Filter for "high-confidence" answers (strong majority agreement)
- Fine-tune on self-generated rationale-answer pairs

**Key Results**:
- PaLM 540B: 74.4% → 82.1% on GSM8K after self-improvement
- Competitive with models trained on human rationales

**Relevance to our study**: Demonstrates that CoT quality scales with generation diversity; methodologically relevant for understanding the ceiling of CoT performance.

---

## 3. Common Methodologies

### Standard Few-Shot CoT (Wei et al., 2022)
- Provide k examples (typically k=8) where each answer includes step-by-step reasoning
- Use greedy decoding
- **Pros**: Reliable, well-studied | **Cons**: Requires hand-crafted examples

### Zero-Shot CoT (Kojima et al., 2022)
- Append "Let's think step by step" before generating the answer
- Two-pass: generate reasoning, then extract answer
- **Pros**: No examples needed, universal | **Cons**: Lower accuracy than few-shot CoT

### Self-Consistency (Wang et al., 2022)
- Sample N reasoning paths (N=40 typical), majority vote
- Works with any CoT variant
- **Pros**: +10-18pp improvement | **Cons**: N× API calls (expensive)

### Least-to-Most Prompting (Zhou et al., 2022)
- Explicitly decompose then sequentially solve
- **Pros**: Better generalization to harder problems | **Cons**: More complex prompting

### PAL / Code-Based CoT (Gao et al., 2022)
- Generate Python code instead of natural language reasoning
- **Pros**: Eliminates arithmetic errors | **Cons**: Requires code-capable model

### Tree of Thoughts (Yao et al., 2023)
- Tree-based search with BFS/DFS
- **Pros**: Very high accuracy on hard problems | **Cons**: Extremely expensive (many LLM calls)

---

## 4. Standard Baselines

For our experiment, the following baselines should be established:

| Baseline | Description | Expected Performance (GSM8K) |
|----------|-------------|------------------------------|
| Direct prompting (0-shot) | Ask model to answer directly, no examples | ~10-30% |
| Direct prompting (few-shot) | 8 examples without reasoning | ~30-40% |
| Zero-shot CoT | "Let's think step by step" trigger | ~40-60% |
| Few-shot CoT | 8 examples with reasoning steps | ~55-80% |
| Self-Consistency CoT | Few-shot CoT + majority voting (40 samples) | ~74-90% |

*Ranges reflect variation across model sizes and families. Modern models (GPT-4, Claude 3, Gemini Ultra) score significantly higher.*

---

## 5. Evaluation Metrics

### Primary Metric
- **Exact Match Accuracy**: Percentage of problems where extracted final answer matches ground truth
- For GSM8K: extract number after `####`
- For MATH: extract content of `\\boxed{...}`

### Secondary Metrics
- **Accuracy by difficulty level** (MATH Level 1-5)
- **Accuracy by problem category** (Algebra, Geometry, etc.)
- **Step-level accuracy**: Whether intermediate reasoning steps are correct (requires annotation)
- **Token efficiency**: Average tokens generated per problem

### Answer Normalization
Mathematical answers require careful normalization:
- Equivalent forms: `1/2`, `0.5`, `50%`, `\frac{1}{2}` all represent the same value
- Symbolic equivalence checking: `x^2 + 2x + 1` = `(x+1)^2`
- Common libraries: `sympy` for symbolic comparison, custom regex for number extraction

---

## 6. Datasets in the Literature

| Dataset | Size | Task | Difficulty | Primary Papers |
|---------|------|------|------------|----------------|
| GSM8K | 8,500 (7.5K/1K) | Grade school math word problems | Medium | Cobbe 2021, Wei 2022, Kojima 2022 |
| MATH | 12,500 (7.5K/5K) | Competition math (AMC, AIME) | Hard (5 levels) | Hendrycks 2021 |
| MultiArith | 600 | Multi-step arithmetic | Easy-Medium | Wei 2022, Kojima 2022 |
| AQuA-RAT | ~100K | Algebraic word problems (MCQ) | Medium | Wei 2022, Wang 2022 |
| SVAMP | 1,000 | Math word problems | Medium | Wei 2022, Wang 2022 |
| ASDiv | 2,305 | Arithmetic story problems | Easy-Medium | Wei 2022 |
| CommonsenseQA | 12K | Commonsense reasoning (MCQ) | Medium | Wei 2022, Wang 2022 |
| StrategyQA | 2,780 | Strategic yes/no questions | Medium | Wei 2022, Wang 2022 |
| SCAN | ~8K | Compositional generalization | Variable | Zhou 2022 |
| BIG-bench Hard | 23 tasks | Hard reasoning tasks | Hard | Gao 2022 |

**For our experiment**: Focus on GSM8K (well-studied, easy to evaluate) and MATH (difficulty stratification).

---

## 7. Gaps and Opportunities

### Gaps in Current Literature

1. **Cross-model family comparison**: Most papers evaluate on 1-2 model families. Systematic comparison across GPT-4, Claude, and Gemini families is underexplored.

2. **Problem complexity stratification**: Wei et al. show emergent effects at model scale, but within-dataset difficulty stratification (e.g., by number of steps, arithmetic complexity) is less systematically studied.

3. **Consistency of gains**: Do the 15-57pp gains reported depend on specific model versions? As models improve, the relative gain of CoT may shrink (ceiling effects).

4. **Budget-optimal prompting**: At fixed cost, when is zero-shot CoT sufficient vs. few-shot CoT? When is self-consistency worth the 40× cost?

5. **Failure mode analysis**: What types of problems does CoT fail on that direct prompting also fails on? When does CoT help and when doesn't it?

### Research Opportunities for Our Experiment

1. **Cross-model comparison** (GPT-4, Claude 3, Gemini Pro): Directly tests whether CoT gains are model-family-agnostic.

2. **Difficulty-stratified analysis**: MATH Level 1-5 provides a natural experiment — if our hypothesis is correct, CoT gain should increase monotonically with level.

3. **Cost-accuracy tradeoff**: Compare direct vs. zero-shot CoT vs. few-shot CoT at fixed API budget.

4. **Step count vs. accuracy**: Within GSM8K, problems requiring more steps should benefit more from CoT.

---

## 8. Recommendations for Our Experiment

### Experimental Design

**Conditions** (recommended minimum viable set):
1. Direct prompting (zero-shot): Model answers without reasoning
2. Zero-shot CoT: Add "Let's think step by step"
3. Few-shot CoT (8 examples): Include reasoning chains in exemplars

**Optional** (if budget allows):
4. Self-Consistency (40 samples of zero-shot CoT): Tests upper bound
5. Least-to-Most: Tests harder problem generalization

**Datasets**:
- GSM8K test set: 1,319 problems (primary benchmark)
- MATH test set: stratified sample of 50 problems per difficulty level (5 × 50 = 250 problems)

**Models** (if budget allows three):
- GPT-4 (or gpt-4o)
- Claude 3.5 Sonnet (or claude-3-5-sonnet)
- Gemini 1.5 Pro (or gemini-2.0-flash)

### Cost Estimation (GSM8K, 1,319 problems)
- Avg tokens per problem: ~300 input + ~200 output = 500 tokens
- Direct prompting: 1,319 × 500 = 659,500 tokens ≈ $0.66 (gpt-4o @ $1/1M tokens)
- Zero-shot CoT: 1,319 × 700 = 923,300 tokens ≈ $0.92
- Few-shot CoT (8 examples adds ~2K tokens): 1,319 × 2,800 = ~3.7M tokens ≈ $3.70
- Total for 3 conditions × 3 models: ~$15-20 (well within $50 budget)

### Success Criteria
- Primary: Does CoT (any variant) improve GSM8K accuracy by ≥15%? (Hypothesis confirmation threshold)
- Secondary: Is the improvement larger on MATH Level 4-5 than Level 1-2?
- Tertiary: Is the improvement consistent (within ±5%) across GPT-4, Claude, and Gemini?

### Implementation Notes
1. Use the `openai/gsm8k` dataset from HuggingFace (already downloaded)
2. Use `EleutherAI/hendrycks_math` for MATH (stratified sampling)
3. Answer extraction: `answer.split("####")[-1].strip()` for GSM8K
4. For MATH: regex `r'\\boxed\{([^}]+)\}'` to extract answer
5. Consider using `sympy` for symbolic equivalence checking on MATH answers
6. Log all API responses for reproducibility

### Risk Mitigation
- **Risk**: API rate limits during long runs → Solution: Add delays, use batch API where available
- **Risk**: Context window exceeded with 8-shot examples → Solution: Select shorter examples or use 4-shot
- **Risk**: MATH answers need normalization → Solution: Use established normalization code from Hendrycks repo
- **Risk**: Models may not follow format → Solution: Add explicit format instructions ("Final answer: ####")
