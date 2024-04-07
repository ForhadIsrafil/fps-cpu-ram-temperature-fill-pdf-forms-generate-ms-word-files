import flet as ft
import psutil
import time
import math
from flet import Text, Column, Row
import flet.canvas as cv
import math


def pg(value):
    pr = ft.ProgressRing(width=150, height=150, stroke_width=10)
    pr.color = "#FF5733"
    pr.bgcolor = "#96DED1"
    pr.value = value
    return pr


def show_disk_data(page: ft.Page):
    page.window_width = 800
    page.window_height = 500
    page.window_resizable = False
    page.update()

    d_disk_data = int(psutil.disk_usage('D:\\').percent)
    c_disk_data = int(psutil.disk_usage('C:\\').percent)

    disk_percent_value = Text('', size=20, width=ft.FontWeight.BOLD, )
    page.add(
        ft.Column(
            controls=[
                Text("Storage", size=50, width=ft.FontWeight.BOLD, text_align='CENTER'),
                Row(controls=[
                    ft.Stack(
                        [
                            pg(c_disk_data * 0.01),
                            ft.Container(
                                content=Text(c_disk_data, size=20, width=ft.FontWeight.BOLD),
                                alignment=ft.alignment.center,

                            ),
                            ft.Container(
                                content=Text("Disk", size=20, width=ft.FontWeight.BOLD),
                                alignment=ft.alignment.bottom_center,
                            ),
                        ],
                        width=150,
                        height=150
                    ),
                ],
                    spacing=30,
                    vertical_alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    alignment=ft.MainAxisAlignment.CENTER

                ),

            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=50,
            alignment=ft.MainAxisAlignment.CENTER,

        )
    )
    # while True:
    #     disk_data = int(psutil.disk_usage('D:\\').percent)
    #     print(psutil.disk_partitions(all=True))
    #     print(psutil.disk_usage('D:\\'))
    #     time.sleep(1)
    #     pr.value = disk_data * 0.01
    #     disk_percent_value.value = disk_data
    #     page.update()
    page.update()


ft.app(target=show_disk_data)
