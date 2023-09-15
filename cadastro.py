from PySimpleGUI import PySimpleGUI as sg

# [ ‘NeutralBlue’, ‘Purple’, ‘Reddit’, ‘Reds’, ‘SandyBeach’, ‘SystemDefault’, ‘SystemDefault1’, ‘SystemDefaultForReal’, ‘Tan’, ‘TanBlue’, ‘TealMono’, ‘Topanga’]

# layout
sg.theme('Purple')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(25, 1)) ],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(25, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'leandro' and valores['senha'] == '123456':
            print('Seja Bem-Vindo')
        else:
            print('Você mamou')