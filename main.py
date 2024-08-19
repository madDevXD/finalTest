import flet as ft

def main(page: ft.Page):
    page.title = 'Hello, Flet!'
    page.add(ft.Text('Hello, World!'))

ft.app(target=main)
