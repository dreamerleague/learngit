#coding = utf-8

'''
    Extract text from images.

    use Tesseract to achieve it.
    '''


import os
import sys
import time


my_dir = '/home/moma/Intern_Record'
name_list = os.listdir(my_dir+os.sep+'images')
# print name_list

# source = my_dir+os.sep+'test_images'+os.sep+'814185.jpg'
# target = my_dir+os.sep+'77777'
# source = '/home/moma/Intern_Record/test_images/814185.jpg'
# target = '/home/moma/Intern_Record/77777'
# # os.system('tesseract /home/moma/Intern_Record/test_images/814185.jpg /home/moma/Intern_Record/77777')
# os.system('tesseract %s %s' %(source,target))
# # os.system("tesseract my_dir+os.sep+test_imagrs+os.sep+'814185.jpg' my_dir+os.sep+'77777'")
# # os.system("tesseract source target")
# print source
# print target
# print type(source)
# os.system("tesseract source target")
# os.system(tesseract /home/moma/Intern_Record/test_images/814185.jpg /home/moma/Intern_Record/888888)

start_time=time.time()
for name in name_list:
	source = my_dir+os.sep+'images'+os.sep+name
	target = my_dir+os.sep+'my_test_result_v2'+os.sep+name
	os.system('tesseract %s %s' %(source,target))

end_time=time.time()
print end_time-start_time