from reservas import *
# - EJERCICIO 1:
def test_lee_reservas(fichero:str) -> None:
    print(f"Estos son las reservas: {lee_reservas(fichero)}")

if __name__ == "__main__":
    test_lee_reservas("data/reservas.csv")