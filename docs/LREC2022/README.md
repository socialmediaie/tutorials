---
layout: default
title: "Information extraction from social media:  A hands-on tutorial on tasks, data, and open source tools"
description: "LREC 2022 Tutorial. June 20th, 2022"
permalink: /LREC2022/
---

# LREC 2022 Tutorial

[Tutorial Home](../)

* **Date:** June 20, 2022
* **Time:** afternoon session
* **Venue:** TBD
* **Slides:** 
* **Contact:** Shubhanshu Mishra at [https://twitter.com/TheShubhanshu](https://twitter.com/TheShubhanshu)


## Tutorial description

In this hands-on tutorial (details and material at: https://socialmediaie.github.io/tutorials/), we introduce the participants to working with social media data, which are an example of Digital Social Trace Data (DSTD). The DSTD abstraction allows us to model social media data with rich information associated with social media text, such as authors, topics, and time stamps. We introduce the participants to several Python-based, open-source tools for performing Information Extraction (IE) on social media data. Furthermore, the participants will be familiarized with a catalogue of more than 30 publicly available social media corpora for various IE tasks such as named entity recognition (NER), part of speech (POS) tagging, chunking, super sense tagging, entity linking, sentiment classification, and hate speech identification. We will also show how these approaches can be expanded to word in a multi-lingual setting. Finally, the participants will be introduced to the following applications of extracted information:

*	combining network analysis and text-based signals to rank accounts, and 
*	correlation between sentiment and user-level attributes in existing corpora. 
The tutorial aims to serve the following use cases for social media researchers:
*	high accuracy IE on social media text via multi-task and semi-supervised learning, including the recent transformer-based tools which work across languages, 
*	rapid annotation of new data for text classification via active human-in-the-loop learning, 
*	temporal visualization of the communication structure in social media corpora via social communication temporal graph visualization technique, and
*	detecting and prioritizing needs during crisis events (e.g, COVID19). 
*	Furthermore, the participants will be familiarized with a catalogue of more than 30 publicly available social media corpora for various IE tasks, e.g., named entity recognition (NER), part of speech (POS) tagging, chunking, super sense tagging, entity linking, sentiment classification, and hate speech identification. 


This will be a **3-hours**  long tutorial session using Python based, open source tools. The tutorial will be structured as follows:


###	Setup and Introduction (1 hr)

*	Introducing the differences between social media data versus newswire and academic data, 
*	Digital Social Trace Data abstraction for social media data, 
*	Introduction to information extraction tasks for social media data, e.g., sequence tagging (named entity, part of speech tagging, chunking, and super-sense tagging), and text classification (sentiment prediction, sarcasm detection, and abusive content detection)

###	Applications of information extraction (1 hr): 
*	Indexing social media corpora in database, 
*	Network construction from text corpora, 
*	Visualizing temporal trends in social media corpora using social communication temporal graphs, 
*	Aggregating text-based signals at the user-level, 
*	Improving text classification using user-level attributes, 
*	Analyzing social debate using sentiment and political identity signals otherwise, 
*	Detecting and Prioritizing Needs during Crisis Events (e.g., COVID19), 
*	Mining and Analyzing Public Opinion Related to COVID-19, and 
*	Detecting COVID-19 Misinformation in Videos on YouTube

###	Collecting and distributing social media data (30 mins): 
*	Overview on available annotated tweet datasets, 
*	Respecting API terms and user privacy considerations for collecting & sharing social media data, 
*	Demo on collecting data from a few social media APIs, such as Twitter and Reddit 

###	Break 30 mins

###	Improving IE on social media data via Machine Learning (2 hr 30 mins):
*	Semi-supervised learning for Twitter NER (https://github.com/napsternxg/TwitterNER), 
*	Multi-task learning for social media IE (https://socialmediaie.github.io), 
*	Active learning for annotating social media data for text classification (https://github.com/uiuc-ischool-scanr/SAIL another version pySAIL to be released soon), 
*	Finetuning transformer models for monolingual and multi-lingual social media NLP tasks. 
*	Biases in social media NER. 
*	Utilizing Social Context for improving NLP Models. 

###	Conclusion and future directions (10 mins): 
*	Open questions in social media IE, 
*	Tutorial feedback and additional questions

Resources to follow up and questions from participants.
* Project page: [https://socialmediaie.github.io/](https://socialmediaie.github.io/)
* TwitterNER: [https://github.com/napsternxg/TwitterNER ](https://github.com/napsternxg/TwitterNER )
* Social Communication Temporal Graph: [https://shubhanshu.com/social-comm-temporal-graph/](https://shubhanshu.com/social-comm-temporal-graph/)
* SocialMediaIE for multi-task learning: [https://github.com/socialmediaie/SocialMediaIE](https://github.com/socialmediaie/SocialMediaIE)