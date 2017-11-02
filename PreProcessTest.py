textFile = open('brown-train.txt', 'r')
textFile2 = open('brown-train-padded.txt', 'w')
for line in textFile:
    lineEdited = "<s> " + line.replace('\n', ' </s> \n')
    textFile2.write(lineEdited.lower())
textFile.close()
textFile2.close()



textFile = open('brown-train-padded.txt', 'r')
dictionary = dict()
for line in textFile:
    for word in line.split():
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
textFile.close()
textFile = open('brown-train-padded.txt', 'r')
textFile2 = open('brown-train-processed.txt', 'w')
for line in textFile:
    for word in line.split():
        if dictionary[word] == 1:
            textFile2.write("<unk>" + " ")
        else:
            textFile2.write(word + " ")
    textFile2.write("\n")
textFile.close()
textFile2.close()