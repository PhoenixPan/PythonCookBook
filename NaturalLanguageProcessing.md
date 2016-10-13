```
import re

def load_federalist_corpus(filename):
    """ Load the federalist papers as a tokenized list of strings, one for each eassay"""
    with open(filename, "rt") as f:
        data = f.read()
    papers = data.split("FEDERALIST")
    
    # all start with "To the people of the State of New York:" (sometimes . instead of :)
    # all end with PUBLIUS (or no end at all)
    locations = [(i,[-1] + [m.end()+1 for m in re.finditer(r"of the State of New York", p)],
                 [-1] + [m.start() for m in re.finditer(r"PUBLIUS", p)]) for i,p in enumerate(papers)]
    papers_content = [papers[i][max(loc[1]):max(loc[2])] for i,loc in enumerate(locations)]

    # discard entries that are not actually a paper
    papers_content = [p for p in papers_content if len(p) > 0]

    # replace all whitespace with a single space
    papers_content = [re.sub(r"\s+", " ", p).lower() for p in papers_content]

    # add spaces before all punctuation, so they are separate tokens
    punctuation = set(re.findall(r"[^\w\s]+", " ".join(papers_content))) - {"-","'"}
    for c in punctuation:
        papers_content = [p.replace(c, " "+c+" ") for p in papers_content]
    papers_content = [re.sub(r"\s+", " ", p).lower().strip() for p in papers_content]
    
    authors = [tuple(re.findall("MADISON|JAY|HAMILTON", a)) for a in papers]
    authors = [a for a in authors if len(a) > 0]
    
    numbers = [re.search(r"No\. \d+", p).group(0) for p in papers if re.search(r"No\. \d+", p)]
    
    return papers_content, authors, numbers
        
papers, authors, numbers = load_federalist_corpus("pg18.txt")
```


```
import collections # optional, but we found the collections.Counter object useful
import scipy.sparse as sp
import numpy as np

def tfidf(docs):
    """
    Create TFIDF matrix.  This function creates a TFIDF matrix from the
    docs input.

    Args:
        docs: list of strings, where each string represents a space-separated
              document
    
    Returns: tuple: (tfidf, all_words)
        tfidf: sparse matrix (in any scipy sparse format) of size (# docs) x
               (# total unique words), where i,j entry is TFIDF score for 
               document i and term j
        all_words: list of strings, where the ith element indicates the word
                   that corresponds to the ith column in the TFIDF matrix
    """
    from collections import Counter
    cnt = Counter()
    dict_occurances = {}
    for doc in docs:
        cnt = cnt + Counter(doc.split())
        for each in Counter(doc.split()):
            if dict_occurances.has_key(each):
                dict_occurances[each] += 1
            else:
                dict_occurances[each] = 1
                
    all_words = []
    for word in cnt.items():
        all_words.append(word[0])
          
    # 86 words in all docs
    oooo = 0
    for each in dict_occurances:
        if dict_occurances[each] == len(docs):
            oooo += 1
    print oooo
    
    all_words = []
    for key in dict_occurances:
        all_words.append(key)
        
    import math
    denominator = float(len(docs))
    idf = {}
    for word in all_words:
        this_idf = math.log(denominator/dict_occurances[word])
        idf[word] = this_idf
    
    row = []
    col = []
    data = []
    row_count = 0
    col_count = 0
    for doc in docs:
        doc_words = doc.split()
        tf = Counter(doc_words)
        counter_words = []
        for word in all_words:
            tfdif = idf[word] * tf[word]
            if word in doc_words and tfdif != 0:
                row.append(row_count)
                col.append(col_count)
                data.append(tfdif)
            col_count += 1
        row_count += 1
        col_count = 0
    
    coo = sp.coo_matrix((data, (row, col)))
    
    return coo, all_words

data = [
    "the goal of this lecture is to explain the basics of free text processing",
    "the bag of words model is one such approach",
    "text processing via bag of words"
]
# Test 1
X_tfidf, words = tfidf(data)
print X_tfidf.todense()
print words

# Test 2
X_tfidf, words = tfidf(papers)
print X_tfidf.nnz

```
