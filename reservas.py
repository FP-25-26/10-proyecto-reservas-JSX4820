from typing import NamedTuple, List, Tuple
from datetime import datetime, date
from funciones_auxiliares import *
import csv
Reserva = NamedTuple("Reserva", [("nombre", str), ("dni", str), ("fecha_entrada", date), ("fecha_salida", date), ("tipo_habitacion", str), ("num_personas", int), ("precio_noche", float), ("servicios_adicionales", List[str])])

# - EJERCICIO 1:
def lee_reservas(fichero:str) -> List[Reserva]:
    reservas = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, dni, fecha_entrada, fecha_salida, tipo_habitacion, num_personas, precio_noche, servicios_adicionales in lector:
            nombre = nombre.strip()
            dni = dni.strip()
            fecha_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%d").date()
            fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d").date()
            tipo_habitacion = tipo_habitacion.strip()
            num_personas = int(num_personas)
            precio_noche = float(precio_noche)
            servicios_adicionales = servicios_adicionales.split(',')
            reservas.append(Reserva(nombre, dni, fecha_entrada, fecha_salida, tipo_habitacion, num_personas, precio_noche, servicios_adicionales))
    return reservas

# - EJERCICIO 2:
# Para calcular el total facturado hay que ver el número de días de la estancia
def total_facturado(reservas:List[Reserva], fecha_inicio: date | None = None, fecha_fin: date | None = None) -> float:
    facturado = sum(reserva.precio_noche*(reserva.fecha_salida - reserva.fecha_entrada).days 
                    for reserva in reservas if(fecha_inicio == None or reserva.fecha_entrada >= fecha_inicio) 
                    and (fecha_fin == None or reserva.fecha_entrada <= fecha_fin))
    return facturado

# - EJERCICIO 3:
def reservas_mas_largas(reservas:List[Reserva], n:int = 3) -> List[Tuple[str, date]]:
    list_aux = [(reserva.nombre, reserva.fecha_entrada, (reserva.fecha_salida - reserva.fecha_entrada).days) for reserva in reservas]
    list_aux.sort(reverse=True, key=lambda l:l[2])
    return list_aux[:n]