import time
from art import *
from rich import print, spinner
from rich.console import Console
from rich.progress import track, Progress
import random

console = Console()
console.print("Wathcdog", style="bold red")

Art = text2art("Wathcdog")
print(Art)


while True:

    with console.status(status="[bold green]Watching folders...", spinner="arrow2") as status:
        time.sleep(10)
    # with console.status(status="[bold green]Please wait - solving global problems...", spinner="weather"):
    #     time.sleep(10)


