
import pygame
import random
pygame.font.init()

screen = pygame.display.set_mode((900, 650))

width = 1000
length = 700
array = [0]*100
arr_clr = [('red')]*100
Color_line = (255,0,0); #red
clr =[(0, 204, 102), (255, 0, 0),
(0, 0, 153), (255, 102, 0)]
def generate():
    for i in range(1, 100):
        arr_clr[i] = (255,0,0)
        array[i] = random.randrange(1,100)
    print(array)

def drawLine(num,x,y):
    pygame.draw.line(screen,Color_line, (x,y),(x,y+num))


def drawArray():
    x = 100
    y = 100
    for i in array:
        drawLine(i,x,y)
        x += 5
    pygame.display.flip()
def update():
    screen.fill((255,255,255))
    drawArray()
    pygame.display.update()
    pygame.time.delay(5)


def mergeSort(arr,l,r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def merge(arr,l,mid,r):
    n1 = mid - l + 1
    n2 = r - mid

    # create temp arrays
    left = [0] * (n1)
    right = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        left[i] = arr[l + i]

    for j in range(0, n2):
        right[j] = arr[mid + 1 + j]

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
    pygame.event.pump()
    while i < n1 and j < n2:
        arr_clr[i] = clr[1]
        arr_clr[j] = clr[1]
        update()
        arr_clr[i] = clr[0]
        arr_clr[j] = clr[0]
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = left[i]
        update()
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = right[j]
        update()
        j += 1
        k += 1

def main():
    print("main run")
    global running
    running = True
    generate()

    while running:
        (mergeSort(array,0,len(array)-1))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                running = False
        update()
        pygame.display.update()


# # Driver code to test above
# arr = [12, 11, 13, 5, 6, 7]
# n = len(arr)
# print("Given array is")
# for i in range(n):
#     print("%d" % arr[i]),
#
# mergeSort(arr, 0, n - 1)
# print("\n\nSorted array is")
# for i in range(n):
#     print("%d" % arr[i]),

if __name__== "__main__":
    main()

