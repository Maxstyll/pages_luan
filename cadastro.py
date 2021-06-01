from h2o_wave import Q, main, ui, app
#######################################################################################################################

@app('/modelo')
async def serve(q: Q):
    card = q.page.add('header', ui.header_card(box = '1 1 9 2',
                        title = 'modelo de cadastro',
                        subtitle = 'Projetos',
                        icon = 'ExploreData'))

    if q.args.show_inputs:
        q.page['login_user'].items = [
            ui.text(f'textbox_date={q.args.textbox_date}'),
            ui.text(f'textbox_name={q.args.textbox_name}'),
            ui.text(f'textbox_loss={q.args.textbox_loss}'),
            ui.text(f'textbox_acuracy={q.args.textbox_acuracy}'),
            ui.text(f'textbox_dataset={q.args.textbox_dataset}'),
            ui.button(name='login_user', label='next', primary=True),
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