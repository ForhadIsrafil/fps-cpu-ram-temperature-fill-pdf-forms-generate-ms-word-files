import flet as ft
import time
import gpustat
from flet import Text, Column, Row
import psutil


def home(page: ft.Page):
    page.window_width = 800
    page.window_height = 500
    page.window_resizable = False
    page.update()


    