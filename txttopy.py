to_read = open('txttopy.txt', 'r' )


# data = to_read.readline()
#data=to_read.readlines()
data=to_read.read().splitlines() 

print(data)
print(type(data))
print(len(data)) 

to_read.close()

# for i in to_read: 
#     print (i)
# to_read.close()    