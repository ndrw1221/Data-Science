def draw_grid(m=2, n=3):
    index = 0
    while index < m:
        print('+'+' - - +'*n)
        print('/'+'     /'*n)
        print('/'+'     /'*n)
        index = index + 1
    print('+'+' - - +'*n)

if __name__ == '__main__':    
    draw_grid()
    draw_grid(3, 2)