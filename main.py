import flet as ft

def main(page: ft.Page):
    page.bgcolor = 'blue'
    
    cols = ft.Text('cloudflare deploy',color='white')
    page.add(cols)
    
ft.app(target=main)