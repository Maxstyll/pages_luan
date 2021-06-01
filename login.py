from h2o_wave import Q, main, ui, app
#######################################################################################################################

@app('/login')
async def serve(q: Q):
    card = q.page.add('header', ui.header_card(box = '1 1 9 2',
                        title = 'login',
                        subtitle = 'Projetos',
                        icon = 'ExploreData'))

    if q.args.show_inputs:
        q.page['login_user'].items = [
            ui.text(f'textbox_login={q.args.textbox_login}'),
            ui.text(f'textbox_senha={q.args.textbox_senha}'),
            ui.button(name='show_form', label='Back', primary=True),
        ]
    else:
        q.page['login_user'] = ui.form_card(box='3 3 5 3', items=[
            ui.textbox(name='textbox_login', label='Login', required=True),
            ui.textbox(name='textbox_senha', label='Senha', required=True),
            ui.button(name='show_inputs', label='Entrar', primary=True),
        ])
    await q.page.save()