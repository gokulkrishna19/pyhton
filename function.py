def calculateTotal(exp):
    total = 0
    for item in exp:
        total +=item
    return total


List1=[200,300,400,100]
List2=[1000,1000]

TotalOfList1=calculateTotal(List1)
TotalOfList2=calculateTotal(List2)

print("List1 Total is ",TotalOfList1)
print("List2 Total is ",TotalOfList2)