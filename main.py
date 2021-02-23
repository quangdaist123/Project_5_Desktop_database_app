from tkinter import Label, Entry, Listbox, Button, Scrollbar, SUNKEN, StringVar, IntVar, DoubleVar, END
from hdpitkinter import HdpiTk
import backend


def get_entries():
    # Set default values for tuple packing if the YEAR entry and PRICE entry is not specified
    # when using SEARCH function
    if ent_year.get() == '' or ent_price.get() == '':
        return title.get(), author.get(), 0, 0.0
    return title.get(), author.get(), year.get(), price.get()


def clear_entries():
    ent_title.delete(0, END)
    ent_author.delete(0, END)
    ent_year.delete(0, END)
    ent_price.delete(0, END)


def get_selected_line(event=None):
    # Tkinter's bind method requires 'event' parameter
    if event is not None:
        line_index = event.widget.curselection()
    else:
        line_index = listbox.curselection()
    if not line_index:
        return
    selected_line = listbox.get(line_index)
    # Clear entries
    clear_entries()

    # Insert selected row to entries
    ent_title.insert(0, selected_line[0])
    ent_author.insert(0, selected_line[1])
    ent_year.insert(0, selected_line[2])
    ent_price.insert(0, selected_line[3])
    return selected_line


def add_command():
    backend.add_book(*get_entries())
    clear_entries()
    view_command()


def del_command():
    backend.delete_book(get_entries()[0])
    clear_entries()
    view_command()


def update_command():
    backend.update_book(*get_entries())
    clear_entries()
    view_command()


def search_command():
    result = backend.search_book(*get_entries())
    view_command(result)


def view_command(result=None):
    if result is None:
        result = backend.view_all()
    # Clear old items and load updated ones in listbox
    listbox.delete(0, END)
    for index, book in enumerate(result):
        listbox.insert(END, book)


root = HdpiTk()
root.tk.call('tk', 'scaling', 2.0)
root.title("BookStore")
root.columnconfigure(0, weight=3)
root.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
# root.rowconfigure((4, 5), weight=2)
# Mấy cột còn lại weight = 0, ko co dãn

listbox = Listbox(root, width=35)
listbox.grid(row=0, column=0, rowspan=7, sticky='news', padx=15, pady=15)
# Insert selected book into entries
listbox.bind('<<ListboxSelect>>', get_selected_line)
scroll_bar = Scrollbar(root)
scroll_bar.grid(row=0, column=1, rowspan=7)
# Attach a scrollbar to the listbox
listbox.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=listbox.yview)

title = StringVar()
lbl_title = Label(root, text='Title').grid(row=0, column=2, sticky='e')
ent_title = Entry(root, width=13, borderwidth=2, relief=SUNKEN, textvariable=title)
ent_title.grid(row=0, column=3, padx=15)

author = StringVar()
lbl_author = Label(root, text='Author').grid(row=1, column=2, sticky='e')
ent_author = Entry(root, width=13, borderwidth=2, relief=SUNKEN, textvariable=author)
ent_author.grid(row=1, column=3)

year = IntVar()
lbl_year = Label(root, text='Year').grid(row=2, column=2, sticky='e')
ent_year = Entry(root, width=13, borderwidth=2, relief=SUNKEN, textvariable=year)
ent_year.grid(row=2, column=3)

price = DoubleVar()
lbl_price = Label(root, text='Price').grid(row=3, column=2, sticky='e')
ent_price = Entry(root, width=13, borderwidth=2, relief=SUNKEN, textvariable=price)
ent_price.grid(row=3, column=3)

btn_add = Button(root, text='Add', width=7, command=add_command).grid(row=4, column=2)
btn_update = Button(root, text='Update', width=7, command=update_command).grid(row=4, column=3)
btn_del = Button(root, text='Del', width=7, command=del_command).grid(row=5, column=2)
btn_search = Button(root, text='Search', width=7, command=search_command).grid(row=5, column=3)
btn_view = Button(root, text='View all', width=7, command=view_command).grid(row=6, column=2)
btn_close = Button(root, text='Close', width=7, command=root.destroy).grid(row=6, column=3)

# Show full book list when first open
view_command()

root.mainloop()
