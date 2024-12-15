sentence="""With our sentence examples, seeing a word within
the context of a sentence helps you better understand it and know how to
use it correctly. From long to short, simple to complex, this tool
can assist you with how to use words that may have more than one meaning."""
punct=['.',',',':',';','"',"'"]
for e in punct:
    if e in sentence:
        sentence = sentence.replace(e,'')
pool = [word.strip() for word in sentence.split()]
wordset = list(set(pool))

dic = {word:pool.count(word) for word in wordset}
res = sorted(dic.items(), key=lambda x:x[1], reverse=True) # (단어, 반복횟수) 사전에서 반복횟수(x[1])을 기준으로 내림차순으로 정렬
for key, value in res:
    print(f'{key}: {value}')