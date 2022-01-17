## Abstract

Information extraction (IE) [<sup>1</sup>] is a common sub-area of natural language processing that focuses on identifying structured data from unstructured data. One example of IE is to identify named entities in a text, e.g., &quot;**Barack Obama** served as the president of the **USA**&quot;. Here, Barack Obama and USA are named entities of types of PERSON and LOCATION, respectively. Another example is to identify sentiment expressed in a text, e.g., &quot;This movie was awesome&quot;. Here, the sentiment expressed is positive. Finally, identifying various linguistic aspects of a text, e.g., part of speech tags, noun phrases, dependency parses, etc., which can serve as features for additional IE tasks.

This tutorial introduces participants to a) the usage of Python based, open source tools that support IE from social media data (mainly Twitter), and b) best practices for ensuring the reproducibility of research. Participants will learn and practice various semantic and syntactic IE techniques that are commonly used for analyzing tweets. Additionally, participants will be familiarized with the landscape of publicly available tweet data, and methods for collecting and preparing them for analysis. Finally, participants will be trained to use a suite of open source tools ([SAIL] for active learning[<sup>2</sup>], [TwitterNER] for named entity recognition[<sup>3</sup>], and [SocialMediaIE] for multi task learning[<sup>4</sup>]), which utilize advanced machine learning techniques (e.g., deep learning, active learning with human-in-the-loop, and multi-task learning) to perform IE on their own or existing datasets. The tools introduced in the tutorial will focus on the three main stages of IE, namely, collection of data (including annotation), data processing and analytics, and visualization of the extracted information.

[<sup>1</sup>]: https://doi.org/10.1561/1900000003 "Sunita Sarawagi. 2007. Information Extraction.Foundations and Trends®in Databases1, 3 (mar 2007), 261–377."
[<sup>2</sup>]: https://doi.org/10.1145/2700171.2791022 "Shubhanshu Mishra, Jana Diesner, Jason Byrne, and Elizabeth Surbeck. 2015. Sentiment Analysis with Incremental Human-in-the-Loop Learning andLexical Resource Customization. InProceedings of the 26th ACM Conference on Hypertext &#38; Social Media (HT ’15). ACM, New York, NY, USA,323–325."
[<sup>3</sup>]: https://www.aclweb.org/anthology/W16-3927 "Shubhanshu Mishra and Jana Diesner. 2016. Semi-supervised Named Entity Recognition in noisy-text. InProceedings of the 2nd Workshop on NoisyUser-generated Text (WNUT). The COLING 2016 Organizing Committee, Osaka, Japan, 203–212"
[<sup>4</sup>]: https://doi.org/10.1145/3342220.3344929 "Shubhanshu Mishra. 2019. Multi-dataset-multi-task Neural Sequence Tagging for Information Extraction from Tweets. InProceedings of the 30th ACM Conference on Hypertext &#38; Social Media (HT ’19). ACM, Hof, Germany."
[SocialMediaIE]: https://github.com/socialmediaie
[TwitterNER]: https://github.com/napsternxg/TwitterNER
[SAIL]: https://github.com/uiuc-ischool-scanr/SAIL


## Previous and upcoming tutorial details

| Date               	| Venue                                                  				    |
|-----------------------|---------------------------------------------------------------------------|
| Jun 20, 2022 			| [LREC, Marseille, France](./LREC2022)                            		    |
| Apr 10, 2022 			| [ECIR, Stavanger, Norway](./ECIR2022)                            		    |
| May 11, 2020 			| ~~[LREC, Marseille, France](./LREC2020)~~ - Cancelled due to Covid        |
| May 11, 2021.         | [TheWebConf, Ljubljana, Slovenia](./WWW2021)                              |
| Jul 17, 2020 			| [IC2S2, Boston, USA](./IC2S2_2020)                              		    |
| May 11, 2020 			| [LREC, Marseille, France](./LREC2020)                            		    |
| Sep 17, 2019 			| [ACM HyperText, Hof, Germany](./HT2019)                                   |
| Jul 24, 2019      	| [University of Illinois at Urbana-Champaign, Research park](./UIUC2019)   |


## Expected background and prerequisite of audience

