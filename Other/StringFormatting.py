#Python string formatting

#String format()
price=45
msg="Ttotal bill is {}. Thank you"
print(msg.format(price))

print("\n")
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#can add parameters inside the curly brackets to specify how to convert the value
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

print("\n")
#Multiple values
items=2
rate=10
total=items*rate
msg="For {} items, with rate of {}, bill is {}. Thank you"
print(msg.format(items,rate,total))

#Index numbers in multiple values
items=2
rate=10
total=items*rate
msg="your bill is {2:.2f}, for {0} quantity of rate {1}. Thank you"
print(msg.format(items,rate,total))

print("\n")
#Refer same value more than once
items=2
rate=10
total=items*rate
msg="your bill is {2:.2f}, for {0} quantity of rate {1}. so please pay in cash rupees {2} Thank you."
print(msg.format(items,rate,total))

print("\n")
#Named Indexes: But then you must use names when you pass the parameter values. example: msg.format(items=2)
#items=2
#rate=10
#total=items*rate
msg="your bill is {total}, for {items} quantity of rate {rate}. so please pay in cash rupees {total} Thank you."
print(msg.format(items=2,rate=10,total=items*rate))
