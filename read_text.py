
def read_text():
    #text = open("/Users/tiagoprimo/Google Drive/Primo Backup/Softwares Desenvolvidos/UdemyStudy/udemyPyStudy/text")
    #contents_of_file = text.read()
    #print(contents_of_file)

    found_words = list()

    for line in open("text"):
        words = line.split()
        #print(words)
        for i in range(len(words)):
            if match_with_dictionary_of_words(words[i]):
                #print("Achei a palavra: " + words[i])
                found_words.append([words[i]])

    for item in found_words:
        print(item)


def match_with_dictionary_of_words(word):
    for line in open("dictionaryofwords"):
        dictionary = line.split()
        #print(dictionary)
        for i in range(len(dictionary)):
            if dictionary[i] == word:
                return True;

read_text()

