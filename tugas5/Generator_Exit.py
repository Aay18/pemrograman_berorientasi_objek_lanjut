def my_generator():
    try:
        yield 11
        yield 12
        yield 13
    except GeneratorExit:
        print("Generator stopped")

gen = my_generator()

print(next(gen))
print(next(gen))
gen.close()
