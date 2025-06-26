import customtkinter as ctk

#Aparência do Tema
ctk.set_appearance_mode('dark')


#Criação das Funções de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    #Verificar o usuário e senha
    if usuario == 'admin' and senha == '1234':
        resultado_login.configure(text='Login bem sucedido!', text_color='green')
    else:
        resultado_login.configure('Usuário ou senha incorretos!', text_color='red')



#Janela Principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

# Criação os campos
#Label do Usuário
label_usuario = ctk.CTkLabel(app, text='Usuário:')
label_usuario.pack(pady=10)
#Entry do Usuário
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)
#Label da Senha
label_senha = ctk.CTkLabel(app, text='Senha:')
label_senha.pack(pady=10)
#Entry da Senha
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite seu senha', show='*')
campo_senha.pack(pady=10)
#Button
botao_login = ctk.CTkButton(app, text='Entrar', command=validar_login)
botao_login.pack(pady=10)
#campo Feedback de login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)


#Iniciar a aplicação
app.mainloop()
