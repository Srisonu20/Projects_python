# # # # def non_repeat(str):
# # # #     return str
# # # # str = "ashishdash"
# # # #
# # # # for i  in str:
# # # #     if
# # # #         print("non_repeat:",non_repeat(str))
# # # #     else:
# # # #         print ("not")
# # #
# # #
# # # list = ['24','35','5','50','23']
# # #
# # # import time
# # #
# # # from selenium.webdriver.chrome import webdriver
# # # from selenium.webdriver.chrome.webdriver import WebDriver
# # # from selenium.webdriver.common.by import By
# # #
# # # # driver = webdriver.Chrom
# # # # driver.get("https://www.amazon.in/ref=nav_logo")
# # # # driver.find_element(By.XPATH,"//a[@id='nav-hamburger-menu']")
# # # # driver.window.maximize()
# # # # time.sleep(2)
# # # # driver.quit()
# # #
# # # n = int(input(" "))
# # #
# # # if n % 2 != 0:
# # #     print("Weird")
# # #
# # # elif n % 2 == 0 and range(2, 6):
# # #     print("Not Weird")
# # #
# # # elif n % 2 == 0 and range(6, 21):
# # #     print("Weird")
# # #
# # # elif n % 2 == 0 and n > 20:
# # #     print("Not Weird")
# # #
# # # else:
# # #     print("none")
# # from itertools import count
# #
# #
# # # from unittest import result
# # # def add(x,y):
# # #     if y==0:
# # #         return x
# # #     else:
# # #         return add(x+1,y-1)
# # #
# # # num1 =   1
# # # num2 = 2
# # #
# # # result = add(num1,num2)
# # # print(result)
# #
# # # def fact(x):
# # #     if x == 0:
# # #         return 1
# # #     else:
# # #         return fact(x-1)* x
# # # x = 3
# # # print(fact(x))
# #
# # # add = lambda x,y:x+y
# # #
# # # num1 = 3
# # # num2 = 4
# # #
# # # print(add(num1,num2))
# #
# # # num1 = 3
# # # num2 = 45
# # #
# # # import operator
# # # sum = operator.add(num1,num2)
# # #
# # # print("sum of {0} and {1} is {2}".format(num1,num2,sum))
# # #
# # # L = ["a","b","b","o"]
# # # res = ''.join(L)
# # # print(res)
# #
# # # mylist = ["python", "hub"]
# # # for i in mylist:
# # #     mylist.append(i.upper())
# # # print(mylist)
# #
# # # def recur(n):
# # #     if n<=1:
# # #         return n
# # #     else:
# # #         return n+recur(n-1)
# # #
# # # n = 16
# # # if n < 0:
# # #     print("positive")
# # #
# # # else:
# # #     print(recur(n))
# #
# #
# # # a = 3
# # # b = 5
# # # x =[a,b]
# # # x.sort()
# # # print(x[-0])
# #
# # # def si (p,t,r):
# # #     si = (p*t*r)/100
# # #     return si
# # # p = 10000
# # # t=5
# # # r=8
# # # print(si(p,t,r))
# #
# # # n =  153
# # # s = n
# # # b = len(str(n))
# # # sum = 0
# # # print(b)
# # # # import pdb
# # # # pdb.set_trace()
# # # print(3**3)
# # # r = n % 10
# # # print(n)
# # # sum = sum + (r ** b)
# # # print(sum)
# # # n = n // 10
# # # print(n)
# # # s = n
# # # while n!=0:
# # #     r = n % 10
# # #     n = n//10
# # # sum = sum + (r**b)
# # # if sum == s:
# # #     print("yes")
# # #
# # # else:
# # #     print("not")
# #
# # # def prime(x,y):
# # #     prime_lst = []
# # #     for i in range (x,y):
# # #         if i == 0 or i == 1:
# # #             continue
# # #         else:
# # #             for j in range (2,int(i/2)+1):
# # #                 if i % j == 0:
# # #                     break
# # #                 else:
# # #                     prime_lst.append(i)
# # #
# # #     return prime_lst
# # #
# # #
# # # starting = 2
# # # ending = 7
# # # lst = prime(starting,ending)
# # # if len(lst) == 0:
# # #     print ("no")
# # # else:
# # #     print(lst)
# # #
# # #
# # # def prime(x, y):
# # #     prime_list = []
# # #     for i in range(x, y):
# # #         if i == 0 or i == 1:
# # #             continue
# # #         else:
# # #             for j in range(2, int(i / 2) + 1):
# # #                 if i % j == 0:
# # #                     break
# # #             else:
# # #                 prime_list.append(i)
# # #     return prime_list
# # #
# # #
# # # # Driver program
# # # starting_range = 2
# # # ending_range = 7
# # # lst = prime(starting_range, ending_range)
# # # if len(lst) == 0:
# # #     print("There are no prime numbers in this range")
# # # else:
# # #     print("The prime numbers in this range are: ", lst)
# #
# #
# # # num = 11
# # # if num >1:
# # #     for i in range (2, int(num/2)+1):
# # #         if (num % i) == 0:
# # #             print("no")
# # #             break
# # #     else:
# # #         print("yes")
# # #
# # # else:
# # #     print("no")
# #
# # # def fib(n):
# # #     if n <= 0:
# # #         print("incorrect")
# # #
# # #     elif n == 1:
# # #         return 0
# # #     elif n == 2:
# # #         return 1
# # #     else:
# # #         return fib(n-1)+fib(n-2)
# # # print(fib(int(input("Enter"))))
# #
# # # FibArray = [0,1]
# # # def fib(n):
# # #     if  n < 0:
# # #         print("incor")
# # #     elif n <= len(FibArray):
# # #         return FibArray[n-1]
# # #     else:
# # #         temp_fib = fib(n-1)+fib(n-2)
# # #         FibArray.append(temp_fib)
# # #         return temp_fib
# # #
# # # print(fib(9))
# #
# # # def fib(n):
# # #     a = 0
# # #     b = 1
# # #     if n<0:
# # #         print("incor")
# # #
# # #     elif n == 0:
# # #         return a
# # #     elif n == 1:
# # #         return b
# # #     else:
# # #         for i in range(2,n):
# # #             c = a + b
# # #             a = b
# # #             b = c
# # #         return b
# # #
# # # print(fib(9))
# #
# #
# # # import math
# # # def issqrt(x):
# # #     s  = int(math.sqrt(x))
# # #     return s*s == x
# # # def isfab(n):
# # #     return  issqrt(5*n*n+4) or issqrt(5*n*n-4)
# # # for i in range(1,11):
# # #     if (isfab(i)==True):
# # #         print("yes")
# # #
# # #     else:
# # #         print("no")
# #
# # # def sqr(n):
# # #     s
# # #
# # # n=4
# # # print(sqr(n))
# # #
# # # def sqr(n):
# # #     return (n*(n+1)*(2*n+1))//6
# # # n = 4
# # # print(sqr(n))
# #
# # def sum_arr(arr):
# #     sum = 0
# #     for i in arr:
# #         sum = sum + i
# #
# #     return(sum)
# #
# #
# # # n = int(input("enter"))
# # # arr = list(map(int,input("").split(' ')[:n]))
# # # print(arr)
# # #
# # # na = len(arr)
# # # print(na)
# # #
# # # ans = sum_arr(arr)
# # # print(ans)
# #
# # # n = int(input("enter"))
# # # arr = list ( map(int, input().split()[:n]))
# # # na = len (arr)
# # # print(na)
# # # ans = sum(arr)
# # # print(ans)
# #
# # # from functools import reduce
# # # def sum_arr(arr):
# # #     sum = reduce(lambda a,b:a+b,arr)
# # #     return sum
# # # n = int(input("enter"))
# # # arr = list(map(int,input("enter").split()[:n]))
# # # na = len(arr)
# # # print(na)
# # # ans = sum_arr(arr)
# # # print(ans)
# #
# # # n = int(input("enter"))
# # # list = list(map(int,input("enter").split()[:n]))
# # # s = 0
# # # for i , a in  enumerate(list):
# # #     s = s + a
# # # print(s)
# # # print(len(list))
# #
# # # list = [1,2,3]
# # # s = 0;
# # # for i , a in enumerate(list):
# # #     s=s+a
# # #
# # # print(s)
# #
# # #divide and conquer
# #
# # # def sum_arr(arr, low, high):
# # #     if low == high:
# # #         return arr[low]
# # #     mid = (low+high)//2
# # #     sum_left_arr = sum_arr(arr, low, mid)
# # #     sum_right_arr = sum_arr(arr, mid+1, high)
# # #     return sum_left_arr+sum_right_arr
# # # arr=[1,2,3]
# # # print(sum_arr(arr, 0 ,len(arr)-1))
# # #
# # # from collections import Counter
# # #
# # # arr = [1,2,3,4]
# # # c =  Counter(arr)
# # # sum = 0
# # # for key, value in c.items():
# # #     sum += key*value
# # # print(sum)
# #
# #
# #
# # def large_arr(arr,n):
# #     max = arr[0]
# #     for i in range(1,n) :
# #         if arr[i]>max:
# #             max = arr[i]
# #     return max
# # # arr = [1,5,2,3]
# # # n = len(arr)
# # # print(n)
# # # print(large_arr(arr,n))
# # #
# # # n=int(input("enter"))
# # # arr = list(map(int,input().split()[:n]))
# # # ans = max(arr)
# # # print(ans)
# #
# # # def rot(arr,n,d):
# # #     temp = []
# # #     i = 0
# # #     while (i < d):
# # #         temp.append(arr[i])
# # #         i = i+1
# # #     i = 0
# # #     while (d < n) :
# # #         arr[i] = arr[d]
# # #         i = i +1
# # #         d = d+1
# # #     arr[:] = arr[:i]+temp
# # #     return arr
# # # arr = [1, 2, 3, 4, 5, 6, 7]
# # # print("Array after left rotation is: ", end=' ')
# # # print(rot(arr, len(arr), 5))
# #
# # # def aray(arr,len):
# # #     product = 1
# # #     for i in range(len):
# # #         product = (product*arr[i])
# # #     return product
# # #
# # # arr=[1,2,3,4,5,6]
# # # n = 11
# # # len = len(arr)
# # # print(aray(arr,len))
# #
# #
# # #
# def revr(str):
#     str1= ""
#
#
#     for i in str :
#         str1 = i +str1
#
#     return str1
#
# count = str.count(s)
# str = "sri"
# print(revr(str))
# print(len(str))
# print(count(s))
# #
# #
# # _
#
#
#
# class String:
#     def __init__(self,str1,str2):
#         self.str1 = str1
#         self.str2 = str2
#
#     def print_result(self):
#         print(self.str1, self.str2)
#
# class Reverse(String):
#     def reversed_str(self,str1,str2):
#         new_str1 = "" .join([i for i in reversed(str1)])
#         new_str2 = "".join([j for j in reversed(str2)])
#         # for i in str1:
#         #     new_str1 = i + new_str1
#         #
#         # for j in str2:
#         #     new_str2= j+new_str2
#         #
#         return new_str1, new_str2
#
#
#
# #     def result(self):
# #
# #
# #         result = Reverse(str1,str2)
# #         result.print_result()
# #         reversed_str1, reversed_str2 = result.reversed_str(str1,str2)
# #
# #         print(reversed_str1)
# #         print(reversed_str2)
# # str1 = "sri"
# # str2 = "era"
# # x = Reverse(str1,str2)
# # x.result()
#
#
# x = Reverse(str1 = "sri",str2="era")
# print(( x.reversed_str(str1 = "sri",str2="era")))
#
#
# class String:
#     def reverse(self, str1, str2):
#         self.str1 = str1
#         self.str2 = str2
#
#         new_str = " "
#         for i in str1:
#             new_str1 = " ".join([i for i in reversed(str1)])
#             new_str2 = " ".join([i for i in reversed(str2)])
#         return new_str1 + " and " + new_str2
#
#     def print_str(self):
#         print(self.str1)
#         print(self.str2)
#
#
# str1 = "ari"
# str2 = "sri"
# x = String()
# y = x.reverse(str1, str2)
# print(y)


