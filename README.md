# RAGLens---Enterprise-RAG-Evaluation

# Sample Wikipedia Articles (500-doc subset)

This repository contains a **sample** of 500 English Wikipedia articles extracted from the Wikimedia dump (enwiki_namespace_0_*.jsonl). The sample was created for use in ML/NLP experiments and educational projects.

## Source & License
- Source: https://www.kaggle.com/datasets/wikimedia-foundation/wikipedia-structured-contents
- Original license: **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**.
  See: https://creativecommons.org/licenses/by-sa/4.0/ and https://dumps.wikimedia.org/legal.html

## What is included
- `sample_500.jsonl` — sampled records (fields: id, title, text_snippet, categories).
- `notebooks/` — code used to sample and preprocess the dataset.

## Attribution 
This dataset contains content from Wikimedia (https://www.wikipedia.org). When redistributing or using portions of Wikipedia text, we attribute the original source as required by CC BY-SA 4.0. See the license for details.


## Results and Visualization

<img width="700" height="200" alt="chunks" src="https://github.com/user-attachments/assets/30469083-129f-4356-aa80-5ed77ee28820" />


Chunking Summary:
Strategy	Outcome

tok_300	Over-chunking → unnecessary splitting & added redundancy

tok_500	Best tradeoff between coherence & chunking

tok_1000	Chunking not applied at all


<img width="800" height="700" alt="image" src="https://github.com/user-attachments/assets/95ec440f-b028-4380-8000-dc97d3400c10" />


The blue color depicts the distinct topics in the text and this segmentation is good for retrieval.

The green color shows the chunks of text that have similar meaning.
