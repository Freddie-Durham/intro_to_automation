import numpy as np
import matplotlib.pyplot as plt


def plot_surface(R_s, Z_s, save_fig=True):
    """
    Args:
        R_s (_type_): radius
        Z_s (_type_): flux
        save_fig (bool, optional): pretty obvious. Defaults to True.
    """
    plt.plot(R_s, Z_s)
    plt.axis("equal")
    plt.xlabel("R [m]")
    plt.ylabel("Z [m]")
    if save_fig:
        plt.savefig("miller.png")


def flux_surface(
    A,
    kappa,
    delta,
    R0,
    theta=np.linspace(0, 2 * np.pi),
):
    """Calculates flux surface using Miller parameterisation
    Args:
        A (_type_): area
        kappa (_type_): no clue
        delta (_type_): delta
        R0 (_type_): probably radius
        theta (_type_, optional): probably an angle. Defaults to np.linspace(0, 2 * np.pi).

    Returns:
        _type_: parameters for plotting
    """
    r = R0 / A
    R_s = R0 + r * np.cos(theta + (np.arcsin(delta) * np.sin(theta)))
    Z_s = kappa * r * np.sin(theta)
    return R_s, Z_s


def area(r, z):
    """Find area of cross section of axisymmetric tokamak

    Args:
        r (_type_): minor radius
        z (_type_): z value

    Returns:
        _type_: number
    """
    # abs because (r, z) start on the out-board midplace and r decreases
    return np.abs(np.trapezoid(z, r))


def main():
    R_s, Z_s = flux_surface(2.2, 1.5, 0.3, 2.5)
    plot_surface(R_s, Z_s)


if __name__ == "__main__":
    main()
