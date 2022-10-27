from cgitb import text
import tkinter as tk
import yfinance as yf

win = tk.Tk()
win.title('Stock info')

top_widget = tk.Frame(win)
label = tk.Label(top_widget, text='Write stock ticker:')
label.pack(side=tk.LEFT)
entry = tk.Entry(top_widget)
entry.pack(side=tk.RIGHT)
top_widget.pack()

scrollbar = tk.Scrollbar(win)
text_box = tk.Text(win, height=20, width=100, padx=5, pady=5, font='Helvetica 12')

scrollbar.pack(side=tk.RIGHT, fill = tk.Y)
text_box.pack(expand=True, fill= tk.BOTH)
scrollbar.config(command=text_box.yview)
text_box.config(yscrollcommand=scrollbar.set)

def download_data(e):
    text_box.delete('1.0', tk.END)
    stock = str(e.widget.get())
    
    if not stock:
        print('No stock ticker!')
        return
    
    stock = stock.upper().strip()
    print('download stock data:', stock)

    stock_data = yf.Ticker(stock)
    print(stock_data.info, '\n')

    text_box.insert(tk.END, 'Ticker: ' + stock + '\n\n')

    for key in stock_data.info.keys():
        try:
            v = str(key) + ': ' + stock_data.info[str(key)] + '\n'
            text_box.insert(tk.END, v)
        except:
            pass
    
    history = stock_data.history(period='1y', interval='1mo')
    text_box.insert(tk.END, f'\n{history}')

entry.bind('<Return>', download_data)


win.mainloop()