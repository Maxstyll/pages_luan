from h2o_wave import Q, main, ui, app

async def getLogin(q: Q):
    bory = q.page['bory']
    if q.args.show_inputs:
        bory.items = [
            ui.text(f'textbox_login={q.args.textbox_login}'),
            ui.text(f'textbox_senha={q.args.textbox_senha}'),
            ui.button(name='show_form', label='Back', primary=True),
            ui.button(name='', label='Back', primary=True),
        ]
    else:
        bory = ui.form_card(box='1 11 12 2', items=[
            ui.textbox(name='textbox_login', label='Login', required=True),
            ui.textbox(name='textbox_senha', label='Senha', required=True),
            ui.button(name='show_inputs', label='Entrar', primary=True),
        ])

    return q