# def list_test(list):
#     counter = 0
#
#     for i in list:
#
#         counter = counter + 1
#     return counter

# list = [ 1,2,3,45]
#
# print(list_test(list))

# list = [1,2,3,4,5]
# print(str(list))
# counter = 0
# for i in list:
#
#     counter = counter+1
# print(str(counter))

#
# class String:
#     def reverse(self, str1, str2):
#         self.str1 = str1
#         self.str2 = str2
#
#         new_str = " "
#         for i in str1:
#             new_str1 = " ".join([i for i in reversed(str1)])
#             new_str2 = " ".join([i for i in reversed(str2)])
#         return new_str1 + " and " + new_str2
#
#     def print_str(self):
#         print(self.str1)
#         print(self.str2)
#
#
# str1 = "ari"
# str2 = "sri"
# x = String()
# y = x.reverse(str1, str2)
# print(y)


# def find_list(list,i):
#
#     for i in list:
#         if (i % 2 == 0):
#             print( i )
#         else:
#             print("none")
#     return i
# list = [1,2,10,5,20,40]
# print(find_list(list,2))



# def exist_list(arr,i):
#
#     if arr.count(89):
#         print("exist")
#     else :
#         print("none")

#     return arr
# i = int(input("enter i"))
# n = int( input("enter n"))
#
#
# arr = list(map(int,input("").split(' ')[:n]))
#
#
# print(exist_list(arr,i))


