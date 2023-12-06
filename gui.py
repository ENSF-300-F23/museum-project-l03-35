import tkinter
import mysql.connector
from tkinter import messagebox, ttk


def connect_and_execute(event=None):
    user_name = entry_user.get()
    password = entry_pass.get()
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user=user_name,
            password=password
        )
        cursor = conn.cursor()
        with open("art_collection.sql", "r") as sql_file:
            sql_script = sql_file.read()
            statements = sql_script.split(';')
            for statement in statements:
                if statement.strip():
                    cursor.execute(statement)
                    conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "Database setup complete.")
        main_menu()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")

button_style = {
        'bg': '#007acc',
        'fg': 'white',
        'font': ('Helvetica', 13, 'bold'),
        'width': 15,
        'height': 2,
        'relief': tkinter.RAISED,
        'borderwidth': 2,
        'cursor': 'hand2',
    }

def on_enter(e, btn):
    btn['background'] = '#00ccb8'

def on_leave(e, btn):
    btn['background'] = '#007acc'

def main_menu():
    root.withdraw()
    main_menu = tkinter.Toplevel(root)
    main_menu.title("Main Menu")

    window_width = 500
    window_height = 300
    screen_width = main_menu.winfo_screenwidth()
    screen_height = main_menu.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    main_menu.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    main_menu.minsize(window_width, window_height)

    main_menu.configure(bg='#f0f0f0')

    button_frame = tkinter.Frame(main_menu, bg='#f0f0f0')
    button_frame.pack(pady=50)

    btn_admin = tkinter.Button(button_frame, text="ADMIN",command=create_admin_login_window, **button_style)
    btn_admin.pack(pady=10)
    btn_admin.bind("<Enter>", lambda e, btn=btn_admin: on_enter(e, btn))
    btn_admin.bind("<Leave>", lambda e, btn=btn_admin: on_leave(e, btn))

    btn_data_entry = tkinter.Button(button_frame, text="DATA ENTRY", **button_style)
    btn_data_entry.pack(pady=10)
    btn_data_entry.bind("<Enter>", lambda e, btn=btn_data_entry: on_enter(e, btn))
    btn_data_entry.bind("<Leave>", lambda e, btn=btn_data_entry: on_leave(e, btn))

    btn_guest = tkinter.Button(button_frame, text="GUEST", command=guest_interface, **button_style)
    btn_guest.pack(pady=10)
    btn_guest.bind("<Enter>", lambda e, btn=btn_guest: on_enter(e, btn))
    btn_guest.bind("<Leave>", lambda e, btn=btn_guest: on_leave(e, btn))

    button_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def guest_interface():
    guest_window = tkinter.Toplevel(root)
    guest_window.title("Guest Browsing Interface")
    window_width, window_height = 500, 325
    center_x, center_y = calculate_center(guest_window, window_width, window_height)
    guest_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    btn_display_artists = tkinter.Button(guest_window, text="Display Artists", command=lambda: display_artists(guest_window), **button_style)
    btn_display_artists.pack(pady=10)
    btn_display_artists.bind("<Enter>", lambda e, btn=btn_display_artists: on_enter(e, btn))
    btn_display_artists.bind("<Leave>", lambda e, btn=btn_display_artists: on_leave(e, btn))

    btn_view_collection = tkinter.Button(guest_window, text="View Collection", command=lambda: view_collection(guest_window), **button_style)
    btn_view_collection.pack(pady=10)
    btn_view_collection.bind("<Enter>", lambda e, btn=btn_view_collection: on_enter(e, btn))
    btn_view_collection.bind("<Leave>", lambda e, btn=btn_view_collection: on_leave(e, btn))

    btn_borrowed_art = tkinter.Button(guest_window, text="Borrowed Art", command=lambda: borrowed_art(guest_window), **button_style)
    btn_borrowed_art.pack(pady=10)
    btn_borrowed_art.bind("<Enter>", lambda e, btn=btn_borrowed_art: on_enter(e, btn))
    btn_borrowed_art.bind("<Leave>", lambda e, btn=btn_borrowed_art: on_leave(e, btn))

    btn_view_all = tkinter.Button(guest_window, text="View All", command=lambda: view_all(guest_window), **button_style)
    btn_view_all.pack(pady=10)
    btn_view_all.bind("<Enter>", lambda e, btn=btn_view_all: on_enter(e, btn))
    btn_view_all.bind("<Leave>", lambda e, btn=btn_view_all: on_leave(e, btn))

