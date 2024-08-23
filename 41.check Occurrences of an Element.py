import time
fruits=["apple","banana","mango","apricot","alf"]
print('"wich fruits you wants"')
iwant=input("which fruits you want:")
exist=iwant in fruits
time.sleep(3)
print("if fruit exist than 'TRUE' if not exists'FALSE:'",exist)