# def exist_list(arr,i):
#     for i in arr:
#         if i == 3:
#             print("exist")
#         else :
#             print("none")
#     return arr
#
# i = int(input("enter i"))
# n = int( input("enter n"))
# arr = list(map(int,input("").split(' ')[:n]))
# print(exist_list(arr,i))


# def list_clear(list):
#     if list == list.clear():
#         print("list cleared")
#     else:
#         print(list)
#
#
# list = [1, 2, 3, 4, 5]
# print(list_clear(list))


# def list_clear(list):
#     pass
#
# list = [1, 2, 3, 4, 5]
# print(list_clear(list.clear()))

# def clear_list(list):
#     # print(str(list))
#     list *= 0
#
#
# list = [1, 2, 3, 4, 5, 6, 7, 89]
# print(clear_list(list))
#
# def del_list(list):
#
#     del list[:]
#
#
# list = [1, 2, 3, 4, 5, 6]
# print(del_list(list))

# def del_list(list):
#     while len(list) != 0:
#         list.pop()
#
#
# list = [1, 2, 3, 4, 5, 6]
# print(del_list(list))

# def del_list(list):
#     list = list[:4]
#
#
# list = [1, 2, 3, 4, 5, 6]
# print(del_list(list))

# def removal_list(list):
#     pass
# list = [1,2,3,4,5,6]
# list.remove(5)
# print(str(list))

