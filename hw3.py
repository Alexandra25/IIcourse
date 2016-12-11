import urllib.request
import re

#массив с ссылками на новости
mas = ['https://russian.rt.com/nopolitics/news/339692-garri-potter-rossiya',
      'http://echo.msk.ru/news/1887792-echo.html',
       'http://tass.ru/kultura/3846920',
       'http://7info.ru/news/world-culture/vyshel_novyj_garri_potter/']

#массив с регулярками
masreg = ['class="article__summary ">(.*?)<div class="rtcode">',
          '<span class="_ga1_on_ include-relap-widget contextualizable">(.*?)<div class="actionBlock" id="e1887792">',
          'js-mediator-article">(.*?)<div class="extra-content">',
          '"yandexContextAsyncCallbacks".;(.*?)<script type="text/javascript"']

#пустой массив для записи текстов новостей
mastext = []

#запись html и чистка от тегов и т.д.
for i in range(0,4):
    req = urllib.request.Request(mas[i])
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    regText = re.compile (masreg[i], re.DOTALL)
    text1 = regText.findall(html)
    text = text1[0]
    regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
    regSpace = re.compile('\s{2,}', flags=re.U | re.DOTALL)
    regSign = re.compile('&.*?;', flags=re.U | re.DOTALL)
    clean_t = regSpace.sub("", text)
    clean_t = regTag.sub("", clean_t)
    clean_t = regSign.sub("", clean_t)
    mastext.append(clean_t)
    
#пустой массив для словоформ
masword = []

#разделение текстов на слова, добавление в массив слов
for text in mastext:
    text = text.lower()
    txt = text.split()
    items = set()
    for word in txt:
        word = word.strip(' ,.?')
        items.add(word)
    masword.append(items)

#пересечение множеств, общие словоформы
a = masword[0] & masword[1] & masword[2] & masword[3]

b = set()
c = set()
for i in range(0, 4):
    for el in masword[i]:
        if el not in b:
            b.add(el)
        else:
            c.add(el)

#разность множеств, уникальные словоформы
d = b - c

#запись результатов в файлы
file1 = open("commonwords", "w")
file1.write(sorted(a))
file1.close()

file2 = open("uniquewords", "w")
file2.write(sorted(d))
file2.close()
    
          
