import flet as ft

def main(page: ft.Page):
    page.bgcolor = 'blue'
    
    cols = ft.Text('cloudflare deploy',color='white')
    cols2 = ft.Text('For Deploy test',color='white')
    page.add([cols,cols2])
    
ft.app(target=main)
