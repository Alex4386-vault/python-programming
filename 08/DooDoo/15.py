def unpack_it(**kwargs):
    print("Name:", kwargs['name'])
    print("Age:", kwargs['age'])
    print("Address:", kwargs['address'])

mydic = {"name": "Kim", "age": 22, "address": "Seoul"}
unpack_it(**mydic)
