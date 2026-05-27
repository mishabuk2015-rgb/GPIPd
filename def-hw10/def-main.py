from def_ import calculate

print(calculate())


print("-" * 45)



from def_ import change_case


print(change_case("hello", True))


print(change_case(text="world", upper=False))


print(change_case("python"))

params = {"text": "Rust", "upper": False}
print(change_case(**params))


params2 = {"text": "GAME", "upper": True}
print(change_case(**params2))



print("-" * 45)


from def_ import sum_numbers


print(sum_numbers("10,20,30"))
