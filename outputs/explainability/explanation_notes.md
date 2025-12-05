# Explainability Notes (LIME & Counterfactual Analysis)

This document summarises the methodology, rationale, and interpretation guidelines for the LIME-based explainability experiments conducted on the fine-tuned Setswana offensive-language detection models. All examples shown in this directory are *sanitised* by masking offensive tokens with `***` to ensure safe public release.

---

## 1. Purpose of the Explainability Analysis

The explainability component supports:
- transparency of model behaviour,
- interpretability for forensic workflows,
- validation of semantic-trigger assumptions,
- inspection of individual predictions,
- and replication by other researchers.

LIME (Local Interpretable Model-Agnostic Explanations) was used to compute *token-level contributions* for selected instances in the holdout test set.

Counterfactual analysis was used to evaluate whether replacing or neutralising trigger-like terms changes the model's prediction.

---

## 2. Methodology Overview

### 2.1 LIME Setup
- **Explainer:** `LimeTextExplainer`
- **Class names:** `["Non-offensive", "Offensive"]`
- **Top features:** 8–12 per explanation
- **Tokenisation:** HuggingFace WordPiece/BPE tokens
- **Sampling:** 500–2000 perturbed samples per instance
- **Model function:** `predict_proba()` wrapper calling the fine-tuned transformer

Each LIME explanation highlights tokens in the instance with *positive* or *negative* contribution toward the "Offensive" class.

### 2.2 Sanitisation
To protect users and comply with ethical distribution of offensive-language datasets:
- Raw offensive text is **not** included in this directory.
- Offensive tokens in examples are masked as:  
  `O *** tota` or `Ga o na ***`
- No identifiers, metadata, or platform information is included.
- Only contribution plots and masked text samples are provided.

---

## 3. Counterfactual Protocol

A counterfactual instance was created by applying **minimal edits** to the original sentence:

- Replace an offensive trigger word with a neutral synonym  
- Or remove a trigger entirely  
- Or substitute a benign Setswana term of similar grammatical role

Each original–counterfactual pair includes:
- Masked text (no raw offensive content)
- Whether the prediction **Flipped (Yes/No)**
- LIME-dominant tokens before/after the edit
- Probability shift for the offensive class

A flip indicates that the model was sensitive to the removed/changed trigger.  
No flip indicates contextual robustness.

---

## 4. How to Interpret LIME Outputs

### 4.1 Positive Weights
Tokens with **positive contribution** (typically shown in red) increase the probability of the *Offensive* label.

Common patterns include:
- Trigger-like words (masked as `***`)
- Intensifiers
- Surrounding context tokens influencing sentiment

### 4.2 Negative Weights
Tokens with **negative contribution** (typically in green) push prediction toward *Non-offensive*.

These may include:
- Neutral verbs
- Polite structures
- Discourse markers such as “ga”, “mme”, “jalo”

### 4.3 Limitations
- Subword tokenisation may split Setswana words unpredictably.
- LIME approximates the local neighbourhood and is inherently unstable.
- Token masking may reduce interpretability (necessary for safety).
- Colloquial or sarcastic usage may not align with feature contributions.

---

## 5. Files Included in This Directory

### `lime_instance.html`
Interactive HTML rendering of LIME explanations for selected test instances.

### `token_contribution_plot.png`
Combined summary of token-level contributions for selected samples.

### `explanation_notes.md`
(You are reading this file.)

---

## 6. Reproduction Instructions

To regenerate the files:
1. Load the fine-tuned model from HuggingFace.
2. Use the `explainability_LIME_setswana.ipynb` notebook (in `/notebooks/`).
3. Provide a list of test samples (masked or synthetic).
4. Save outputs into `outputs/explainability/`.

Dependencies:
- `lime`
- `transformers`
- `torch`
- `matplotlib`
- `pandas`

---

## 7. Ethical Precautions

- **No harmful language** is included raw; all content is masked.
- Explanations must be interpreted **by trained analysts**, not for automated decision making.
- Counterfactuals illustrate model behaviour, not legal or social judgements.
- No real user data or platform-identifiable information is included.

---

## 8. Citation
If you use these explainability assets, please reference the associated paper:

*Kekgathetse, B. (2025). Fine-Tuning Transformer Models for Semantic Detection of Cybercrime in Setswana.*

---


