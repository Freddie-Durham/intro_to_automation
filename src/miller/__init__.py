import numpy as np
import matplotlib.pyplot as plt
import argparse
import tomli


def plot_surface(R_s, Z_s,filename="miller.png",save_fig=True):
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
        plt.savefig(filename)


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
    
    parser = argparse.ArgumentParser(
    prog="Miller",
    description="Runs miller and generates plot",
    epilog="bottom text",
    )

    parser.add_argument("--filename",type=str,default="input.toml")  # positional argument
    args = parser.parse_args()
    
    with open(args.filename, "rb") as f:
        data = tomli.load(f)
    
    parser.add_argument("--plotname",type=str,default="miller.png")  # positional argument
    parser.add_argument("--A",type=float,default=data["miller"]["A"])  # option that takes a value
    parser.add_argument("--kappa",type=float,default=data["miller"]["kappa"])
    parser.add_argument("--delta",type=float,default=data["miller"]["delta"])
    parser.add_argument("--R0",type=float,default=data["miller"]["R0"])

    args = parser.parse_args()

    R_s, Z_s = flux_surface(A=args.A,kappa=args.kappa,delta=args.delta,R0=args.R0)
    plot_surface(R_s, Z_s,filename=args.plotname)


if __name__ == "__main__":
    main()
