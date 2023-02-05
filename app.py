import os
times = input("")
num = 0
os.chdir('/')
fakePath = os.path.dirname(os.path.realpath(__file__))
fakeFile = open(fakePath+'/fakeFile/fakeFile.txt', 'r')
fakeData = fakeFile.readline()
fakeFile.close()
fakeFile = open(fakePath+'/fakeFile/fakeFile.txt', 'w')
print(fakeData)
while num < int(times):
 print('s')
 fakeFile.write('1')

 os.chdir(fakePath)
 os.system('git add .')
 os.system('git commit -m "fake commit"')
 os.system('git push')
 num += 1
