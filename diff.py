
import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher
#creating matching object
from csv import writer
from csv import reader
nlp = spacy.load('en_core_web_sm')
phrase_matcher = PhraseMatcher(nlp.vocab)
phrase_matcher2 = PhraseMatcher(nlp.vocab)
i=0
opphrase = ['define','who','what','name','list','label','locate',
            'match','mention','when','which','can you','can we',
            'examples','syntax','where']

opphrase2 = ['how','explain','interpret','describe','summarize',
            'justify','do you know','why','write a code','brief','can','write'
            'implement','differentiate','between','difference','compare','different'
            'solve','program','write a code','write a program','develop','evaluate',
            'construct','build','code']

patterns1 = [nlp(text) for text in opphrase]
patterns2 = [nlp(text) for text in opphrase2]
df = pd.read_csv('all_questions.csv')

phrase_matcher.add('1',None,*patterns1)
phrase_matcher2.add('2',None,*patterns2)
sent = ''
matched_phrase = []
for i in range(len(df)):
    sent = df.loc[i,'Questions'].lower()
    newsent = nlp(sent)
    if phrase_matcher(newsent)!= []:
        matched_phrase.append(phrase_matcher(newsent))
        df.loc[i,'Difficulty'] = '1'
        df.to_csv('all_questions.csv',index=False)

    if phrase_matcher2(newsent)!=[]:
        df.loc[i,'Difficulty'] = '2'
        df.to_csv('all_questions.csv',index=False)   
        
            
print("DOne")
#print(df.loc[2,'Questions'].lower())