# dictionary is a collection of key:value pairs. 
# Each key is associated with each value and we can retrive and manipulate data using key.

dict1 = {"name" : "laxmi","age": 20,"Degree":"BE"}

print(dict1)
print(type(dict1))

print(len(dict1)) 

dict1["college"] = "AGMR" # Updating the dictionary
print(dict1)

print(dict1["name"])# Accessing value

dict1["age"] = "39" # Updating the age
print(dict1) 

dict1["Friend"] = "nagaveni" # Adding a key value to the dictionary
print(dict1)

del dict1["age"] # Deleting the age by "del"
print(dict1)

dict1.pop("Degree") # Deleting key by "pop()"
print(dict1)

dict1.get("my heart")
print(dict1)

print(dict1.keys()) # return all the keys
print(dict1.values()) # Return all the values 
print(dict1.items()) # Return all key value pairs


new_dict = {"city":"gadag",}
dict1.update(new_dict)
print(dict1)

dict2 = {"gadag":"good","hubli":"bad"}
print(dict2)
dict3 = {"Mysure":"dosa","koppal":"vada"}

dict_total = [dict2, dict3,]
print(dict_total)

print(f"best food : {dict3["Mysure"] + " & "  + dict3["koppal"]}")

mix = {"city":"gadag",
       2 : "near sabarmati ashram",
       "list1" :{"ragi","rice"},
       "new dict":{"home":"hubli"},
       "weight" :"38.9 kg"}
print(mix)

# Student Marks Management System
students = {
       "laxmi" : 85,
       "swati" : 97,
       "nivas" : 87,
       "kiran" : 69,
       "sneha" : 73
}

for name,marks in students.items():
       print(name,":",marks )
       
# Search for a student
name = input("Enter student name to search :")

if name in students :
       print("Marks :",students[name])
else:
       print("student not found")
 
 # Update marks      
name = input("Enter student name to update :")

if name in students:
       marks = int(input("Enter new marks :"))
       students[name] = marks
       print("Marks updated successfully")
else:
       print("Student not found")
 
 #display students scoring above 80      
print("Student scoring above 80 :")

for name, marks in students.items():
       if marks>80:
              print(name,":",marks)

# Online shopping cart
cart = {
       "Laptop" : 50000,
       "Mouse" : 500,
       "Keyboard" : 1500,
       "Headphones" : 2000
}

print("Shopping cart:")

for product,price in cart.items():
       print(product,":",price)

cart["USB cable"]=300

cart["Mouse"] = 600

total =0

for price in cart.values():
       total+= price
print("total cost : ",total)

expensive_product =max(cart,key=cart.get)

print("Most Exoensive Product:",expensive_product)
print("Price:",cart[expensive_product])
