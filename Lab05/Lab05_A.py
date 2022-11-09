import matplotlib.pyplot as plt
import pandas as pd


def main():
    """Get sale unit of bathingsoap and facewash in sales_data.csv and show
    it using the subplots. The figure will be in the xkcd style.
    """
    SALES_DATA_DF = pd.read_csv("sales_data.csv")
    y1 = SALES_DATA_DF["bathingsoap"]
    y2 = SALES_DATA_DF["facewash"]
    x = SALES_DATA_DF["month_number"]
    plt.xkcd()  # use the xkcd style for plotting

    # make subplots with 2 rows and 1 column, share x axis for the subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 5))

    # plot sales units of Bathingsoap for each month
    ax1.plot(x, y1, color="k", marker="o", lw=3)
    ax1.set(xticks=x, yticks=[7500, 10000, 12500], title="Sales data of a Bathingsoap")

    ax2.plot(x, y2, color="k", marker="o", lw=3)
    ax2.set(
        yticks=[1500, 2000], title="Sales data if a facewash", xlabel="Month Number"
    )

    fig.supylabel("Sales units in numbers", x=0.05)  # common ylabel for subplots
    fig.tight_layout()  # use tight layout

    plt.savefig("Lab05_A.jpg", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
