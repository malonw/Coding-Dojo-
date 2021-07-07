# 1. Biggie Size
Alist = [-1,3,5,-5]
for x in range (len(Alist)) :
    if Alist[x] < 0 :
        Alist[x] = str("big")
print(Alist)
print("---------------")
# 2. Count Positives
list1 = [1,6,-4, 2,-7,-2]
y = 0
print(list1)
for x in range (len(list1)) :
    if list1[x] > 0 :
        y += 1
list1[-1]=y
print(list1)
print("---------------")
# 3. Sum Total
def sum_total(list3) :
    print(sum(list3))
    return
sum_total([1,2,3,4])
sum_total([6,3,-2])
# Works fine in Python Tutor, does not work here(because list and sum are built in functions, learning is fun and frustrating (incase anyone is actually looking at these)
print("---------------")
# 4. Average
def avg(Blist) :
    print(sum(Blist)/len(Blist))
avg([1,2,3,4])
# 5. Length
print("---------------")

def length(Clist) :
    print(len(Clist))
length([37,2,1,-9])
length([])
print("---------------")
# 6. Minimum
def mini(Dlist) :
    if len(Dlist) > 0 :
        print(min(Dlist))
    else :
        return False

mini([37,2,1,-9])
mini([])
print("---------------")
# 7. Maximum
def Max(elist) :
    if len(elist) > 0 :
        print(max(elist))
    else :
        return False

Max([37,2,1,-9])
Max([])
print("---------------")
# 8. Ultimate Analysis
def ult(flist) :
    if len(flist) > 0 :
        avg=(sum(flist)/len(flist))
        Dict={f"Sum= ":sum(flist), "Average = ": avg, "Minimum = ":min(flist), "Maximum = ":max(flist), "Length = ": len(flist)}
        print(Dict)
    else :
        return False
ult([37,2,1,-9])
print("---------------")
# 9. Reverse List
def Rev(Rlist) :
    if len(Rlist) > 0 :
        print(Rlist)
        Rlist.reverse()
        print(Rlist)
    else :
        return False

Rev([37,2,1,-9])