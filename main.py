import time
import os
import tqdm

#os.system('cmd.exe')
print('____________ Github ____________\n')
progressbar = tqdm.tqdm(total=100,leave=True)

print('\nCriando o arquivo README.md...')
os.system("echo '# Utilitario_Github' >> README.md")
time.sleep(2)
progressbar.update(10)

print('\nIniciando o repositorio(git init)...')
os.system("git init")
time.sleep(2)
progressbar.update(10)

print('\nAdicionando arquivos na branch(git add)...')
os.system("git add .")
time.sleep(2)
progressbar.update(20)

while True:
    mensagem = input("\nQual a mensagem do commit?\n( [ENTER] para a mensgem default ( first commit )) ")
    if not mensagem:
        mensagem = 'first commit'
        mensagem = '"'+mensagem+'"'
        break
    else:
        mensagem = '"'+mensagem+'"'
        print('Adicionando a mensagem de commit (Commit)...')
        break
os.system("git commit -m "+mensagem)

time.sleep(2)
progressbar.update(20)

while True:
    remote = input("\nQual o link do remote? ")
    if len(remote) <  19:
        print("Link não adicionado ou o link esta errado!")
    else:
        print('Adicionando link do remote (git remote add https://git...)')
        break
os.system("git remote add origin "+remote)
time.sleep(2)
progressbar.update(20)

print("\nEnviando(Push)...")
os.system("git push -u origin master")
time.sleep(2)
progressbar.update(20)

print("\n________ Projeto enviado!________")
progressbar.close()
time.sleep(5)

