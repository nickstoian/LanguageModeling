# Nicolas Stoian
# CS780 Natural Language Processing
# Homework - Language Modeling

def padStartStop(inFile, outFile):
    inputTextFile = open(inFile, 'r')
    outputTextFile = open(outFile, 'w')
    for line in inputTextFile:
        lineEdited = "<s> " + line.replace('\n', ' </s>\n')
        outputTextFile.write(lineEdited.lower())
    inputTextFile.close()
    outputTextFile.close()


padStartStop('brown-train.txt', 'brown-train-padded.txt')
padStartStop('brown-test.txt', 'brown-test-padded.txt')
padStartStop('learner-test.txt', 'learner-test-padded.txt')


textFile = open('brown-train-padded.txt', 'r')
dictionary = dict()
for line in textFile:
    for word in line.split():
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
textFile.close()


inputTextFile = open('brown-train-padded.txt', 'r')
outputTextFile = open('brown-train-processed.txt', 'w')
for line in inputTextFile:
    for word in line.split():
        if dictionary[word] == 1:
            outputTextFile.write("<unk>" + " ")
        elif word == '</s>':
            outputTextFile.write(word)
        else:
            outputTextFile.write(word + " ")
    outputTextFile.write("\n")
inputTextFile.close()
outputTextFile.close()
