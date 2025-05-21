"""
This program helps you to convert between celsius and f and kelvin
"""
from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep

console = Console()

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def show_results(temp_c):
    table = Table(title="Temperature Conversion Results", style="bold green")

    table.add_column("From", style="cyan", no_wrap=True)
    table.add_column("To Fahrenheit", justify="right")
    table.add_column("To Kelvin", justify="right")

    temp_f = celsius_to_fahrenheit(temp_c)
    temp_k = celsius_to_kelvin(temp_c)
    table.add_row(f"{temp_c}°C", f"{temp_f:.2f}°F", f"{temp_k:.2f} K")

    console.print(table)

    reverse_table = Table(title="Reverse Conversions", style="bold magenta")
    reverse_table.add_column("From", style="cyan", no_wrap=True)
    reverse_table.add_column("To Celsius", justify="right")

    reverse_table.add_row(f"{temp_f:.2f}°F", f"{fahrenheit_to_celsius(temp_f):.2f}°C")
    reverse_table.add_row(f"{temp_k:.2f} K", f"{kelvin_to_celsius(temp_k):.2f}°C")

    console.print(reverse_table)

def main():
    console.rule("[bold blue]Temperature Converter")
    temp_list = [0, 25, 100]

    for temp_c in track(temp_list, description="Converting temperatures..."):
        sleep(0.5)
        show_results(temp_c)

    console.rule("[bold green]All conversions done!")

if __name__ == "__main__":
    main()
