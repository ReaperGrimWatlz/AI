def quicksort(list1):
    if len(list1)<=1:
        return list1
    else:
        x=len(list1)//2
        sort=sorted([list1[0],list1[x],list1[-1]])
        piviot=sort[1]
        same=[]
        less=[]
        more=[]
        for i in list1:
            if i<piviot:
                less.append(i)
            elif i==piviot:
                same.append(i)
            elif i>piviot:
                more.append(i)
            else:
                print("What?")
        return quicksort(less)+same+ (quicksort(more))
#main
size=int(input("Enter Size of the list"))
sin=[]
for i in range(size):
    sin.append(int(input("Enter Elements")))
sorted_list=quicksort(sin)
print("Orignal List: ",sin,"\n","Sorted List: ",sorted_list)