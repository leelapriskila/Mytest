def main():
    size = int(input("Enter size of the list: "))
    myList = []
    
    print("Enter %d elements: " % size)
    
    for i in range(size):
        data = int(input("Enter element %d: " % (i + 1)))
        myList.append(data)   
    
    n = int(input("By how much you want to rotate the elements of the list: "))

    #leftRotateList(myList, n)
    #print len(myList)
    print("After rotating by a factor of %d:" %n)
    if len(myList)>=n:
        print myList[n:]+myList[:n]
    elif len(myList)<n:
        l = n % len(myList)
        print myList[l:]+myList[:l]
    elif n==0:
       print myList

main()    
