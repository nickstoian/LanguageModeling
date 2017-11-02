# LanguageModeling
Language modeling homework for NLP course

Nicolas Stoian
CS780 Natural Language Processing
Homework - Language Modeling

PreProcess.py is a python script that performs the 3 pre-processing steps specified in the homework assignment
It requires the 3 text files included with the homework assignment to located in the same folder
1. brown-train.txt
2. brown-test.txt
3. learner-test.txt
It will produce 4 output files required to run the other 2 scripts included in this homework submission
1. brown-train-padded.txt
2. brown-test-padded.txt
3. learner-test-padded.txt
4. brown-train-processed.txt
Please run PreProcess.py first, before running the other 2 scripts

BuildAndRunModels.py trains the language models and performs the computations required to answer questions 1, 2, 5, 6, and 7
All of the answers and required values are outputted to the console
It requires 3 files to be present in the same folder
1. brown-test-padded.txt
2. learner-test-padded.txt
3. brown-train-processed.txt

CompareCorpora.py performs the operations required to answer questions 3 and 4
All of the answers and required values are outputted to the console
It requires 4 files to be present in the same folder
1. brown-train-padded.txt
2. brown-test-padded.txt
3. learner-test-padded.txt
4. brown-train-processed.txt

Homework1.pdf is a document containing a writeup of the questions and answers from the homework assignment
