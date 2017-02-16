 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import os.path
import json
import random
import codecs
import sys

listOfDictionaries = [{}]
wordCount = {}

def importArrays(id = 'C323206de5fa67be8fa53b1474c5f6023'):
    lod = 'ListOfDictionaries.json'
    tempString = ''
    words = []
    i = 0
    groupId = id

    """
    if os.path.isfile(lod):
        return 0
    else:
    """
    log = ''
    if id != 'C323206de5fa67be8fa53b1474c5f6023' and id is not None:#Useless
        log = open('log.txt', 'r')
    else:
        log = open('log.txt', 'r')
    messageLog = log.read()

    for letter in messageLog:
        if letter != ' ' and letter != '\n':
            tempString += letter
        else:
            if len(tempString) != 0:
                if tempString[0] == '`' and tempString[len(tempString) - 1] == '`':
                    words.append(tempString[1:])
                else:
                    words.append(tempString)
            else:
                continue
            tempString = ''
    words.append(tempString)
        
    while True:
        pair = words[i:i+2]
        if len(pair) == 1:
            break
        if pair[0] in listOfDictionaries[0] and listOfDictionaries[0][pair[0]][0] == pair[1]:
            listOfDictionaries[0][pair[0]][1] += 1
        elif pair[0] in listOfDictionaries[0]:
            listOfDictionaries.append({pair[0]:[pair[1],1]})
        else:
            listOfDictionaries[0][pair[0]] = [pair[1],1]
        if i >= len(words) - 1:
            break
        else:
            i += 1

    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
            
    with open('ListOfDictionaries.json', 'w') as fp:
        json.dump(listOfDictionaries, fp, ensure_ascii=False)

    with open('WordCount.json', 'w') as wc:
        json.dump(wordCount, wc, ensure_ascii = False)


def createChain():
    starterWords = []
    currentWord = ''
    chain = ''
    
    f = open('ListOfDictionaries.json', 'r')
    listOfDictionaries = json.load(f)
    f.close()

    for word in listOfDictionaries[0].keys():
        #print(len(word))
        #print(listOfDictionaries[0])
        try:
            if word[0] == "`":
                starterWords.append(word)
        except Exception:
                print('error')
    try:
        currentWord = random.sample(starterWords, 1)[0]
    except Exception, e:
        currentWord = starterWords.pop()
    chain += currentWord + ' '
    #print currentWord + ' ~~~~~~'


    while True:
        listOfProbableWords = []

        for i in range(0, len(listOfDictionaries)):
            if currentWord in listOfDictionaries[i]:
                for k in range(1, listOfDictionaries[i][currentWord][1] + 1):
                    if currentWord in listOfDictionaries[i]:
                        for repeat in range(0,10):
                            listOfProbableWords.append(listOfDictionaries[i][currentWord][0])
        try:
            randomWord = random.sample(listOfProbableWords, 1)[0]
        except Exception, e:
            randomWord = listOfProbableWords.pop()

        
        currentWord = randomWord
        chain += currentWord + ' '
        lastChar = currentWord[len(currentWord) - 1]
        firstChar = currentWord[0]

        if lastChar == '`' or firstChar == '`':
            print chain[1:-2]
            break
            
    outputfile = open('chain.txt', 'w')
    outputfile.write(chain[1:-2])
    outputfile.close()
    return chain[1:-2]

def run(id = 'shakespeare'):
    importArrays(id)
    chain = createChain()
    return chain
            
if __name__ == '__main__':
    importArrays('log.txt')
    createChain()
