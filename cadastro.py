from h2o_wave import Q, main, ui, app
#######################################################################################################################

@app('/cadastro')
async def serve(q: Q):
    card = q.page.add('header', ui.header_card(box = '1 1 9 2',
                        title = 'modelo de cadastro',
                        subtitle = 'Projetos',
                        icon = 'ExploreData'))

    if q.args.show_inputs:
        q.page['login_user'].items = [
            ui.textbox(name='textbox_login', label='Login', required=True),
            ui.textbox(name='textbox_senha', label='Senha', required=True),
            ui.button(name='login_user', label='Back', primary=True),
        ]
    else:
        q.page['login_user'] = ui.form_card(box='3 3 5 5', items=[
            ui.textbox(name='textbox_date', label='date', mask='(999) 999 - 9999'),
            ui.textbox(name='textbox_name', label='name', required=True),
            ui.textbox(name='textbox_loss', label='loss', required=True),
            ui.textbox(name='textbox_acuracy', label='acuracy', required=True),
            ui.textbox(name='textbox_dataset', label='dataset', required=True),
            ui.button(name='show_inputs', label='inselt', primary=True),
        ])
        

    await q.page.save()