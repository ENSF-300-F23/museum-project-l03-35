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

    btn_admin = tkinter.Button(button_frame, text="ADMIN", command=admin_interface, **button_style)
    btn_admin.pack(pady=10)
    btn_admin.bind("<Enter>", lambda e, btn=btn_admin: on_enter(e, btn))
    btn_admin.bind("<Leave>", lambda e, btn=btn_admin: on_leave(e, btn))

    btn_data_entry = tkinter.Button(button_frame, text="DATA ENTRY", command=data_entry_interface, **button_style)
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

def admin_interface():
    admin_window = tkinter.Toplevel(root)
    admin_window.title("ADMIN INTERFACE")
    window_width, window_height = 800, 600  
    center_x, center_y = calculate_center(admin_window, window_width, window_height)
    admin_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    admin_window.configure(bg='#f0f0f0')
    label_font = ('Arial', 12)
    entry_font = ('Arial', 10)

    frame_sql_command = tkinter.Frame(admin_window, bg='#f0f0f0')
    frame_sql_command.pack(pady=20, padx=20, fill='both', expand=True)

    label_sql_command = tkinter.Label(frame_sql_command, text="ENTER THE SQL COMMAND:", font=label_font, bg='#f0f0f0')
    label_sql_command.pack(pady=(0, 5))
    text_sql_command = tkinter.Text(frame_sql_command, height=10, width=70, font=entry_font)
    text_sql_command.pack(expand=True, fill='both')
    btn_execute_command = tkinter.Button(frame_sql_command, text="EXECUTE ", command=lambda: execute_sql_command(text_sql_command.get("1.0", tkinter.END)), **button_style)
    btn_execute_command.pack(pady=10)
    btn_execute_command.bind("<Enter>", lambda e, btn=btn_execute_command: on_enter(e, btn))
    btn_execute_command.bind("<Leave>", lambda e, btn=btn_execute_command: on_leave(e, btn))

    frame_sql_file = tkinter.Frame(admin_window, bg='#f0f0f0')
    frame_sql_file.pack(pady=20, padx=20, fill='x')

    label_sql_file = tkinter.Label(frame_sql_file, text="SQL SCRIPT FILE PATH:", font=label_font, bg='#f0f0f0')
    label_sql_file.pack(pady=(0, 5), side=tkinter.LEFT)
    entry_sql_file = tkinter.Entry(frame_sql_file, width=50, font=entry_font)
    entry_sql_file.pack(pady=(0, 5), side=tkinter.LEFT, expand=True, fill='x')
    btn_run_script = tkinter.Button(frame_sql_file, text="RUN SCRIPT", command=lambda: run_sql_script(entry_sql_file.get()), **button_style)
    btn_run_script.pack(pady=(0, 5), side=tkinter.LEFT)
    btn_run_script.bind("<Enter>", lambda e, btn=btn_run_script: on_enter(e, btn))
    btn_run_script.bind("<Leave>", lambda e, btn=btn_run_script: on_leave(e, btn))


def execute_sql_command(command):
    try:
        conn = mysql.connector.connect(host="localhost", user=entry_user.get(), password=entry_pass.get(), database="ArtCollection")
        cursor = conn.cursor()
        cursor.execute(command)

        output = ""
        column_headers = [i[0] for i in cursor.description]
        output += ", ".join(column_headers) + "\n"

        if cursor.with_rows:
            results = cursor.fetchall()
            for row in results:
                output += ", ".join(map(str, row)) + "\n"

        conn.commit()

        if output:
            messagebox.showinfo("Result", output)
        else:
            messagebox.showinfo("Success", "SQL Command Executed Successfully")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()
        if conn.is_connected():
            conn.close()

def run_sql_script(file_path):
    try:
        conn = mysql.connector.connect(host="localhost", user=entry_user.get(), password=entry_pass.get(), database="ArtCollection")
        cursor = conn.cursor()

        with open(file_path, 'r') as file:
            sql_script = file.read()

        output = ""
        for result in cursor.execute(sql_script, multi=True):
            if result.with_rows:
                column_headers = [i[0] for i in result.description]
                output += ", ".join(column_headers) + "\n"

                results = result.fetchall()
                for row in results:
                    output += ", ".join(map(str, row)) + "\n"
                output += "\n"  

        conn.commit()

        if output:
            messagebox.showinfo("Result", output)
        else:
            messagebox.showinfo("Success", "SQL Script Executed Successfully")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found. Please check the file path.")
    finally:
        cursor.close()
        if conn.is_connected():
            conn.close()

