'''
# №1
a = 5
b = 1.5
print(a + b)
print(a * b)
print(a / b)
p = 3.14159
print(type(a / b))
s = p * 5 ** 2
print(round(s, 2))
'''

'''
# №2
s = " Hello, Python! "
s = s.strip()
print(s)
s = s.replace('!', '?')
print(s)
s = s.upper()
print(s)
s = s.lower()
s = s.replace('?', '!')
assert s == 'hello, python!'
print(s)
'''

'''
# №3
import copy


num = [7, 2, 5]
num.append(4)
num.insert(1, 10)
pl = [1, 1, 1]
num.extend(pl)
num.remove(7)
pop = []
pop.append(num[0])
num.pop(-1)
num.sort()
num.reverse()
c = num.count(2)
print(num.index(1))
new_num = num.copy()
d_new_num = copy.deepcopy(num)
num.clear()
print(new_num)
print(d_new_num)
print(num)

'''

'''
# №4
t = (1, 2, 3)
t2 = t + (4, 5)
print(t2)
print(t2.count(2))
print(t2.index(4))
print(t)
'''

'''
# №5
values = [3, 1, 3, 2, 1, 5, 2]
unique_values = set(values)
print(unique_values, len(unique_values))
other = {2, 4, 5}
print(unique_values & other)
print(unique_values | other)
print(unique_values - other)
print(other - unique_values)
'''

'''
# №6
scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores["Bob"] = 95
print(scores.get("Bob"))
print(scores.get("Dave"))
scores.pop("Alice")
print(scores)
print(len(scores))
print(scores.keys())
print(scores.values())
'''

# №7
text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
text = text.strip().lower().replace('    ', '').replace('!', '.')
text = text.replace('\n', '')
text = text.split('.')
text.pop(-1)
p1 = text[0]

# print(text)
p1 = p1.split(' ')
print(p1)
print(p1.count('python'))
p = ' '.join(p1)
print(p.startswith("python"), p.endswith("language"))
text = ' '.join(text)
print(text)
print(len(text), text.count('a'), text.find('data'))
text.split(' ')
text = ' '.join(text)
print(p)
dict = {'python': 2, 'is': 3, 'a': 1, 'powerful': 1, 'programming': 1, 'language.': 1, 'it': 1, 'used': 1, 'in': 1, 'data': 1, 'science,': 1, 'web': 1, 'development,': 1, 'automation,': 1, 'and': 1, 'many': 1, 'other': 1, 'fields.': 1, 'easy': 1, 'to': 1, 'learn,': 1, 'yet': 1, 'very': 1, 'versatile.': 1}

def clean_text(text):
    text = text.lower()
    text = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
    return text

