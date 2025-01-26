# Vision Language Models as Image Classifiers: An Experimental Study

This repository contains the code and data for my bachelor thesis on evaluating Vision Language Models (VLMs) in image classification tasks.
I explore the performance of various VLMs, including closed-source models like GPT-4V and open-source models like LLaVA and Qwen2-VL, across different classification complexities (20-way, 100-way, and 1000-way).

Key findings:
- In 1000-way classification, GPT-40 achieved an impressive 79% accuracy, comparable to the first ResNet.
- Open-source models performed well in 20-way and 100-way classifications but lagged in 1000-way classification compared to closed-source models.
- Scaling up the LLM does not impact the performance of image classification. For this pure CV problem the task performance is driven by architecture and correctly align of vision encoder and LLM during training.

Thesis: [link](https://github.com/the-future-dev/MM_LLMs-vs-CV/blob/master/VLMs%20as%20Image%20Classifiers.pdf)

Feel free to reach out if you have any questions
