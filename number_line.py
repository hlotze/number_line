"""
read excel file "Jahrestag.xlsx"
and genrate a number line of years
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Setup a plot such that only the bottom spine is shown
def setup(ax):
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1)
    ax.tick_params(which='major', length=5)
    ax.tick_params(which='minor', width=0.75)
    ax.tick_params(which='minor', length=2.5)
    #ax.set_xlim(-0.5, 5.5)
    ax.set_xlim(1900, 2030)
    ax.set_ylim(0, 1)
    ax.patch.set_alpha(0.0)

def main():
    fname = "./Jahrestage.xlsx"
    df = pd.read_excel(fname)

    plt.figure(figsize=(8, 6))

    # Multiple Locator
    ax = plt.subplot(8, 1, 1)
    setup(ax)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    #ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))

    #x_arr = [0, np.euler_gamma, np.sqrt(2), np.pi]
    x_arr = [x.year for x in df["date"].to_list()]
    y_arr = np.full(len(x_arr), 0.2)
    ax.plot(x_arr, y_arr, "ro")

    plt.show()
    
if __name__ == '__main__':
    main()