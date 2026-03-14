#Call the tkinter library to visualize my Calculator app
import tkinter as tk

# Create a function to count the Final Price
def count_discount():
    price = float(entry_price.get())
    discount = float(entry_discount.get())

    final_price = price - (price * discount / 100)

    label_result.config(text=f"Final Price: Rp {final_price:,.2f}")


# Create a window for my Calculator app
window = tk.Tk()
window.title("Mister Calculator")
window.geometry("300x300")

# This is for the Normal Price label
label_price = tk.Label(window, text="Normal Price :")
label_price.pack()

#This is for the text box to input the Normal Price
entry_price = tk.Entry(window)
entry_price.pack()

# This is for the Discount label
label_discount = tk.Label(window, text="Discount (%) :")
label_discount.pack()

#This is for the text box to input the Discount
entry_discount = tk.Entry(window)
entry_discount.pack()

# This is for the Count button
button_count = tk.Button(window, text="Count", command=count_discount)
button_count.pack()

# This is for the Result label
label_result = tk.Label(window, text="Final Price : ")
label_result.pack()

# Run my Calculator app
window.mainloop()