'''Have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str. 
  For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number. '''
  
def DashInsert(str): 
    a = ''
    for x in range(0,len(str)-1):
        a += str[x]
        if int(str[x])%2 != 0 and int(str[x+1])%2 != 0:
            a += '-'
    a += str[-1]
    return(a)
# keep this function call here  
print DashInsert(raw_input())
