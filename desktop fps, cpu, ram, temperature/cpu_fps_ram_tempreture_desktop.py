import flet as ft
import random
import psutil
import time
import gpustat

## Print GPU usage information (tempreture, fan speed, utilization etc) ** separate GUI
for gpu in gpustat.new_query():
    print(
        f"GPU {gpu.index}: {gpu.name}, Utilization: {gpu.utilization}%, temperature: {gpu.temperature}C, GPU Fan Speed: {gpu.fan_speed}")

# while True:
#     cpu_rate = psutil.cpu_percent(interval=1)
#     ram_rate = psutil.virtual_memory()
#     disk_rate = psutil.disk_usage('/')
#     print('CPU : ', cpu_rate)
#     print('RAM : ', ram_rate)
#     print('Disk : ', disk_rate)
#     time.sleep(1)

# def main(page: ft.Page):
#     pr = ft.ProgressRing(width=100, height=100, stroke_width=20)
#     pr.color = ft.colors.AMBER_800
#
#     page.add(
#         ft.Text("Circular progress indicator", style="headlineSmall"),
#         ft.Row([pr, ft.Text("Wait for the completion...")]),
#         ft.Text("Indeterminate cicrular progress", style="headlineSmall"),
#         ft.Column(
#             [ft.ProgressRing(width=100, height=100, ), ft.Text("I'm going to run for ages...")],
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#         ),
#     )
#
#     while True:
#         pr.value = round(random.randint(90, 100) * 0.01, 2)
#         time.sleep(0.7)
#         print(pr.value)
#         if pr.value == 1.0:
#             pr.color = ft.colors.RED
#             pr.animate_scale = 5
#         else:
#             pr.color = ft.colors.AMBER_800
#         page.update()
# for i in range(0, 101):
#     # pr.value = i * 0.01
#     # time.sleep(2)
#     # pr.value = 50
#     pr.value = random.randint(1, 80) * 0.01
#     time.sleep(0.1)
#     page.update()


# ft.app(target=main)
