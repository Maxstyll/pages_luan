# Buscas!
# A simple example to get you started with Wave.
# #buscas
# ---
# Import `Site` and the `ui` module from the `h2o_wave` package
import random
from faker import Faker
from h2o_wave import main, app, Q, ui

fake = Faker()

_id = 0


class Issue:
    def __init__(self, text: str, status: str, accuracy: float, icon: str, notifications: str):
        global _id
        _id += 1
        self.id = f'I{_id}'
        self.text = text
        self.status = status
        self.views = 1
        self.progress = accuracy
        self.icon = icon
        self.notifications = notifications


# Create some issues
issues = [
    Issue(
        text=fake.sentence(),
        status=('Closed' if i % 2 == 0 else 'Open'),
        accuracy=random.random(),
        icon=('BoxCheckmarkSolid' if random.random() > 0.5 else 'BoxMultiplySolid'),
        notifications=('Off' if random.random() > 0.5 else 'On')) for i in range(100)
]

# Create columns for our issue table.
columns = [
    ui.table_column(name='text', label='model', searchable=True),
    ui.table_column(name='done', label='Done', cell_type=ui.icon_table_cell_type()),
    ui.table_column(name='Date', label='Date'),
    ui.table_column(name='Accuracy', label='Accuracy', cell_type=ui.progress_table_cell_type()),
]

#####################################################################################################
@app('/body')
async def serve(q: Q):
    card = q.page.add('header', ui.header_card(box = '1 1 9 2',
	                                     title = 'busca de modelos',
										 subtitle = '',
										 icon = 'ExploreData',))

                                         
    q.page['form'] = ui.form_card(box='1 3 -1 6', items=[
        ui.table(
            name='issues',
            columns=columns,
            rows=[ui.table_row(
                name=issue.id,
                cells=[issue.text,issue.icon, str(issue.views),
                       str(issue.progress)]) for issue in issues],
        )
    ])


    if q.args.show_inputs:
        q.page['example'].items = [
            ui.textbox(name='textbox_date', label='date', mask='(999) 999 - 9999'),
            ui.textbox(name='textbox_name', label='name', required=True),
            ui.textbox(name='textbox_loss', label='loss', required=True),
            ui.textbox(name='textbox_acuracy', label='acuracy', required=True),
            ui.textbox(name='textbox_dataset', label='dataset', required=True),
            ui.button(name='example', label='inselt', primary=True),
        ]
    else:
     q.page['login_user'] = ui.form_card(box='3 3 5 3', items=[
            ui.textbox(name='textbox_login', label='Login', required=True),
            ui.textbox(name='textbox_senha', label='Senha', required=True),
            ui.button(name='example', label='Entrar', primary=True),
     ])
        
    q.page['example'] = ui.form_card(box='1 9 -1 10', items=[
        ui.buttons([
            ui.button(name='show_inputs', label='to create', primary=True),
            ]),
        ])        
    await q.page.save()