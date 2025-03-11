import flet as ft
    # print(page.client_ip)
    # print(page.platform)
    # print(page.window.width)
    # print(ft.PagePlatform.MACOS==page.platform)
    
import logging
logging.basicConfig(level=logging.DEBUG)

def main(page: ft.Page):

    title = ft.Text(value='PRAY & CRY',size=60,color='#000000',style=ft.TextStyle(font_family='zaramain',weight=ft.FontWeight.W_100,letter_spacing=0),text_align=ft.TextAlign.CENTER)
    prayHands = ft.Image(src='https://uctmfeyuzyigljzvslth.supabase.co/storage/v1/object/sign/testbuck/mdi--hands-pray.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJ0ZXN0YnVjay9tZGktLWhhbmRzLXByYXkucG5nIiwiaWF0IjoxNzQxNjMyODcyLCJleHAiOjE3NzMxNjg4NzJ9.fRNPJTFObYox9F8AytUlfdh--ytlz-rWgsx86tUVYEg',width=30,height=30)
    header01 = ft.Text(value="Dear My Father",size=20,color='#000000',style=ft.TextStyle(font_family='zaramain',weight=ft.FontWeight.W_100,letter_spacing=0),text_align=ft.TextAlign.CENTER)
    textfiled01 = ft.TextField(label='My Prayer',hint_text='Dear Heavenly Father...',max_lines=5,color='#141F64',border_color='#141F64',width=380,multiline=True,cursor_color='#1024C6',cursor_radius=10,cursor_width=10,label_style=ft.TextStyle(color='#9E9E9E'),bgcolor='#FBFCFD',hint_fade_duration=500)
    header01Col = ft.Column(controls=[ft.Row(controls=[prayHands,header01]),textfiled01],horizontal_alignment=ft.CrossAxisAlignment.START,width=380,)
    
    
    bibleCross = ft.Image(src='https://uctmfeyuzyigljzvslth.supabase.co/storage/v1/object/sign/testbuck/arcticons--quick-bible.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJ0ZXN0YnVjay9hcmN0aWNvbnMtLXF1aWNrLWJpYmxlLnBuZyIsImlhdCI6MTc0MTYzMzExNywiZXhwIjoxNzczMTY5MTE3fQ.i94G5zZrSvW8dkdcgPdmzqz1ddSf18MzoGIHzvUGhV0',width=30,height=30)
    header02 = ft.Text(value='From My Father',size=20,color='#000000',style=ft.TextStyle(font_family='zaramain',weight=ft.FontWeight.W_100,letter_spacing=0),text_align=ft.TextAlign.CENTER)
    iconbutton01 = ft.IconButton(icon=ft.CupertinoIcons.BOOK)
    header02Row = ft.Row(controls=[ft.Row(wrap=True,controls=[bibleCross,header02]),iconbutton01],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    exp01 = ft.ExpansionPanel(header=ft.ListTile(title=ft.Text(f"태초에 하나님이...")),content=ft.ListTile(
        title=ft.Text('창세기 1:1'),
        subtitle=ft.Text('태초에 하나님이 천지를 창조하시니라'),
    ))
    exp02 = ft.ExpansionPanel(header=ft.ListTile(title=ft.Text(f"하나님이 세상을...")),content=ft.ListTile(
        title=ft.Text('요한복음 3:16'),
        subtitle=ft.Text('하나님이 세상을 이처럼 사랑하사 독생자를 주셨으니 이는 저를 믿는 자마다 멸망치 않게 하려 하심이라.'),
    ))
    exp03 = ft.ExpansionPanel(header=ft.ListTile(title=ft.Text(f"여호와는 나의...")),content=ft.ListTile(
        title=ft.Text('시편 23:1'),
        subtitle=ft.Text('여호와는 나의 목자시니 내가 부족함이 없으리로다'),
    ))
    expansions = ft.ExpansionPanelList(elevation=10,controls=[exp01,exp02,exp03])
    header02Col = ft.Column(controls=[header02Row,expansions],horizontal_alignment=ft.CrossAxisAlignment.START,width=380,)
    
    
    heartImg = ft.Image(src='https://uctmfeyuzyigljzvslth.supabase.co/storage/v1/object/sign/testbuck/fluent-emoji-flat--pink-heart.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJ0ZXN0YnVjay9mbHVlbnQtZW1vamktZmxhdC0tcGluay1oZWFydC5wbmciLCJpYXQiOjE3NDE2MzMyMDMsImV4cCI6MTc3MzE2OTIwM30.IJJ0tbbfg-s4oOxlvtjdDmBpJg4LTcDaEXScehdAOsU',width=30,height=30)
    header03 = ft.Text(value="God's Love Letter",size=20,color='#000000',style=ft.TextStyle(font_family='zaramain',weight=ft.FontWeight.W_100,letter_spacing=0),text_align=ft.TextAlign.CENTER)
    iconbutton02 = ft.IconButton(icon=ft.Icons.REDEEM)
    iconbutton03 = ft.IconButton(icon=ft.Icons.IOS_SHARE)
    icon03Col = ft.Row(controls=[iconbutton02,iconbutton03],wrap=True)
    header03Row = ft.Row(controls=[ft.Row(wrap=True,controls=[heartImg,header03]),icon03Col],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,width=380)
    imageContainer = ft.Container(content=ft.Image(src='https://uctmfeyuzyigljzvslth.supabase.co/storage/v1/object/sign/testbuck/dearFather.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJ0ZXN0YnVjay9kZWFyRmF0aGVyLnBuZyIsImlhdCI6MTc0MTYzMTk1MCwiZXhwIjoxNzczMTY3OTUwfQ.q_4VD-BySML6LI2eykFLAswD1W4jUTV6bmHSdzDY65w',fit=ft.ImageFit.FIT_WIDTH),width=380)
    
    mainColumn = ft.Container(content=ft.Column(controls=[
        title,
        header01Col,
        header02Col,
        header03Row,imageContainer
    ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,scroll=ft.ScrollMode.AUTO),alignment=ft.alignment.top_center)
    
    # page.add(mainColumn)
    page.add(ft.SafeArea(content=mainColumn,expand=True))
    page.navigation_bar = ft.CupertinoNavigationBar(selected_index=0,
        bgcolor='#fbfbfb',
        inactive_color=ft.Colors.GREY,
        active_color=ft.Colors.BLACK,
        destinations=[
            ft.NavigationBarDestination(icon=ft.CupertinoIcons.BOOKMARK,label=""),
            ft.NavigationBarDestination(icon=ft.CupertinoIcons.HOUSE_ALT, label=''),
            ft.NavigationBarDestination(icon=ft.CupertinoIcons.PERSON),
            
        ]
    )
    
    
    page.bgcolor = '#ffffff'
    page.fonts={'zaramain':'https://uctmfeyuzyigljzvslth.supabase.co/storage/v1/object/sign/testbuck/OPTIBodoni-Antiqua.otf?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJ0ZXN0YnVjay9PUFRJQm9kb25pLUFudGlxdWEub3RmIiwiaWF0IjoxNzQwOTkxMDM0LCJleHAiOjE3NzI1MjcwMzR9.BYxXY6vXOOoyk_L1xudbJzfy42bRI90WtWzFfGOJDcY','typo1':'AmericanTypewriter.ttc','typo2':'MTCORSVA.TTF'}
    page.window.height,page.window.width = 852,393 # 논리적 해상도임.(물리적해상도는 )
    page.update()
ft.app(main,view=ft.WEB_BROWSER,web_renderer=ft.WebRenderer.CANVAS_KIT)
