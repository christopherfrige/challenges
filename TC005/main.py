import requests
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from credentials import user, pwd

def baixarAnexos():
    # Procurará os anexos e clicará se existir
    try:
        temAnexos = browser.find_element_by_class_name("attachmentslist")
        if temAnexos:
            anexos = browser.find_elements_by_class_name("attachment-name")
            for anexo in anexos:
                anexo.click()
    # Se não houverem anexos, irá retornar
    except:
        pass
    finally:
        browser.back()
        time.sleep(intervalo)


# Tempo estimado para terminar os downloads (segundos) depois de acessar todos emails
tempoDownload = 10
intervalo = 3

# Inicializa o navegador e entra no site
browser = webdriver.Chrome()
browser.get("https://webmail.trackcash.com.br/")

# Preenche os campos de login e senha, depois clica no botão para entrar
username = browser.find_element_by_id("user")
username.send_keys(user)
password = browser.find_element_by_id("pass")
password.send_keys(pwd)
loginButton = browser.find_element_by_id("login_submit").click()
# Levando em conta o tempo de carregamento, um intervalo de X segundos até o resto das ações
time.sleep(intervalo)

# Procura os emails não lidos e coloca numa lista
novosEmails = browser.find_elements_by_xpath('//*[@class="message unread" or @class="message unread focused"]')
for i in range(0, len(novosEmails)):
    # Procura cada email individualmente
    novoEmail = browser.find_element_by_xpath('//*[@class="message unread" or @class="message unread focused"]')

    # Declaração para fazer um doubleclick
    acao = ActionChains(browser)
    acao.double_click(novoEmail).perform()    
    time.sleep(intervalo)

    # Procura anexos no email, se achar irá baixar
    baixarAnexos()

# Para terminar os downloads em andamento e melhor visualização no terminal
if len(novosEmails)>=1:
    print("Terminando os downloads...")
    time.sleep(tempoDownload)
    print("Downloads finalizados.")
else:
    print("Nenhum e-mail novo.")
