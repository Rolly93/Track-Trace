import os
import csv
from backend import References


def myrequest():
    data_csv = "C:\\Users\\nld-rolandor\\Documents\\BACK_UP\\Proyect\\excelfile\\Reporte de Cruces Exportacion.csv"
    with open(data_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for track in reader:
                   
            referencia = References(
             track["\ufeffREFERENCIA"],            
             track['Cliente'],
             track['TipoVehiculo'],
             track['numVehiculo'],
             track['cruce 1ra o 2da vuelta'],
             track['scac'],
             track['todFecha'],
             track['todTiempo'],
             track['tnfFecha'],
             track['tnfTiempo'],
             track['dxsFecha'],
             track['dxsTiempo'],
             track['dlyFecha'],
             track['dlyTiempo'],
             track['dlyTipo'],
             track['afsFecha'],
             track['afsTiempo'],
             track['dpuFecha'],
             track['dpuTiempo'],
             track['exrFecha'],
             track['exrTiempo'],
             track['exrNotas'],
             track['eccFecha'],
             track['eccTiempo'],
             track['ilrFecha'],
             track['ilrTiempo'],
             track['ilrtipo'],
             track['iltNotas'],
             track['clrFecha'],
             track['clrTiempo'],
             track['st1Fecha'],
             track['st1Tiempo'],
             track['st1Notas'],
             track['tscFecha'],
             track['tscTiempo'],
             track['tscNotas'])
            References.print_info(referencia)
        
        
           
