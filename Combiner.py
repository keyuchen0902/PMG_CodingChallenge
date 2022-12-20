import sys

class Diff_col_excep(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
 
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))

class File_not_exist(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
 
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))

#改进方法：写一个方法首先check文件大小，如果太大就拆成小块的文件
#此函数作用是读取每个csv文件的内容，第一行是header，我们要添加一个新的列叫filename，之后每行都是内容，添加至content，注意要添加换行符。
def handleFile(filename):
    fileHeader = ""
    fileContent = ""
    try:
        with open(filename, "r") as csv:            
            headers = True
            for line in csv:
                if headers:
                    # mergedHeaders is just the headers from the last file
                    headers = False
                    fileHeader = line[:-1] + ",\"filename\"\n"
                else:
                    # for each line in the csv file remove the new line character at the end of each line and append the filename 
                    fileContent += f"{line.strip()},\"{filename}\"\n"     # line.strip() removes the new line character
        return fileHeader, fileContent
        
    except:
        raise File_not_exist("Can't open file!")

#该函数是合并两个列相同的文件到一起，分别处理两个文件，在处理文件时，通过上述函数拿到header和content，分别添加至合并后的header和content
def combineCSV(filenames):
    # Setup output
    mergedCsv = ""

    # Store headers
    mergedHeaders = ""

    for filename in filenames:        
        newHeader, newContent = handleFile(filename)
        if (mergedHeaders!="" and mergedHeaders!=newHeader):
            # different columns
            raise Diff_col_excep("Different file columns")
        else:
            mergedHeaders = newHeader
            mergedCsv += newContent

    # adding headers
    # mergedHeaders = f"{mergedHeaders[:-1]},\"filename\"\n"  

    mergedCsv = mergedHeaders + mergedCsv

    print(mergedCsv)

def main():
    combineCSV(sys.argv[1:])
    
if __name__ == '__main__':
    main()
    