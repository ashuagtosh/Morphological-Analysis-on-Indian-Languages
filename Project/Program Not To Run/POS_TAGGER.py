import io
import os.path

f = open("synset.txt")
text = f.readlines()

dictionary_list = list()

start = 0

start_tocalculate_paraend = 0
item_no = dict()

for line in text:
    line = line.decode("utf-8-sig").encode('utf8')
    line = line.decode('utf8')
    #print(line)
    if(len(line)>1):
        if(line.find(u"::")!=-1):
            l = line.find(u'::')
            #print("Line No : " + str(start+1) + "Index is : " + str(l))
            #print(line[:l] + line[l+2:])
            #print(type(line[:l]))
            item_no[line[:l].encode('utf8').strip('\t')] = line[l+2:]
        else:
            pass    
    else:
        #print(item_no)
        dictionary_list.insert(start_tocalculate_paraend,item_no)
        item_no = dict()
        start_tocalculate_paraend = start_tocalculate_paraend + 1
        #print(item_no)
    start = start + 1
dictionary_list.insert(start_tocalculate_paraend,item_no)

import copy

for i in dictionary_list:
    f_name = i['CAT'].strip('\n')+".txt"
    if(os.path.isfile(f_name)):
        wf = open(f_name,'a')
        #x = list()
        #x = copy.deepcopy(i['SYNSET-PUNJABI'].split(','))
        wf.write(i['SYNSET-PUNJABI'].encode("utf8"))
        wf.close()
    else:
        wf = open(f_name,'w')
        wf.write(i['SYNSET-PUNJABI'].encode("utf8"))
        wf.close()
    
