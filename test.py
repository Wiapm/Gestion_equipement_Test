from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

# Instancier le navigateur web
driver = webdriver.Chrome()

# Ouvrir l'URL de votre page
driver.get("http://127.0.0.1:8000/")
time.sleep(2)

# Rechercher à nouveau le bouton après le survol
button_element = driver.find_element(By.XPATH, "//span[@class='navlink' and contains(text(), 'Superviseur')]")

# Utiliser ActionChains pour effectuer un survol sur l'élément
actions = ActionChains(driver)
actions.move_to_element(button_element).perform()

# Attendre que le bouton soit cliquable
wait = WebDriverWait(driver, 10)
button_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='navlink' and contains(text(), 'Superviseur')]")))

# Cliquer sur le bouton en utilisant JavaScript
driver.execute_script("arguments[0].click();", button_element)

# Attendre quelques secondes pour voir l'apparence
time.sleep(2)


time.sleep(0.2)
# Find the search box input by its CSS selector
search_box = driver.find_element(By.CSS_SELECTOR, "input.form-control.input_user")

# Type "admin" into the search box
search_text = "admin"
for char in search_text:
    search_box.send_keys(char)
    time.sleep(0.2)  # Add a delay of 0.2 seconds between each character

# Find the password input by its CSS selector
password_input = driver.find_element(By.CSS_SELECTOR, "input.form-control.input_pass[type='password']")

# Type "admin" into the password input box
password_text = "aaa"
for char in password_text:
    password_input.send_keys(char)
    time.sleep(0.2)  # Add a delay of 0.2 seconds between each character

# Find the submit button by its CSS selector
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# Click on the submit button to perform the login action
submit_button.click()

# Wait for some time to observe the results after clicking the submit button
time.sleep(1)  # Adjust the sleep time as needed


eyedropper_icon = driver.find_element(By.CLASS_NAME, "bx.bxs-eyedropper")

# Perform a hover action on the "bx bxs-eyedropper" element
actions = ActionChains(driver)
actions.move_to_element(eyedropper_icon).perform()

# Wait for some time to observe the results after performing the hover action
time.sleep(1)

# Find the element with class "fas fa-flask icon-lab"
flask_icon = driver.find_element(By.CLASS_NAME, "fas.fa-flask.icon-lab")

# Perform a hover action on the "fas fa-flask icon-lab" element
actions = ActionChains(driver)
actions.move_to_element(flask_icon).perform()

# Wait for some time to observe the results after performing the hover action

# Click on the search box icon to activate it
time.sleep(1)

# Click on the search box icon to activate it
time.sleep(1)
search_bar = driver.find_element(By.CSS_SELECTOR, ".bx.bx-chevron-right.toggle")
time.sleep(1)
search_bar.click()
time.sleep(1)



# Find the search box input by its CSS selector
search_box = driver.find_element(By.CSS_SELECTOR, ".search-box input[name='Marque']")

search_box.clear()

# Slowly type "Test_PCR" into the search box
search_text = "UMP-ENSA"
for char in search_text:
    search_box.send_keys(char)
    time.sleep(0.2)  # Add a delay of 0.2 seconds between each character

# Press the Enter key to perform the search
search_box.send_keys(Keys.ENTER)

# Wait for some time to observe the search results (you may adjust the sleep time as needed)
time.sleep(1)

# Click on the search box icon to activate it again
search_bar = driver.find_element(By.CSS_SELECTOR, ".bx.bx-chevron-right.toggle")
search_bar.click()

time.sleep(1)

# Find the search box input by its CSS selector
search_box = driver.find_element(By.CSS_SELECTOR, ".search-box input[name='Marque']")

search_box.clear()

# Slowly type "GMSR fS-chimie" into the search box
search_text = "GMS"
for char in search_text:
    search_box.send_keys(char)
    time.sleep(0.2)  # Add a delay of 0.2 seconds between each character

# Press the Enter key to perform the search
search_box.send_keys(Keys.ENTER)

# Wait for some time to observe the search results (you may adjust the sleep time as needed)
time.sleep(1)

# Click on the search box icon to activate it again
search_bar = driver.find_element(By.CSS_SELECTOR, ".bx.bx-chevron-right.toggle")
search_bar.click()

# Wait for some time to observe the search results (you may adjust the sleep time as needed)
time.sleep(1)

