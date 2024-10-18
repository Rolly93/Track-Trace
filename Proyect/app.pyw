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
    
    def captureScreen(self,):
        self._root.withdraw()
        capture = Toplevel(self._root)      
        capture.title("Captura de Eventos")

        def on_close():
            capture.destroy()
            self._root.deiconify()  # Show the main window again
        
        capture.protocol("WM_DELETE_WINDOW", on_close)

def main():
    root = Tk()
    app = Screen(root)
    root.title("Track & Trace Main")
    add_event_bottun = ttk.Button(root,text="Add Events", command=app.captureScreen).grid(row=1,column=0)
    root.mainloop()

if __name__ == "__main__" :
    main()
