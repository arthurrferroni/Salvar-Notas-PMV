import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Mudar pasta de download do webdriver
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": r"C:\""}
options.add_experimental_option("prefs", prefs)

# Desabilita o PDF Viewer do Chrome
chromeOptions = webdriver.ChromeOptions()
prefs = {"plugins.plugins_disabled": ["Chrome PDF Viewer"]}


# Definido o webdriver.Chrome() como navegador
navegador = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)

# Abrir o site de Emissão de Notas da Prefeitura de Varginha
navegador.get("https://nfe.etransparencia.com.br/mg.varginha/nfe/principal.aspx")

# Estas quatro linha fazem o login no sistema, há um tempo de 15 segundos para digitar o Captcha
navegador.find_element_by_xpath('//*[@id="vUSRCLOG"]').send_keys("")
navegador.find_element_by_xpath('//*[@id="vUSRDPWD"]').send_keys("")
time.sleep(15)
navegador.find_element_by_xpath('//*[@id="IMAGE6"]').click()
time.sleep(5)

# Seleção das empresas conforme planilha
navegador.find_element_by_xpath('//*[@id="IMGEMPRESA_MPAGE"]').click()
time.sleep(5)
navegador.switch_to.frame("gxp0_ifrm")
navegador.find_element_by_xpath('/html/body/form/div[2]/div[2]/div[1]/div/table/tbody/tr['
                                '4]/td/table/tbody/tr/td/fieldset/table/tbody/tr[2]/td[2]/input').send_keys(
    '')
navegador.find_element_by_xpath('//*[@id="CONSUTAR"]').click()
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="vIMAGESTATUS_0001"]').click()
time.sleep(4)

# Acessar a área para baixar as notas
navegador.find_element_by_xpath('//*[@id="NFEMenu"]/li[3]/a').click()
navegador.find_element_by_xpath('//*[@id="NFEMenu"]/li[3]/ul/li[4]/a').click()
time.sleep(2)

# Selecionar a competência anterior para filtrar as notas emitidas
navegador.find_element_by_xpath('//*[@id="TABLEACTIONS"]/tbody/tr/td[1]/input').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="vMES"]').click()
navegador.find_element_by_xpath('//*[@id="vMES"]').send_keys(Keys.ARROW_UP)
navegador.find_element_by_xpath('//*[@id="vMES"]').send_keys(Keys.ENTER)
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="VERIFICAR"]').click()
time.sleep(5)

# Baixar os arquivos nescessários

# Salvar XML
navegador.find_element_by_xpath('//*[@id="TABLEFILTROACTIONS"]/tbody/tr/td[3]/input').click()
time.sleep(5)
navegador.switch_to.frame("gxp0_ifrm")
time.sleep(4)
navegador.find_element_by_xpath('//*[@id="TABLE3"]/tbody/tr/td[2]/input').click()
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="IMAGE2"]').click()

# Salvar talão fiscal
navegador.switch_to.default_content()
navegador.find_element_by_xpath('//*[@id="TABLEFILTROACTIONS"]/tbody/tr/td[2]/input').click()
navegador.switch_to.default_content()
time.sleep(4)

# Salvar relatório sintético
navegador.find_element_by_xpath('//*[@id="TABLEFILTROACTIONS"]/tbody/tr/td[1]/input').click()
time.sleep(4)
navegador.switch_to.frame("gxp0_ifrm")
navegador.find_element_by_xpath('//*[@id="TABLEACTIONS"]/tbody/tr/td[2]/input').click()
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="TABLEACTIONS"]/tbody/tr/td[2]/input').send_keys(Keys.ESCAPE)
