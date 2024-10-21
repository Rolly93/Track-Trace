import os
import datetime
import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox




def missingData(not_found ,data_csv , export_file):
    new_Data = not_found
    with open(data_csv,'a' , newline='',encoding='utf-8') as csvfile:
        fieldnames = new_Data

        writer =csv.DictWriter(csvfile , fieldnames = fieldnames)

        for row in new_Data:
            writer.writerow(row)

def loaddata():
    try:
        # lista vacia para almacenar ref del reporte
        referencias = {}
        
        '''
        # definiendo la fecha actual por sistema
        myday = str(datetime.date.today()).split("-")
        year = myday[0]
        month = myday[1]
        today = myday[2]
         # my excel report '''
        #export_file = f"F:/branch/TRAFFIC/T&V/FTP para Trafico/Done/{year}/{month}/{today}/"
       
        # se abre el reporte para registrar en un diccionario ya que no se repite la referencia.
        data_csv = f"C:\\Users\\nld-rolandor\\Documents\\BACK_UP\\Proyect\\excelfile\\Reporte de Cruces Exportacion.csv"

        '''
        # Check if the directory exists
        if not os.path.exists(export_file):
            messagebox.showerror("Error", f"Directory does not exist: {export_file}")
            return
        '''
        # Get a list of files
        #file_list = os.listdir(export_file)

        not_found = []

        # creating a list as dictionary for the scacs
        trans_path = {
            "TFSQ": "F:/FTP/FEMA_FTP/OUT/",
            "RAYC": "F:/FTP/FTP_Rayo/OUT/",
            "SBCV": "F:/FTP/FTP_SBC/OUT/",
            "LCMZ": "F:/FTP/FTP_JARDEL/OUT/",
            "FMSR": "F:/FTP/FTP JOMIJE/OUT/",
            "CJRA": "F:/FTP/FTP CJRA/OUT/",
            "GALA": "F:/FTP/GALA_FTP/OUT/",
            "MOGF": "F:/FTP/SFTP-MOGA/OUT",
            "TFBB": "F:/FTP/FTP_TSI/OUT/",
            "TJOM": "F:/FTP/FTP JOMIJE/OUT/"
        }


        # Check if the CSV file exists
        #csv_file_path
        if not os.path.exists(data_csv ):
            messagebox.showerror("Error", f"CSV file does not exist: {data_csv}")
            return

        with open(data_csv, newline='' , encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                
                ref = row['\ufeffREFERENCIA'].strip()
                trl = row['numVehiculo'].strip()
                referencias[ref] = trl
     

        # comparacion de busqueda reporte vs documentos reportados en ruta F:/
        for i, f in enumerate(file_list):
            if f[:10] in referencias:
                ttk.Label(mainframe, text=f[:10]).grid(column=1, row=i, sticky=(W, E))
                ttk.Label(mainframe, text=referencias[f[:10]]).grid(column=2, row=i, sticky=(W, E))
            else:
                #ttk.Label(mainframe, text=f[:10]).grid(column=1, row=i, sticky=(W, E))
                #ttk.Label(mainframe, text="referencia pendiente").grid(column=2, row=i, sticky=(W, E))
                not_found.append(f[:10])
        missingData(not_found,data_csv,export_file)

        # imprimiendo lo que no se tiene en reporte
        if not not_found:
            print("No reference missing")
        else:
            print(f"Reference missing: {not_found}")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        root.after(30000,loaddata)

root = Tk()
root.title("Track & Trace Main")
mainframe = ttk.Frame(root, padding="10 20 20 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
referencia = StringVar()

loaddata()
root.mainloop()
