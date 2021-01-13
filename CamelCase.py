#this progrma asks users to enter string then changes first letter 
#of each word to capital
#then displays it

#this function asks users to enter string then returns it
def get_sentence():
    print('enter sentence: ')
    sentence=input()
    return sentence

#splits the sentence and returns words as list
def split_sentence(sentence):
    words=sentence.split()
    return words

#changes each word's first letter to capital and returns it as list
def modify(words):
    camelCase=[]
    for word in words:
        camelCase.append(word.capitalize())
    return camelCase

# adds word list as string and displays it
def display_sentence(camelcase):
    #for word in camelcase:
        #print(word)
    string=''
    for word in camelcase:
        string+=word
    print(string)

def main():
    sentence=get_sentence()
    words=split_sentence(sentence)  
    camelCase=modify(words)
    display_sentence(camelCase)

main()