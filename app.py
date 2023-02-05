import os
os.chdir('/')
fakePath = os.path.dirname(os.path.realpath(__file__)) )
fakeFile = open(fakePath+'/fakeFile/fakeFile.txt', 'r')
fakeData = fakeFile.readline()
fakeFile.close()
fakeFile = open(fakePath+'/fakeFile/fakeFile.txt', 'r')
try:
 fakeFile.write(Int(fakeData)+1)
except:
 print('e')
 fakeFile.write(1)
os.system('git add .')
os.system('git commit')
os.system('git push')
