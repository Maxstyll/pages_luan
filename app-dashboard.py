# https://wave.h2o.ai/
# http://localhost:10101/dashboard


# pip install h2o
# pip install h2o_wave

# wave run app-dashboard.py
import pandas as pd
from h2o_wave import site, main, ui, data


def carregar_dados():
    dados = pd.read_csv('dados/application_data.csv')
    print(dados.shape)
    return dados

dataset = carregar_dados()

page = site['/dashboard']

################################################################################
card = page.add('header', ui.header_card(box='1 1 10 2',
                                        title = 'Data App - DashBoard',
                                        subtitle =  'Mini-Projeto',
                                        icon = 'ExploreData'))



################################################################################
# Grafico

df_bar = dataset.loc[:200, ['NAME_INCOME_TYPE', 'AMT_INCOME_TOTAL', 'CODE_GENDER']]
grafico1 = page.add('bar_plot', ui.plot_card(box = '1 3 4 4',
                                            title='Total de Rendimentos por Tipo de Rendimentos e Gênero',
                                            data = data(fields = df_bar.columns.tolist(), rows =df_bar.values.tolist()),
                                            plot = ui.plot(marks = [ui.mark(type = 'interval',
                                                                            x = '=NAME_INCOME_TYPE',
                                                                            y = '=AMT_INCOME_TOTAL',
                                                                            color = '=CODE_GENDER',
                                                                            dodge = 'auto')])))


################################################################################
df_pont = dataset.loc[:200, ['DAYS_REGISTRATION', 'DAYS_ID_PUBLISH', 'NAME_EDUCATION_TYPE']]
grafico2 = page.add('point_plot', ui.plot_card(box = '5 3 6 2',
                                            title='Clientes por Escolaridade',
                                            data = data(fields = df_pont.columns.tolist(), rows =df_pont.values.tolist()),
                                            plot = ui.plot(marks = [ui.mark(type = 'point',
                                                                            x = '=DAYS_REGISTRATION',
                                                                            y = '=DAYS_ID_PUBLISH',
                                                                            color = '=NAME_EDUCATION_TYPE')])))



################################################################################

df_pont_sized = dataset.loc[:200, ['AMT_INCOME_TOTAL', 'AMT_CREDIT', 'AMT_ANNUITY']]
grafico3 = page.add('point_plot_sized', ui.plot_card(box = '5 5 6 2',
                                            title='Total de Rentabilidade por Total de Crédito',
                                            data = data(fields = df_pont_sized.columns.tolist(), rows =df_pont_sized.values.tolist()),
                                            plot = ui.plot(marks = [ui.mark(type = 'point',
                                                                            x = '=AMT_INCOME_TOTAL',
                                                                            y = '=AMT_CREDIT',
                                                                            color = '=AMT_ANNUITY')])))



################################################################################

df_bar_stacked = dataset.loc[:200, ['AMT_INCOME_TOTAL', 'NAME_INCOME_TYPE', 'NAME_FAMILY_STATUS']]
grafico4 = page.add('bar_stacked', ui.plot_card(box = '1 7 10 4',
                                            title='Total de Rentabilidade por Tipo de Rendimento e status Familiar',
                                            data = data(fields = df_bar_stacked.columns.tolist(), rows =df_bar_stacked.values.tolist()),
                                            plot = ui.plot(marks = [ui.mark(type = 'interval',
                                                                            x = '=AMT_INCOME_TOTAL',
                                                                            y = '=NAME_INCOME_TYPE',
                                                                            color = '=NAME_FAMILY_STATUS',
                                                                            dodge = 'auto')])))



################################################################################

df_linhas = dataset.loc[:200, ['SK_ID_CURR', 'AMT_INCOME_TOTAL']]
grafico5 = page.add('linhas', ui.plot_card(box = '1 11 5 4',
                                            title='Total de Rendimento Por tipo de Empréstimo',
                                            data = data(fields = df_linhas.columns.tolist(), rows =df_linhas.values.tolist()),
                                            plot = ui.plot(marks = [ui.mark(type = 'line',
                                                                            x = '=SK_ID_CURR',
                                                                            y = '=AMT_INCOME_TOTAL',
                                                                            curve = 'smooth')])))



################################################################################

df_area = dataset.loc[:200, ['AMT_INCOME_TOTAL', 'NAME_EDUCATION_TYPE', 'NAME_FAMILY_STATUS']]
grafico6 = page.add('area', ui.plot_card(box = '6 11 5 4',
                                            title='Total de Rendimento Por tipo de Rendimento e Estado Civil',
                                            data = data(fields = df_area.columns.tolist(), rows =df_area.values.tolist()),
                                            plot = ui.plot(marks = [ui.mark(type = 'area',
                                                                            x = '=NAME_EDUCATION_TYPE',
                                                                            y = '=AMT_INCOME_TOTAL',
                                                                            color = '=NAME_FAMILY_STATUS')])))




################################################################################

df_linhas_step = dataset.loc[:200, ['SK_ID_CURR', 'AMT_INCOME_TOTAL']]
grafico7 = page.add('linhas_step', ui.plot_card(box = '1 15 5 4',
                                            title='Total de Rendimento Por Tipo de Empréstimo (Step)',
                                            data = data(fields = df_linhas_step.columns.tolist(), rows =df_linhas_step.values.tolist()),
                                            plot = ui.plot(marks = [ui.mark(type = 'path',
                                                                            x = '=SK_ID_CURR',
                                                                            y = '=AMT_INCOME_TOTAL',
                                                                            curve = 'step')])))

page.save()