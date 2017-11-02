import math

textFile = open('brown-train-processed.txt', 'r')
unigramDict = dict()
numTokens = 0
for line in textFile:
    for word in line.split():
        numTokens += 1
        if word not in unigramDict:
            unigramDict[word] = 1
        else:
            unigramDict[word] += 1
print(len(unigramDict.items()))
print(numTokens)
print(unigramDict['<unk>'])
print(unigramDict['.'])

values = unigramDict.values()
n = 0
for val in values:
    n += val
print(n)



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
print(bigramDict.get('<s>' + ' ' + 'the'))
print(bigramDict.get('the' + ' ' + 'grand'))
print(bigramDict.get('<unk>' + ' ' + '<unk>'))
print(bigramDict.get('<unk>'))

sentence = "<s> He was laughed off the screen . </s>"
sentenceProb = 1
logProb = 0
for word in sentence.lower().split():
    if word not in unigramDict:
        word = "<unk>"
    print(word)
    sentenceProb *= (unigramDict[word] / numTokens)
    logProb += math.log2(unigramDict[word] / numTokens)
    print(unigramDict[word])
print()
print()
print(math.log2(sentenceProb))
print(logProb)