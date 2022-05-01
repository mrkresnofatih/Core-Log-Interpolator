def interpolate(tab_x, tab_y, x):
    if x <= tab_x[0]:
        return tab_y[0]
    elif x > tab_x[-1]:
        return tab_y[-1]
    else:
        i = 0
        while x > tab_x[i]:
            i = i + 1
        return tab_y[i - 1] + (tab_y[i] - tab_y[i - 1])*(x - tab_x[i - 1])/(tab_x[i] - tab_x[i - 1])
