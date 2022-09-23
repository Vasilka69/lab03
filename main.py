from random import randint

def puzsort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                buff = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = buff

def main():
    arr = []
    for i in range(15):
        arr.append(randint(1, 99))
    print(arr)
    puzsort(arr)
    print(arr)

main()