# Find the element with class "bx-home-alt"
home_icon = driver.find_element(By.CLASS_NAME, "bx-home-alt")

# Perform a hover action on the "bx-home-alt" element
actions = ActionChains(driver)
actions.move_to_element(home_icon).perform()

home_icon = driver.find_element(By.CLASS_NAME, "bx-home-alt")
home_icon.click()

# Wait for some time to observe the results after performing the hover action
time.sleep(1)



# Click on the search box icon to activate it again
search_bar = driver.find_element(By.CSS_SELECTOR, ".bx.bx-chevron-right.toggle")
search_bar.click()

time.sleep(1)

# Find the element with class "bx bx-bar-chart-alt-2 icon"
bar_chart_button = driver.find_element(By.CLASS_NAME, "bx.bx-bar-chart-alt-2.icon")

# Perform a hover action on the button
actions = ActionChains(driver)
actions.move_to_element(bar_chart_button).perform()

# Wait for some time to observe the results after performing the hover action

# Click on the button
bar_chart_button.click()

# Wait for some time to observe the results after performing the hover action

# ...


# Find the delete button by its CSS selector
delete_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-danger[href='/supprimer_equipement/4']")

# Wait for some time before clicking the delete button
time.sleep(1)  # Adjust the sleep time as needed (2 seconds in this example)

# Perform a "hover" on the delete button before clicking it
actions = ActionChains(driver)
actions.move_to_element(delete_button).perform()

# Wait for some time to observe the "hover"
time.sleep(1)  # Adjust the sleep time as needed (1 second in this example)

# Click on the delete button
delete_button.click()

# Wait for some time to observe the results after clicking the button
# ...
time.sleep(1)

# Find the "Annuler" button by its CSS selector
annuler_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-warning[href='/showEquipement/']")

# Wait for some time before clicking the "Annuler" button
time.sleep(2)  # Adjust the sleep time as needed (2 seconds in this example)

# Perform a "hover" on the "Annuler" button before clicking it
actions = ActionChains(driver)
actions.move_to_element(annuler_button).perform()

# Wait for some time to observe the "hover"
time.sleep(1)  # Adjust the sleep time as needed (1 second in this example)

# Click on the "Annuler" button
annuler_button.click()

# Wait for some time to observe the results after clicking the "Annuler" button
time.sleep(1)  # Adjust the sleep time as needed (2 seconds in this example)


# Find the delete button by its CSS selector
delete_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-danger[href='/supprimer_equipement/4']")

# Wait for some time before clicking the delete button
time.sleep(2)  # Adjust the sleep time as needed (2 seconds in this example)

# Perform a "hover" on the delete button before clicking it
actions = ActionChains(driver)
actions.move_to_element(delete_button).perform()

# Wait for some time to observe the "hover"
time.sleep(1)  # Adjust the sleep time as needed (1 second in this example)

# Click on the delete button
delete_button.click()

# Wait for some time to observe the results after clicking the button
# ...
time.sleep(1)




# Find the "Confirmer" button by its CSS selector
confirmer_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-danger[type='submit'][value='Confirmer']")

# Wait for some time before clicking the "Confirmer" button
time.sleep(1)  

# Perform a "hover" on the "Confirmer" button before clicking it
actions = ActionChains(driver)
actions.move_to_element(confirmer_button).perform()

# Wait for some time to observe the "hover"
time.sleep(1)  # Adjust the sleep time as needed (1 second in this example)

# Click on the "Confirmer" button
confirmer_button.click()

# Wait for some time to observe the results after clicking the "Confirmer" button
time.sleep(1)  # Adjust the sleep time as needed (2 seconds in this example)




modify_button_selector = "a.btn.btn-primary[href='/equipements/17/modifier/']"

# Trouver le bouton "Modifier" par le sélecteur CSS
modify_button = driver.find_element(By.CSS_SELECTOR, modify_button_selector)

# Effectuer un survol sur le bouton "Modifier"
actions = ActionChains(driver)
actions.move_to_element(modify_button).perform()

# Attendre quelques secondes pour voir l'apparence après le "hover"
time.sleep(1)

# Cliquer sur le bouton "Modifier" après le "hover"
modify_button.click()

# Attendre quelques secondes pour observer les résultats après le clic
time.sleep(1)
modifier_button = driver.find_element(By.CSS_SELECTOR, "button.btn-save")

