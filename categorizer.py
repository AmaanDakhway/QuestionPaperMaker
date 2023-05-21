import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher
import csv


df = pd.read_csv('all_questions.csv')


nlp = spacy.load('en_core_web_sm')

phrase_matcher1 = PhraseMatcher(nlp.vocab)
phrase_matcher2 = PhraseMatcher(nlp.vocab)
phrase_matcher3 = PhraseMatcher(nlp.vocab)
phrase_matcher4 = PhraseMatcher(nlp.vocab)

i=0

mlphrase = ['machine learning','deep learning','decision tree','regression',
            'neural network','supervised','unsupervised','classification','nlp',
            'types of machine learning','clustering','natural language processing',
            'artificial intelligence','ai','ann','ml','hanoi','expert system','turing',
            'a*','breadth-first search','depth-first search','uniform cost','pruning',
            'partial-order planning','naive bayes','agents','environment','bidirectional',
            'iterative deepening','fuzzy logic','fopl','deep learning','k-means']

osphrase = ['linux','operating system','bash','dos','file permission',
            'yum','file system','directory','linux command','unix','kernel system',
            'running process','cli','gui','user modes','linux shell','linux server',
            'process management','scheduling','process state model','distributed operating system',
            'network operating system','embedded','file access','file system','allocation method',
            'free space', 'mass storage','scheduling','raid','memory management','swapping',
            'contigious memeory allocation','paging','page table','segmentation','virtual memory',
            'demand paging','page replacement','thrashing','inter-process communication','synchronization',
            'race','critical region','message passing','deadlock','deadlock characterization','detection','recovery',
            'prevention','avoidance','process','state model','context switching','threads',
            'scheduling','long term','short term','job scheduler','cpu scheduler','preemptive','non preemtive',
            'first come first serve','fcfs','shortest job first','sjf','longest remaining time first','lrtf',
            'round robin','starvation','aging','critical section','inter process communication',
            'semaphores','resourse allocation graph','rag','banker','page table','batch','time sharing',
            'distributed','network operating','os',]

sqlphrase = ['sql','mysql','sql command','database management system','primary key','oracle',
            'unique key','foreign key','entities and relationship','sql server','acid',
            'joins','view in sql','delete command','select command','olap','oltp','dba',
            'data normalization','ordbms','table','oracle grid','mongodb','collection',
            'aggregation','crud','sql syntax','relational database','nosql','couchdb',
            'dbms','rdbms','normalization','denormalization','joins in sql', 'database',
            'data abstraction','data independence','dba', 'database adminitrator','entity',
            'attributes', 'keys','primary key','secondary key','weak entity','generalization',
            'specialization','Aggregation','realtional model','schemas','foreign key',
            'data definition','ddl','set operation','data manipulation','dml','data control','dcl',
            'integrity constraints', 'relational schema','grant','revoke','1nf','2nf','3nf','tcl',
            'acid','default constraint','constraint','index','indexes','entities','delete','truncate',
            'views','inner join','outter join','self join','join','union','having clause','where clause',
            'databases','groupby','group by','trigger','commit','rollback','savepoint','aggregate',
            'like','']

dsphrase = ['data structure','binary tree','linked list','stack','fifo','binary search tree',
            'data abstraction','non-linear data','linear data','lifo','merge sort','selection sort',
            'bubble sort','avl','queue','dfs','bfs','sorting algorithm','graph']

patterns1 = [nlp(text) for text in mlphrase]
phrase_matcher1.add('AI',None,*patterns1)

patterns2 = [nlp(text) for text in osphrase]
phrase_matcher2.add('OS',None,*patterns2)

patterns3 = [nlp(text) for text in sqlphrase]
phrase_matcher3.add('SQL',None,*patterns3)

patterns4 = [nlp(text) for text in dsphrase]
phrase_matcher4.add('DS',None,*patterns4)

sent = ''
for i in range(len(df)):
    sent = df.loc[i,'Questions'].lower()
    newsent = nlp(sent)
    if phrase_matcher1(newsent)!=[]:
        df.loc[i,'Category'] = 'AI'
        df.to_csv('all_questions.csv',index=False)
        ai = df[df['Category']=='AI']
        ai.to_csv('ai.csv', index=False)
            
    elif phrase_matcher2(newsent)!=[]:
        df.loc[i,'Category'] = 'OS'
        df.to_csv('all_questions.csv',index=False)
        os = df[df['Category']=='OS']
        os.to_csv('os.csv', index=False)
            
    elif phrase_matcher3(newsent)!=[]:
        df.loc[i,'Category'] = 'SQL'
        df.to_csv('all_questions.csv',index=False)
        sql = df[df['Category']=='SQL']
        sql.to_csv('sql.csv', index=False)
            
    elif phrase_matcher4(newsent)!=[]:
        df.loc[i,'Category'] = 'DS'
        df.to_csv('all_questions.csv',index=False)
        ds = df[df['Category']=='DS']
        ds.to_csv('ds.csv', index=False)
            
    else:
        df.loc[i,'Category'] = 'Other'
        df.to_csv('all_questions.csv',index=False)
        other = df[df['Category']=='Other']
        other.to_csv('other.csv', index=False)
print('Done')
