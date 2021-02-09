import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
predata=pd.read_excel(r"C:\Users\ASUS\Desktop\代码\美赛\C题\2021_MCM_Problem_C_Data\2021_MCM_Problem_C_Data\2021MCMProblemC_DataSet.xlsx")
"""
#4440 all//58 <2019/3 NULL/11 format mistake
fig=plt.figure(figsize=(20, 6.5))
# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axis('equal')
labels=['normal','ages ago','NULL and format mistake']
sizes=[4368,58,14]
explode=tuple([0.1] * 3)
patches,l_text,p_text=plt.pie(sizes, explode=explode,labels=labels, shadow=True,autopct='%1.1f%%')
# l_text是饼图对着文字大小，p_text是饼图内文字大小
for t in p_text:
    t.set_size(5)
for t in l_text:
    t.set_size(6)
plt.title('Validornot',fontdict = {'family' : 'SimHei',
'weight' : 'normal',
'size'   : 30,
})
plt.legend(['normal','ages ago','NULL and format mistake'])

plt.savefig('null')
plt.show()
"""
"""
predata=predata[(predata['Lab Status']=='Positive ID') | (predata['Lab Status']=='Negative ID')]
predata=pd.DataFrame(predata)

predata['Detection Date'].apply(lambda x:print(str(x).split()[0].split('-')[2]))
predata['day'] = predata['Detection Date'].apply(lambda x:str(x).split()[0].split('-')[2]).astype('int')

predata['month'] = predata['Detection Date'].apply(lambda x:str(x).split()[0].split('-')[1]).astype('int')
predata['DateTime'] = predata['Detection Date'].apply(lambda x:str(x).split()[0])
predata['weekday'] = predata['DateTime'].apply(lambda x: datetime.datetime.strptime(str(str(x).split('-')[0] + '-' + str(x).split('-')[1] + '-' + str(x).split('-')[2]), '%Y-%m-%d').isoweekday())
predata['isweekend'] = predata['weekday'].apply(lambda x:x/6).astype('int')
predata = predata.drop(['Detection Date', 'DateTime'], axis=1)
predata = predata.drop(['Lab Comments','Submission Date'],axis=1)
pd.DataFrame.to_excel(predata,'SVMdata.xlsx')
"""

import collections
def tokenize(sentences, token='word'):
    #Split sentences into word or char tokens
    if token == 'word':
        list=[];
        for sentence in sentences:
            sentence=str(sentence)
            if sentence==' ':

                list.append([])
            else:
                list.append(sentence.split(' '))
        return list
    elif token == 'char':
        return [list(sentence) for sentence in sentences]
    else:
        print('ERROR: unkown token type '+token)

class Vocab(object):
    def __init__(self, tokens, min_freq=0, use_special_tokens=False):
        counter = count_corpus(tokens)  # :
        self.token_freqs = list(counter.items())
        self.idx_to_token = []
        if use_special_tokens:
            # padding, begin of sentence, end of sentence, unknown
            self.pad, self.bos, self.eos, self.unk = (0, 1, 2, 3)
            self.idx_to_token += ['', '', '', '']
        else:
            self.unk = 0
            self.idx_to_token += ['']
        self.idx_to_token += [token for token, freq in self.token_freqs
                        if freq >= min_freq and token not in self.idx_to_token]
        self.token_to_idx = dict()
        for idx, token in enumerate(self.idx_to_token):
            self.token_to_idx[token] = idx

    def __len__(self):
        return len(self.idx_to_token)

    def __getitem__(self, tokens):
        if not isinstance(tokens, (list, tuple)):
            return self.token_to_idx.get(tokens, self.unk)
        return [self.__getitem__(token) for token in tokens]

    def to_tokens(self, indices):
        if not isinstance(indices, (list, tuple)):
            return self.idx_to_token[indices]
        return [self.idx_to_token[index] for index in indices]

def count_corpus(sentences):
    #print(sentences)
    tokens = [tk for st in sentences for tk in st]

    return collections.Counter(tokens)  # 返回一个字典，记录每个词的出现次数


data=pd.read_excel(r"C:\Users\ASUS\Desktop\代码\美赛\C题\代码\2\SVMdata.xlsx")
##for text pre
text = list(data['Notes'])
tokens = tokenize(text)
print(tokens)
#print(tokens)
mydict=count_corpus(tokens)
f='字典.txt'
tmp=mydict.items()
d_order=sorted(tmp,key=lambda x:x[1],reverse=True)
print(d_order)
with open(f,'w',encoding="utf-8") as fo:
    for k,v in d_order:
        print("%s,%s" %(k,v),sep='',file=fo)
key=[]
for i in range(21,31,1):
    key.append(d_order[i][0])
print(key)
print(data._stat_axis.values.tolist() )
for i in key:
    data[i] = data.apply(lambda _: 0, axis=1)
for i in range(2069):
    for j in tokens[i]:
        if j in key:
            data.loc[i,j]+=1
class_mapping = {'Negative ID':0, 'Positive ID':1}
data['Lab Status'] = data['Lab Status'].map(class_mapping)

data.to_excel('SVM final.xlsx')


