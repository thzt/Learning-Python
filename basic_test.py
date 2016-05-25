# -*- coding: utf-8 -*-
# 题目来源：https://zhuanlan.zhihu.com/p/21102354

# 题 1
# 检查密码规则合法性
# 考察基本编码能力和字符串处理
# 参考 python 文档的字符串库

# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10
import re
def valid_password(pwd):
    return True if re.match(r'^[a-zA-Z](?:[a-zA-Z]|\d|_){1,9}$',pwd) else False

print(valid_password('a_'))
print(valid_password('a123456789'))
print(valid_password('a1234567890'))
print(valid_password('a'))



# 题 2
# 返回 100 内的素数列表
# 考察基本的循环和选择概念、列表的使用
def prime_numbers():
    return filter(lambda x:not [x%i for i in range(2,x) if x%i==0],range(2,101))

print(prime_numbers())
    


# 题 3
# 给定一个只包含字母的字符串，返回单个字母出现的次数
# 考察字典的概念和使用
# 返回值为包含元组的列表，格式如下（对列表中元组的顺序不做要求）
# 参数 "hello"
# 返回值 [('h', 1), ('e', 1), ('l', 2), ('o', 1)]
def letter_count(str):
    dict={}
    for x in str:
        if dict.has_key(x):
            dict[x]=dict[x]+1
        else:
            dict[x]=1

    return zip(dict.iterkeys(),dict.itervalues())

print(letter_count('hello'))

    
    
# 题 4
# 给定一个英文句子（一个只有字母的字符串），将句中所有单词变为有且只有首字母大写的形式
def cap_string(str):
    return re.sub(r'\w+',lambda m:m.group(0).capitalize(),str)

print(cap_string('abc def gh'))



# 题 5
# 写一个 Queue 类，它有两个方法，用法如下
class Queue:
    def __init__(self):
        self._items=[]

    def enqueue(self,n):
        self._items.append(n)
        
    def dequeue(self):
        return self._items.pop(0)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue()) # 1
print(q.dequeue()) # 2
print(q.dequeue()) # 3