# def removal_list(list1):
#     pass
# lst_list = [1,12,3,5,5,5,5,5,6,4,8]
# lst_list = set(lst_list)
# lst_list.discard(5)
# lst_list = list(lst_list)
#
# print(str(lst_list))

# def removal_list(start,old_list, new_list, ele):
#     if start == len(old_list):
#         return new_list
#     elif old_list[start] == ele:
#         pass
#     else:
#         new_list.append(old_list[start])
#
#     return removal_list(start+1, old_list,new_list,ele)
# new_list = [1,2,3,4,5,6,8,9,10]
# start = 0
# ele = 10
# print(removal_list(start,new_list,[],ele))

# def rev_list(mylist):
#     for i in mylist:
#         i = list(reversed(mylist))
#     return i
# mylist = [1,2,3,4,5,6]
# print(rev_list(mylist))



# class RVR_LIST:
#     def __reversed__(self,vowels):
#         self.vowels = vowels
#         print(list(reversed(self.vowels)))
#
#     def revers(self,str):
#         print(list(reversed(str)))
#         self.str = str
#         for i in reversed(str):
#             print(i,end ="")
#
# vowels = ["a","e","i","o","u"]
# str = "geeks for geeks"
# x = RVR_LIST()
#
# y1 = x.revers(str)


