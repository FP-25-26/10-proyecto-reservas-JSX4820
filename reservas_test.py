from reservas import *
# - EJERCICIO 1:
def test_lee_reservas(fichero:str) -> None:
    print(f"Estos son las reservas: {lee_reservas(fichero)}")

# - EJERCICIO 2:
def test_total_facturado(reservas:List[Reserva], fecha_inicio: date | None = None, fecha_fin: date | None = None) -> None:
    print(f"Este es el total facturado en el período {fecha_inicio} - {fecha_fin}: {total_facturado(reservas, fecha_inicio, fecha_fin)}")

# - EJERCICIO 3:
def test_reservas_mas_largas(reservas:List[Reserva], n:int = 3) -> None:
    print(f"Estas son las {n} reservas más largas: {reservas_mas_largas(reservas, n)}")

if __name__ == "__main__":
    reservas = lee_reservas("data/reservas.csv")
    #test_lee_reservas("data/reservas.csv")
    #test_total_facturado(reservas)
    test_reservas_mas_largas(reservas)