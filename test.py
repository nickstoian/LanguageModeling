import math

textFile = open('brown-train-processed.txt', 'r')
unigramDict = dict()
#numTokens = 0
for line in textFile:
    for word in line.split():
        #numTokens += 1
        if word not in unigramDict:
            unigramDict[word] = 1
        else:
            unigramDict[word] += 1

values = unigramDict.values()
numTokens = 0
for val in values:
    numTokens += val

print(len(unigramDict.items()))

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

print(len(bigramDict.items()))


sentence = "<s> He was laughed off the screen . </s>"
sentenceProb = 1
logProb = 0
print(sentence)
print()
for word in sentence.lower().split():
    if word not in unigramDict:
        word = "<unk>"
    sentenceProb *= (unigramDict[word] / numTokens)
    logProb += math.log2(unigramDict[word] / numTokens)
    print("p(" + word + ") =", str(unigramDict[word]) + "/" + str(numTokens))
print()
#print(math.log2(sentenceProb))
#print(logProb)
print("The unigram log probability =", logProb)
print()

sentenceProb = 1
logProb = 0
for word in sentence.lower().split():
    if word not in unigramDict:
        word = "<unk>"
    if word == '<s>':
        prevWord = word
        print("p(" + word + ") =", str(unigramDict[word]) + "/" + str(unigramDict[word]))
    elif prevWord + " " + word not in bigramDict:
        print("p(" + word + "|" + prevWord + ") =", str(0) + "/" + str(unigramDict[word]))
        prevWord = word
    else:
        sentenceProb *= (bigramDict[prevWord + " " + word] / unigramDict[prevWord])
        logProb += math.log2(bigramDict[prevWord + " " + word] / unigramDict[prevWord])
        print("p(" + word + "|" + prevWord + ") =", str(bigramDict[prevWord + " " + word]) + "/" + str(unigramDict[prevWord]))
        prevWord = word

print()
#print(math.log2(sentenceProb))
#print(logProb)
print("The bigram log probability =", logProb)

sentenceProb = 1
logProb = 0
for word in sentence.lower().split():
    if word not in unigramDict:
        word = "<unk>"
    if word == '<s>':
        prevWord = word
        print("p(" + word + ") =", str(unigramDict[word]) + "/" + str(unigramDict[word]))
    elif prevWord + " " + word not in bigramDict:
        sentenceProb *= (1 / (unigramDict[prevWord] + len(bigramDict.items())))
        logProb += math.log2(1 / (unigramDict[prevWord] + len(bigramDict.items())))
        print("p(" + word + "|" + prevWord + ") =", str(1) + "/" + str(unigramDict[word] + len(bigramDict.items())))
        prevWord = word
    else:
        sentenceProb *= ((bigramDict[prevWord + " " + word] + 1) / (unigramDict[prevWord] + len(bigramDict.items())))
        logProb += math.log2((bigramDict[prevWord + " " + word] + 1) / (unigramDict[prevWord] + len(bigramDict.items())))
        print("p(" + word + "|" + prevWord + ") =", str(bigramDict[prevWord + " " + word] + 1) + "/" + str(unigramDict[prevWord] + len(bigramDict.items())))
        prevWord = word

print()
print(math.log2(sentenceProb))
#print(logProb)
print("The bigram log probability =", logProb)