def data_entry_interface():
    data_entry_window = tkinter.Toplevel(root)
    data_entry_window.title("DATA ENTRY INTERFACE")
    window_width, window_height = 500, 300  
    center_x, center_y = calculate_center(data_entry_window, window_width, window_height)
    data_entry_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    data_entry_window.configure(bg='#f0f0f0')

    frame_buttons = tkinter.Frame(data_entry_window, bg='#f0f0f0')
    frame_buttons.pack(expand=True)

    btn_artists = tkinter.Button(frame_buttons, text="ARTISTS", command=lambda: artists_data_entry(data_entry_window), **button_style)
    btn_artists.grid(row=0, column=0, padx=10, pady=10)
    btn_artists.bind("<Enter>", lambda e, btn=btn_artists: on_enter(e, btn))
    btn_artists.bind("<Leave>", lambda e, btn=btn_artists: on_leave(e, btn))

    btn_artworks = tkinter.Button(frame_buttons, text="ARTWORKS", command=lambda: artworks_data_entry(data_entry_window), **button_style)
    btn_artworks.grid(row=0, column=1, padx=10, pady=10)
    btn_artworks.bind("<Enter>", lambda e, btn=btn_artworks: on_enter(e, btn))
    btn_artworks.bind("<Leave>", lambda e, btn=btn_artworks: on_leave(e, btn))

    frame_buttons.grid_rowconfigure(0, weight=1)
    frame_buttons.grid_columnconfigure(0, weight=1)
    frame_buttons.grid_columnconfigure(1, weight=1)

def artists_data_entry(parent_window):
    # Create a new window for artist data entry
    artist_entry_window = tkinter.Toplevel(parent_window)
    artist_entry_window.title("Artist Data Entry")
    artist_entry_window.geometry("800x600")

    # Create main frames for layout
    top_frame = tkinter.Frame(artist_entry_window)
    top_frame.pack(side="top", fill="x")

    middle_frame = tkinter.Frame(artist_entry_window)
    middle_frame.pack(fill="x")

    bottom_frame = tkinter.Frame(artist_entry_window)
    bottom_frame.pack(side="bottom", fill="x")

    # Add widgets to the top frame
    tkinter.Label(top_frame, text="Artist Information", font=("Arial", 16)).pack(side="left")
    # ... Add more widgets as needed

    # Add entry widgets and labels to the middle frame
    # For example: Artist ID, Name, Birth Year, Nationality
    tkinter.Label(middle_frame, text="Artist ID").grid(row=0, column=0, padx=5, pady=5)
    artist_id_entry = tkinter.Entry(middle_frame)
    artist_id_entry.grid(row=0, column=1, padx=5, pady=5)

    tkinter.Label(middle_frame, text="Name").grid(row=1, column=0, padx=5, pady=5)
    name_entry = tkinter.Entry(middle_frame)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    tkinter.Label(middle_frame, text="Birth Year").grid(row=2, column=0, padx=5, pady=5)
    birth_year_entry = tkinter.Entry(middle_frame)
    birth_year_entry.grid(row=2, column=1, padx=5, pady=5)

    tkinter.Label(middle_frame, text="Nationality").grid(row=3, column=0, padx=5, pady=5)
    nationality_entry = tkinter.Entry(middle_frame)
    nationality_entry.grid(row=3, column=1, padx=5, pady=5)

    # Add buttons to the bottom frame
    add_button = tkinter.Button(bottom_frame, text="Add", **button_style)
    add_button.pack(side="left", padx=10)
    add_button.bind("<Enter>", lambda e, btn=add_button: on_enter(e, btn))
    add_button.bind("<Leave>", lambda e, btn=add_button: on_leave(e, btn))

    update_button = tkinter.Button(bottom_frame, text="Update", **button_style)
    update_button.pack(side="left", padx=10)
    update_button.bind("<Enter>", lambda e, btn=update_button: on_enter(e, btn))
    update_button.bind("<Leave>", lambda e, btn=update_button: on_leave(e, btn))

    delete_button = tkinter.Button(bottom_frame, text="Delete", **button_style)
    delete_button.pack(side="left", padx=10)
    delete_button.bind("<Enter>", lambda e, btn=delete_button: on_enter(e, btn))
    delete_button.bind("<Leave>", lambda e, btn=delete_button: on_leave(e, btn))

    reset_button = tkinter.Button(bottom_frame, text="Reset", **button_style)
    reset_button.pack(side="left", padx=10)
    reset_button.bind("<Enter>", lambda e, btn=reset_button: on_enter(e, btn))
    reset_button.bind("<Leave>", lambda e, btn=reset_button: on_leave(e, btn))

    exit_button = tkinter.Button(bottom_frame, text="Exit", **button_style, command=artist_entry_window.destroy)
    exit_button.pack(side="left", padx=10)
    exit_button.bind("<Enter>", lambda e, btn=exit_button: on_enter(e, btn))
    exit_button.bind("<Leave>", lambda e, btn=exit_button: on_leave(e, btn))


    artist_tree = ttk.Treeview(middle_frame, columns=("ArtistID", "Name", "BirthYear", "Nationality"), show='headings', height=8)
    artist_tree.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

    artist_tree.heading("ArtistID", text="Artist ID",anchor='center')
    artist_tree.heading("Name", text="Name",anchor='center')
    artist_tree.heading("BirthYear", text="Birth Year",anchor='center')
    artist_tree.heading("Nationality", text="Nationality",anchor='center')

    artist_tree.column("ArtistID", anchor="center")
    artist_tree.column("Name", anchor="center")
    artist_tree.column("BirthYear", anchor="center")
    artist_tree.column("Nationality", anchor="center")

    fetch_artists_data(artist_tree)

