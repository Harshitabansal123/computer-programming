def test(dictt, N):
    result = sorted(dictt, key=dictt.get, reverse=True)[:N]
    return result 
dictt = {'a':5, 'b':14, 'c': 32, 'd':35, 'e':24, 'f': 100, 'g':57, 'h':8, 'i': 100}
print("Original Dictionary:")
print(dictt)
N = int(input("Enter Number of Maximum Values you want to display"))
print(N,"maximum value(s) in the said dictionary:")
print(test(dictt, N))