# class Y:
#     def lys(self,str):
#
#         for char in reversed(str):
#
#             print(char, end="")
#
# str = " geek for geeks "
# x = Y()
# y1 =x.lys(str)


"""//// Reverse do  not work for "STRINGS"////"""
# string = "bjugug"
# string.reverse()
# print(string)


""" #------>>>#/// Slicing for rverse ///"""
# my_list = ["aoo", 1123, 122, 1, 8, 2, 56]
# print(my_list)
# my_list = my_list[::-1]
# print(my_list)
#
# string = "strijng"
# string = string[::-1]
# print(string)


"""# /////////summation of items in list///////"""

# for loop
# def summ(list):
#     total = 0
#     for i in range(0,len(list)):
#         total = total + i
#     return total
#
# list = [1,2,3,4,5,6,8,7]
# print(summ(list))

# string = "dshjijo"
# print(len(string))

# sum()
# def summ(list):
#     s = sum(list)
#     return s
#
#
# list = [1, 2, 3, 4, 5, 6]
# print(summ(list))


"""#  ////lambda of sum////"""
# list12= [1.2,12,2,5,5,5666,4]
# print(sum(list(filter(lambda x:(x),(list12)))))




"""# ////////// RECURSIVE sum METHOD ///////"""
# def recursive_of_list(list,size):
#     if size == 0:
#         return 0
#     else:
#         return list[size-1]+recursive_of_list(list,size-1)
# list = [1,2,53,6,4,6,5]
# print(recursive_of_list(list,len(list)))

""" ///////Multiply/////"""
"""///// from recur method ///// """

# def prod_recur(list1,size):
#     if size == 1:
#         return 1
#     else:
#         return list1[size -1] * prod_recur(list1,size-1)
#
# list1 = [1,2,2,1,3,5,666,4,5,85,6,5]
# print(list1)
# print(prod_recur(list1,len(list1)))

""" to remove duplicates and multiply"""
# set1 = list(set(list1))
# print(set1)
# print(prod_recur(set1,len(set1)))

""" using for loop and multiply"""
# def prod(lis):
#     total = 1
#     for i in range(0,len(lis)):
#         total = total *lis[i]
#     return total

# lis = [ 1,2,3,4,5,6,6,5,2,1,3]
# print(lis)
# print(prod(lis))
""" to remove duplicates"""
# set1 = list(set(lis))
# print(set1)
# print(prod(set1))

""" using reduce"""
# from functools import reduce

# def prod(lis):
#     x = reduce(lambda x, y : x * y ,lis)
#     return x
# lis = [1,2,3,4,5,6]
# print(prod(lis))

""" using numpy.prod"""
# import numpy
# def multi(lis):
#     x = numpy.prod(lis)
#     return x
# lis= [ 1,2,34,5,6,4]
# print(multi(lis))


"""smallest num in liost"""
# def small_list(lis):
#     x = lis.sort()
#     return lis[0]
# lis= [1,2,3,4,5,-6555]
# print(small_list(lis))

"""using reverse"""
# def small_lis(lis1):
#     x1 = lis1.sort(reverse = True)
#     return lis1[-1]
# lis1= [ 1,265,565,-56546,655]
# print(small_lis(lis1))

"""""""""using user input with min func"""""""""
# def small_lis(lis2):
#     num = int(input("enter num of lis: "))
#     for i in range(1,num+1):
#         ele = int(input("enter ele"))
#         lis2.append(ele)
#     return min(lis2)
#
# lis2 = []
# print(small_lis(lis2))


""""Largest num in list"""
# def largest(arr):
#     x = arr.sort()
#     return arr[-0]
# arr = [1,25,3,4650000,56,]
# print(largest(arr))


"""using reverse"""
# def lar(lis):
#     x = lis.sort(reverse = True)
#     return lis[0]
# lis= [ 1,22,6,65,565]
# print(lar(lis))

"""user input method with max func"""
# def large_lis(lis2):
#     num = int(input("enter num of lis: "))
#     for i in range(1,num+1):
#         ele = int(input("enter ele"))
#         lis2.append(ele)
#     return max(lis2)

