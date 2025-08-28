# Hierarchical Text Classification for Toxic Conversations

This repository contains the code for a project focused on classifying toxic relational dynamics in conversations. The primary objective is to address the challenges of multi-class, single-label text classification in a domain where class definitions are nuanced and linguistically similar.

-----

## The Task

The main goal is to assign a single label to a given conversation, identifying the specific type of toxic dynamic it represents. This is framed as a **multi-class, single-label classification problem**.

-----

## Semantic Overlap

A key challenge in this domain is the high degree of **semantic overlap** between classes. Different categories of toxic behavior often share similar vocabulary and phrasing, which makes it difficult for standard classification models to distinguish between them effectively. This project explores a hierarchical architecture specifically designed to mitigate this issue.

-----

## Repository Structure

The project is organized into a series of Jupyter notebooks that document the experimental process:

  * `01_data_exploration.ipynb`: Initial analysis of the dataset and class distributions.
  * `02_LR_Multiclass_Classification_baseline_*.ipynb`: Baseline models using Logistic Regression.
  * `03_SVM_Multiclass_Classification_baseline_*.ipynb`: Baseline models using Support Vector Machines (SVM).
  * `04_LLM_*.ipynb`: Baseline models using a fine-tuned Large Language Model (LLM).
  * `05_Hierarchical_Classification.ipynb`: Implementation of the proposed hierarchical classification model.

-----

## Methodology Overview

1.  **Baseline Analysis**: Standard "flat" classification models (Logistic Regression, SVM, LLM) are implemented to establish performance benchmarks. Both full conversations and individual turns are used as input strategies.
2.  **Hierarchical Framework**: A two-stage classification model is proposed to address the class overlap. A "generalist" model first sorts conversations into broad categories, after which "specialist" models perform fine-grained classification within each category.
