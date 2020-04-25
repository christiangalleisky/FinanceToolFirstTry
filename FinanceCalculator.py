import tkinter as tk

HowManyFiveYearPeriods0, contributions0, interestRates0 = 0, 0, 0

def g():
    interestRates = E2.get()
    interestRates0 = interestRates.split(',')
    contributions = E3.get()
    contributions0 = contributions.split(',')
    HowManyFiveYearPeriods0 = int(E1.get())
    BarChart(interestRates0, contributions0, HowManyFiveYearPeriods0)

root = tk.Tk()
top = tk.Tk()
top.title("Gathering Info:")
L1 = tk.Label(top, text="How many five year periods?").grid(row=0, column=0)
E1 = tk.Entry(top, bd = 2)
E1.grid(row=0, column=1)
L2 = tk.Label(top, text="Comma seperated, interest rates for those years:").grid(row=1, column=0)
E2 = tk.Entry(top, bd =5)
E2.grid(row=1, column=1)
L3 = tk.Label(top, text="Comma seperated, annual contributions:").grid(row=2, column=0)
E3 = tk.Entry(top, bd =8)
E3.grid(row=2, column=1)
b = tk.Button(top, text='DONE?', command=g).grid(row=3, column=0)

def BarChart(intRate, conts, FiveYears):


    root.title("Tkinter Bar and Pie Graph")

    #here is for bar chart............

    tk.Label(root, text='Bar Chart in thousands').pack()

    data = gatherData(FiveYears, conts, intRate)
    c_width = 400
    c_height = 500
    c = tk.Canvas(root, width=c_width, height=c_height, bg= 'white')
    c.pack()
    frame = tk.Frame(root, width=400, height=500)
    frame.pack(expand=True, fill='both')
    vbar = tk.Scrollbar(frame, orient='vertical')
    vbar.pack(side='right', fill='y')
    vbar.config(command=c.yview)

    #experiment with the variables below size to fit your needs

    y_stretch = 1
    y_gap = 20
    x_stretch = 10
    x_width = 20
    x_gap = 20
    for x, y in enumerate(data):
    # calculate reactangle coordinates
        x0 = x * x_stretch + x * x_width + x_gap
        y0 = c_height - (y * y_stretch + y_gap)
        x1 = x * x_stretch + x * x_width + x_width + x_gap
        y1 = c_height - y_gap
    # Here we draw the bar
        c.create_rectangle(x0, y0, x1, y1, fill="red")
        c.create_text(x0+2, y0, anchor=tk.SW, text=str(y))

def gatherData(HowManyFiveYearPeriods, contributions, interestRates):
    i = 0
    sum = 0
    partialSums = []
    while i < HowManyFiveYearPeriods:
        x = 0
        while x < 5:
            sum += int(contributions[i])
            sum += sum * (float(interestRates[i]) / 100) #divide to shrink largest columns
            x += 1
        partialSums.append(sum/1000)
        i += 1
    return partialSums


root.mainloop()
top.mainloop()