# lis2 = []
# print(small_lis(lis2))

""""second largest num in list"""""
# def second_large(lis):
#     second_lar = 0
#     largest = min(lis)
#     for i in range(len(lis)):
#         if lis[i] > largest:
#             second_lar = largest
#             largest = lis[i]
#         else:
#             second_lar =  max(second_lar,lis[i])
#     return second_lar
# lis = [1,4,55,625,55855,55]
# print(second_large(lis))


"""  Comprehenisive   """
# def sec(arr):
#     s1 = [x for x in arr if x < max(arr)]
#     return max(s1)
# arr = [1,2,5,154654,1654654,4,65496456565]
# print(sec(arr))

# def sec(arr):
#     maximum = max(arr)
#     sec_arr = []
#     for x in arr:
#         if x < maximum:
#             sec_arr.append(x)
#
#
#     return max(sec_arr)
#
# arr = [1,2,5,154654,1654654,4,65496456565]
# print(sec(arr))



""""   Lambda   """
# def sec(arr):
#     maximum = max(arr)
#     max1 = max(arr, key = lambda x : min (arr)-1 if (x == maximum) else  x)
#     return max1
#
# arr = [23,65569,656,26296,2659,626]
# print(sec(arr))
# def sec(arr):
#
#     maximum = max(arr)
#
#     def c_key(x):
#         if x == maximum:
#             return min(arr)-1
#         else:
#             return x
#     max1 = max(arr,key = c_key)
#     return max1
#
# arr = [5,6,7,8]
# print(sec(arr))


# """"""""""""""""even num in LIST""""""""""""""""
# def even(lis):
#
#     for num in lis:
#         if num % 2 ==  0:
#             print(num, end=" ")
# lis = [121,4946,49646,659,56]
#
# def even_list(lis):
#     num = 0
#     while num < len(lis):
#         if lis[num] %

# ************ list Comprehensive for Even numbers====********

# list1 = [10, 27, 4, 45, 44, 93]
# x = list(filter(lambda x : (x % 2 == 0) , list1))
# print(x)

# ************ list Comprehensive for ODD numbers====********
# list1 = [10, 27, 4, 45, 44, 93]
# x = list(filter(lambda x : (x % 2 != 0) , list1))
# print(x)



# ********** List Lambda function for Even Numbers************
# list1 = [10, 27, 4, 45, 44, 93]
# x = [num for num in list1 if num%2 == 0]
# print(x)

# ********** List Lambda function for ODD Numbers************
# list1 = [10, 27, 4, 45, 44, 93]
# x = [num for num in list1 if num%2 != 0]
# print(x)

# *********  RECURSIVE METHOOD ***************
# def even_num(list1, n=0):
#     if n == len(list1):
#         exit()
#     if list1[n] % 2 == 0:
#         print(list1[n], end=" ")
#     even_num(list1, n + 1)
#
#
# list1 = [23, 616, 3, 66, 3, 6532, 89]
# print(even_num(list1))

# ************ RECURsive method for ODD number *************
# def even_num(list1,n =0):
#
#     if n == len(list1):
#         exit()
#     if list1[n] %2 != 0:
#         print(list1[n], end=" ")
#     even_num(list1, n+1)
# list1= [212,646,9,26459,3,6966]
# print(even_num(list1))


# *********** RANGE Function  for Even Numbers  ***************
# for n in range(0,100,2):
#     print(n , end=" ")



# ************************* POSITIVE NUM IN LIST *******
# lis = [12,-5,-5965,2629,-5895]
# for num in lis:
#     if num <= 0 :
#         print(num, end = " ")

# lis = [12,-5,-5965,2629,-5895]
# num = 0
# while (num < len(lis)):
#     if lis[num] >= 0:
#         print(lis[num], end = " ")
#     num = num + 1

# ********* Recursive ********
# def pos(lis, n = 0):
#     if n ==  len(lis):
#         exit()
#     if lis[n] >= 0:
#         print(lis[n], end= " ")
#     even(lis, n+1)
# lis = [12,-56,99,-987,-89,465459]
# print(even(lis))


