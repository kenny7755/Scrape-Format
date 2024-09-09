import eel 
eel.init('web')

@eel.expose 
def formatfunc():
    with open(r'fileInput') as test_file:
        global x
        x = test_file.readline()
        for x in test_file:
            print(x.replace('"', '\n').replace(',', '\n').strip())
    return 

with open('x', 'w') as new_file:
    new_file.write(str(formatfunc()))
eel.start('index.html')