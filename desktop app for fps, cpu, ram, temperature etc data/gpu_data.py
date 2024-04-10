import flet as ft
import time
import gpustat
from flet import Text, Column, Row


def pg(value):
    pr = ft.ProgressRing(width=150, height=150, stroke_width=10)
    pr.color = "#FF5733"
    pr.bgcolor = "#96DED1"
    pr.value = value * 0.01
    return pr


def show_gpu_data(page: ft.Page):
    # page.window_width = 800
    # page.window_height = 500
    # page.window_resizable = False
    # page.update()

    # progress value
    utilization_pg = pg(0)
    temperature_pg = pg(0)

    # text value
    utilization_percent_value = Text('', size=50, width=ft.FontWeight.BOLD, )
    temperature_percent_value = Text('', size=50, width=ft.FontWeight.BOLD, )
    fan_speed_value = Text('', size=20, width=ft.FontWeight.BOLD, )

    fan_obj = ft.Container(
        width=150,
        height=150,
        content=ft.Image(src=f"/images/fan.png", fit=ft.ImageFit.CONTAIN, color="#77B0AA"),
        rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(0, ft.AnimationCurve.LINEAR)
    )

    page.add(
        ft.Column(
            controls=[
                Text("GPU", size=50, width=ft.FontWeight.BOLD, text_align='CENTER'),
                Row(controls=[
                    Column(
                        controls=[
                            ft.Stack(
                                [
                                    utilization_pg,
                                    ft.Container(
                                        content=utilization_percent_value,
                                        alignment=ft.alignment.center,
                                    ),
                                ],
                                width=150,
                                height=150
                            ),
                            Text("Utilization", size=20, width=ft.FontWeight.BOLD),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    Column(
                        controls=[
                            ft.Stack(
                                [
                                    temperature_pg,
                                    ft.Container(
                                        content=temperature_percent_value,
                                        alignment=ft.alignment.center,
                                    ),
                                ],
                                width=150,
                                height=150
                            ),
                            Text("Temperature", size=20, width=ft.FontWeight.BOLD),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    Column(
                        controls=[
                            fan_obj,
                            ft.Container(
                                content=fan_speed_value,
                                alignment=ft.alignment.center,
                            ),

                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )

                ],
                    spacing=30,
                    # vertical_alignment=ft.CrossAxisAlignment.SPACE_EVENLY,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=50,
            alignment=ft.MainAxisAlignment.CENTER,

        )
    )
    while True:
        ## Print GPU usage information (tempreture, fan speed, utilization etc) ** separate GUI
        for gpu in gpustat.new_query():
            # utilization
            utilization = gpu.utilization
            utilization_pg.value = utilization * 0.01
            utilization_percent_value.value = utilization

            # temperature
            temperature = gpu.temperature
            temperature_pg.value = temperature * 0.01
            temperature_percent_value.value = temperature

            fan_speed = gpu.fan_speed
            fan_speed_value.value = "Fan Speed: " + str(fan_speed)

            # print(
            #     f"GPU {gpu.index}: {gpu.name}, Utilization: {gpu.utilization}%, temperature: {gpu.temperature}C, GPU Fan Speed: {gpu.fan_speed}")

            fan_obj.rotate.angle += 1 if temperature <= 40 else 2
            fan_obj.animate_rotation.duration = 300

            page.update()


# ft.app(target=show_gpu_data)
