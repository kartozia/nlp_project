import re

file = open('my_emails.txt', 'r', encoding = 'utf-8')
text = file.read()

letters = re.findall('ЭТОМОЁПИСЬМОНОМЕР:([0-9]{1,4})(.+?)ЭТОКОНЕЦПИСЬМАНОМЕР:', text, flags = re.DOTALL)

def cleaner(text):
    
    return text

def splitter(text):
    words = text.split()
    for x in range(len(words)):
        words[x] = words[x].strip()
    return words

def sent_splitter(text):
    sent1 = ''
    for x in text:
        #print(x)
        while x != '.|!|?':
            sent1 += str(x)
    sent1 += x
    return sent1
    
print(letters[1][1])
print(sent_splitter(letters[1][1]))

def tag_checker(word):
    tag = ''
    cyr = re.search('[а-я]', word)
    lat = re.search('[a-z]', word)
    num = re.search('[0-9]', word)
    if cyr and lat and num:
        tag = 'super-lex-numb'
    elif cyr != None and lat == None and num == None:
        tag = 'cyr'
    elif cyr == None and lat != None and num == None:
        tag = 'lat'
    elif cyr != None and lat != None and num == None:
        tag = 'mixed'
    elif cyr == None and lat == None and num != None:
        tag = 'numbers'

    if word[0] == '#':
        tag += 'hashtag '
    elif re.seach('https://', word) == True:
        tag += 'link '
    else:
        pass
    return tag

def lang_checker_let(letter):
    lang = None
    cyr = re.search('[а-я]', word)
    lat = re.search('[a-z]', word)
    if cyr and lat:
        pass
    elif cyr != None and lat == None:
        lang = 'Russian'
    elif cyr == None and lat != None:
        de = re.seach('')
    return lang

class Token:
    def __init__(self, name = '', tag = '', lang = '', l_id = 0, t_id = 0):
        self.name = name
        self.lang = lang
        self.tag = tag
        self.l_id = letter
        self.t_id = t_id
    def output(self):
        print('Token ' +  str(self.t_id) +': \'' + self.name + '\'')
        print('Type: ' + self.tag)
        print('Language: ' + self.lang)
        print('Document: letter' + str(self.l_id))
        
def main(letters):
    t_id = 0
    tokens = []
    for x in range(len(letters)):
        l_id = x[0]
        letter = x[1]
        lang = lang_checker_let(letter)
        letter = cleaner(letter)
        words = splitter(letter)
        for w in words:
            t_id += 1
            if lang == None:
                lang = lang_checker(word)
            tag = tag_checker(word)
            token = Token(w, tag, lang, l_id, t_id)
            tokens.append(token)
