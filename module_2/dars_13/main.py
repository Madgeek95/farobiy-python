# a = [0 for x in range(5)]
# # print(a)
# sum_even = 0
# sum_odd = 0
# for i in range(1,len(a)):
#     a[i] = i
# for i in range(len(a)):
#     if i %2 ==0:
#         sum_even += a[i]
#     else:  
#         sum_odd += a[i]

# print(f"Juft: {sum_even}, Toq: {sum_odd}")

def foo(a):
    return a

b = foo

print(b(5))