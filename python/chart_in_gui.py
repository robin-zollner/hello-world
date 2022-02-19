# Importing pandas
import pandas as pd
from pandas import DataFrame

# Creating DataFrames from prepared JSON files
df1 = pd.read_json('Bar_Chart.json')
df2 = pd.read_json('Line_Chart_Data.json')
df3 = pd.read_json('Scatter_Chart_Data.json')

# Importing tkinter as GUI and matplotlib for plotting
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# create main GUI window
root = tk.Tk()
figframe = tk.Frame(root).pack(side=tk.TOP, fill=tk.BOTH)
uiframe = tk.Frame(root).pack(side=tk.TOP, fill=tk.BOTH)

# Create Button Command Functions
def readText():
	input_text = e1.get()
	msg = tk.messagebox.showinfo("Entered Text", input_text)
	print(input_text)

# adding UI elements
b1 = tk.Button(uiframe, text="Quit", command=root.quit).pack(side=tk.TOP)#, fill='x')
l1 = tk.Label(uiframe, text="Enter Text:").pack(side=tk.TOP)#, fill='x')
e1 = tk.Entry(uiframe,bd=5, textvariable="StringVar")
e1.pack(side=tk.TOP)#, fill='x')
input_text = '';
print(e1.get())
b2 = tk.Button(uiframe, text="Read Entry Text", command = readText).pack(side=tk.TOP)
l2 = tk.Label(uiframe, text=input_text).pack(side=tk.TOP, fill='x')


# First Figure
figure1 = plt.Figure(figsize=(6,5), dpi=100) # creates matplotlib figure
ax1 = figure1.add_subplot(111) # creates axes inside figure
bar1 = FigureCanvasTkAgg(figure1, figframe) # inserts figure into tk window
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH) # positions figure in tk window
df1 = df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum() # defines x-axis
df1.plot(kind='bar', legend=True, ax=ax1) # plots data as bar chart
ax1.set_title('Country vs GDP Per Capita') # sets chart title
ax1.set_xlabel('Country') # sets x-axis label
ax1.set_ylabel('GDP per Capita') # sets y-axis label

# Second Figure
figure2 = plt.Figure(figsize=(6,5), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, figframe)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')
ax2.set_xlabel('Year')
ax2.set_ylabel('Unemployment Rate(%)')

# Third Figure
figure3 = plt.Figure(figsize=(6,5), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Interest_Rate'], df3['Stock_Index_Price'], color='g')
scatter3 = FigureCanvasTkAgg(figure3, figframe)
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend(['Stock_Index_Price'])
ax3.set_xlabel('Interest Rate')
ax3.set_ylabel('Stock Index Price')
ax3.set_title('Interst Rate Vs. Stock Index Price')

# run GUI
root.mainloop()