import os, re

def mystem_1():
    text = 'C:' + os.sep + 'Users' + os.sep + 'Note' + os.sep +  'alexandra' + os.sep + 'anna_kar.txt'
    new = 'C:' + os.sep + 'Users' + os.sep + 'Note' + os.sep + 'alexandra' + os.sep + 'annakar_new.txt'
    os.system ('C:\mystem.exe ' + text + ' ' + new + ' -nd')
    return new

def function1(new):
    f = open ('C:/Users/Note/alexandra/annakar_new.txt', 'r', encoding = 'utf-8')
    f.readlines()
    sql_file = open ('C:/Users/Note/alexandra/anna_kar.sql', 'a', encoding = 'utf-8')
    sql_file.write('CREATE TABLE Lemmas (id INTERGER PRIMARY KEY, slovoforma VARCHAR(100), lemma VARCHAR(100);\n')
    
    dictionary = {}
    
    for line in f:
        res = re.search ('(.*?){(.*?)}', 'f')
        if res:
            slovoforma = res.group(1)
            if slovoforma not in dictionary:
                dictionary[slovoforma] = i
                i = 0
                lemma = res.group(2)
                sql_file.write ('INSERT INTO Lemmas (id, slovoforma, lemma) VALUES (' + str(i) + ',\'' + word + ',\'' + ',\'' + ',' + lemma + ');\n')
                i += 1

    sql_file.close
    return dictionary
            
def function2(new):
    f = open ('C:/Users/Note/alexandra/annakar_new.txt', 'r', encoding = 'utf-8')
    f.readlines()
    sql_file = open ('C:/Users/Note/alexandra/anna_kar.sql', 'a', encoding = 'utf-8')
    sql_file.write('CREATE TABLE Commonlemmas (id INTERGER PRIMARY KEY, slovoforma VARCHAR(100), number_sl VARCHAR(100), number_l VARCHAR(100), lemma VARCHAR(100);\n')

    i = 0
    
    for word in f:
        for key in dictionary:
            if key == word:
                sql_file.write ('INSERT INTO Commonlemmas (id, slovoforma, number_sl, number_l) VALUES (' + str(i) + ',\'' + word + ',\'' + ',' + str(f[key]) + ', ' + str(i+1) + ');\n')
                i += 1
    f.close
    sql_file.close
    

def main():
    mystem_1()
    function2 (function1 (mystem_1()))
    

if __name__ == '__main__':
    main()
             
