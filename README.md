# A Forensic Linguistic Dataset for Offensive Content Detection in Low-Resource Language: Setswana
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17824911.svg)](https://doi.org/10.5281/zenodo.17824911)
[![HF Dataset](https://img.shields.io/badge/HuggingFace-dataset-%23ffcc00)](https://huggingface.co/datasets/mopatik/setswana-offensive-977)
[![HF Models](https://img.shields.io/badge/HuggingFace-models-%23ffcc00)](https://huggingface.co/mopatik)
- Corpus: 977 items (477 offensive; 500 non-offensive)
- Splits: 80/20 holdout (tag-free), 5-fold CV on 80%
- Models: PuoBERTa (no triggers), Afro-XLM-R (no triggers)
- Docs: see data_statement/DATASTATEMENT.md
# Abstract

This paper presents a monolingual Setswana dataset for offensive language detection, developed for digital forensic applications. The dataset comprises texts drawn from social media, civic discourse, and lexicographic sources, and includes span-level semantic trigger annotations. Double coding yielded strong inter-annotator agreement, with a Cohen’s kappa of 0.86. The corpus was divided in an 80:20 ratio into a training set and an untouched, semantic-trigger-free (tag-free) holdout set. Model selection was conducted using five-fold stratified cross-validation on the training split, followed by final evaluation on the holdout set. Classical machine-learning baselines, including TF--IDF with Naïve Bayes, Logistic Regression, and a Linear Support Vector Machine, were benchmarked against transformer models under tag-free training. On the tag-free holdout set, the classical models achieved macro F1 Scores of 0.80-0.87, while the transformers performed only marginally better. However, the 95\% bootstrap confidence intervals for macro F1 overlapped, and the paired Wilcoxon signed-rank test was non-significant ($p = 0.625$), with negligible effect sizes, indicating no statistically reliable difference at this corpus scale. 
			
In contrast, training with semantic trigger tags and testing on tag-free data reduced transformer performance, suggesting supervision leakage. For forensic traceability, Local Interpretable Model-agnostic Explanations (LIME) and Stabilized LIME (S-LIME) were applied. Their attributions aligned with annotated trigger spans and remained stable across perturbations, while counterfactual edits identified the conditions under which predictions changed. Limitations include dataset size and dialectal coverage. The dataset and reproducible code have been released to support low-resource forensic natural language processing.

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