We want to make this tutorial as accessible as possible to the Hypertext community. However, all our tools are implemented in the Python programming language, and we will be using these tools to go through the tutorial. Providing full working knowledge of Python during this tutorial is not possible. Hence, we expect basic proficiency with Python for data analysis use cases. Those who are unfamiliar with Python can prepare themselves before the tutorial by going through the tutorial provided at: [https://www.learnpython.org/](https://www.learnpython.org/).

We do not presume knowledge of machine learning concepts or deep neural networks. We will be providing just enough background to help you utilize these concepts for IE.

We expect participants to bring their own laptops with all the tools installed. Details on what tools need to be installed will be provided a week before the tutorial.

Finally, we expect basic familiarity with social media platforms like Twitter and Facebook. For participants who want to collect their own Twitter data for a tutorial exercise need to have a Twitter account, which can be bran new and just used for this workshop. For participants without a Twitter account, this exercise will still be screen presented and documentation provided such that participants can follow along and work through the examples later. The same is true for all exercises provided in the tutorial.

## Presenter Bio's

### [Shubhanshu Mishra](https://shubhanshu.com/)

Content Understanding Research, Twitter, Inc.

Shubhanshu Mishra is a Senior Machine Learning Researcher at Twitter. He earned his Ph.D. in Information Sciences from the University of Illinois at Urbana-Champaign in 2020 His thesis was titled [Information extraction from digital social trace data: applications in social media and scholarly data analysis](http://shubhanshu.com/phd_thesis/). His current work is at the intersection of machine learning, information extraction, social network analysis, and visualizations. His research has led to the development of open source tools of open source information extraction solutions from large scale social media and scholarly data. He has finished his Integrated Bachelor's and Master's degree in Mathematics and Computing from the Indian Institute of Technology, Kharagpur in 2012. 


### [Rezvaneh (Shadi) Rezapour](https://www.shadirezapour.com/)

Department of Information Science at Drexel's College of Computing and Informatics

Shadi is an Assistant Professor in the Department of Information Science at Drexel's College of Computing and Informatics. Her research interests lie at the intersection of Computational Social Science and Natural Language Processing (NLP). More specifically, she is interested in bringing computational models and social science theories together, to analyze texts and better understand and explain real-world behaviors, attitudes, and cultures. Her research goal is to develop "socially-aware" NLP models that bring social and cultural contexts in analyzing (human) language to better capture attributes, such as social identities, stances, morals, and power from language, and understand real-world communication. Shadi completed her Ph.D. in Information Sciences at University of Illinois at Urbana-Champaign (UIUC) where she was advised by Dr. Jana Diesner.

### [Jana Diesner](http://jdiesnerlab.ischool.illinois.edu/)

School of Information Sciences, University of Illinois at Urbana-Champaign

Jana Diesner is an Associate Professor at the School of Information Sciences at the University of Illinois at Urbana-Champaign. Her research in social computing and human-centered data science combines methods from natural language processing, social network analysis, and machine learning with theories from the social sciences, humanities, and linguistics to advance knowledge and discovery about interaction-based and information-based systems. Her lab is currently working on projects related to 1) biases in data, technology, and human decision-making; 2) validating social science theories in contemporary contexts; 3) impact assessment; 4) crisis informatics; and 5) data governance and responsible computing. Diesner has published over 55 referred articles. She got her PhD (2012) from the School of Computer Science at Carnegie Mellon University. For more information, see [http://jdiesnerlab.ischool.illinois.edu/](http://jdiesnerlab.ischool.illinois.edu/).


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
*	Rezapour, R., Wang, L., Abdar, O., & Diesner, J. (2017). Identifying the overlap between election result and candidates’ ranking based on hashtag-enhanced, lexicon-based sentiment analysis. In 2017 IEEE 11th International Conference on Semantic Computing (ICSC) (pp. 93-96). IEEE.
*	Rezapour, R., Shah, S. H., & Diesner, J. (2019). Enhancing the measurement of social effects by capturing morality. In Proceedings of the Tenth Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis (pp. 35-45). Association for Computational Linguistics (ACL).
*	Rezapour, R., Dinh, L., & Diesner, J. (2021). Incorporating the Measurement of Moral Foundations Theory into Analyzing Stances on Controversial Topics. In Proceedings of the 32nd ACM Conference on Hypertext & Social Media - HT ’21 (pp. 177-188). Held online. 
*	Sarol, M. J., Dinh, L., Rezapour, R., Chin, C. L., Yang, P., & Diesner, J. (2020). An Empirical Methodology for Detecting and Prioritizing Needs during Crisis Events. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: Findings (EMNLP) (pp. 4102-4107).
*	Mishra, S., & Haghighi, A. (2021). Improved Multilingual Language Model Pretraining for Social Media Text via Translation Pair Prediction. In Proceedings of the Seventh Workshop on Noisy User-generated Text (W-NUT 2021) (pp. 381–388). Online: Association for Computational Linguistics. Retrieved from https://aclanthology.org/2021.wnut-1.42
*	Kulkarni, V., Mishra, S., & Haghighi, A. (2021). {LMSOC}: An Approach for Socially Sensitive Pretraining. In Findings of the Association for Computational Linguistics: EMNLP 2021 (pp. 2967–2975). Punta Cana, Dominican Republic: Association for Computational Linguistics. Retrieved from https://aclanthology.org/2021.findings-emnlp.254

