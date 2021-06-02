from h2o_wave import main, app, Q, ui, on, handle_on
import login

@app('/index')
async def serve(q: Q):
    if not q.client.initialized:
        q.client.initialized = True
        q.page['header'] = ui.markdown_card(
            box='1 1 12 2',
            title='header',
            content='[Spam](#menu/spam) / [Ham](#menu/ham) / [Eggs](#menu/eggs) / [About](#about)',
        )
        q.page['menu'] = ui.markdown_card(
            box='1 3 12 2',
            title='Menu',
            content='[Spam](#menu/spam) / [Ham](#menu/ham) / [Eggs](#menu/eggs) / [About](#about)',
        )
        
        q.page['bory'] = ui.markdown_card(
            box='1 3 12 2',
            title='bory',
            content='[Spam](#menu/spam) / [Ham](#menu/ham) / [Eggs](#menu/eggs) / [About](#about)',
        )

        q.page['footer'] = ui.markdown_card(
            box='1 11 12 2',
            title='footer',
            content='[Spam](#menu/spam) / [Ham](#menu/ham) / [Eggs](#menu/eggs) / [About](#about)',
        )

        await q.page.save()
    else:
        await handle_on(q)