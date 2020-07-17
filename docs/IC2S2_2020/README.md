---
layout: default
title: "Information extraction from social media:  A hands-on tutorial on tasks, data, and open source tools"
description: "IC2S2 2020 Tutorial. July 17th, 2020"
permalink: /IC2S2_2020/
---

# IC2S2 2020 Tutorial

[Tutorial Home](../)

* **Date:** July 17, 2020
* **Time:** TBD
* **Venue:** TBD
* **Slides:** 
* **Speakers:**
  - **[Shubhanshu Mishra](https://shubhanshu.com/):** Twitter, Inc. (presented work was done during PhD at the iSchool at University of Illinois Urbana-Champaign, USA)
  - **[Rezvaneh (Shadi) Rezapour](https://sites.google.com/view/rezapour/home):** The iSchool at University of Illinois Urbana-Champaign, USA 
  - **[Jana Diesner](http://jdiesnerlab.ischool.illinois.edu/):** The iSchool at University of Illinois Urbana-Champaign, USA 
* **Contact:** Shubhanshu Mishra at [https://twitter.com/TheShubhanshu](https://twitter.com/TheShubhanshu)


# Tutorial description
In this hands-on tutorial, we introduce the participants to working with social media data, which are an example of Digital Social Trace Data (DSTD). The DSTD abstraction allows us to model social media data with rich information associated with social media text, such as authors, topics, and time. We introduce the participants to several Python based open source tools for performing IE on social media data. Furthermore, the participants will be familiarized with a catalogue of more than 30 publicly available social media corpora for various IE tasks, e.g., named entity recognition (NER), part of speech (POS) tagging, chunking, super sense tagging, entity linking, sentiment classification, and hate speech identification. Finally, the participants will be introduced to the following applications of extracted information: a) Ranking users based on their enthusiasm and support towards social causes, b) Correlation between sentiment and user-level attributes in existing corpora. The tutorial aims to serve the following use cases for social media researchers: a) high accuracy IE on social media text via multi-task and semi-supervised learning, b) rapid annotation of new data for text classification via active human-in-the-loop learning, c) temporal visualization of the communication structure in social media corpora via social communication temporal graph visualization technique.  


# Rationale
Information extraction (IE) is a common sub-area of natural language processing that focuses on identifying structured information  from unstructured data. While there are numbers of open source tools for performing IE on newswire and academic publication corpora, there is a lack of such tools when dealing with social media corpora, which tends to exhibit very different linguistic patterns compared to the other corpora. It has also been found that publicly available tools for IE, which are trained on news and academic corpora do not tend to perform very well on social media corpora. 

## Topics of interest include:
- machine learning for social media IE, 
- generating annotated text classification data using active human-in-the-loop learning, 
- public corpora for social media IE, 
- open source tools for social media IE, 
- visualizing social media corpora

## Benefit to IC2S2 community
Many scholars of computational social science work with social media text for their research. This tutorial will allow them to use state of the art methods for processing  social media text which can strengthen the quality of their analysis. 

This will be a **3-hours**  long tutorial session using Python based, open source tools. The tutorial will be structured as follows:

# Pre-arrival material

