def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        str2=""
        for j in range(i,i+k):
            if string[j] not in str2:
                str2=str2+string[j]
        print(str2)
