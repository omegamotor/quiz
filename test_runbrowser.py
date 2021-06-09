import unittest
from selenium import webdriver
from django.test import TestCase
import time
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class MyTestCase(unittest.TestCase):

    def registerNewUser(self):
        fake = Faker()
        login = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password1')
        password2 = self.browser.find_element_by_id('id_password2')
        email = self.browser.find_element_by_id('id_email')
        button_register = self.browser.find_element_by_id('register_submit')

        new_user_login = fake.user_name()
        new_user_email = fake.email()
        new_user_password = 'TajneHasło123'

        login.send_keys(new_user_login)
        email.send_keys(new_user_email)
        password.send_keys(new_user_password)
        password2.send_keys(new_user_password)
        button_register.send_keys(Keys.ENTER)
        time.sleep(2)

        data = [new_user_login, new_user_password,  new_user_email]

        return data

    def addNewQuiz(self):
        fake = Faker()
        random_title = fake.sentence(3)
        random_description = fake.sentence(4)
        category = 'Historia'

        title = self.browser.find_element_by_id('id_title')
        Description = self.browser.find_element_by_id('id_description')
        ddelement = Select(self.browser.find_element_by_id('id_category'))
        ddelement.select_by_value('6')
        button_create_quiz = self.browser.find_element_by_id('add-quiz-button')

        title.send_keys(random_title)
        Description.send_keys(random_description)
        button_create_quiz.send_keys(Keys.ENTER)
        time.sleep(2)

        data = [random_title, random_description, category]
        return data

    def addQuestion(self):
        title = self.browser.find_element_by_id('id_title')
        correct_answer = self.browser.find_element_by_id('id_correct_answer')
        id_answerA = self.browser.find_element_by_id('id_answerA')
        id_answerB = self.browser.find_element_by_id('id_answerB')
        id_answerC = self.browser.find_element_by_id('id_answerC')
        button_add_question = self.browser.find_element_by_id('add-question')

        title.send_keys('Nowe pytanie')
        correct_answer.send_keys('prawidłowa odpowidź')
        id_answerA.send_keys('Odpowiedź A')
        id_answerB.send_keys('Odpowiedź B')
        id_answerC.send_keys('Odpowiedź C')

        button_add_question.send_keys(Keys.ENTER)
        time.sleep(2)

        data = [title, correct_answer, id_answerA, id_answerB, id_answerC]

        return data

    def login(self, user_login='admin', user_password='admin'):

        login = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        button_login = self.browser.find_element_by_id('submit_login')

        login.send_keys(user_login)
        password.send_keys(user_password)
        button_login.send_keys(Keys.ENTER)
        time.sleep(2)

        data = [user_login, user_password]

        return data

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'C:\Users\Robert\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.exe')

    # def test_nav_elements(self):
    #     self.assertEqual(True, True)

    def test_home_page_title(self):
        self.browser.get('http://localhost:8000')
        self.header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Najnowsze Quizy', self.header_text)

    def test_category_page_title(self):
        self.browser.get('http://localhost:8000/category')
        self.header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Kategorie', self.header_text)

    def test_ranking_page_title(self):
        self.browser.get('http://localhost:8000/ranking')
        self.header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Ranking użytkowników', self.header_text)

    def test_footer_title(self):
        self.browser.get('http://localhost:8000/')
        self.footer = self.browser.find_element_by_class_name('container-fluid').text
        self.assertIn('Quizy XYZ', self.footer)

    # Logowanie
    def test_login(self):
        self.browser.get('http://localhost:8000/login/')
        self.login()
        self.header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Najnowsze Quizy', self.header_text)

    def test_login_bad_password(self):
        self.browser.get('http://localhost:8000/login/')

        login = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        button_login = self.browser.find_element_by_id('submit_login')

        login.send_keys('admin')
        password.send_keys('ad')
        button_login.send_keys(Keys.ENTER)
        time.sleep(2)

        self.header_text = self.browser.find_elements_by_class_name('alert-danger')[0].find_element_by_tag_name('li').text

        self.assertIn('Wprowadź poprawne wartości pól użytkownik oraz hasło. Uwaga: wielkość liter ma znaczenie.', self.header_text)

    # Wylogowywanie
    def test_logout(self):
        self.browser.get('http://localhost:8000/login/')
        self.login()
        self.header_text = self.browser.find_element_by_link_text('Wyloguj').click()
        self.header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Zostałeś Wylogowany', self.header_text)

    # Rejestracja
    def test_register(self):
            self.browser.get('http://localhost:8000/register/')
            self.registerNewUser()
            self.header_text = self.browser.find_elements_by_class_name('alert-success')[0]
            self.assertIn('Konto zostało utworzone', self.header_text.text)# Rejestracja

    def test_register_too_short_password(self):
            self.browser.get('http://localhost:8000/register/')

            fake = Faker()
            login = self.browser.find_element_by_id('id_username')
            password = self.browser.find_element_by_id('id_password1')
            password2 = self.browser.find_element_by_id('id_password2')
            email = self.browser.find_element_by_id('id_email')
            button_register = self.browser.find_element_by_id('register_submit')

            new_user_login = fake.user_name()
            new_user_email = fake.email()
            new_user_password = 'Ta123'

            login.send_keys(new_user_login)
            email.send_keys(new_user_email)
            password.send_keys(new_user_password)
            password2.send_keys(new_user_password)
            button_register.send_keys(Keys.ENTER)
            time.sleep(2)

            self.header_text = self.browser.find_element_by_id('error_1_id_password2').find_element_by_tag_name('strong')
            self.assertIn('To hasło jest za krótkie. Musi zawierać co najmniej 8 znaków.', self.header_text.text)

    # dodawanie Quizu z 1 pytaniem
    def test_add_quiz(self):
            self.browser.get('http://localhost:8000/login/')
            self.login()

            self.header_text = self.browser.find_element_by_link_text('Dodaj Quiz').click()
            time.sleep(2)

            new_quiz = self.addNewQuiz()
            quiz_title = new_quiz[0]
            self.addQuestion()

            # self.header_text = self.browser.find_element_by_link_text('Strona główna').click()
            # time.sleep(2)

            self.header_text = self.browser.find_element_by_link_text('Home').click()
            time.sleep(2)

            self.header_text = self.browser.find_element_by_link_text(quiz_title).click()
            time.sleep(2)

            self.header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn(quiz_title, self.header_text)

    def test_question_in_quiz(self):
        self.browser.get('http://localhost:8000/login/')
        self.login()

        self.header_text = self.browser.find_element_by_link_text('Dodaj Quiz').click()
        time.sleep(2)
        new_quiz = self.addNewQuiz()
        quiz_title = new_quiz[0]

        question_data = self.addQuestion()

        self.header_text = self.browser.find_element_by_link_text(quiz_title).click()
        time.sleep(2)

        self.header_text = self.browser.find_element_by_tag_name('h5').text
        self.assertIn(question_data[0], self.header_text)

    def test_quiz_in_category(self):
        self.browser.get('http://localhost:8000/login/')
        self.login()
        time.sleep(2)

        self.browser.find_element_by_link_text('Dodaj Quiz').click()
        time.sleep(2)

        new_quiz = self.addNewQuiz()
        quiz_title = new_quiz[0]
        quiz_category = new_quiz[2]
        self.addQuestion()

        self.browser.find_element_by_link_text('Kategorie').click()
        time.sleep(2)

        self.browser.find_element_by_link_text(quiz_category).click()
        time.sleep(2)

        self.last_quiz_in_category = self.browser.find_elements_by_class_name('card-text')[-1].text
        self.assertIn(quiz_title, self.last_quiz_in_category)

    def test_quiz_author(self):
        self.browser.get('http://localhost:8000/login/')
        self.user = self.login()[0]
        time.sleep(2)

        self.browser.find_element_by_link_text('Dodaj Quiz').click()
        time.sleep(2)

        new_quiz = self.addNewQuiz()
        quiz_title = new_quiz[0]
        quiz_category = new_quiz[2]
        self.addQuestion()

        self.browser.find_element_by_link_text('Home').click()
        time.sleep(2)

        self.browser.find_element_by_link_text(quiz_title).click()
        time.sleep(2)

        self.author = self.browser.find_element_by_id('author').text
        self.assertIn(self.user, self.author)

    def test_profile_user_name(self):
        self.browser.get('http://localhost:8000/register/')
        new_user = self.registerNewUser()

        self.header_text = self.browser.find_element_by_link_text('Zaloguj').click()
        time.sleep(2)
        self.login(new_user[0], new_user[1])

        self.header_text = self.browser.find_element_by_link_text('Profil').click()
        time.sleep(2)

        self.header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn(new_user[0], self.header_text)

    def test_profile_email(self):
        self.browser.get('http://localhost:8000/register/')
        new_user = self.registerNewUser()

        self.header_text = self.browser.find_element_by_link_text('Zaloguj').click()
        time.sleep(2)
        self.login(new_user[0], new_user[1])

        self.header_text = self.browser.find_element_by_link_text('Profil').click()
        time.sleep(2)

        self.header_text = self.browser.find_element_by_id('email').text
        self.assertIn(new_user[3], self.header_text)

    def test_user_rename(self):
        self.browser.get('http://localhost:8000/register/')
        register_user = self.registerNewUser()

        self.browser.find_element_by_link_text('Zaloguj').click()
        time.sleep(2)
        self.login(register_user[0], register_user[1])
        time.sleep(2)

        self.browser.find_element_by_link_text('Profil').click()
        time.sleep(2)

        login = self.browser.find_element_by_id('id_username')
        button_login = self.browser.find_element_by_id('profile-button')

        faker = Faker()
        new_username = faker.user_name()

        login.send_keys(new_username)
        button_login.send_keys(Keys.ENTER)
        time.sleep(2)

        self.old_username = self.browser.find_element_by_id('username').text
        self.assertIn(new_username, self.old_username)




    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    unittest.main()






















