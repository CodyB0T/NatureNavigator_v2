import tkinter
import os
from tkintermapview import TkinterMapView

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1000}x{700}")
root_tk.title("map_view_simple_example.py")

# path for the database to use
script_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_directory, "data/offline_tiles.db")

# create map widget and only use the tiles from the database, not the online server (use_database_only=True)
map_widget = TkinterMapView(
    root_tk,
    width=1000,
    height=700,
    corner_radius=0,
    use_database_only=True,
    max_zoom=19,
    database_path=database_path,
)
map_widget.pack(fill="both", expand=True)

map_widget.set_position(33.93828806151399, -84.5194541141494)
map_widget.set_zoom(20)

root_tk.mainloop()
