def unpack_it(name, age, address):
    print("Name:", name)
    print("Age:", age)
    print("Address:", address)

mydic = {"name": "Kim", "age": 22, "address": "Seoul"}
unpack_it(**mydic)
