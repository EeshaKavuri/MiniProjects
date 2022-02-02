papers = {'Madison':[10,14,37,

def read_files(filename):
    strings = []
    for file in filename:
        with open(f'federalist_{file}.txt') as f:
            strings.append(f.read())

    return ('\n'.join(strings))

federalist_by_author = {}
for author,files in papers.items():
    federalist_by_author[author] = read_files(files)

for author in aperes:
    print(federalist_by_author[author][:100])

authors = ('Hamilton','Madison','Disrupted','Jay','Shared')
author_tokens = {}
length_distrbution = {}

for author in authors:
    tokens=nltk.worf_tokenize(federalist_by_author[author])
    author_tokens[author] = ([token for 
    
