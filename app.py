import os
os.chdir('/')
fakePath = os.path.dirname(os.path.realpath(__file__))
fakeFile = open(fakePath+'/fakeFile/fakeFile.txt', 'r')
fakeData = fakeFile.readline()
fakeFile.close()
fakeFile = open(fakePath+'/fakeFile/fakeFile.txt', 'w')
try:
 fakeFile.write(str(int(fakeData)+1))
except:
 print('e')
 fakeFile.write(str(1))
os.chdir(fakePath)
os.system('git add .')
os.system('git commit -m "fake commit"')
os.system('git push')
