def swapFile():
    fileNamea =  input("Enter the file name:- ")
    fileNameb =  input("")
    numberOfWords = 0

    file =  open(fileNamea, 'r')
    file2=  open(fileNameb, 'r')
    for text in file:
        text = text.split()
