punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip()) 
def strip_punctuation(s):
    for i in s: 
        if i in punctuation_chars:
            s=s.replace(i,"")
    return s
def get_pos(x):
    a=x.split() 
    c=0
    for i in a:
        i=i.lower() 
        i=strip_punctuation(i)
        if i in positive_words:
            c+=1
    return c 
def get_neg(x):
    a=x.split() 
    c=0
    for i in a:
        i=i.lower() 
        i=strip_punctuation(i)
        if i in negative_words:
            c+=1
    return c 
f=open("project_twitter_data.csv","r") 
g=open("resulting_data.csv","w") 
g.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
bg=f.readlines() 
for i in range(1,len(bg)):
    words=bg[i].split(',') 
    string=words[0]
    no_tweets=int(words[1])
    no_replies=int(words[2])
    pos=get_pos(string)
    neg=get_neg(string)
    diff=pos-neg 
    g.write('{},{},{},{},{}'.format(no_tweets,no_replies,pos,neg,diff)) 
    g.write('\n')
f.close()
g.close()
