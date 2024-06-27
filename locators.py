from selenium.webdriver.common.by import By

class Locators():
    # кнопка "войти в аккаунт на главной"
    auth_button_main_page = (By.XPATH,".//button[contains(text(),'Войти в аккаунт')]")
    # кнопка "зарегистрироваться" на странице авторизации
    registr_button_auth_page = (By.XPATH,'.//a[@href="/register"]')
    # заголовок h2 на странице регистрации
    registr_header_regist_page = (By.XPATH, "//h2[text()='Регистрация']")
    # поле ввода имени на странице регистрации
    name_input_regist_page = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']")
    # поле ввода email на странице регистрации и авторизации
    email_input_auth_and_regist_page = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")
    # поле ввода пароля  на странице регистрации и авторизации
    password_input_auth_and_registr = (By.XPATH, './/input[@type="password"]')
    # кнопка "зарегистрироваться" на странице регистрации
    registr_button_regist_page = (By.XPATH,"//button[contains(text(),'Зарегистрироваться')]")
    # заголовок h2 на странице авторизации
    auth_header_auth_page = (By.XPATH, "//h2[contains(text(), 'Вход')]")
    # сообщение о некорректности пароля на странице регистрации
    incorrect_pass_registr_page = (By.XPATH,"//p[contains(text(),'Некорректный пароль')]")
    # кнопка "войти" на странице авторизации
    auth_button_auth_page = (By.XPATH,"//button[contains(text(),'Войти')]")
    # общий XPATH для заголовков на странице регистрации и авторизации
    h2_auth_and_registr_page = (By.XPATH,"//main//h2")
    # заголовок на главной странице
    main_header_main_page = (By.XPATH,"//h1")
    # кнопка "личный кабинет" в хэдере любой страницы
    lk_button_in_head = (By.XPATH,'//div[@id="root"]//a[@href="/account"]')
    # текстовая кнопка "войти" на странице регистрации и восстановления пароля
    auth_button_registr_and_restore_page = (By.XPATH, '//a[@href="/login"]')
    # текстовая кнопка "восстановить пароль" на странице авторизации
    restore_password_auth_page = (By.XPATH,'//a[@href="/forgot-password"]')
    # поля отображения email на странице лк
    email_field_lk_page = (By.XPATH,"//label[contains(text(),'Логин')]/following-sibling::input[@name='name']")
    # кнопка "кноструктор" в хедере
    konstr_button_in_head = (By.XPATH," //p[contains(text(),'Конструктор')]")
    # кнопка перехода на главную в хедере
    main_button_in_header = (By.XPATH,'//div/a[@href= "/"]')
    # кнопка "выход" в ЛК
    logout_button_lk_page = (By.XPATH," //button[contains(text(),'Выход')]")
    # локатор раздела "булки" на главной
    bulki_buuton_main_page = (By.XPATH, "//span[contains(text(),'Булки')]/parent::*")
    # локатор раздела "соусы" на главной
    sous_button_main_page = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::*")
    # локатор раздела "начинки" на главной
    nachinki_button_main_page = (By.XPATH, "// span[contains(text(), 'Начинки')]/parent::*")
    # локатор h2 с текстом "Булки"
    bulki_h2_main_page = (By.XPATH,"//h2[contains(text(),'Булки')]")
    # локатор h2 с текстом "Соусы"
    sous_h2_main_page = (By.XPATH, "//h2[contains(text(),'Соусы')]")
    # локатор h2 с текстом "Начинки"
    nachinki_h2_main_page = (By.XPATH, "//h2[contains(text(),'Начинки')]")


