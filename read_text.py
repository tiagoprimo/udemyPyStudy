# read two text files, finding the repetitive words.
import urllib

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


#esta função acessa um conteúdo da internet, assim como temos o open para aquivos do HD, temos urrlib.open para conteudos internet
def check_profanity(text_to_check):
    connection = urllib.urlopen()
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print ("Documento encontrado ou retorno verdade de uma API")
    elif "false" in output:
        print ("Documento não encontrado ou retorno falso de uma API")
    else:
        print ("Não consegui abrir o documento")



read_text()

