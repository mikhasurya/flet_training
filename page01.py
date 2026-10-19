import flet as ft

@ft.component
def Page01():
    counter, set_counter = ft.use_state(0)
    init_val, set_init_val = ft.use_state("")

    txtfld_init_val = ft.TextField(hint_text="Init Val",value=init_val, on_change=lambda e:set_init_val(e.control.value))

    def reset_init_val(e) -> None:
        set_counter(int(init_val)) if init_val.isdigit() else None

    return ft.Column(
            controls=[
                txtfld_init_val,

                ft.Button(
                    content="Set",
                    on_click=reset_init_val
                ),

                ft.Button( 
                    content="Next",
                    on_click=lambda _:ft.context.page.navigate("/page2"),
                ),

                ft.Row(
                    controls=[
                        ft.Button(
                            content="+1",
                            on_click=lambda e:set_counter(counter+1)
                        ),
                        ft.Text(
                            f"{counter}"
                        )
                    ]
                )
            ],
        ) 