def fetch_artists_data(tree):
    try:
        conn = mysql.connector.connect(host="localhost", user=entry_user.get(), password=entry_pass.get(), database="ArtCollection")
        cursor = conn.cursor()
        cursor.execute("SELECT ArtistID, Name, BirthYear, Nationality FROM Artists")
        rows = cursor.fetchall()

        for i in tree.get_children():
            tree.delete(i)
        for row in rows:
            tree.insert('', 'end', values=row)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()

def add_artist(artist_id_entry, name_entry, birth_year_entry, nationality_entry):
    artist_id = artist_id_entry.get()
    name = name_entry.get()
    birth_year = birth_year_entry.get()
    nationality = nationality_entry.get()


    try:
        conn = mysql.connector.connect(host="localhost", user=entry_user.get(), password=entry_pass.get(), database="ArtCollection")
        cursor = conn.cursor()
        
        # Create the insert SQL command
        sql = "INSERT INTO Artists (ArtistID, Name, BirthYear, Nationality) VALUES (%s, %s, %s, %s)"
        values = (artist_id, name, birth_year, nationality)
        
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Artist added successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()

def update_artist(artist_id_entry, name_entry, birth_year_entry, nationality_entry):
    # Get the artist data from the entry fields
    artist_id = artist_id_entry.get()
    name = name_entry.get()
    birth_year = birth_year_entry.get()
    nationality = nationality_entry.get()

    # Connect to the database and update the artist details
    try:
        conn = mysql.connector.connect(host="localhost", user=entry_user.get(), password=entry_pass.get(), database="ArtCollection")
        cursor = conn.cursor()

        # Create the update SQL command
        sql = "UPDATE Artists SET Name=%s, BirthYear=%s, Nationality=%s WHERE ArtistID=%s"
        values = (name, birth_year, nationality, artist_id)
        
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Artist updated successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()

def delete_artist(artist_id_entry):
    # Get the artist ID from the entry field
    artist_id = artist_id_entry.get()

    # Connect to the database and delete the artist
    try:
        conn = mysql.connector.connect(host="localhost", user=entry_user.get(), password=entry_pass.get(), database="ArtCollection")
        cursor = conn.cursor()

        # Create the delete SQL command
        sql = "DELETE FROM Artists WHERE ArtistID=%s"
        values = (artist_id,)
        
        cursor.execute(sql, values)
        conn.commit()
        messagebox.showinfo("Success", "Artist deleted successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()


def reset_entries(*entries):
    for entry in entries:
        entry.delete(0, 'end')
    

def artworks_data_entry():
    pass


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
