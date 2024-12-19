import miller as m
import numpy as np
import matplotlib.pyplot as plt

def plot_area(A, D, save_fig=True):
    """plot area vs delta

    Args:
        A (_type_): area
        D (_type_): delta
        save_fig (bool, optional): save figure. Defaults to True.
    """
    plt.plot(A, D)
    plt.axis("equal")
    plt.xlabel("Area")
    plt.ylabel("Delta")
    if save_fig:
        plt.savefig("AvsD.png")

def main():
    deltas = np.linspace(0,1,100)
    areas = np.zeros_like(deltas)
    
    for (i,d) in enumerate(deltas):
        r,z = m.flux_surface(2.2, 1.5,deltas[i],2.5)
        areas[i] = m.area(r,z)
    
    plot_area(deltas,areas)   
       

if __name__ == "__main__":
    main()