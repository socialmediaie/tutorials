---
layout: default
title: "Information extraction from social media:  A hands-on tutorial on tasks, data, & open source tools"
description: "TheWebConf 2021 Tutorial. April 14th, 2021"
permalink: /WWW2021/
---

# WWW 2021 Tutorial

[Tutorial Home](../)

* **Date:** April 14, 2021
* **Time:** 9:00 AM EST (3:00 PM CEST)
* **Venue:** 12:00 PM EST (6:00 PM CEST)
* **Tutorial URL:** [https://theweb.miteam.eu/asset/tJrKgy3y4na4dssWc](https://theweb.miteam.eu/asset/tJrKgy3y4na4dssWc)
* **Slides:** 
* **Contact:** Shubhanshu Mishra at [https://twitter.com/TheShubhanshu](https://twitter.com/TheShubhanshu)
* **Presenters**: Shubhanshu Mishra, Rezvaneh (Shadi) Rezapour, Jana Diesner

## Tutorial description

In this hands-on tutorial, we introduce the participants to working with social media data, which are an example of Digital Social Trace Data (DSTD). The DSTD abstraction allows us to model social media data with rich information associated with social media text, such as authors, topics, and time stamps. We introduce the participants to several Python-based, open-source tools for performing Information Extraction (IE) on social media data. Furthermore, the participants will be familiarized with a catalogue of more than 30 publicly available social media corpora for various IE tasks such as named entity recognition (NER), part of speech (POS) tagging, chunking, super sense tagging, entity linking, sentiment classification, and hate speech identification. Finally, the participants will be introduced to the following applications of extracted information: a) combining network analysis and text-based signals to rank accounts, and b) correlation between sentiment and user-level attributes in existing corpora. The tutorial aims to serve the following use cases for social media researchers: a) high accuracy IE on social media text via multitask and semi-supervised learning, including the recent transformer based tools, b) rapid annotation of new data for text classification via active human-in-the-loop learning, c) temporal visualization of the communication structure in social media corpora via social communication temporal graph visualization technique, and d) detecting and prioritizing needs during crisis events (e.g., COVID19). 

**Intended audience:** Researchers of social media datasets, computational social scientists, machine learning and NLP researchers.


## Agenda

This will be a **3-hours**  long tutorial session using Python based, open source tools. The tutorial will be structured as follows:


### Setup and Introduction (30 mins)

* Introducing the differences between social media data versus newswire and academic data, 
* Digital Social Trace Data abstraction for social media data, 
* Introduction to information extraction tasks for social media data, e.g., sequence tagging (named entity, part of speech tagging, chunking, and super-sense tagging), and text classification (sentiment prediction, sarcasm detection, and abusive content detection)

### Applications of information extraction (40 mins)

* Indexing social media corpora in database, Network construction from text corpora, 
* Visualizing temporal trends in social media corpora using social communication temporal graphs, 
* Aggregating text-based signals at user level, Improving text classification using user level attributes, 
* Analyzing social debate using sentiment and political identity signals otherwise, 
* Detecting and Prioritizing Needs during Crisis Events (e.g., COVID19), 
* Mining and Analyzing Public Opinion Related to COVID-19, and 
* Detecting COVID-19 Misinformation in Videos on YouTube

### Collecting and distributing social media data (15 mins)

* Overview on available annotated tweet datasets, 
* Respecting API terms and user privacy considerations for collecting & sharing social media data, 
* Demo on collecting data from a few social media APIs, such as Twitter and Reddit 

### Break 10 mins

