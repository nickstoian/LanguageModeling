# Nicolas Stoian
# CS780 Natural Language Processing
# Homework - Language Modeling

import math

textFile = open('brown-train-processed.txt', 'r')
unigramDict = dict()
bigramDict = dict()
prevWord = ""
for line in textFile:
    for word in line.split():
        if word not in unigramDict:
            unigramDict[word] = 1
        else:
            unigramDict[word] += 1
        if word == '<s>':
            prevWord = word
        elif prevWord + " " + word not in bigramDict:
            bigramDict[prevWord + " " + word] = 1
            prevWord = word
        else:
            bigramDict[prevWord + " " + word] += 1
            prevWord = word
unigramVocSize = len(unigramDict.keys())
textFile.close()

print("Question 1")
print("Number of word types (unique words) in training corpus =", unigramVocSize)
print()


values = unigramDict.values()
numTokens = 0
for val in values:
    numTokens += val


print("Question 2")
print("Number of word tokens in training corpus =", numTokens)
print()


def computeSentenceLogProbsAndPerplexity(sentence, unigramDict, bigramDict, numTokens):
    print("Sentence =", sentence)
    print()
    numWords = len(sentence.split())
    logProb = 0
    for word in sentence.lower().split():
        if word not in unigramDict:
            word = "<unk>"
        if word == '<s>':
            pass
        else:
            logProb += math.log2(unigramDict[word] / numTokens)
            print("p(" + word + ") =", str(unigramDict[word]) + "/" + str(numTokens))
    print()
    print("The unigram log probability =", logProb)
    l = (1 / numWords) * logProb
    print("The unigram perplexity =", pow(2, -l))
    print()
    sentenceProb = 1
    prevWord = ""
    for word in sentence.lower().split():
        if word not in unigramDict:
            word = "<unk>"
        if word == '<s>':
            prevWord = word
        elif prevWord + " " + word not in bigramDict:
            sentenceProb *= (0 / unigramDict[prevWord])
            print("p(" + word + "|" + prevWord + ") =", str(0) + "/" + str(unigramDict[prevWord]))
            prevWord = word
        else:
            sentenceProb *= (bigramDict[prevWord + " " + word] / unigramDict[prevWord])
            print("p(" + word + "|" + prevWord + ") =",
                  str(bigramDict[prevWord + " " + word]) + "/" + str(unigramDict[prevWord]))
            prevWord = word
    print()
    if sentenceProb == 0:
        print("The bigram log probability =", str(0))
        print("The bigram perplexity =", "Undefined")
    else:
        print("The bigram log probability =", math.log2(sentenceProb))
        l = (1 / numWords) * math.log2(sentenceProb)
        print("The bigram perplexity =", pow(2, -l))
    print()
    logProb = 0
    for word in sentence.lower().split():
        if word not in unigramDict:
            word = "<unk>"
        if word == '<s>':
            prevWord = word
        elif prevWord + " " + word not in bigramDict:
            logProb += math.log2(1 / (unigramDict[prevWord] + len(unigramDict.items())))
            print("p(" + word + "|" + prevWord + ") =", str(1) + "/" + str(unigramDict[word] + len(unigramDict.items())))
            prevWord = word
        else:
            logProb += math.log2((bigramDict[prevWord + " " + word] + 1) / (unigramDict[prevWord] + len(unigramDict.items())))
            print("p(" + word + "|" + prevWord + ") =", str(bigramDict[prevWord + " " + word] + 1) + "/" + str(
                unigramDict[prevWord] + len(unigramDict.items())))
            prevWord = word
    print()
    print("The bigram with plus one smoothing log probability =", logProb)
    l = (1 / numWords) * logProb
    print("The bigram with plus one smoothing perplexity =", pow(2, -l))
    print()
    print()


print("Question 5 and Question 6")
sentence1 = "<s> He was laughed off the screen . </s>"
sentence2 = "<s> There was no compulsion behind them . </s>"
sentence3 = "<s> I look forward to hearing your reply . </s>"
computeSentenceLogProbsAndPerplexity(sentence1, unigramDict, bigramDict, numTokens)
computeSentenceLogProbsAndPerplexity(sentence2, unigramDict, bigramDict, numTokens)
computeSentenceLogProbsAndPerplexity(sentence3, unigramDict, bigramDict, numTokens)


def computeTestFilePerplexity(textFile, unigramDict, bigramDict, numTokens):
    numWords = 0
    numWordsBigram = 0
    numLines = 0
    numLinesDiscarded = 0
    for line in textFile:
        numLines += 1
        for word in line.split():
            numWords += 1
            numWordsBigram += 1
    textFile = open(textFile.name, 'r')
    totalUnigramLogProb = 0
    totalBigramLogProb = 0
    totalSmoothedBigramLogProb = 0
    for line in textFile:
        logProb = 0
        for word in line.split():
            if word not in unigramDict:
                word = "<unk>"
            if word == '<s>':
                pass
            else:
                logProb += math.log2(unigramDict[word] / numTokens)
        totalUnigramLogProb += logProb
        sentenceProb = 1
        prevWord = ""
        for word in line.split():
            if word not in unigramDict:
                word = "<unk>"
            if word == '<s>':
                prevWord = word
            elif prevWord + " " + word not in bigramDict:
                sentenceProb *= (0 / unigramDict[prevWord])
                prevWord = word
            else:
                sentenceProb *= (bigramDict[prevWord + " " + word] / unigramDict[prevWord])
                prevWord = word
        if sentenceProb == 0:
            numWordsBigram -= len(line.split())
            numLinesDiscarded += 1
        else:
            totalBigramLogProb += math.log2(sentenceProb)
        logProb = 0
        for word in line.split():
            if word not in unigramDict:
                word = "<unk>"
            if word == '<s>':
                prevWord = word
            elif prevWord + " " + word not in bigramDict:
                logProb += math.log2(1 / (unigramDict[prevWord] + len(unigramDict.items())))
                prevWord = word
            else:
                logProb += math.log2((bigramDict[prevWord + " " + word] + 1) / (unigramDict[prevWord] + len(unigramDict.items())))
                prevWord = word
        totalSmoothedBigramLogProb += logProb
    print("Test corpus name =", textFile.name)
    print()
    l = (1 / numWords) * totalUnigramLogProb
    print("The total unigram perplexity =", pow(2, -l))
    print()
    l = (1 / numWordsBigram) * totalBigramLogProb
    print("The total bigram perplexity =", pow(2, -l))
    print(numLinesDiscarded, "of", numLines, "sentences had zero probability and were discarded")
    print()
    l = (1 / numWords) * totalSmoothedBigramLogProb
    print("The total bigram with plus one smoothing perplexity =", pow(2, -l))
    print()
    print()


print("Question 7")
textFile1 = open('brown-test-padded.txt', 'r')
textFile2 = open('learner-test-padded.txt', 'r')
computeTestFilePerplexity(textFile1, unigramDict, bigramDict, numTokens)
computeTestFilePerplexity(textFile2, unigramDict, bigramDict, numTokens)
textFile1.close()
textFile2.close()