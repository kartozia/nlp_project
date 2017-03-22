import re

#дефисы типа Поезд Москва-Петербург, девочка-одуванчик

def cleaner(text):
    lines0 = text.split('\\n')
    n = 0
    lines = []
    for i in lines0:
        if i != '':
            lines.append(i)
    i = 0
    while i != len(lines):
        if len(re.findall('[0-9]*:[0-9]* пользователь', lines[i])) > 0:
            break
        i += 1
    lines = lines[:i]
    lines_str = ''
    for i in lines:
        lines_str += i
        lines_str += ' '
    return lines_str

def splitter(text):
    words = text.split()
    for x in range(len(words)):
        words[x] = words[x].strip('!)(;,\":-?')
        #words[x] = strip_dot(words[x])
        for i in words:
            if i == '':
                del i
        for i in words:
            if len(re.findall('--', i)) > 0:
                re.sub('--', '-', i)
    return words

def sent_splitter(text):
    sent1 = ''
    for x in text:
        while x != '.|!|?':
            sent1 += str(x)
    sent1 += x
    return sent1
    
def tag_checker(word):
    tag = ''
    if word == '' or word == None:
        tag = 'empty'
    else:
        cyr = re.search('[а-я]|[А-Я]', word)
        lat = re.search('[a-z]|[A-Z]', word)
        num = re.search('[0-9]', word)
        if cyr and lat and num:
            tag = 'super-lex-numb'
        elif cyr != None and lat == None and num == None:
            tag = 'cyr'
            initial = re.search('([А-Я]{1})\.([А-Я]{1})\.', word)
            if initial:
                tag += ' initial'
        elif cyr == None and lat != None and num == None:
            tag = 'lat'
        elif cyr != None and lat != None and num == None:
            tag = 'mixed'
        elif cyr != None and lat == None and num != None:
            tag = 'cyr-num'
        elif cyr == None and lat == None and num != None:
            tag = 'numbers'
            time =  re.search('[0-9]{2}\:[0-9]{2}', word)
            if time:
                tag = 'time'
            date = re.search('([0-9]{1,2}(\:|\.|\-| )[0-9]{1,2}(\:|\.|\-| )[0-9]{2})|([0-9]{1,2}(\:|\.|\-| )[0-9]{1,2}(\:|\.|\-| )[0-9]{4})', word)
            if date:
                tag = 'date'
            phone = re.search('(8|\+7)([0-9]{10})|([0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2})', word)
            if phone:
                tag = 'phone'
            nazv = re.search('«.{,15}?»', word)
            if nazv:
                tag = 'name of smth'
        

        if word[0] == '#':
            tag += ' hashtag '
        elif word[0] == '@':
            tag += ' @-tag'
        link = re.search('http(s)://', word)
        if link:
            tag = 'link '
        mail = re.search('.+?@[a-z]{3,7}\.[a-z]{2,3}', word)
        if mail:
            tag = 'mail'
    if tag == '':
        tag = 'something'
    return tag

def lang_checker_let(letter):
    lang = None
    cyr = re.search('[а-я]', letter)
    lat = re.search('[a-z]', letter)
    if cyr and lat:
        pass
    elif cyr != None and lat == None:
        lang = 'Russian'
    #elif cyr == None and lat != None:
       # de = re.seach('')
    return lang

class Token:
    def __init__(self, name = '', tag = '', t_id = 0, l_id = 0, lang = ''):
        self.name = name
        self.lang = lang
        self.tag = tag
        self.l_id = l_id
        self.t_id = t_id
    def output(self):
        return str('\nToken ' +  str(self.t_id) +': \'' + self.name + '\' \nType: ' + self.tag + '\nDocument: letter' + str(self.l_id) + '\n')

def main(letters):
    t_id = 0
    tokens = []
    for x in letters:
        l_id = x[0]
        letter = x[1]
        lang = lang_checker_let(letter)
        letter = cleaner(letter)
        words = splitter(letter)
        for word in words:
            t_id += 1
            #if lang == None:
                #lang = lang_checker(word)
            tag = tag_checker(word)
            token = Token(word, tag, lang, t_id, l_id)
            tokens.append(token)
    return tokens

def main_test(text):
    t_id = 0
    tokens = []
    l_id = 0
    letter = cleaner(text)
    words = splitter(letter)
    for word in words:
        t_id += 1
        tag = tag_checker(word)
        token = Token(word, tag, t_id, l_id)
        tokens.append(token)
    return tokens

file1 = open('ling_emails.txt', 'r', encoding = 'utf-8')
text1 = file1.read()
letters = re.findall('ЭТОМОЁПИСЬМОНОМЕР:([0-9]{1,4})(.+?)ЭТОКОНЕЦПИСЬМАНОМЕР:', text, flags = re.DOTALL)
file2 = open('test.txt', 'r', encoding = 'utf-8')
text2 = file.read()

tokens1 = main(letters)
tokens2 = main_test(text2)
