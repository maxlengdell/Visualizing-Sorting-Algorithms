
import pygame
import random
pygame.font.init()

screen = pygame.display.set_mode((900, 650))
array = [0]*150
arr_clr = [('red')]*150
Color_line = (255,0,0); #red
clr =[(0, 204, 102), (255, 0, 0),
(0, 0, 153), (255, 102, 0)]
def generate():
    for i in range(1, len(array)):
        arr_clr[i] = (255,0,0)
        array[i] = random.randrange(1,300)
    print(array)

def drawLine(num,x,y):
    pygame.draw.line(screen,Color_line, (x,y),(x,y+num))

def drawArray():
    x = 100
    y = 0
    for i in array:
        drawLine(i,x,y)
        x += 5
    pygame.display.flip()
def update():

    screen.fill((255,255,255))
    drawArray()
    pygame.display.update()
    pygame.event.pump()
    pygame.time.delay(50)

def partition(arr, low, high):
    pivot = arr[high]
    i = low-1

    for j in range(low,high):
        if(arr[j] < pivot):
            #swap
            i+=1
            update()
            swap(arr,i,j)
    swap(arr, i+1,high)
    update()
    pygame.event.pump()

    return i + 1
def quickSort(arr, low, high):
    if(low < high):
        pi = partition(arr,low,high)
        quickSort(arr,low, pi-1)
        quickSort(arr, pi+1, high)
def swap(arr,i,j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

generate()
running = True
while running:
    for event in pygame.event.get():
        quickSort(array, 0, len(array) - 1)
        if event.type == pygame.quit():
            running = False
            pygame.quit()
            quit()
        else:
            quickSort(array, 0, len(array) - 1)

        if event.type == pygame.K_RETURN:
            print("run")

    update()
    pygame.display.update()
# def main():
#     print("main run")
#     global running
#     running = True
#     generate()
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.quit():
#                 running = False
#                 pygame.quit()
#                 quit()
#             if event.type == pygame.K_RETURN:
#                 print("return")
#
#         update()
#         pygame.display.update()
#
# if __name__== "__main__":
#     main()
#
