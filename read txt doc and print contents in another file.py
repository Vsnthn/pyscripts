import string
data_from_file=[]
seperated_data=[]
num_count=0
caps_count=0
punc_count=0
small_count=0
with open('test.txt') as f:
    contents = f.read()
    for i in contents:
        data_from_file.append(i)
for b in data_from_file:
    if b.isdigit():
        num_count+=1
z=f"the num count is {num_count}:"
seperated_data.append(z)
for c in data_from_file:
    if c.isupper():
        caps_count+=1
y=f"the caps count is {caps_count}:"
seperated_data.append(y)
for d in data_from_file:
    if d.islower():
        small_count+=1
x=f"the small count is {small_count}:"
seperated_data.append(x)
for e in data_from_file:
    if e in string.punctuation:
        punc_count+=1
w=f"the punc count is {punc_count}:"
seperated_data.append(w)
with open("report.txt", "a") as o:
    for i in seperated_data:
        o.write(i+"\n")
    