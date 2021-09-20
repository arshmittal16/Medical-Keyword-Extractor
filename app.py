import pandas as pd
import pkg_resources
from symspellpy import SymSpell, Verbosity
import nltk
import json
import os
from flask import Flask, jsonify, request

# app
app = Flask(__name__)

#script
def NER(text):
## Input Text
# text = "Hi Doctor, it was great meeting you yesterday. I took a Urine Test as specified. I am having chills, stomachache and nausea. I think I have a cancer. I took 3 paracetamol yesterday."

    ## Preprocessing Text
    import re
    import string
    text = re.sub(r"[\?\@\#\.\/\,\\$\^\*\'\[\]\=]"," ",text)

    ## Diseases Identification
    diseases = pd.read_csv('https://drive.google.com/uc?export=download&id=1ca0dWuCPX7bmkHE6CW5OTY3pQPequ005')
    diseases = diseases['3']
    dsbr = list(diseases)
    drgs = []
    frqs = []

    g = pd.Series(dsbr).value_counts() 
    g = g.to_dict() 
    for i in g.keys():
        drgs.append(i)
    for j in g.values():
        frqs.append(j)

    drgs = [str(each_string).lower() for each_string in drgs] 
    frqs = [str(each_string).lower() for each_string in frqs] 
    df = pd.DataFrame()
    df['Symptoms'] = drgs
    df['Frequencies'] = frqs

    df.to_csv('gcsv.txt',index=False)

    # replacing the comma with colon in the file to set it as a best and unique seperator
    inputFile = open("gcsv.txt", "r")
    exportFile = open("gcsv1.txt", "w")
    for line in inputFile:
        new_line = line.replace(',', ':') 
        exportFile.write(new_line) 

    inputFile.close()
    exportFile.close()

    with open('gcsv1.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('file1.txt', 'w') as fout:
        fout.writelines(data[1:])

    import nltk
    nltk.download('punkt')
    from nltk.tokenize import word_tokenize

    toks = []
    # storing all the word tokenized messages in a list 
    toks.append(word_tokenize(text))


    from itertools import islice
    import pkg_resources
    from symspellpy import SymSpell 
    # reading the dictionary file created above.
    sym_spell = SymSpell(prefix_length=7)
    dictionary_path = ("file1.txt")
    sym_spell.load_dictionary(dictionary_path, 0, 1,separator=':')

    # print(list(islice(sym_spell.words.items(), 5)))

    import nltk
    nltk.download('punkt')
    from nltk.util import ngrams

    unigrams = toks

    bigrams = []
    for wr in unigrams:
        if len(wr)<=1:
            bigrams.append([' '.join(wr)])
        else:
            ng = ngrams(wr, 2)
            bigrams.append([ ' '.join(grams) for grams in ng])

    trigrams = []
    for wr in unigrams:
        if len(wr)<=2:
            trigrams.append([' '.join(wr)])
        else:
            ng = ngrams(wr, 3)
            trigrams.append([ ' '.join(grams) for grams in ng])

    from tqdm import tqdm

    unigrams_2 = []
    for input_term in tqdm(unigrams):
        list_1 = []
    for x in input_term: 


    # input word given by the user
    # max edit distance per lookup 

        k = x.lower()
        suggestions = sym_spell.lookup(k, Verbosity.CLOSEST,
                                max_edit_distance=0) 
    #    print('--------',x,'--------') 
    # Getting suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
        
        #list_1.append((x,k,suggestion.term, suggestion.distance, suggestion.count))
    # storing only the original term when matched with any suggested term in the dictionary with edit distance 0
            list_1.append(x.lower()) 

    if len(list_1)!=0:
        unigrams_2.append(list_1)
    else:
        unigrams_2.append(['NA'])

    from tqdm import tqdm

    bigrams_2 = []
    for input_term in tqdm(bigrams):
        list_1 = []
    for x in input_term: 


    # input word given by the user
    # max edit distance per lookup 

        k = x.lower()
        suggestions = sym_spell.lookup(k, Verbosity.CLOSEST,
                                max_edit_distance=0)
    #    print('--------',x,'--------') 
    # Getting suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
    # storing only the original term when matched with any suggested term in the dictionary with edit distance 0
            list_1.append(x.lower())
    if len(list_1)!=0:
        bigrams_2.append(list_1)
    else:
        bigrams_2.append(['NA'])

    from tqdm import tqdm

    trigrams_2 = []
    for input_term in tqdm(trigrams):
        list_1 = []
    for x in input_term: 


    # input word given by the user
    # max edit distance per lookup 

        k = x.lower()
        suggestions = sym_spell.lookup(k, Verbosity.CLOSEST,
                                max_edit_distance=0)
    #    print('--------',x,'--------') 
    # Getting suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
    # storing only the original term when matched with any suggested term in the dictionary with edit distance 0
            list_1.append(x.lower())
    if len(list_1)!=0:
        trigrams_2.append(list_1)
    else:
        trigrams_2.append(['NA'])

    DISEASES = unigrams_2 + bigrams_2 + trigrams_2

    ##############################################################

    ## Symptoms Identification

    path = 'https://drive.google.com/uc?export=download&id=1GJe__IWxWk8oUd8h08GVBEPyyIelQyUC'
    symp = pd.read_csv(path)
    sybr = list(symp['Symptoms'])
    drgs = []
    frqs = []

    g = pd.Series(sybr).value_counts() 
    g = g.to_dict() 
    for i in g.keys():
        drgs.append(i)
    for j in g.values():
        frqs.append(j)

    drgs = [str(each_string).lower() for each_string in drgs] 
    frqs = [str(each_string).lower() for each_string in frqs] 
    df = pd.DataFrame()
    df['Symptoms'] = drgs
    df['Frequencies'] = frqs

    df.to_csv('gcsv.txt',index=False)

    inputFile = open("gcsv.txt", "r")
    exportFile = open("gcsv1.txt", "w")
    for line in inputFile:
        new_line = line.replace(',', ':') 
        exportFile.write(new_line) 

    inputFile.close()
    exportFile.close()

    with open('gcsv1.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('file1.txt', 'w') as fout:
        fout.writelines(data[1:])

    import nltk
    nltk.download('punkt')
    from nltk.tokenize import word_tokenize

    toks = []
    # storing all the word tokenized messages in a list 
    toks.append(word_tokenize(text))

    from itertools import islice
    import pkg_resources
    from symspellpy import SymSpell 
    # reading the dictionary file created above.
    sym_spell = SymSpell(prefix_length=7)
    dictionary_path = ("file1.txt")
    sym_spell.load_dictionary(dictionary_path, 0, 1,separator=':')

    # Print out first 5 elements to demonstrate that dictionary is
    # successfully loaded 
    # print(list(islice(sym_spell.words.items(), 5)))

    import nltk
    nltk.download('punkt')
    from nltk.util import ngrams

    unigrams = toks

    # making bigrams for the above sentances 
    bigrams = []
    for wr in unigrams:
        if len(wr)<=1:
            bigrams.append([' '.join(wr)])
        else:
            ng = ngrams(wr, 2)
            bigrams.append([ ' '.join(grams) for grams in ng])

    # making trigrams for the above sentances 
    trigrams = []
    for wr in unigrams:
        if len(wr)<=2:
            trigrams.append([' '.join(wr)])
        else:
            ng = ngrams(wr, 3)
            trigrams.append([ ' '.join(grams) for grams in ng])


    from tqdm import tqdm

    unigrams_2 = []
    for input_term in tqdm(unigrams):
        list_1 = []
    for x in input_term: 


    # input word given by the user
    # max edit distance per lookup 

        k = x.lower()
        suggestions = sym_spell.lookup(k, Verbosity.CLOSEST,
                                max_edit_distance=0) 
    #    print('--------',x,'--------') 
    # Getting suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
        
        #list_1.append((x,k,suggestion.term, suggestion.distance, suggestion.count))
    # storing only the original term when matched with any suggested term in the dictionary with edit distance 0
            list_1.append(x.lower()) 

    if len(list_1)!=0:
        unigrams_2.append(list_1)
    else:
        unigrams_2.append(['NA'])

    from tqdm import tqdm

    bigrams_2 = []
    for input_term in tqdm(bigrams):
        list_1 = []
    for x in input_term: 


    # input word given by the user
    # max edit distance per lookup 

        k = x.lower()
        suggestions = sym_spell.lookup(k, Verbosity.CLOSEST,
                                max_edit_distance=0)
    #    print('--------',x,'--------') 
    # Getting suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
    # storing only the original term when matched with any suggested term in the dictionary with edit distance 0
            list_1.append(x.lower())
    if len(list_1)!=0:
        bigrams_2.append(list_1)
    else:
        bigrams_2.append(['NA'])

    from tqdm import tqdm

    trigrams_2 = []
    for input_term in tqdm(trigrams):
        list_1 = []
    for x in input_term: 


    # input word given by the user
    # max edit distance per lookup 

        k = x.lower()
        suggestions = sym_spell.lookup(k, Verbosity.CLOSEST,
                                max_edit_distance=0)
    #    print('--------',x,'--------') 
    # Getting suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
    # storing only the original term when matched with any suggested term in the dictionary with edit distance 0
            list_1.append(x.lower())
    if len(list_1)!=0:
        trigrams_2.append(list_1)
    else:
        trigrams_2.append(['NA'])

    SYMPTOMS = unigrams_2 + bigrams_2 + trigrams_2

    ## Tests Identification

    path = 'https://drive.google.com/uc?export=download&id=1Ra0ywjBs1uOQugbCQQicH7IaqL_DiHe1'
    path1 = 'https://drive.google.com/uc?export=download&id=1dnf5xYC4tZnLkpShsd45I_zTeS23AFMT'

    t1 = pd.read_csv(path)
    t2 = pd.read_csv(path1)
    t1 = t1['Data File Description']
    t2 = t2['Tests']

    tests = pd.concat([t1, t2])
    test = list(tests)
    drgs = []
    frqs = []

    g = pd.Series(test).value_counts() 
    g = g.to_dict() 
    for i in g.keys():
        drgs.append(i)
    for j in g.values():
        frqs.append(j)

    drgs = [str(each_string).lower() for each_string in drgs] 
    frqs = [str(each_string).lower() for each_string in frqs] 

    df = pd.DataFrame()
    df['Tests'] = drgs
    df['Frequencies'] = frqs

    df.to_csv('gcsv.txt',index=False)

    inputFile = open("gcsv.txt", "r")
    exportFile = open("gcsv1.txt", "w")
    for line in inputFile:
        new_line = line.replace(',', ':') 
        exportFile.write(new_line) 

    inputFile.close()
    exportFile.close()

    with open('gcsv1.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('file1.txt', 'w') as fout:
        fout.writelines(data[1:])

    import nltk
    nltk.download('punkt')
    from nltk.tokenize import word_tokenize

    toks = []
    # storing all the word tokenized messages in a list 
    toks.append(word_tokenize(text))

    from itertools import islice
    import pkg_resources
    from symspellpy import SymSpell 
    # reading the dictionary file created above.
    sym_spell = SymSpell(prefix_length=7)
    dictionary_path = ("file1.txt")
    sym_spell.load_dictionary(dictionary_path, 0, 1,separator=':')

    # Print out first 5 elements to demonstrate that dictionary is
    # successfully loaded 
    # print(list(islice(sym_spell.words.items(), 5)))

    import nltk
    nltk.download('punkt')
    from nltk.util import ngrams

    unigrams = toks

    bigrams = []
    for wr in unigrams:
        if len(wr)<=1:
            bigrams.append([' '.join(wr)])
        else:
            ng = ngrams(wr, 2)
            bigrams.append([ ' '.join(grams) for grams in ng])

    trigrams = []
    for wr in unigrams:
        if len(wr)<=2:
            trigrams.append([' '.join(wr)])
        else:
            ng = ngrams(wr, 3)
            trigrams.append([ ' '.join(grams) for grams in ng])

    from tqdm import tqdm

    unigrams_2 = []
    for input_term in tqdm(unigrams):
        list_1 = []
    for x in input_term: 


    # input word given by the user
    # max edit distance per lookup 

        k = x.lower()
        suggestions = sym_spell.lookup(k, Verbosity.CLOSEST,
                                max_edit_distance=0) 
    #    print('--------',x,'--------') 
    # Getting suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
        
        #list_1.append((x,k,suggestion.term, suggestion.distance, suggestion.count))
    # storing only the original term when matched with any suggested term in the dictionary with edit distance 0
            list_1.append(x.lower()) 

    if len(list_1)!=0:
        unigrams_2.append(list_1)
    else:
        unigrams_2.append(['NA'])

    from tqdm import tqdm

    bigrams_2 = []
    for input_term in tqdm(bigrams):
        list_1 = []
    for x in input_term: 


    # input word given by the user
    # max edit distance per lookup 

        k = x.lower()
        suggestions = sym_spell.lookup(k, Verbosity.CLOSEST,
                                max_edit_distance=0)
    #    print('--------',x,'--------') 
    # Getting suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
    # storing only the original term when matched with any suggested term in the dictionary with edit distance 0
            list_1.append(x.lower())
    if len(list_1)!=0:
        bigrams_2.append(list_1)
    else:
        bigrams_2.append(['NA'])

    from tqdm import tqdm

    trigrams_2 = []
    for input_term in tqdm(trigrams):
        list_1 = []
    for x in input_term: 


    # input word given by the user
    # max edit distance per lookup 

        k = x.lower()
        suggestions = sym_spell.lookup(k, Verbosity.CLOSEST,
                                max_edit_distance=0)
    #    print('--------',x,'--------') 
    # Getting suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
    # storing only the original term when matched with any suggested term in the dictionary with edit distance 0
            list_1.append(x.lower())
    if len(list_1)!=0:
        trigrams_2.append(list_1)
    else:
        trigrams_2.append(['NA'])

    TESTS = unigrams_2 + bigrams_2 + trigrams_2


    ## Drugs Identifiation

    path = 'https://drive.google.com/uc?export=download&id=1DtyfrBQqr4FE_VO-OXlvJpnSTosid07u'
    drugs = pd.read_csv(path)

    drugs = drugs['drugs']

    drugs = list(drugs)

    drgs = []
    frqs = []

    g = pd.Series(drugs).value_counts() 
    g = g.to_dict() 
    for i in g.keys():
        drgs.append(i)
    for j in g.values():
        frqs.append(j)

    drgs = [str(each_string).lower() for each_string in drgs] 
    frqs = [str(each_string).lower() for each_string in frqs] 

    df = pd.DataFrame()
    df['Drugs'] = drgs
    df['Frequencies'] = frqs
    df.to_csv('gcsv.txt',index=False)

    inputFile = open("gcsv.txt", "r")
    exportFile = open("gcsv1.txt", "w")
    for line in inputFile:
        new_line = line.replace(',', ':') 
        exportFile.write(new_line) 

    inputFile.close()
    exportFile.close()

    with open('gcsv1.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('file1.txt', 'w') as fout:
        fout.writelines(data[1:])

    import nltk
    nltk.download('punkt')
    from nltk.tokenize import word_tokenize

    toks = [] 
    toks.append(word_tokenize(text))

    from itertools import islice
    import pkg_resources
    from symspellpy import SymSpell 
    # reading the dictionary file created above.
    sym_spell = SymSpell(prefix_length=7)
    dictionary_path = ("file1.txt")
    sym_spell.load_dictionary(dictionary_path, 0, 1,separator=':')

    # Print out first 5 elements to demonstrate that dictionary is
    # successfully loaded 
    # print(list(islice(sym_spell.words.items(), 5)))

    import nltk
    nltk.download('punkt')
    from nltk.util import ngrams

    unigrams = toks

    bigrams = []
    for wr in unigrams:
        if len(wr)<=1:
            bigrams.append([' '.join(wr)])
        else:
            ng = ngrams(wr, 2)
            bigrams.append([ ' '.join(grams) for grams in ng])

    trigrams = []
    for wr in unigrams:
        if len(wr)<=2:
            trigrams.append([' '.join(wr)])
        else:
            ng = ngrams(wr, 3)
            trigrams.append([ ' '.join(grams) for grams in ng])

    from tqdm import tqdm

    unigrams_2 = []
    for input_term in tqdm(unigrams):
        list_1 = []
    for x in input_term: 


    # input word given by the user
    # max edit distance per lookup 

        k = x.lower()
        suggestions = sym_spell.lookup(k, Verbosity.CLOSEST,
                                max_edit_distance=0) 
    #    print('--------',x,'--------') 
    # Getting suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
        
        #list_1.append((x,k,suggestion.term, suggestion.distance, suggestion.count))
    # storing only the original term when matched with any suggested term in the dictionary with edit distance 0
            list_1.append(x.lower()) 

    if len(list_1)!=0:
        unigrams_2.append(list_1)
    else:
        unigrams_2.append(['NA'])

    from tqdm import tqdm

    bigrams_2 = []
    for input_term in tqdm(bigrams):
        list_1 = []
    for x in input_term: 


    # input word given by the user
    # max edit distance per lookup 

        k = x.lower()
        suggestions = sym_spell.lookup(k, Verbosity.CLOSEST,
                                max_edit_distance=0)
    #    print('--------',x,'--------') 
    # Getting suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
    # storing only the original term when matched with any suggested term in the dictionary with edit distance 0
            list_1.append(x.lower())
    if len(list_1)!=0:
        bigrams_2.append(list_1)
    else:
        bigrams_2.append(['NA'])

    from tqdm import tqdm

    trigrams_2 = []
    for input_term in tqdm(trigrams):
        list_1 = []
    for x in input_term: 


    # input word given by the user
    # max edit distance per lookup 

        k = x.lower()
        suggestions = sym_spell.lookup(k, Verbosity.CLOSEST,
                                max_edit_distance=0)
    #    print('--------',x,'--------') 
    # Getting suggestion term, edit distance, and term frequency
        for suggestion in suggestions:
    # storing only the original term when matched with any suggested term in the dictionary with edit distance 0
            list_1.append(x.lower())
    if len(list_1)!=0:
        trigrams_2.append(list_1)
    else:
        trigrams_2.append(['NA'])

    DRUGS = unigrams_2 + bigrams_2 + trigrams_2

    ## Lists Making:

    d = []
    s = []
    t = []
    dr = []

    for i in DISEASES:
        for j in i:
            if j not in d:
                d.append(j)

    for i in SYMPTOMS:
        for j in i:
            if j not in s:
                s.append(j)

    for i in TESTS:
        for j in i:
            if j not in t:
                t.append(j)

    for i in DRUGS:
        for j in i:
            if j not in dr:
                dr.append(j)

    if len(d)!=1:
        d.remove('NA')
    
    if len(s)!=1:
        s.remove('NA')

    if len(t)!=1:
        t.remove('NA')

    if len(dr)!=1:
        dr.remove('NA')

    dic = {'Diseases Found:': d,
            'Symptoms Found:': s,
            'Tests Found:':t,
            'Drugs Found:': dr}

    js = json.dumps(dic)

    return js


# routes
@app.route('/gg/<text>', methods=['GET'])

def predict(text):
    # output = {'results': 123}
    # text="Hello i am Doctor with chills stomachach kidney failure paracetamol headache dolo easy";
    output=NER(text)
    # return data
    # output = 
    return jsonify(results=output)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

if __name__ == '__main__':
    app.run(port = 5000, debug=True)