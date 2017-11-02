# Nicolas Stoian
# CS780 Natural Language Processing
# Homework - Language Modeling

textFile = open('brown-train-padded.txt', 'r')
unigramDict = dict()
for line in textFile:
    for word in line.split():
        if word not in unigramDict:
            unigramDict[word] = 1
        else:
            unigramDict[word] += 1
textFile.close()


def unigramCompare(textFile, unigramDict):
    numTokens = 0
    numTokensNotInTraining = 0
    for line in textFile:
        for word in line.split():
            numTokens += 1
            if word not in unigramDict:
                numTokensNotInTraining += 1
    print("Test file name =", textFile.name)
    print("Total number of words in file =", numTokens)
    print("Number of words not appearing in training data =", numTokensNotInTraining)
    print("Percentage of words not appearing in training data =", (numTokensNotInTraining / numTokens) * 100, "%")
    print()
    print()


print("Question 3")
textFile1 = open('brown-test-padded.txt', 'r')
textFile2 = open('learner-test-padded.txt', 'r')
unigramCompare(textFile1, unigramDict)
unigramCompare(textFile2, unigramDict)
textFile1.close()
textFile2.close()


textFile = open('brown-train-processed.txt', 'r')
bigramDict = dict()
prevWord = ""
for line in textFile:
    for word in line.split():
        if word == '<s>':
            prevWord = word
        elif prevWord + " " + word not in bigramDict:
            bigramDict[prevWord + " " + word] = 1
            prevWord = word
        else:
            bigramDict[prevWord + " " + word] += 1
            prevWord = word
textFile.close()


def bigramCompare(textFile, unigramDict, bigramDict):
    numBigrams = 0
    numBigramsNotInTraining = 0
    for line in textFile:
        prevWord = ""
        for word in line.split():
            if word not in unigramDict:
                word = "<unk>"
            if word == '<s>':
                prevWord = word
            elif prevWord + " " + word not in bigramDict:
                numBigramsNotInTraining += 1
                numBigrams += 1
                prevWord = word
            else:
                numBigrams += 1
                prevWord = word
    print("Test file name =", textFile.name)
    print("Total number of bigrams in file =", numBigrams)
    print("Number of bigrams not appearing in training data =", numBigramsNotInTraining)
    print("Percentage of bigrams not appearing in training data =", (numBigramsNotInTraining / numBigrams) * 100, "%")
    print()
    print()


print("Question 4")
textFile1 = open('brown-test-padded.txt', 'r')
textFile2 = open('learner-test-padded.txt', 'r')
bigramCompare(textFile1, unigramDict, bigramDict)
bigramCompare(textFile2, unigramDict, bigramDict)
textFile1.close()
textFile2.close()

