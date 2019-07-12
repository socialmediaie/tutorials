## Abstract

Information extraction (IE) [<sup>1</sup>] is a common sub-area of natural language processing that focuses on identifying structured data from unstructured data. One example of IE is to identify named entities in a text, e.g., &quot;**Barack Obama** served as the president of the **USA**&quot;. Here, Barack Obama and USA are named entities of types of PERSON and LOCATION, respectively. Another example is to identify sentiment expressed in a text, e.g., &quot;This movie was awesome&quot;. Here, the sentiment expressed is positive. Finally, identifying various linguistic aspects of a text, e.g., part of speech tags, noun phrases, dependency parses, etc., which can serve as features for additional IE tasks.

This tutorial introduces participants to a) the usage of Python based, open source tools that support IE from social media data (mainly Twitter), and b) best practices for ensuring the reproducibility of research. Participants will learn and practice various semantic and syntactic IE techniques that are commonly used for analyzing tweets. Additionally, participants will be familiarized with the landscape of publicly available tweet data, and methods for collecting and preparing them for analysis. Finally, participants will be trained to use a suite of open source tools ([SAIL] [<sup>2</sup>], [TwitterNER] [<sup>3</sup>], and [SocialMediaIE]), which utilize advanced machine learning techniques (e.g., deep learning, active learning with human-in-the-loop, and multi-task learning) to perform IE on their own or existing datasets. The tools introduced in the tutorial will focus on the three main stages of IE, namely, collection of data (including annotation), data processing and analytics, and visualization of the extracted information.

[<sup>1</sup>]: https://doi.org/10.1561/1900000003 "Sunita Sarawagi. 2007. Information Extraction.Foundations and Trends®in Databases1, 3 (mar 2007), 261–377."
[<sup>2</sup>]: https://doi.org/10.1145/2700171.2791022 "Shubhanshu Mishra, Jana Diesner, Jason Byrne, and Elizabeth Surbeck. 2015. Sentiment Analysis with Incremental Human-in-the-Loop Learning andLexical Resource Customization. InProceedings of the 26th ACM Conference on Hypertext &#38; Social Media (HT ’15). ACM, New York, NY, USA,323–325."
[<sup>3</sup>]: https://www.aclweb.org/anthology/W16-3927 "Shubhanshu Mishra and Jana Diesner. 2016. Semi-supervised Named Entity Recognition in noisy-text. InProceedings of the 2nd Workshop on NoisyUser-generated Text (WNUT). The COLING 2016 Organizing Committee, Osaka, Japan, 203–212"
[SocialMediaIE]: https://github.com/socialmediaie
[TwitterNER]: https://github.com/napsternxg/TwitterNER
[SAIL]: https://github.com/uiuc-ischool-scanr/SAIL



## Tutorial description

This will be a **3-hours**  long tutorial session using Python based, open source tools. The tutorial will be structured as follows:

## Introduction (15 mins)

Familiarize participants with various IE tasks for tweets, e.g.:

1. **Sequence tagging** : named entity detection and classification, part of speech tagging, chunking, and super-sense tagging.
2. **Text classification** : sentiment prediction, sarcasm detection, and abusive content detection.

## Applications of information extraction (15 mins)

This includes:

1. Query-based search on text corpora.
2. Visualizing temporal trends in information.

## Responsible and compliant data use of tweets (15 mins)

1. Overview on available annotated tweet datasets.
2. Clarify on terms of service, regulations such as privacy policies, and norms for working with tweets.

## Break (15 mins)

## Hands on session (1 hr. 30 mins)

Gain hands on experience with:

1. Collecting and sharing samples of tweet data, with focus on following Twitter&#39;s terms of service and additional community norms.
2. Efficiently annotating classification data using active human-in-the-loop learning.
3. Using highly accurate and open source models for various IE tasks.
4. Training deep neural network models using multi-task learning for tweet information extraction tasks.
5. Visualize extracted information and tweets using temporal network visualizations.

## Conclusion (15 mins)

Resources to follow up and questions from participants.

## Expected background and prerequisite of audience

We want to make this tutorial as accessible as possible to the Hypertext community. However, all our tools are implemented in the Python programming language, and we will be using these tools to go through the tutorial. Providing full working knowledge of Python during this tutorial is not possible. Hence, we expect basic proficiency with Python for data analysis use cases. Those who are unfamiliar with Python can prepare themselves before the tutorial by going through the tutorial provided at: [https://www.learnpython.org/](https://www.learnpython.org/).

We do not presume knowledge of machine learning concepts or deep neural networks. We will be providing just enough background to help you utilize these concepts for IE.

We expect participants to bring their own laptops with all the tools installed. Details on what tools need to be installed will be provided a week before the tutorial.

Finally, we expect basic familiarity with social media platforms like Twitter and Facebook. For participants who want to collect their own Twitter data for a tutorial exercise need to have a Twitter account, which can be bran new and just used for this workshop. For participants without a Twitter account, this exercise will still be screen presented and documentation provided such that participants can follow along and work through the examples later. The same is true for all exercises provided in the tutorial.

## Author Bio&#39;s

### [Shubhanshu Mishra](https://shubhanshu.com/)

School of Information Sciences, University of Illinois at Urbana-Champaign

Shubhanshu is graduating with a Ph.D. from the School of Information Sciences at the University of Illinois at Urbana-Champaign. He recently defended his thesis titled [Information extraction from digital social trace data: applications in social media and scholarly data analysis](http://shubhanshu.com/phd_thesis/). His current work is at the intersection of machine learning, information extraction, social network analysis, and visualizations. His research has led to the development of open source tools for information extraction from large scale social media and scholarly data. He holds an integrated bachelor&#39;s and master&#39;s degree in Mathematics and Computing from the Indian Institute of Technology, Kharagpur. For more information, see [https://shubhanshu.com/](https://shubhanshu.com/).

### [Jana Diesner](http://jdiesnerlab.ischool.illinois.edu/)

School of Information Sciences, University of Illinois at Urbana-Champaign

Jana Diesner is an Associate Professor at the School of Information Sciences at the University of Illinois at Urbana-Champaign. Her research in social computing and human-centered data science combines methods from natural language processing, social network analysis, and machine learning with theories from the social sciences, humanities, and linguistics to advance knowledge and discovery about interaction-based and information-based systems. Her lab is currently working on projects related to 1) biases in data, technology, and human decision-making; 2) validating social science theories in contemporary contexts; 3) impact assessment; 4) crisis informatics; and 5) data governance and responsible computing. Diesner has published over 55 referred articles. She got her PhD (2012) from the School of Computer Science at Carnegie Mellon University. For more information, see [http://jdiesnerlab.ischool.illinois.edu/](http://jdiesnerlab.ischool.illinois.edu/).


## References

1. Sunita Sarawagi. 2007. Information Extraction.Foundations and Trends®in Databases1, 3 (mar 2007), 261–377. https://doi.org/10.1561/1900000003
2. Shubhanshu Mishra, Jana Diesner, Jason Byrne, and Elizabeth Surbeck. 2015. Sentiment Analysis with Incremental Human-in-the-Loop Learning and Lexical Resource Customization. In Proceedings of the 26th ACM Conference on Hypertext & Social Media (HT'15). ACM, New York, NY, USA,323–325. https://doi.org/10.1145/2700171.2791022
3. Shubhanshu Mishra and Jana Diesner. 2016. Semi-supervised Named Entity Recognition in noisy-text. In Proceedings of the 2nd Workshop on Noisy User-generated Text (WNUT). The COLING 2016 Organizing Committee, Osaka, Japan, 203–212. https://www.aclweb.org/anthology/W16-3927
