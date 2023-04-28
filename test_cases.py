from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_success(driver):
    login(driver,"Admin","admin123")
    assert "Dashboard" in driver.find_element(By.CLASS_NAME,"oxd-topbar-header-title").text
    logout(driver)

def test_login_falied(driver):
    login(driver,"Admin","admin13")
    assert "Invalid credentials" in driver.find_element(By.CLASS_NAME, "oxd-alert-content-text").text

def test_logout(driver):
    login(driver,"Admin","admin123")
    logout(driver)
    assert "Login" in driver.find_element(By.CLASS_NAME, "orangehrm-login-title").text

def test_addEmployee(driver):
    login(driver,"Admin","admin123")
    # click PIM
    clickComponent(driver,"https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index","/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
    # click +Add
    clickComponent(driver,"https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList","/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
    addEmployee_basicDetails(driver)

def test_editEmployee(driver):
    login(driver,"Admin","admin123")
    # click PIM
    clickComponent(driver,"https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index","/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
    # click +edit
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    menu_component = driver.find_element(By.XPATH,"(//button[@class='oxd-icon-button oxd-table-cell-action-space'])[2]")
    menu_component.click()
    emp_id_edit = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input")
    emp_id_edit.send_keys("emp12")
    save = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button")
    save.click()
    # addEmployee_basicDetails(driver)
    time.sleep(5)

def test_deleteEmployee(driver):
    login(driver,"Admin","admin123")
    # click PIM
    clickComponent(driver,"https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index","/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
    # //button[@class='oxd-icon-button oxd-table-cell-action-space'][1]
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    menu_component = driver.find_element(By.XPATH,"(//button[@class='oxd-icon-button oxd-table-cell-action-space'])[1]")
    menu_component.click()
    delete = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")
    delete.click()
    time.sleep(5)



def addEmployee_basicDetails(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
    firstname_field = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input")
    middlename_field = driver.find_element(By.NAME, "middleName")
    lastname_field = driver.find_element(By.NAME, "lastName")
    emp_id = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input")
    firstname_field.send_keys("FirstNameTest")
    middlename_field.send_keys("middleNameTest")
    lastname_field.send_keys("LastNameTest")
    emp_id.send_keys("emp12")
    menu_component = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")
    menu_component.click()
    time.sleep(5)

def clickComponent(driver,url,fullXpath):
    driver.get(url)
    menu_component = driver.find_element(By.XPATH,fullXpath)
    menu_component.click()

def login(driver,username,password):
     # Load the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Find the username and password fields and enter the credentials
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Find and click the login button
    login_button = driver.find_element(By.CLASS_NAME, "oxd-button")
    login_button.click()

def logout(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    # Find the dropdown menu and click it
    dropdown_menu = driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab")
    dropdown_menu.click()

    # Find the logout button and click it
    logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Logout')]")))
    logout_button.click()
