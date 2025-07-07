import tkinter as tk
from tkinter import ttk, messagebox

# Static exchange rates
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.91,
    'INR': 83.12,
    'GBP': 0.78,
    'JPY': 157.45
}

currencies = list(exchange_rates.keys())

# Convert function
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        usd_amount = amount / exchange_rates[from_curr]
        converted_amount = usd_amount * exchange_rates[to_curr]

        result_var.set(f"{amount} {from_curr} = {round(converted_amount, 2)} {to_curr}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")

# Window setup
root = tk.Tk()
root.title("Currency Converter")
root.configure(bg="#bff1e7")

# Responsive UI scaling
screen_width = root.winfo_screenwidth()
if screen_width < 768:
    font_scale = 12
    entry_width = 15
    win_size = "320x420"
else:
    font_scale = 16
    entry_width = 20
    win_size = "450x400"

root.geometry(win_size)

# Title
tk.Label(root, text="💱 Currency Converter", font=("Arial", font_scale + 4, "bold"),
         bg="#bff1e7", fg="#66003F").pack(pady=10)

# Subtitle
tk.Label(root, text="Enter the amount", font=("Arial", font_scale + 1), bg="#bff1e7").pack()

# Amount entry box
amount_entry = tk.Entry(root, font=("Arial", font_scale), width=entry_width, justify='center',
                        bg="white", relief="solid", bd=2)
amount_entry.pack(pady=8)
amount_entry.insert(0, "1")

# Currency selection section with arrow
frame = tk.Frame(root, bg="#bff1e7")
frame.pack(pady=10)

from_currency = ttk.Combobox(frame, values=currencies, state="readonly",
                             font=("Arial", font_scale), width=7, justify='center')
from_currency.current(0)
from_currency.grid(row=0, column=0, padx=5)

# Arrow label
tk.Label(frame, text="→", font=("Arial", font_scale + 2, "bold"), bg="#bff1e7", fg="#333").grid(row=0, column=1)

to_currency = ttk.Combobox(frame, values=currencies, state="readonly",
                           font=("Arial", font_scale), width=7, justify='center')
to_currency.current(1)
to_currency.grid(row=0, column=2, padx=5)

# Convert button
tk.Button(root, text="Convert", command=convert_currency,
          font=("Arial", font_scale), bg="#9e1042", fg="white",
          width=entry_width, relief="raised", bd=3).pack(pady=15)

# Result label
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", font_scale + 1, "bold"),
         bg="#bff1e7", fg="#601134").pack(pady=10)

# Run app
root.mainloop()