def calculate_center(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width / 2 - width / 2)
    center_y = int(screen_height / 2 - height / 2)
    return center_x, center_y

def display_artists(window):
    try:
        conn = mysql.connector.connect(host="localhost", user=entry_user.get(), password=entry_pass.get(), database="ArtCollection")
        cursor = conn.cursor()
        query = "SELECT * FROM Artists"
        cursor.execute(query)
        artists = cursor.fetchall()

        display_window = tkinter.Toplevel(window)
        display_window.title("Artists")

        frame = tkinter.Frame(display_window)
        frame.pack(fill='both', expand=True)

        columns = ('ID', 'Name', 'Birth Year', 'Nationality')
        tree = ttk.Treeview(frame, columns=columns, show='headings')

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor='center', width=100)

        for artist in artists:
            tree.insert('', 'end', values=artist)

        tree.pack(side='left', fill='both', expand=True)

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")



def view_collection(window):
    try:
        conn = mysql.connector.connect(host="localhost", user=entry_user.get(), password=entry_pass.get(), database="ArtCollection")
        cursor = conn.cursor()
        query = "SELECT * FROM Artworks"
        cursor.execute(query)
        artworks = cursor.fetchall()

        display_window = tkinter.Toplevel(window)
        display_window.title("Artworks")
        display_window.geometry("1475x300")

        frame = tkinter.Frame(display_window)
        frame.pack(fill='both', expand=True)

        columns = ('ID', 'Title', 'Artist ID', 'Year', 'Medium', 'Collection', 'Category', 'Status')
        tree = ttk.Treeview(frame, columns=columns, show='headings')

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')

        for artwork in artworks:
            tree.insert('', 'end', values=artwork)

        scrollbar = ttk.Scrollbar(frame, orient='horizontal', command=tree.xview)
        scrollbar.pack(side='bottom', fill='x')
        tree.configure(xscrollcommand=scrollbar.set)
        tree.pack(side='left', fill='both', expand=True)

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")



def borrowed_art(window):
    try:
        conn = mysql.connector.connect(host="localhost", user=entry_user.get(), password=entry_pass.get(), database="ArtCollection")
        cursor = conn.cursor()
        query = "SELECT * FROM Artworks WHERE Status = 'Borrowed'"
        cursor.execute(query)
        borrowed_artworks = cursor.fetchall()
        
        display_window = tkinter.Toplevel(window)
        display_window.title("Borrowed Artworks")
        display_window.geometry("1480x200")
        
        frame = tkinter.Frame(display_window)
        frame.pack(fill='both', expand=True)
        
        columns = ('ID', 'Title', 'Artist ID', 'Year', 'Medium', 'Collection', 'Category', 'Status')
        tree = ttk.Treeview(frame, columns=columns, show='headings')
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')
        
        for artwork in borrowed_artworks:
            tree.insert('', 'end', values=artwork)
        
        scrollbar = ttk.Scrollbar(frame, orient='horizontal', command=tree.xview)
        scrollbar.pack(side='bottom', fill='x')
        tree.configure(xscrollcommand=scrollbar.set)
        tree.pack(side='left', fill='both', expand=True)
        
        cursor.close()
        conn.close()
        
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")