* [Google Colab](https://colab.research.google.com)
* Project page: [https://socialmediaie.github.io/](https://socialmediaie.github.io/)
* TwitterNER: [https://github.com/napsternxg/TwitterNER ](https://github.com/napsternxg/TwitterNER )
* Social Communication Temporal Graph: [https://shubhanshu.com/social-comm-temporal-graph/](https://shubhanshu.com/social-comm-temporal-graph/)
* SocialMediaIE for multi-task learning: [https://github.com/socialmediaie/SocialMediaIE](https://github.com/socialmediaie/SocialMediaIE)


## Software setup

* Make sure you have a google account. Log into that account.
* Try to access the base notebook at on google colab at: [https://colab.research.google.com/drive/1wygmHuawC_UsBNmBWF-S0vVZEPSi3zuf?usp=sharing](https://colab.research.google.com/drive/1wygmHuawC_UsBNmBWF-S0vVZEPSi3zuf?usp=sharing)
* If you would like to use SocialMediaIE on your desktop follow the instructions from: 



# Tutorial day schedule

## INTRODUCTION (SHUBHANSHU AND JANA) (30 MIN) 
* Introducing the differences between social media data versus newswire and academic data
* Digital Social Trace Data abstraction for social media data
* Introduction to information extraction tasks for social media data, e.g. 
  - sequence tagging (named entity, part of speech tagging, chunking, and super-sense tagging), and 
  - text classification (sentiment prediction, sarcasm detection, and abusive content detection)

## APPLICATIONS OF INFORMATION EXTRACTION (SHUBHANSHU, JANA, AND SHADI) (30 MIN)
* Indexing social media corpora in database
* Network construction from text corpora 
* Visualizing temporal trends in social media corpora using social communication temporal graphs (https://shubhanshu.com/social-comm-temporal-graph/) 
* Ranking users based on their enthusiasm and support towards social causes
* Correlation between sentiment and user-level attributes in existing corpora
* Analyzing social debate using sentiment and political identity signals otherwise

## COLLECTING AND DISTRIBUTING SOCIAL MEDIA DATA (SHUBHANSHU AND JANA) (20 MINS)
* Overview on available annotated tweet datasets
* Respecting API terms and user privacy considerations for collecting and sharing social media data
* Demo on collecting data from a few social media APIs, such as Twitter (subject to API availability)

## BREAK (10 MINS)

## IMPROVING IE ON SOCIAL MEDIA DATA USING MACHINE LEARNING (SHUBHANSHU) (1 HRS)
* Semi-supervised learning for Twitter NER (https://github.com/napsternxg/TwitterNER)
* Multi-task learning for social media IE (https://socialmediaie.github.io)
* Active learning for annotating social media data for text classification (https://github.com/uiuc-ischool-scanr/SAIL another version pySAIL to be released soon)

## CONCLUSION AND FUTURE DIRECTIONS (SHUBHANSHU, JANA, AND SHADI) (20 MINS)
* Open questions in social media IE
* Tutorial feedback and additional questions

# TARGET AUDIENCE AND PRE-REQUISITES
The tutorial is aimed at scholars working in the area of social media analysis and who often utilize text-based analysis techniques. We expect the participants to have some familiarity with python programming or ability to run python scripts with their own data. We also expect familiarity with social media platforms like Twitter and Facebook.


# References
* Sarawagi, S. (2007). Information Extraction. Foundations and Trends® in Databases, 1(3), 261–377. https://doi.org/10.1561/1900000003
* Diesner, J. (2014). ConText: Software for the integrated analysis of text data and network data. Social and semantic networks in communication research.
* Mishra, S., & Diesner, J. (2019). Capturing Signals of Enthusiasm and Support Towards Social Issues from Twitter. In Proceedings of the 5th International Workshop on Social Media World Sensors - SIdEWayS’19 (pp. 19–24). New York, New York, USA: ACM Press. https://doi.org/10.1145/3345645.3351104
* Mishra, S., Diesner, J., Byrne, J., & Surbeck, E. (2015). Sentiment Analysis with Incremental Human-in-the-Loop Learning and Lexical Resource Customization. In Proceedings of the 26th ACM Conference on Hypertext & Social Media - HT ’15 (pp. 323–325). New York, New York, USA: ACM Press. https://doi.org/10.1145/2700171.2791022
* Mishra, S. (2019). Multi-dataset-multi-task Neural Sequence Tagging for Information Extraction from Tweets. In Proceedings of the 30th ACM Conference on Hypertext and Social Media - HT ’19 (pp. 283–284). New York, New York, USA: ACM Press. https://doi.org/10.1145/3342220.3344929
* Mishra, S., & Diesner, J. (2018). Detecting the Correlation between Sentiment and User-level as well as Text-Level Meta-data from Benchmark Corpora. In Proceedings of the 29th on Hypertext and Social Media  - HT ’18 (pp. 2–10). New York, New York, USA: ACM Press. https://doi.org/10.1145/3209542.3209562
* Mishra, S., Agarwal, S., Guo, J., Phelps, K., Picco, J., & Diesner, J. (2014). Enthusiasm and support: alternative sentiment classification for social movements on social media. In Proceedings of the 2014 ACM conference on Web science - WebSci ’14 (pp. 261–262). Bloomington, Indiana, USA: ACM Press. https://doi.org/10.1145/2615569.2615667

