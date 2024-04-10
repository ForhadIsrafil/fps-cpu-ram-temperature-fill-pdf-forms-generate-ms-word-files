import flet as ft
import psutil
import time
from flet import Text, Column, Row
import flet.canvas as cv



def pg(value):
    pr = ft.ProgressRing(width=150, height=150, stroke_width=10)
    pr.color = "#FF5733"
    pr.bgcolor = "#96DED1"
    pr.value = value
    return pr

def show_disk_data(page: ft.Page):
    # page.window_width = 800
    # page.window_height = 500
    # page.window_resizable = False
    # page.update()

    c_disk_data = int(psutil.disk_usage('C:\\').percent)
    d_disk_data = int(psutil.disk_usage('D:\\').percent)
    e_disk_data = int(psutil.disk_usage('E:\\').percent)
    f_disk_data = int(psutil.disk_usage('F:\\').percent)

    # disk_percent_value = Text('', size=20, width=ft.FontWeight.BOLD, )
    page.add(
        ft.Column(
            controls=[
                Text("Storage", size=50, width=ft.FontWeight.BOLD, text_align='CENTER'),
                Row(controls=[
                    Column(
                        controls=[
                            ft.Stack(
                                [
                                    pg(c_disk_data * 0.01),
                                    ft.Container(
                                        content=Text(c_disk_data, size=20, width=ft.FontWeight.BOLD),
                                        alignment=ft.alignment.center,

                                    ),
                                ],
                                width=150,
                                height=150
                            ),
                            Text("Drive: C", size=20, width=ft.FontWeight.BOLD),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    Column(
                        controls=[
                            ft.Stack(
                                [
                                    pg(d_disk_data * 0.01),
                                    ft.Container(
                                        content=Text(d_disk_data, size=20, width=ft.FontWeight.BOLD),
                                        alignment=ft.alignment.center,

                                    ),
                                ],
                                width=150,
                                height=150
                            ),
                            Text("Drive: D", size=20, width=ft.FontWeight.BOLD),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    Column(
                        controls=[
                            ft.Stack(
                                [
                                    pg(e_disk_data * 0.01),
                                    ft.Container(
                                        content=Text(e_disk_data, size=20, width=ft.FontWeight.BOLD),
                                        alignment=ft.alignment.center,

                                    ),
                                ],
                                width=150,
                                height=150
                            ),
                            Text("Drive: E", size=20, width=ft.FontWeight.BOLD),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    Column(
                        controls=[
                            ft.Stack(
                                [
                                    pg(f_disk_data * 0.01),
                                    ft.Container(
                                        content=Text(f_disk_data, size=20, width=ft.FontWeight.BOLD),
                                        alignment=ft.alignment.center,

                                    ),
                                ],
                                width=150,
                                height=150
                            ),
                            Text("Drive: F", size=20, width=ft.FontWeight.BOLD),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),

                ],
                    spacing=30,
                    # vertical_alignment=ft.CrossAxisAlignment.SPACE_EVENLY,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        ft.CircleAvatar(bgcolor="#96DED1", radius=5),
                        Text('Free Space', size=10, width=ft.FontWeight.BOLD, color="#96DED1"),

                        ft.CircleAvatar(bgcolor="#FF5733", radius=5),
                        Text('Usage', size=10, width=ft.FontWeight.BOLD, color="#FF5733"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                ),

            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=50,
            alignment=ft.MainAxisAlignment.CENTER,

        )
    )
    page.update()


# ft.app(target=show_disk_data)