def view_all(parent_window):
    try:
        
        conn = mysql.connector.connect(host="localhost", user=entry_user.get(), password=entry_pass.get(), database="ArtCollection")
        cursor = conn.cursor()

        
        display_window = tkinter.Toplevel(parent_window)
        display_window.title("All Museum Data")
        display_window.state('zoomed')
        
        artist_label = tkinter.Label(display_window, text="Artists")
        artist_label.pack()
        artist_columns = ("ArtistID", "Name", "BirthYear", "Nationality")
        artist_tree = ttk.Treeview(display_window, columns=artist_columns, show='headings')
        
        artist_tree.column("ArtistID", width=70, anchor='center')
        artist_tree.column("Name", width=150, anchor='center')
        artist_tree.column("BirthYear", width=70, anchor='center')
        artist_tree.column("Nationality", width=100, anchor='center')
        for col in artist_columns:
            artist_tree.heading(col, text=col)
        artist_tree.pack(expand=True, fill='both')

        
        cursor.execute("SELECT * FROM Artists")
        artists = cursor.fetchall()
        for artist in artists:
            artist_tree.insert('', tkinter.END, values=artist)

        
        artwork_label = tkinter.Label(display_window, text="Artworks")
        artwork_label.pack()
        artwork_columns = ("ArtworkID", "Title", "ArtistID", "CreationYear", "Medium", "CollectionName", "Category", "Status")
        artwork_tree = ttk.Treeview(display_window, columns=artwork_columns, show='headings')
        
        artwork_tree.column("ArtworkID", width=70, anchor='center')
        artwork_tree.column("Title", width=150, anchor='center')
        artwork_tree.column("ArtistID", width=70, anchor='center')
        artwork_tree.column("CreationYear", width=70, anchor='center')
        artwork_tree.column("Medium", width=100, anchor='center')
        artwork_tree.column("CollectionName", width=120, anchor='center')
        artwork_tree.column("Category", width=80, anchor='center')
        artwork_tree.column("Status", width=80, anchor='center')
        for col in artwork_columns:
            artwork_tree.heading(col, text=col)
        artwork_tree.pack(expand=True, fill='both')

        
        cursor.execute("SELECT * FROM Artworks")
        artworks = cursor.fetchall()
        for artwork in artworks:
            artwork_tree.insert('', tkinter.END, values=artwork)

        
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")

def create_admin_login_window():
    admin_login_win = tkinter.Toplevel(root)
    admin_login_win.title("Admin Login")
    admin_login_win.geometry("300x200")  

    tkinter.Label(admin_login_win, text="Username:").pack()
    username_entry = tkinter.Entry(admin_login_win)
    username_entry.pack()

    tkinter.Label(admin_login_win, text="Password:").pack()
    password_entry = tkinter.Entry(admin_login_win, show="*")
    password_entry.pack()

    tkinter.Button(admin_login_win, text="Login", command=lambda: admin_login(username_entry.get(), password_entry.get())).pack()

def admin_login(username, password):
    conn = None
    try:
        conn = mysql.connector.connect(host="localhost", user=username, password=password, database="ArtCollection")
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_ROLE()")
        role = cursor.fetchone()
        if role and role[0] == 'admin':
            messagebox.showinfo("Login Success", "Admin login successful")
            create_admin_main_window()  # Function to create new window
        else:
            messagebox.showerror("Login Failed", "Invalid admin credentials")
    except mysql.connector.Error as err:
        messagebox.showerror("Login Failed", f"Database error: {err}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def create_admin_main_window():
    admin_main_win = tkinter.Toplevel(root)
    admin_main_win.title("Admin Main Menu")
    admin_main_win.geometry("300x200")  # Adjust size as needed
    # Add any admin functionalities you want here
    tkinter.Label(admin_main_win, text="Admin Panel").pack()

root = tkinter.Tk()
root.title("ART MUSEUM MANAGEMENT SYSTEM")
#root.iconbitmap('path_to_your_icon.ico')

window_width = 500
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.minsize(window_width, window_height)
root.configure(bg='#f0f0f0')

title_label = tkinter.Label(root, text="ART MUSEUM MANAGEMENT SYSTEM", font=("Times new roman", 17, 'bold'), bg='#f0f0f0')
title_label.pack(pady=(50, 20))

frame = tkinter.Frame(root, bg='#f0f0f0')
frame.pack(expand=True, pady=(25,10))

label_user = tkinter.Label(frame, text="Enter the User Name:", bg='#f0f0f0')
label_user.grid(row=0, column=0, sticky='w', padx=10, pady=5)

entry_user = tkinter.Entry(frame)
entry_user.grid(row=0, column=1, padx=10, pady=5)

label_pass = tkinter.Label(frame, text="Enter the Password:", bg='#f0f0f0')
label_pass.grid(row=1, column=0, sticky='w', padx=10, pady=5)

entry_pass = tkinter.Entry(frame, show="*")
entry_pass.grid(row=1, column=1, padx=10, pady=5)

button_connect = tkinter.Button(frame, text="Connect and Execute", command=connect_and_execute, bg='#4a7abc', fg='white')
button_connect.grid(row=2, column=0, columnspan=2, pady=20)

root.bind_all('<Return>', connect_and_execute)
entry_user.focus_set()

root.mainloop()
