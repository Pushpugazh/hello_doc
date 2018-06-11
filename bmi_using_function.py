n1 = input('name ')
h1 = float(input('height in meters '))
w1 = float(input('weight in kg '))
n2 = input('name ')
h2 = float(input('height in meters '))
w2 = float(input('weight in kg '))
n3 = input('name ')
h3 = float(input('height in meters '))
w3 = float(input('weight in kg '))


def calculator(name, height, weight):
    bmi = weight / (height ** 2)
    print('bmi: ', bmi)
    if bmi < 25:
        return name + ' is not obese'
    else:
        return name + ' is obese'


t = calculator(n1, h1, w1)
u = calculator(n2, h2, w2)
v = calculator(n3, h3, w3)
print(t);
print(u);
print(v)
