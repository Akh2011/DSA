s = []

s.append('https : //www.cnn.com')
s.append('https : //www.cnn.com/world')
s.append('https : //www.cnn.com/india')
s.append('https : //www.cnn.com/china')

for i in s:
    print(i) 

# Python integrated pop operation

s.pop()

print (' After pop operating ')
for i in s:
    print(i) 

q =[]
q.insert(0, 'https : //www.cnn.com')
q.insert(0, 'https : //www.cnn.com/world')
q.insert(0, 'https : //www.cnn.com/india')
q.insert(0, 'https : //www.cnn.com/china')

q.pop()

for i in q:
    print (i)
