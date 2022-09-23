from random import randint

def puzsort(arr, dir):

    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if dir == 0:
                if arr[j] > arr[j+1]:
                    buff = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = buff
            else:
                if arr[j] < arr[j+1]:
                    buff = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = buff

def main():
    print("0 - по возрастанию, 1 - по убыванию")
    dir = int(input())
    arr = []
    for i in range(15):
        arr.append(randint(1, 99))
    print(arr)
    puzsort(arr, dir)
    print(arr)

main()