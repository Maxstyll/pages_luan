import os
import os.path
from typing import ItemsView
from h2o_wave import main, app, Q, ui


async def uploadImage(q: Q, link):
    q.page.add('boxImage', ui.wide_info_card(
        box='5 3 4 5',
        title='Image Processada',
        caption='''''',
        category='',
        image= link
    ))


@app('/imagens')
async def serve(q: Q):
    card = q.page.add('header', ui.header_card(box='1 1 -1 2',
                                        title = 'Data App - DashBoard',
                                        subtitle =  'Mini-Projeto',
                                        icon = 'ExploreData'))
    links = q.args.user_files
    if links:
        items = [ui.text_xl('Files uploaded!')]
        await uploadImage(q, f'http://localhost:10101/{links[0]}')
    else:
        q.page['boxUpload'] = ui.form_card(box='2 3 3 5', items=[
            ui.text_xl('Upload some files'),
            ui.file_upload(name='user_files', label='Upload', multiple=True),
        ])

        await uploadImage(q, '')    

    await q.page.save()