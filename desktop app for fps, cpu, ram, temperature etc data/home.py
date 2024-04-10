import flet as ft
import time
import gpustat
from flet import Text, Column, Row, Container, View, AppBar
from flet import RouteChangeEvent, ViewPopEvent, MainAxisAlignment, CrossAxisAlignment
import psutil
import cpu_data, hard_disk_data, ram_data, gpu_data

container = Container()


def handle_click(e):
    # if container.current.content != None:
    #     container.current.content.clean()
    #     page.update()
    for obj in e.page.controls[0].controls:
        obj.style.bgcolor = None
    e.control.style.bgcolor = '#FF87AB'

    if e.control.data == 'cpu':
        e.page.controls.pop(-1)

        container.content = cpu_data.show_cpu_data(e.control.page)

    elif e.control.data == 'hard_disk':
        e.page.controls.pop(-1)
        container.content = hard_disk_data.show_disk_data(e.control.page)

    elif e.control.data == 'ram':
        e.page.controls.pop(-1)
        container.content = ram_data.show_ram_data(e.control.page)

    elif e.control.data == 'gpu':
        e.page.controls.pop(-1)
        container.content = gpu_data.show_gpu_data(e.control.page)


def home(page: ft.Page):
    page.window_width = 800
    page.window_height = 590
    page.window_resizable = False
    page.update()


    cpu_button = ft.TextButton(
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2), bgcolor="#56666B"),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="images/cpu-tower.png", height=70, width=70),
                    ft.Text(value="CPU", size=15, color="#e2eff1"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
        on_click=handle_click,
        data='cpu',
        autofocus=True
    )

    hard_disk_button = ft.TextButton(
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2), bgcolor="#56666B"),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="images/storage.png", height=70, width=70),
                    ft.Text(value="Hard Disk", size=15, color="#e2eff1"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
        on_click=handle_click,
        data='hard_disk'
    )

    ram_button = ft.TextButton(
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2), bgcolor="#56666B"),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="images/ram.png", height=70, width=70),
                    ft.Text(value="RAM", size=15, color="#e2eff1"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
        on_click=handle_click,
        data='ram'
    )
    gpu_button = ft.TextButton(
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=2), bgcolor="#56666B"),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="images/graphic-card.png", height=70, width=70),
                    ft.Text(value="GPU", size=15, color="#e2eff1"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
        on_click=handle_click,
        data='gpu'
    )

    page.add(
        Row(
            controls=[
                cpu_button,
                hard_disk_button,
                ram_button,
                gpu_button,

            ],
            # spacing=5,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Divider(),
        container,
    )



ft.app(target=home)
