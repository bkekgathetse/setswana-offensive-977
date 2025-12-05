# Setswana Offensive Language Dataset (977)
- Corpus: 977 items (477 offensive; 500 non-offensive)
- Splits: 80/20 holdout (tag-free), 5-fold CV on 80%
- Models: PuoBERTa (no triggers), Afro-XLM-R (no triggers)
- Docs: see data_statement/DATASTATEMENT.md

# Developing Monolingual Setswana Datasets for Offensive Content Detection

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17824737.svg)](https://doi.org/10.5281/zenodo.17824737))
[![HF Dataset](https://img.shields.io/badge/HuggingFace-dataset-%23ffcc00)](https://huggingface.co/datasets/mopatik/setswana-offensive-977)
[![HF Models](https://img.shields.io/badge/HuggingFace-models-%23ffcc00)](https://huggingface.co/mopatik)


This repository contains code, configuration, seeds, and reproducibility artefacts for the paper:

> **Developing Monolingual Setswana Datasets for Offensive Content Detection**  
> (Submitted to Forensic Science International: Reports)

It includes:
- A monolingual Setswana corpus for offensive language detection (977 instances).
- Training/evaluation code for classical baselines (TF–IDF + NB/LR/SVM) and transformer(PuoBERTa, Afro-XLM-R).
- Tag-free **held-out evaluation**, **counterfactual testing**, and **explainability** (LIME/S-LIME).
- Seeds, exact split indices, and checksums for full reproducibility.

---

## Repository structure



