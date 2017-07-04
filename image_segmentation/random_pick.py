#coding = utf-8


import os
import sys
import random


def random_pick(low,high,num):
	L=range(low,high)
	random.shuffle(L)
	return L[0:num]

def random_pick(low,high,num,my_list):
	L=range(low,high)
	random.shuffle(L)
	target_list=[]
	for i in L[0:num]:
		target_list.append(my_list[i])
	return target_list

a = os.listdir('/home/moma/Intern_Record/images/')
b = random_pick(0,len(a),20,a)
print b
for name in b:
	source1 = '/home/moma/Intern_Record/images'+os.sep+name
	source2 = '/home/moma/Intern_Record/my_test_result'+os.sep+name+'.txt'
	source3 = '/home/moma/Intern_Record/my_test_result_v2'+os.sep+name+'.txt'
	target = '/home/moma/Intern_Record/test_results'
	os.system('cp -r %s %s' %(source1,target))
	os.system('cp -r %s %s' %(source2,target))
	os.system('cp -r %s %s' %(source3,target+os.sep+name+'_v2'))
