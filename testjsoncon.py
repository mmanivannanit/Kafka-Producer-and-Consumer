import json
import re


def read():
    with open('/home/mani/Logs/OrderLog_01-11-2017.log', 'r') as f:
        return [l.strip() for l in f.readlines()]

def batch(content, n=1):
    length = len(content)
    for num_idx in range(0, length, n):
        yield content[num_idx:min(num_idx+n, length)]


def emit(batched):

#parsed_data = re.findall(r'(\w{3} \d+ [\d+:]+) (\S+) (\S+):', 'Jan 27 10:46:57 sabya-ThinkPad-T420 NetworkManager[1462]:')
    #for n, name in enumerate([re.findall(r'[', n)]):
    # for n, name in enumerate([re.findall(r'[^\S\n\t]+',n)]):
    
     for n, name in enumerate('logs'):
         #for n, name in enumerate(['rawlog']):  
         yield name, batched[n]

# def emit(batched):
#     def _quotes(q):
#         return q.replace('"', '')
#     def _pass(p):
#         return p
#     def _num(n):
#         try:
#             return int(n)
#         except ValueError:
#             return n

#     for n, (name, func) in enumerate([
#         ('name', _quotes),
#         ('description', _pass),
#         ('info', _pass),
#         ('author', _pass),
#         ('year', _num)
#     ]):
#         yield name, func(batched[n]

data = {}

#data['key'] = 'value'

content = read()

batched = batch(content, 6)
res = [dict(emit(b)) for b in batched]


with open('/home/mani/Logs/output.json', 'w') as f:
    f.write(json.dumps(res, indent=4))

with open('/home/mani/Logs/output.json') as f:
    val = f.readlines()
    for m in val:
        splitted = m.split()
        splitted = 'Type:' + str(splitted[:2]) + 'Date:' + str(splitted[:3])
        #first = splitted[1]
        #second = splitted[1]
        print(splitted)
        
       
        #print(re.sub(r'\s', '', m).split(','))
        


