#using the function number of letters in the string

def most_frequent(str1):
    dict={}
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
             dict[n]=1
    return dict
print(most_frequent("mississippi"))  
