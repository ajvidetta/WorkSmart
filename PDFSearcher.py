import PyPDF2 

def search(fileName, keyWord):
    # creating a pdf file object 
    pdfFileObj = open(fileName, 'rb')

    #print(fileName)
      
    # creating a pdf reader object
    try:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        
        values = []
        groups = []
        seen = []
        for i in range(pdfReader.numPages):

            # creating a page object 
            pageObj = pdfReader.getPage(i) 
          
            # extracting text from page 
            data = pageObj.extractText()

##            if keyWord in data.lower():
##                if outpt == "": 
##                    outpt+= "'{}' can be found in page(s) {}".format(keyWord, i+1)
##                    
##                else:
##                    outpt+= ", {}".format(i+1)
            if keyWord in data.lower():
                seen.append(i+1)
                if groups == []:
                    groups.append(i+1)
                else:
                    if i in groups:
                        groups.append(i+1)
                    else:
                        if len(groups) == 1:
                            values.append(groups[0])
                            groups.clear()
                            groups.append(i+1)
                        else:
                            mini = groups[0]
                            maxi = groups[-1]
                            values.append("{}-{}".format(mini,maxi))
                            groups.clear()
                            groups.append(i+1)

            #print(i+1)
            #print(values)
            #print(groups)
                    
        if groups != []:
            for i in range(len(groups)):
                values.append(groups[i])                
          
        # closing the pdf file object 
        pdfFileObj.close()

        #print(values)
        #print(seen)

        if values != []:
            outpt = "'{}' can be found in page(s)".format(keyWord)
            for i in range(len(values)):
                outpt+= ", {}".format(values[i])
            return outpt

        else:
            return ""

    except(PyPDF2.utils.PdfReadError):
        print("BAD PDF")

#print(search("/Users/ajvidetta/Desktop/UNI/linguistics/lectures/12. Institutional language.pdf", "institution"))
