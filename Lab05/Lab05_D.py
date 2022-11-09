import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


mu_x, mu_y = 2.5, 2.5
sigma_x, sigma_y = 1, 1
rho = 0


def f(x, y):
    '''The probability density function of a vector [𝑋𝑌]′ in the
       2-dimensional nonsingular case.
    '''
    return ((1 / (2*np.pi*sigma_x*sigma_y*np.sqrt(1-rho**2))) 
            * np.exp(-(1/(2*(1-rho**2)))
                     * (((x-mu_x)/sigma_x)**2
                        + ((y-mu_y)/sigma_y)**2
                        - ((2*rho*(x-mu_x)*(y-mu_y))/(sigma_x*sigma_y))
                       )
                    )
           )

#  Create grid array of x and y
x = np.linspace(0, 5)
y = np.linspace(0, 5)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

def main():
    fig3D = plt.figure(figsize=(8, 8))
    ax = plt.axes(projection='3d')

    ax.plot_surface(X, Y, Z, 
                    rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none'
                   )

    ax.set(xlabel='x axis', ylabel='y axis', zlabel='z axis', 
           zticks=np.arange(0.02, 0.15, 0.02)
          )
    ax.tick_params(labelsize='x-small')

    # Try matching the look in the sheet.
    ax.set_box_aspect((3, 3, 1.2))
    ax.view_init(elev=20)

    plt.savefig('Lab05_D.jpg', dpi=150)
    plt.show()


if __name__ == '__main__':
    main()