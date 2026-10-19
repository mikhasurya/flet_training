import flet as ft

from page01 import Page01
from page02 import Page02


@ft.component
def App():

    return ft.Router(
        manage_views=True,

        routes=[

            ft.Route(
                index=True,
                component=Page01
            ),

            ft.Route(
                path="page2",
                component=Page02
            )
        ],
    )


def main(page: ft.Page):

    page.render(App)


ft.run(main)