### Improving IE on social media data via Machine Learning (1 hr 15 mins)
* Semi-supervised learning for Twitter NER (https://github.com/napsternxg/TwitterNER), 
* Multi-task learning for social media IE (https://socialmediaie.github.io), 
* Active learning for annotating social media data for text classification (https://github.com/uiuc-ischool-scanr/SAIL another version pySAIL to be released soon), 
* Finetuning transformer models for monolingual and multi-lingual social media NLP tasks. 

### Conclusion and future directions (10 mins)
Open questions in social media IE, Tutorial feedback and additional questions



## Resources to follow up and questions from participants.
* Project page: [https://socialmediaie.github.io/](https://socialmediaie.github.io/)
* TwitterNER: [https://github.com/napsternxg/TwitterNER ](https://github.com/napsternxg/TwitterNER )
* Social Communication Temporal Graph: [https://shubhanshu.com/social-comm-temporal-graph/](https://shubhanshu.com/social-comm-temporal-graph/)
* SocialMediaIE for multi-task learning: [https://github.com/socialmediaie/SocialMediaIE](https://github.com/socialmediaie/SocialMediaIE)

## References

*	Sarawagi, S. (2007). Information Extraction. Foundations and Trends® in Databases, 1(3), 261–377. https://doi.org/10.1561/1900000003
*	Diesner, J. (2014). ConText: Software for the integrated analysis of text data and network data. Social and semantic networks in communication research.
*	Mishra, S., & Diesner, J. (2019). Capturing Signals of Enthusiasm and Support Towards Social Issues from Twitter. In Proceedings of the 5th International Workshop on Social Media World Sensors - SIdEWayS’19 (pp. 19–24). New York, New York, USA: ACM Press. https://doi.org/10.1145/3345645.3351104
*	Mishra, S., Diesner, J., Byrne, J., & Surbeck, E. (2015). Sentiment Analysis with Incremental Human-in-the-Loop Learning and Lexical Resource Customization. In Proceedings of the 26th ACM Conference on Hypertext & Social Media - HT ’15 (pp. 323–325). New York, New York, USA: ACM Press. https://doi.org/10.1145/2700171.2791022
*	Mishra, S. (2019). Multi-dataset-multi-task Neural Sequence Tagging for Information Extraction from Tweets. In Proceedings of the 30th ACM Conference on Hypertext and Social Media - HT ’19 (pp. 283–284). New York, New York, USA: ACM Press. https://doi.org/10.1145/3342220.3344929
*	Mishra, S., & Diesner, J. (2018). Detecting the Correlation between Sentiment and User-level as well as Text-Level Meta-data from Benchmark Corpora. In Proceedings of the 29th on Hypertext and Social Media - HT ’18 (pp. 2–10). New York, New York, USA: ACM Press. https://doi.org/10.1145/3209542.3209562
*	Mishra, S., Agarwal, S., Guo, J., Phelps, K., Picco, J., & Diesner, J. (2014). Enthusiasm and support: alternative sentiment classification for social movements on social media. In Proceedings of the 2014 ACM conference on Web science - WebSci ’14 (pp. 261–262). Bloomington, Indiana, USA: ACM Press. https://doi.org/10.1145/2615569.2615667
*	Mishra, S., & Mishra, S. (2019). 3Idiots at HASOC 2019: Fine-tuning Transformer Neural Networks for Hate Speech Identiﬁcation in Indo-European Languages. In Proceedings of the 11th annual meeting of the Forum for Information Retrieval Evaluation (pp. 208–213). Kolkata, India. Retrieved from http://ceur-ws.org/Vol-2517/T3-4.pdf
*	Mishra, S., Prasad, S., & Mishra, S. (2020). Multilingual Joint Fine-tuning of Transformer models for identifying Trolling, Aggression and Cyberbullying at TRAC 2020. In Proceedings of the Second Workshop on Trolling, Aggression and Cyberbullying (TRAC-2020).
*	Schwartz, H. A., Eichstaedt, J. C., Kern, M. L., Dziurzynski, L., Ramones, S. M., Agrawal, M., … Ungar, L. H. (2013). Personality, Gender, and Age in the Language of Social Media: The Open-Vocabulary Approach. PLoS ONE, 8(9), e73791. https://doi.org/10.1371/journal.pone.0073791
*	Kaplan, A. M., & Haenlein, M. (2010). Users of the world, unite! The challenges and opportunities of Social Media. Business Horizons, 53(1), 59–68. https://doi.org/10.1016/j.bushor.2009.09.003
*	Eisenstein, J. (2013). What to do about bad language on the internet. In Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (pp. 359–369). Atlanta, Georgia: Association for Computational Linguistics. Retrieved from https://www.aclweb.org/anthology/papers/N/N13/N13-1037/
*	Diesner, J., & Chin, C.-L. (2015). Usable ethics: practical considerations for responsibly conducting research with social trace data. Proceedings of Beyond IRBs: Ethical Review Processes for Big Data Research.
*	Kosinski, M., Matz, S. C., Gosling, S. D., Popov, V., & Stillwell, D. (2015). Facebook as a research tool for the social sciences: Opportunities, challenges, ethical considerations, and practical guidelines. American Psychologist, 70(6), 543–556. https://doi.org/10.1037/a0039210
*	Kwak, H., Lee, C., Park, H., & Moon, S. (2010). What is Twitter, a social network or a news media? In Proceedings of the 19th international conference on World wide web - WWW ’10 (p. 591). New York, New York, USA: ACM Press. https://doi.org/10.1145/1772690.1772751
*	Mohammad, S. M., Kiritchenko, S., & Zhu, X. (2013). NRC-Canada: Building the State-of-the-Art in Sentiment Analysis of Tweets. Proceedings of the Seventh International Workshop on Semantic Evaluation Exercises (SemEval-2013), 2(SemEval), 321–327. Retrieved from http://www.umiacs.umd.edu/~saif/WebPages/Abstracts/NRC-SentimentAnalysis.htm#download
*	Mohammad, S. M., Sobhani, P., & Kiritchenko, S. (2017). Stance and Sentiment in Tweets. ACM Transactions on Internet Technology, 17(3), 1–23. https://doi.org/10.1145/3003433
*	Pang, B., & Lee, L. (2008). Opinion Mining and Sentiment Analysis. Foundations and Trends® in Information Retrieval, 2(1–2), 1–135. https://doi.org/10.1561/1500000011
*	Hutto, C. J., & Gilbert, E. (2014). Vader: A parsimonious rule-based model for sentiment analysis of social media text. In International AAAI Conference on Web and Social Media. Ann Arbor, Michigan, USA. 
*	Rezapour, R., Wang, L., Abdar, O., & Diesner, J. (2017, January). Identifying the overlap between election result and candidates’ ranking based on hashtag-enhanced, lexicon-based sentiment analysis. In 2017 IEEE 11th International Conference on Semantic Computing (ICSC) (pp. 93-96). IEEE.
*	Rezapour, R., Shah, S. H., & Diesner, J. (2019, June). Enhancing the measurement of social effects by capturing morality. In Proceedings of the Tenth Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis (pp. 35-45). Association for Computational Linguistics (ACL).
*	Sarol, M. J., Dinh, L., Rezapour, R., Chin, C. L., Yang, P., & Diesner, J. (2020). An Empirical Methodology for Detecting and Prioritizing Needs during Crisis Events. In Findings of the Association for Computational Linguistics: EMNLP 2020, (pp 4102–4107), Online, Association for Computational Linguistics (ACL).
