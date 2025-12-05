# A Forensic Linguistic Dataset for Offensive Content Detection in Low-Resource Language: Setswana
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17824911.svg)](https://doi.org/10.5281/zenodo.17824911)
[![HF Dataset](https://img.shields.io/badge/HuggingFace-dataset-%23ffcc00)](https://huggingface.co/datasets/mopatik/setswana-offensive-977)
[![HF Models](https://img.shields.io/badge/HuggingFace-models-%23ffcc00)](https://huggingface.co/mopatik)
- Corpus: 977 items (477 offensive; 500 non-offensive)
- Splits: 80/20 holdout (tag-free), 5-fold CV on 80%
- Models: PuoBERTa (no triggers), Afro-XLM-R (no triggers)
- Docs: see data_statement/DATASTATEMENT.md
# Abstract

This paper introduce a monolingual Setswana dataset (n = 977) for offensive language detection, curated for digital forensic use. Texts span social media and civic discourse, complemented by lexicographic sources, and include span-level semantic trigger annotations. Double-coding achieved Cohen’s kappa  ($\kappa$) = 0.86. The corpus is split 80/20 into a training set and an untouched, trigger free (tag-free) holdout. Model selection uses five-fold stratified cross-validation on the 80\% split, with final evaluation on the 20\% holdout. Classical machine-learning baselines, term-frequency–inverse document frequency (TF–IDF) with Naïve Bayes, Logistic Regression, and Linear Support Vector Machine (SVM), are benchmarked against  transformers, under a no-trigger training setting. On the no trigger (tag-free) holdout, classical models reach Macro-F1 = 0.80–0.87 (e.g., Naïve Bayes: Accuracy 0.86, Macro-F1 0.87), while transformers are slightly higher. Bootstrap 95\% confidence intervals for Macro-F1 overlap, and a paired Wilcoxon signed-rank test is non-significant (p = 0.625) with small/negligible effect sizes, indicating no statistically reliable difference at corpus scale. In contrast, training with trigger markup but testing tag-free degrades performance (PuoBERTa Accuracy 0.642, Macro-F1 0.557), evidencing supervision leakage.
			
To support forensic traceability, Local Interpretable Model-agnostic Explanations (LIME) and Stabilized LIME (S-LIME) are applied. Attributions align with annotated trigger spans, remain stable under across perturbations. Counterfactual edits reveal when predictions flip. We discuss admissibility considerations and limitations (dataset size; dialectal coverage) and outline future work on dialectal scaling, knowledge distillation, attention supervision, and comparisons with other large language models (LLMs). The dataset and reproducible code (GitHub/Hugging Face) will be released to facilitate low-resource forensic natural language processing (NLP).

---


This repository contains code, configuration, seeds, and reproducibility artefacts for the paper:

> **A Forensic Linguistic Dataset for Offensive Content Detection in Low-Resource Language: Setswana**  
> (Submitted to Forensic Science International: Reports)

It includes:
- A monolingual Setswana corpus for offensive language detection (977 instances).
- Training/evaluation code for classical baselines (TF–IDF + NB/LR/SVM) and transformer(PuoBERTa, Afro-XLM-R).
- Tag-free **held-out evaluation**, **counterfactual testing**, and **explainability** (LIME/S-LIME).
- Seeds, exact split indices, and checksums for full reproducibility.

---





