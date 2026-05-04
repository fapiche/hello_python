nom = input("Comment tu t'appelles? ")
age = input("Quel age as tu? ")
age = int(age)
print(f"Salut {nom} ! Tu as {age} ans, c'est noté ! ")
print(f"Dans 10 ans tu auras {age+10} ans. ")
if age>=18:
    print(f"Tu es majeur ! ")
else :
    print(f"Tu es mineur ! ")