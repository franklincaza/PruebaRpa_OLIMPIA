*** Settings ***
Library     SeleniumLibrary

Test Setup       open page
Test Teardown    Close

*** Variables ***
${url}=     https://www.einforma.co/buscador-empresas-empresarios
${Browser}  chrome
${Nit}  Olimpia

*** Test Cases ***
lauch process
    execute process


*** Keywords ***
open page
    open Browser     ${url}     ${Browser}
    title should be     Consultar una empresa por nombre en Colombia - eInforma
    Maximize browser window

execute process

    Input Text    xpath=(//input[@name="search"])[2]    olimpia
    Click Element    //input[@id="boton_buscador_nacional"]
    Execute JavaScript    window.scrollTo(0,500)
    ${scraping}=    Get Text    //*[@id="nacional"]
    log to console      ${scraping}
    capture page screenshot     C:\Users\frank\OneDrive - Practia\Documentos\Selenium\PruebaRPA\Captura de pantallas\UsersfrankOneDrive - Cantura de pantalla 001.png
    Click Link    xpath=(//a[@href="/servlet/app/portal/ENTP/screen/SProductoClienteWeb/prod/LISTA_EMPRESAS/razonsocial/olimpia/indice/13"])[2]
    Click Link    //*[@id="nacional"]/div[3]/div/div[2]/ul/li[4]/a
close
    Sleep       5
    Close Browser
