import gc
from math import *
from time import sleep

screen = []

def matmul(a, b):
    
    if len(a[0]) != len(b):
        print("Error:\nRows do not match coloms.")
    else:
        answer = []
        for i in a:
            colum = []
            for j in range(0, len(b[0])):
                s = 0
                for k in range(0, len(b)):
                    s += i[k] * b[k][j]
                colum.append(s)
            answer.append(colum)
        return answer

rotate = []

def clear():
    global screen
    print(chr(27) + "[2J")
    screen =[" "*60]*26

def update(obj,rable):
    if rable:
        zr = obj.zr
        rz = [
            [cos(zr), -sin(zr)],
            [sin(zr), cos(zr)]
        ]
    for j in obj.points:
        p = [
            [j[0][0]*(obj.w/2)],
            [j[1][0]*(obj.h/2)]
        ]
        if rable:
            p = matmul(rz,p)
        x = round(p[0][0]+obj.x-1)
        y = round(p[1][0]+obj.y-1)
        if y<0 or 26<y:
            y=0
        if x<0 or 60<x:
            x=0
        row = screen[y]
        screen[y] = row[0:x]+obj.color+row[x+len(obj.color):]
    gc.collect()

def render():
    for Z in screen:
        print(Z)

class square:
    def __init__(
    self, x=0, y=0, w=0, h=0, zr=0,c=' '):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.zr = zr
        self.points = [
            [[-1],[-1]],
            [[1],[-1]],
            [[1],[1]],
            [[-1],[1]],
        ]
        self.color = c

class text:
    def __init__(self,x=0,y=0,t=''):
        self.x=x
        self.y=y
        self.w=0
        self.h=0
        self.color=t
        self.points=[
            [[1],[1]]
        ]

objects = {
    "Test":square(15,8,10,10,0,'#'),
    "text":text(7,10,'testing'),
    "test2":square(19,9,10,10,0,'$')
}

while True:
    sleep(0.1)
    clear()
    for i in objects:
        rable = hasattr(objects[i],'zr')
        if rable:
            objects[i].zr +=.1
        update(objects[i],rable)
    render()