a =input("Enter any string :")
print("Length of the string :",len(a))
print("strip function:",a.strip())
print("replace function(\'a\' with \'e\'):",a.replace("a", "e"))
print("count of \'a\' in given text :",a.count("a"))
print("printing postion of first a:",a.find("a"))#-1 if not found
print("upper function:",a.upper())
print("lower function:",a.lower())
print("swap function:",a.swapcase())
print("Slicing function:")
print("\t1)\t",a[2:7])#escape charcter
print("\t2)\t",a[:5])
print("\t3)\t",a[5:])
print("\t4)\t",a[-7:-2])
b=" Thank you !"
print("conctenation of \"thank you \" to the entered string :",a+b)#escape charcter
