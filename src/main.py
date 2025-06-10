import numpy as np
from generator import generate_equations
from eliminacja_gaussa import eliminacja_gaussa
from utils import save
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import time

console = Console()


def pokaz_wynik_rich(rownania, rozwiazanie):
    console.print(
        Panel("[bold cyan]🔢 Wygenerowany układ równań:[/bold cyan]", box=box.ROUNDED)
    )
    for row in rownania:
        console.print(f"[white]{row}[/white]")

    time.sleep(2)
    console.print("\n[bold yellow]🧠 Rozwiązuję układ...[/bold yellow]\n")
    time.sleep(2)

    table = Table(
        title="📊 [bold green]Rozwiązanie układu[/bold green]", box=box.SIMPLE_HEAVY
    )
    table.add_column("Zmienna", justify="center", style="cyan", no_wrap=True)
    table.add_column("Wartość", justify="center", style="bold white")

    for i, val in enumerate(rozwiazanie):
        table.add_row(f"x{i+1}", f"{val:.4f}")

    console.print(table)


def main():
    try:
        liczba_rownan = int(input("Podaj liczbę równań: "))
        if liczba_rownan <= 0:
            raise ValueError("Liczba równań musi być dodatnią liczbą całkowitą.")

        rownania, A, b = generate_equations(liczba_rownan)
        rozwiazanie = eliminacja_gaussa(A, b)

        wynik = [f"x{i+1} = {rozwiazanie[i]:.4f}" for i in range(len(rozwiazanie))]
        wszystko = rownania + [""] + wynik

        plik_wyjsciowy = "rownania.txt"
        save(wszystko, plik_wyjsciowy)

        pokaz_wynik_rich(rownania, rozwiazanie)

    except ValueError as e:
        print(f"Nieprawidłowe dane wejściowe: {e}")


if __name__ == "__main__":
    main()
