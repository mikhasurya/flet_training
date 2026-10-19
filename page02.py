import flet as ft


@ft.component
def Page02():

    return ft.Column(
        #route="/page2",
        controls=[
            ft.Text(
                "HALAMAN 2",
                size=30,
            ),

            ft.DataTable(
                columns=[
                    ft.DataColumn(
                        ft.Text(
                            value="Demo01"
                        )
                    ),
                    ft.DataColumn(
                        ft.Text(
                            value="Demo02"
                        )
                    )                    
                ],
                
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(
                                ft.Row(
                                    wrap=False,
                                    controls=[
                                        ft.Text(
                                            value="Text_01"
                                        ),
                                        ft.Button(
                                            content="Button_01"
                                        ),
                                    ]
                                ),

                                expand=True
                            ),

                            ft.DataCell(
                                ft.Row(
                                    wrap=False,
                                    controls=[
                                        ft.Text(
                                            value="Text_02"
                                        ),
                                        ft.Button(
                                            content="Button_02"
                                        ),
                                    ]
                                ),

                                expand=True
                            )                            
                        ]
                    )
                ]
            ),

            ft.Button(
                content="Back",
                margin=20,
                on_click=lambda:
                ft.context.page.navigate(
                    "/"
                ),
            ),
        ],
    )