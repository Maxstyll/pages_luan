# buscas!
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



    q.page['form'] = ui.form_card(box='1 1 -1 6', items=[
        ui.table(
            name='issues',
            columns=columns,
            rows=[ui.table_row(
                name=issue.id,
                cells=[issue.text,issue.icon, str(issue.views),
                       str(issue.progress)]) for issue in issues],
        )
    ])
    await q.page.save()