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
            reservas.append((nombre, dni, fecha_entrada, fecha_salida, tipo_habitacion, num_personas, precio_noche, servicios_adicionales))
    return reservas

# - EJERCICIO 2:
def total_facturado(reservas:List[Reserva], fecha_inicio: date | None = None, fecha_fin: date | None = None) -> float:
    for reserva in reservas:
        