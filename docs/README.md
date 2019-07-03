# Hands on advanced machine learning for information extraction from tweets tasks, data, and open source tools

## Abstract

Information extraction (IE) [<sup>1</sup>] is a common task for converting unstructured data to structured data. Information extraction enables the usage of existing database techniques for extracting further knowledge from a text corpora. This tutorial will focus on the usage of python based open source tools and practices from reproducible research on sharing of data and code. In this tutorial we will introduce the participants to various semantic and syntactic information extraction tasks commonly used for tweets. Additionally, the participants will be familiarized with the landscape of publicly available training data for tweets, and methods for collecting them. Finally, the participants will be trained to use a suite of open source tools ([SAIL] [<sup>2</sup>], [TwitterNER] [<sup>3</sup>], and [SocialMediaIE]) which utilize advanced machine learning techniques (e.g. deep learning, active learning with human-in-the-loop, and multi-task learning) to perform information extraction on their own data-sets. The tools introduced in the tutorial will focus on the three stages of information extraction, namely, collection of data (including annotation), information extraction from data, and visualization of extracted information. 

[<sup>1</sup>]: https://doi.org/10.1561/1900000003 "Sunita Sarawagi. 2007. Information Extraction.Foundations and Trends®in Databases1, 3 (mar 2007), 261–377."
[<sup>2</sup>]: https://doi.org/10.1145/2700171.2791022 "Shubhanshu Mishra, Jana Diesner, Jason Byrne, and Elizabeth Surbeck. 2015. Sentiment Analysis with Incremental Human-in-the-Loop Learning andLexical Resource Customization. InProceedings of the 26th ACM Conference on Hypertext &#38; Social Media (HT ’15). ACM, New York, NY, USA,323–325."
[<sup>3</sup>]: https://www.aclweb.org/anthology/W16-3927 "Shubhanshu Mishra and Jana Diesner. 2016. Semi-supervised Named Entity Recognition in noisy-text. InProceedings of the 2nd Workshop on NoisyUser-generated Text (WNUT). The COLING 2016 Organizing Committee, Osaka, Japan, 203–212"
[SocialMediaIE]: https://github.com/socialmediaie
[TwitterNER]: https://github.com/napsternxg/TwitterNER
[SAIL]: https://github.com/uiuc-ischool-scanr/SAIL



## Tutorial description

This will be **3 hour** tutorial session using Python based open source tools. The tutorial will be structured as follows:

  - Introduction (15 mins)  
    Familiarize the participants to various information extraction tasks for tweets, e.g.:
    1.  **Sequence tagging**: named entity, part of speech tagging, chunking, and super-sense tagging
    2.  **Text classification**: sentiment prediction, sarcasm detection, and abusive content detection
  - Applications of information extraction (15 mins)  
    Motivate the benefits and use cases of information extraction – namely search, and data visualization.
  - Publicly available tweet data (15 mins)  
    Introduce the participants to publicly available annotated tweet datasets, and their limitations owing to Twitter’s terms of service
    and other privacy policies.
  - Hands on session (1 hr 45 mins)  
    Provide hands on experience of:
    1.  collecting and sharing custom tweet data, with focus on following Twitter’s terms of service,
    2.  efficiently annotating classification data using active human-in-the-loop learning,
    3.  using accurate and open source models for various IE tasks,
    4.  training deep neural network models using multi-task learning for tweet information extraction tasks,
    5.  visualize extracted information and tweets using temporal network visualizations.
  - Conclusion (15 mins)  
    Resources to follow up and questions from participants.

## Expected background and prerequisite of audience

We expect the audience to have some familiarity with python programming or ability to run python scripts with their own data. We also expect familiarity with social media platforms like Twitter and Facebook.

## Author Bio’s

### [Shubhanshu Mishra](https://shubhanshu.com)

School of Information Sciences, University of Illinois at Urbana-Champaign  

Shubhanshu is a final year Ph.D. student at the School of Information Sciences in University of Illinois at Urbana-Champaign. He is working on his thesis titled **Information extraction from digital social trace data: applications in social media and scholarly data analysis**. His current work is at the intersection of machine learning, information extraction, social network analysis, and visualizations. His research has led to the development of open source tools of open source information extraction from large scale social media and scholarly data. He has finished his Integrated Bachelor’s and Master’s degree in Mathematics and Computing from the Indian Institute of Technology, Kharagpur in 2012. He was a fellow of Kishor Vaigyanik Protsahan Yojana (KVPY), a scholarship program funded by the Department of Science and Technology of the Government of India, from 2007 to 2012.

### [Jana Diesner](http://jdiesnerlab.ischool.illinois.edu)

School of Information Sciences, University of Illinois at Urbana-Champaign  

Jana Diesner is an Associate Professor at the School of Information Sciences (the iSchool) at the University of Illinois at Urbana-Champaign, and an affiliate at the Department of Computer Science, the Illinois Informatics Institute, the Information Trust Institute (ITI), and the Cline Center for Democracy. She is also the director of the LIS PhD program. Jana got her PhD in Computation, Organizations and Society (COS, now Societal Computing) from Carnegie Mellon University’s School of Computer Science. Jana’s research is in the areas of Computational Social Science (Social Computing) and Human-Centered Data Science. She integrates and advances methods from Social Network Analysis, Natural Language Processing, and MachineLearning with theories from the social sciences, humanities, and linguistics to answer substantive questions. Using this mixed methods and mixed data perspective, she 1) validates social network theories in contemporary settings, 2) studies consequences of limitations of data provenance and data quality at scale, and 3) assesses the impact of information on people.
