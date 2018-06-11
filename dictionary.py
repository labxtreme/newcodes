name = input("Enter your Name: ")
name="NAME="+name
name=name.split('=')
info=list()
info.append(name)
age= input("Enter your Age: ")
age="AGE="+age
age=age.split('=')
info.append(age)
country= input("Enter your Country: ")
country="COUNTRY="+country 
country=country.split('=')
info.append(country)
language= input("Enter your Language: ")
language="LANGUAGE="+language
language=language.split('=')
info.append(language)
address= input("Enter your Address: ")
address="ADDRESS="+address
address=address.split('=')
info.append(address)
info=dict(info)
print("The Data is \n\n",info)

input("\n\nEnter Any key to exit")

