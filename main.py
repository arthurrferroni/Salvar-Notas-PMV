import time
from selenium import webdriver

# Definido o webdriver.Chrome() como navegador
navegador = webdriver.Chrome()

# Abrir o site de Emissão de Notas da Prefeitura de Varginha
navegador.get("https://nfe.etransparencia.com.br/mg.varginha/nfe/principal.aspx")

# Estas três linha fazem o login no sistema, há um tempo de 15 segundos para digitar o Captcha
navegador.find_element_by_xpath('//*[@id="vUSRCLOG"]').send_keys("")
navegador.find_element_by_xpath('//*[@id="vUSRDPWD"]').send_keys("")
time.sleep(15)

# Após logar, selciona a empresa a ser usada
navegador.find_element_by_xpath('//*[@id="IMAGE6"]').click()
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="IMGEMPRESA_MPAGE"]').click()
time.sleep(10)
navegador.switch_to.frame("gxp0_ifrm")
navegador.find_element_by_xpath('/html/body/form/div[2]/div[2]/div[1]/div/table/tbody/tr[4]/td/table/tbody/tr/td/fieldset/table/tbody/tr[2]/td[2]/input').send_keys('10684160000150')
navegador.find_element_by_xpath('//*[@id="CONSUTAR"]').click()
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="vIMAGESTATUS_0001"]').click()
time.sleep(2)

# Acessar a área para baixar as notas
navegador.find_element_by_xpath('//*[@id="NFEMenu"]/li[3]/a').click()
navegador.find_element_by_xpath('//*[@id="NFEMenu"]/li[3]/ul/li[4]/a').click()
time.sleep(2)

# Filtra as notas
navegador.find_element_by_xpath('//*[@id="TABLEACTIONS"]/tbody/tr/td[1]/input').click()
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="VERIFICAR"]').click()









