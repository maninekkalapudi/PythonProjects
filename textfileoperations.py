file = open('/home/manikanta/Documents/pythonproject/myfile.txt', 'w')
file.write('this first line\n')
file.write('this second line\n')
file.close()

file = open('/home/manikanta/Documents/pythonproject/myfile.txt', 'r')
print(file.read())
file.close()
