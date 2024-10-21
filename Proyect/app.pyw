from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Screen :
    def __init__(self , master):
        self.root = master

    @property
    def root(self):
        return self.root
    @root.setter
    def root(self,value):
             self._root = value
 


    def msgBoxError (self,err):
        messagebox.showerror(title="Error",message=f"Error on system what?? {err}")

    def DataGrid(self):
        panedwindow = ttk.PanedWindow(self._root,orient='vertical')
        panedwindow.grid(row=0,column=0, sticky='nsew')

        top_level=ttk.Frame(panedwindow,width=900,relief=SUNKEN)
      

        self.tree = ttk.Treeview( top_level, columns=(
            "REFERENCIA", "Cliente", "TipoVehiculo", "numVehiculo", "ESTATUS/ FOLIO SI O NO", "scac", "todFecha", 
            "todTiempo", "tnfFecha", "tnfTiempo", "dxsFecha", "dxsTiempo", "dlyFecha", "dlyTiempo", "dlyTipo", 
            "afsFecha", "afsTiempo", "dpuFecha", "dpuTiempo", "exrFecha", "exrHora", "exrNotas", "eccFecha", 
            "eccTiempo", "ilrFecha", "ilrTiempo", "ilrtipo", "iltNotas", "clrFecha", "clrTiempo", "st1Fecha", 
            "st1Tiempo", "st1Notas", "tscFecha", "tscTiempo", "tscNotas"), show="headings")

        vsb = ttk.Scrollbar(top_level, orient='vertical', command=self.tree.yview)
        vsb.pack(side=RIGHT,fill=Y)
        self.tree.configure(yscrollcommand=vsb.set)

        hsb = ttk.Scrollbar(top_level, orient='horizontal', command=self.tree.xview)
        hsb.pack(side=BOTTOM,fill=X)

        self.tree.heading("REFERENCIA", text="REFERENCIA")
        self.tree.heading("Cliente", text="Cliente")
        self.tree.heading("TipoVehiculo", text="TipoVehiculo")
        self.tree.heading("numVehiculo", text="numVehiculo")
        self.tree.heading("ESTATUS/ FOLIO SI O NO", text="ESTATUS/ FOLIO SI O NO")
        self.tree.heading("scac", text="scac")
        self.tree.heading("todFecha", text="todFecha")
        self.tree.heading("todTiempo", text="todTiempo")
        self.tree.heading("tnfFecha", text="tnfFecha")
        self.tree.heading("tnfTiempo", text="tnfTiempo")
        self.tree.heading("dxsFecha", text="dxsFecha")
        self.tree.heading("dxsTiempo", text="dxsTiempo")
        self.tree.heading("dlyFecha", text="dlyFecha")
        self.tree.heading("dlyTiempo", text="dlyTiempo")
        self.tree.heading("dlyTipo", text="dlyTipo")
        self.tree.heading("afsFecha", text="afsFecha")
        self.tree.heading("afsTiempo", text="afsTiempo")
        self.tree.heading("dpuFecha", text="dpuFecha")
        self.tree.heading("dpuTiempo", text="dpuTiempo")
        self.tree.heading("exrFecha", text="exrFecha")
        self.tree.heading("exrHora", text="exrHora")
        self.tree.heading("exrNotas", text="exrNotas")
        self.tree.heading("eccFecha", text="eccFecha")
        self.tree.heading("eccTiempo", text="eccTiempo")
        self.tree.heading("ilrFecha", text="ilrFecha")
        self.tree.heading("ilrTiempo", text="ilrTiempo")
        self.tree.heading("ilrtipo", text="ilrtipo")
        self.tree.heading("iltNotas", text="iltNotas")
        self.tree.heading("clrFecha", text="clrFecha")
        self.tree.heading("clrTiempo", text="clrTiempo")
        self.tree.heading("st1Fecha", text="st1Fecha")
        self.tree.heading("st1Tiempo", text="st1Tiempo")
        self.tree.heading("st1Notas", text="st1Notas")
        self.tree.heading("tscFecha", text="tscFecha")
        self.tree.heading("tscTiempo", text="tscTiempo")
        self.tree.heading("tscNotas", text="tscNotas")
        self.tree.pack(fill=BOTH, expand=True)
  
        self.tree.configure(xscrollcommand=hsb.set)
        panedwindow.add(top_level ,weight=3)
        self._root.grid_rowconfigure(0, weight=1)
        self._root.grid_columnconfigure(0, weight=1)
        print_data

    def print_data(self):
        new_window = Toplevel(self._root)
        new_window.title("Print Data")
        text = Text(new_window)
        text.pack(fill=BOTH, expand=True)

        for child in self.tree.get_children():
            item = self.tree.item(child)
            values = item['values']
            text.insert(END, f"{values}\n")


    def captureScreen(self):
        self._root.withdraw()
        capture = Toplevel(self._root)      
        capture.title("Captura de Eventos")

        def on_close():
            capture.destroy()
            self._root.deiconify()  # Show the main window again
        
        capture.protocol("WM_DELETE_WINDOW", on_close)

def main():

    root = Tk()
    window_width = 800
    window_height = 600

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position to center the window
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)

    # Set the geometry of the window
    root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    app = Screen(root)
    root.title("Track & Trace Main")
    app.DataGrid()
    #add_event_bottun = ttk.Button(root,text="Add Events", command=app.captureScreen).grid(row=1, column=0)
    root.mainloop()

if __name__ == "__main__" :
    main()

