import flet as ft
import psutil
import time
import math

from flet import Text, Column, Row


def show_cpu_data(page: ft.Page):

    page.window_width = 800
    page.window_height = 500
    page.window_resizable = False
    page.update()

    pr = ft.ProgressRing(width=200, height=200, stroke_width=20)
    pr.color = "#FF5733"
    pr.bgcolor = "#96DED1"

    cpu_percent_value = Text('', size=50, width=ft.FontWeight.BOLD, )
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    Text("CPU", size=50, width=ft.FontWeight.BOLD, text_align='CENTER'),
                    ft.Stack(
                        [
                            pr,
                            ft.Container(
                                content=cpu_percent_value,
                                alignment=ft.alignment.center
                            )
                        ],
                        width=200,
                        height=200
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=50,
                # alignment=ft.MainAxisAlignment.CENTER,

            ),
            alignment=ft.alignment.center,
            margin=10
        )
    )
    while True:
        cpu_data = int(psutil.cpu_percent())
        print(cpu_data)
        time.sleep(1)
        pr.value = cpu_data * 0.01
        cpu_percent_value.value = cpu_data
        page.update()


ft.app(target=show_cpu_data)
