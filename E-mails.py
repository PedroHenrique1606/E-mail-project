import os
import smtplib
from email.message import EmailMessage

senha = '123456'
#você vai inserir a senha do seu e-mail aqui acima

#CONFIGURAR E-MAIL E SENHA
email_user = 'simpleprogramation28@gmail.com'
email_pass = senha

#gera um e-mail
msg = EmailMessage()
msg['Sbject'] = 'Relatório semanal.'
#aqui fica do que se trata a mensagem

msg['From'] = ''
#aqui você insere o seu e-mail, de onde vai sair a mensagem
#exemlplo: msg['From'] = 'lucianohuck7745@gmail.com'

msg['To'] = ''
#aqui você coloca o e-mail que você deseja enviar a mensagem
#exemplo: msg['To'] = 'joseluiz99penha@gmial.com'

msg.set_content('Olá, Bom dia^-^')
#aqui vai o conteúdo da mensagem que você deseja enviar!

# Enviar o e-mail
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_user,email_pass)
    smtp.send_message(msg)
#aqui ele vai logar na sua conta e-mail e realizar o envio da mensagem!

print('E-mails enviados')
