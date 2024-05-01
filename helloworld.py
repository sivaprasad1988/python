def findSmallestNumber(list):
    key = 0 
    smallestValue = list[0]
    for item in list: 
        if(item < smallestValue):
            smallestValue = item
    print(smallestValue)        
              
    
findSmallestNumber([1,368,584,5,2,10])