# Cliquer sur le bouton "Modifier"
modifier_button.click()


time.sleep(1)

# Localiser l'élément à l'aide du sélecteur CSS
ajout_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary[href='/ajouter/']")

# Utiliser execute_script() pour cliquer sur l'élément
driver.execute_script("arguments[0].click();", ajout_button)

time.sleep(1)

driver.find_element(By.ID, "id_Reference").send_keys("15")
driver.find_element(By.ID, "id_Etat").send_keys("Installé")
driver.find_element(By.ID, "id_Marque").send_keys("Test_PCR")
driver.find_element(By.ID, "id_Laboratoire").send_keys("Date_Acquisition")
driver.find_element(By.ID, "id_Categorie").send_keys("Chimie")

# Attendre quelques secondes pour voir les données remplies
time.sleep(1)

# Cliquer sur le bouton "Ajouter"
ajouter_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Ajouter')]")
ajouter_button.click()

time.sleep(1)


# Click on the search box icon to activate it again
search_bar = driver.find_element(By.CSS_SELECTOR, ".bx.bx-chevron-right.toggle")
search_bar.click()



time.sleep(1)

# Localiser l'icône de la cloche en utilisant un sélecteur CSS
bell_icon = driver.find_element(By.CSS_SELECTOR, "i.bx.bx-bell.icon")

# Effectuer un survol sur l'icône de la cloche
actions = ActionChains(driver)
actions.move_to_element(bell_icon).perform()

# Attendre quelques secondes pour que le survol soit visible
time.sleep(1)

# Cliquer sur l'icône de la cloche après le survol
bell_icon.click()

# Attendre quelques secondes pour voir le résultat après le clic
time.sleep(1)




# Click on the search box icon to activate it again
search_bar = driver.find_element(By.CSS_SELECTOR, ".bx.bx-chevron-right.toggle")
search_bar.click()

time.sleep(1)



logout_icon = driver.find_element(By.CSS_SELECTOR, "i.bx.bx-log-out.icon")

# Effectuer un survol sur l'icône de déconnexion
actions = ActionChains(driver)
actions.move_to_element(logout_icon).perform()
time.sleep(1)
logout_icon.click()
time.sleep(1)

icon_element = driver.find_element(By.CSS_SELECTOR, "i.bx.bxs-arrow-from-right")
icon_element.click()


# Localiser le bouton en utilisant un sélecteur CSS
button_element = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary[href='/Visiteur/contact_laboratoire/14/']")

# Créer une instance de la classe ActionChains pour effectuer un survol
actions = ActionChains(driver)
actions.move_to_element(button_element).perform()

# Attendre quelques secondes pour afficher le résultat du survol
time.sleep(2)

# Cliquer sur le bouton
button_element.click()

time.sleep(0.2)
# Find the search box input by its CSS selector
search_box = driver.find_element(By.CSS_SELECTOR, "input.form-control.input_user")

# Type "admin" into the search box
search_text = "soso"
for char in search_text:
    search_box.send_keys(char)
    time.sleep(0.2)  # Add a delay of 0.2 seconds between each character

# Find the password input by its CSS selector
password_input = driver.find_element(By.CSS_SELECTOR, "input.form-control.input_pass[type='password']")

# Type "admin" into the password input box
password_text = "laarabi123"
for char in password_text:
    password_input.send_keys(char)
    time.sleep(0.2)  # Add a delay of 0.2 seconds between each character

# Find the submit button by its CSS selector
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# Click on the submit button to perform the login action
submit_button.click()

button_element = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary[href='/Visiteur/contact_laboratoire/14/']")
button_element.click()
time.sleep(3)
nom_input = driver.find_element(By.ID, "id_nom")
nom_input.clear()  # Effacer le contenu actuel du champ
nom_input.send_keys("wiam")
time.sleep(1)
# Remplir le champ "Votre adresse e-mail" avec "wiamstudy@gmail.com"
email_input = driver.find_element(By.ID, "id_email")
email_input.clear()  # Effacer le contenu actuel du champ
email_input.send_keys("wiamstudy@gmail.com")

# Cliquer sur le bouton "Envoyer"
envoyer_button = driver.find_element(By.CLASS_NAME, "custom-button")
envoyer_button.click()

# Attendre quelques secondes pour voir le résultat après le clic
time.sleep(6)












time.sleep(5000)

