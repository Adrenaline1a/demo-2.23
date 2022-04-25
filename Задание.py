#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
from threading import Thread
from time import sleep


def func1():
    x = 0.3
    y = math.cos(x)
    EPS = 1e-07
    a = 1
    S, n = 0.0, 0
    while math.fabs(a) > EPS:
        S += ((-1)**n*x**(2*n))/(math.factorial(2*n))
        a = S - y 
        n += 1
        print(f"Функция 1 - S={S}")
        sleep(0.4)
    print(f"Вывод функция 1:  S={S}")
    

def func2():
    x = 0.4
    y = math.log(x+1)
    EPS = 1e-07
    a = 1
    S, n = 0.0, 1
    while math.fabs(a) > EPS:
        S += ((-1)**(n-1)*x**n)/n
        a = S - y
        n += 1
        print(f"Функция 2 - S={S}")
        sleep(0.4)
    print(f"Вывод функция 2: S={S}")


if __name__ == "__main__":
    th1 = Thread(target=func1)
    th2 = Thread(target=func2)
    th1.start()
    th2.start()
