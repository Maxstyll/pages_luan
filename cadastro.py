# Cadastros!
# A simple example to get you started with Wave.
# #cadastro
# ---
# Import `Site` and the `ui` module from the `h2o_wave` package
from h2o_wave import Q, main, ui, app
#######################################################################################################################

@app('/body')
async def serve(q: Q):


    if q.args.show_inputs:
        q.page['login_user'].items = [
            ui.text(f'textbox_date={q.args.textbox_date}'),
            ui.text(f'textbox_name={q.args.textbox_name}'),
            ui.text(f'textbox_loss={q.args.textbox_loss}'),
            ui.text(f'textbox_acuracy={q.args.textbox_acuracy}'),
            ui.text(f'textbox_dataset={q.args.textbox_dataset}'),
            ui.button(name='show_form', label='Back', primary=True),
        ]
    else:
        q.page['login_user'] = ui.form_card(box='1 1 5 5', items=[
            ui.textbox(name='textbox_date', label='date', mask='(999) 999 - 9999'),
            ui.textbox(name='textbox_name', label='name', required=True),
            ui.textbox(name='textbox_loss', label='loss', required=True),
            ui.textbox(name='textbox_acuracy', label='acuracy', required=True),
            ui.textbox(name='textbox_dataset', label='dataset', required=True),
            ui.button(name='login', label='inselt', primary=True),
        ])
        

    await q.page.save()