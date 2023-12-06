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

    btn_admin = tkinter.Button(button_frame, text="ADMIN", **button_style)
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
        for artist in artists:
            artist_info = f"ID: {artist[0]}, Name: {artist[1]}, Birth Year: {artist[2]}, Nationality: {artist[3]}"
            label = tkinter.Label(display_window, text=artist_info)
            label.pack()
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
        for artwork in artworks:
            artwork_info = f"ID: {artwork[0]}, Title: {artwork[1]}, Artist ID: {artwork[2]}, Year: {artwork[3]}, Medium: {artwork[4]}, Collection: {artwork[5]}, Category: {artwork[6]}, Status: {artwork[7]}"
            label = tkinter.Label(display_window, text=artwork_info)
            label.pack()
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
        for artwork in borrowed_artworks:
            artwork_info = f"ID: {artwork[0]}, Title: {artwork[1]}, Artist ID: {artwork[2]}, Year: {artwork[3]}, Medium: {artwork[4]}, Collection: {artwork[5]}, Category: {artwork[6]}, Status: {artwork[7]}"
            label = tkinter.Label(display_window, text=artwork_info)
            label.pack()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")


def view_all(parent_window):
    try:
        # Connect to the database
        conn = mysql.connector.connect(host="localhost", user=entry_user.get(), password=entry_pass.get(), database="ArtCollection")
        cursor = conn.cursor()

        # Create a new pop-up window as a child of the parent window
        display_window = tkinter.Toplevel(parent_window)
        display_window.title("All Museum Data")
        display_window.state('zoomed')
        # display_window.geometry("1050x800")  # Adjust size as needed

        # Treeview for Artists
        artist_label = tkinter.Label(display_window, text="Artists")
        artist_label.pack()
        artist_columns = ("ArtistID", "Name", "BirthYear", "Nationality")
        artist_tree = ttk.Treeview(display_window, columns=artist_columns, show='headings')
        # Set column headings and widths
        artist_tree.column("ArtistID", width=70, anchor='center')
        artist_tree.column("Name", width=150, anchor='center')
        artist_tree.column("BirthYear", width=70, anchor='center')
        artist_tree.column("Nationality", width=100, anchor='center')
        for col in artist_columns:
            artist_tree.heading(col, text=col)
        artist_tree.pack(expand=True, fill='both')

        # Fetch and display Artists data
        cursor.execute("SELECT * FROM Artists")
        artists = cursor.fetchall()
        for artist in artists:
            artist_tree.insert('', tkinter.END, values=artist)

        # Treeview for Artworks
        artwork_label = tkinter.Label(display_window, text="Artworks")
        artwork_label.pack()
        artwork_columns = ("ArtworkID", "Title", "ArtistID", "CreationYear", "Medium", "CollectionName", "Category", "Status")
        artwork_tree = ttk.Treeview(display_window, columns=artwork_columns, show='headings')
        # Set column headings and widths
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

        # Fetch and display Artworks data
        cursor.execute("SELECT * FROM Artworks")
        artworks = cursor.fetchall()
        for artwork in artworks:
            artwork_tree.insert('', tkinter.END, values=artwork)

        # Close cursor and connection
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")

def close_all_windows():
    root.destroy()

root = tkinter.Tk()
root.title("ART MUSEUM MANAGEMENT SYSTEM")
#root.iconbitmap('path_to_your_icon.ico')
root.protocol("WM_DELETE_WINDOW", close_all_windows)

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
