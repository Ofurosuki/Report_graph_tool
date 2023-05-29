import pyperclip
# when you want to import data from excel to python
data=pyperclip.paste()
data=data.split('\n')
del data[-1] # delete the last empty element なんかいらない空白が入るので削除
data_=[float(i) for i in data]
print(data_)
pyperclip.copy(str(data_))