# ********** Positive num using COMPREHENSIVE   ****
# lis = [12,-56,99,-987,-89,465459]
# x = [n for n in lis if n >= 0 ]
# print(x)

# ********* LAMBDA ******
# lis = [12,-56,99,-987,-89,465459]
# x = list(filter(lambda x : (x<= 0) ,lis ))
# print(x)

# ******* Positive numbers in Range of list *******
# s = -8
# e = 46
# list1 = []
# for num in range(s,e+1):
#     if num < 0:
#         list1.append(num)
# print(list1, end = "")

# **************** Negative numbers in range of list *************
# def neg(lis,s, e):
#     for i in range(s, e+1):
#         if i >= 0:
#             lis.append(i)
#     return lis
# s = -8
# e = 9
# lis = []
# print(neg(lis,s,e))


""" Remove elements  WITH  Comprehensive and based on perticular elements"""


# lis =[1541,4,84.56,595,549.656]
# x = {84.56,549.656}
# y = [i for i in lis if i not in x]
# print(y)

""" Remove elements WITHOUT Comprehensive and based on perticular elements"""

# def lis(liss, x):
#     y = []
#     for i in liss:
#         if i not in x:
#             y.append(i)
#     return y
#
# n = int(input("enter"))
# liss = list(map(int, input().split(" ")[:n]))
# x = [2,3]
# print(lis(liss,x))

""" Remove elements  based on INDEX of  elements"""
# def lis(list1,x):
#     for i in sorted(x, reverse = True):
#         del list1[i]
#     return list1
# list1 = [1,265,359,3,94,49,2]
# x = [0,1,2]
# print(lis(list1,x))

"""    Remove empty list in a list  """
# lis =[1541,4,[],595,549.656,[],[],[]]
# x = []
# y = []
# for i in lis:
#     if i != x:
#         y.append(i)
# print(y)

""" or else use comprehensive method without INDEX """
# lis = [1541,4,[],595,549.656,[],[],[]]
# x = [[]]
# y = [i for i in lis if i not in x]
# print(y)

"""   using DEL method  based on INDEX """
# lis = [1541,4,[],595,549.656,[],[],[]]
# x = [2,5,6,7]
#
# for i in sorted(x, reverse = True):
#     del lis[i]
# print(lis)


"""  COPY or CLONE a list using shallow and deepcopy methods"""
# import copy
# lis = [11,2165,123,[15,1216,326],626,235,33,3335]
# lis1 = copy.copy(lis)
# print(id(lis1), lis1)
# lis2 = copy.deepcopy(lis)
# print(id(lis2),lis2)


"""  COPY or CLONE a list Using SLICE method   """
# lis = [11,2165,123,[15,1216,326],626,235,33,3335]
# lis1 = lis[:]
# print(lis)
# print(lis1)

"""  COPY or CLONE a list Using ASSIGNMENT operator   """
# lis = [11,2165,123,[15,1216,326],626,235,33,3335]
# lis1 = lis
# print(lis)
# print(lis1)


"""  COPY or CLONE a list Using  "EXTEND method"  """
# lis = [11,2165,123,[15,1216,326],626,235,33,3335]
# lis1 = []
# lis1.extend(lis)
# print(lis)
# print(lis1)

"""  occurence of a list elemnet  using "FOR LOOP"  """

# def count1(lis,x):
#     count = 0
#     for i in lis:
#         if i == x:
#             count = count + 1
#     return count
# lis = [11,2165,123,626,235,33,33,33,33,3,33,33335]
# x = 33
# print(count1(lis,x))


"""  occurence of a list elemnet  using "LIST COMPREHENSIVE"  """
# lis = [11,2165,123,626,235,33,33,33,33,3,33,33335]
# ele = 33
# x = [i for i in lis if i == ele]
# print(x)
# print(len(x))


"""  occurence of a list elemnet  using "COUNT FUNCTION"  """
# def  cou(lis,x):
#     return lis.count(x)
# lis = [11,2165,123,626,235,33,33,33,33,3,33,33335]
# x = 33
# print(cou(lis,x))
