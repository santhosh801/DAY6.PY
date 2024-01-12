# def insert(king, element):
#     king.append(element)
# king = [1,12,232,323,23,23,3]
# queen = 1

# insert(king,queen)
# print(king)

# def aa(o,N):
#     asd = (N * (N + 1)) // 2
#     aaa = sum(o)
#     ed = asd - aaa
#     return ed

# # Example usage
# N = 10  # Assuming the array should contain elements from 1 to 10
# given_array = [1, 2, 3, 4, 5, 6, 7, 8, 10]  # One element is missing (9)
# result = aa(given_array, N)
# print("Missing element is:", result)

def missingNumber(na,N):
        
        array =(N*(N+1)//2)
        asas=sum(na)
        missingNumber=array-asas
        return missingNumber 
N=5        
given = [1,2,3,5]
result = missingNumber(given,N)
print(result)