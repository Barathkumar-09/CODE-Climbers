def add(num1,num2): 
	return num1+num2 
def sub(num1,num2): 
	return num1-num2 
def mul(num1,num2): 
	return num1*num2 
def div(num1,num2): 
	return num1/num2 
ch=int(input("""Enter your choice :
		1. Add  
		2. Subtract 
		3. Multiply  
		4. Divide
		choice:"""))
 
num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 
if ch==1: 
	print(num1,"+",num2,"=",add(num1,num2)) 
elif ch==2: 
	print(num1,"-",num2,"=",sub(num1,num2)) 
elif ch==3: 
	print(num1,"*",num2,"=",mul(num1,num2)) 
elif ch==4: 
	print(num1,"/",num2,"=",div(num1,num2)) 
else: 
	print("wrong input") 
