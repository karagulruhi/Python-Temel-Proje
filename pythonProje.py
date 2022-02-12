# #1
# items=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# def duzlestrici(items):
#     duzListe=[]
#     for idx,item in enumerate(items):
#         if type(items[idx]) == list:
#             for i in item:
#                 print(i)
#                 duzListe.append(i)
#         else:
#             duzListe.append(item)
#     return duzListe
#     print(duzListe)

# duzlestrici(items)

#2
lst = [[1, 2], [3, 4], [5, 6, 7]]
def dondur(lst):
    yeniList = lst[::-1]
    cokYeniList=[]
    for idx,i in enumerate(yeniList):
        cokYeniList.append(yeniList[idx][::-1])
    
    return cokYeniList
      

print(dondur(lst))