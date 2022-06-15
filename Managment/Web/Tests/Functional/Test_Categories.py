import time
import pytest
from Managment.Web.Utils.utils import Utilitis
from Managment.Web.Base.BasePage import Base
from Managment.Web.Pages.Categories_page import CategoriesPageFunc

@pytest.mark.usefixtures('connect_home_page')
class TestCategories(Base):
    """test 1"""
    def test_add_new_category_to_my_store_correctly(self):
        driver = self.driver
        #using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        #entering the categories page
        category.click_categories_navbar()

        #clicking on adding a category
        util.addBtn()
        time.sleep(2)
        driver.implicitly_wait(10)

        #insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name("גרב")
        driver.implicitly_wait(10)

        #insert department name
        category.insert_department_name("קוניאק")
        driver.implicitly_wait(10)

        #insert name field
        category.insert_field_name("גרב")
        driver.implicitly_wait(10)

        #select type
        category.type_option("טקסט")
        driver.implicitly_wait(10)

        #click on add
        category.click_on_category_add_button()
        time.sleep(3)
        driver.implicitly_wait(2)
        util.assertFunc(category.get_text_name(),"גרב")
        util.assertFunc(category.get_text_dep(),"קוניאק")

    """test 2"""
    def test_add_new_category_to_my_store_incorrectly_when_name_field_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        # util.connect_home_page()
        category = CategoriesPageFunc(driver)
        driver.implicitly_wait(10)

        # entering the categories page
        category.click_categories_navbar()
        time.sleep(3)
        driver.implicitly_wait(10)

        # clicking on adding a category
        util.addBtn()
        time.sleep(5)
        driver.implicitly_wait(10)

        # insert category name
        category.click_status_active_op()
        time.sleep(3)
        # category.insert_new_category_name("גרבר")
        driver.implicitly_wait(10)

        #insert department name
        category.insert_department_name("קוניאק")
        driver.implicitly_wait(10)

        # insert name field
        category.insert_field_name("גרבר")
        driver.implicitly_wait(10)

        # select type
        category.type_option("טקסט")
        driver.implicitly_wait(10)

        # click on add
        category.click_on_category_add_button()
        time.sleep(3)
        driver.implicitly_wait(2)
        util.assertFunc(category.get_required_message_name(),"נא למלא שדה זה")

    """test 3"""
    def test_add_new_category_to_my_store_incorrectly_when_category_field_null(self):

        driver = self.driver
        #using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        #entering the categories page
        category.click_categories_navbar()

        #clicking on adding a category
        time.sleep(2)
        util.addBtn()
        time.sleep(2)
        driver.implicitly_wait(10)

        #insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name("גרב")
        driver.implicitly_wait(10)

        #insert category name
        category.click_status_active_op()
        time.sleep(5)
        category.insert_new_category_name("גרב")

        # insert department name
        # category.insert_department_name("")

        #insert name field
        category.insert_field_name("גרב")

        #select type
        category.type_option("טקסט")

        #click on add
        category.click_on_category_add_button()
        category.click_none()
        driver.implicitly_wait(2)
        time.sleep(4)
        a = util.get_text("//div[contains(@class,'formItem_departmentIds')]//div[contains(@class,'form_note')][contains(text(),'נא למלא שדה זה')]")
        util.assertFunc(a,"נא למלא שדה זה")


    """test 4"""
    def test_add_new_category_to_my_store_incorrectly_when_second_name_field_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # entering the categories page
        category.click_categories_navbar()

        # clicking on adding a category
        util.addBtn()
        time.sleep(2)
        driver.implicitly_wait(10)

        # insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name("גרב")
        driver.implicitly_wait(10)

        # insert department name
        category.insert_department_name("קוניאק")
        # driver.implicitly_wait(10)

        # select type
        category.type_option("טקסט")
        time.sleep(5)
        # click on add
        category.click_on_category_add_button()
        time.sleep(7)
        driver.implicitly_wait(2)
        category.click_on_category_add_button()
        time.sleep(7)
        util.assertFunc(category.get_required_message_second_name_field() , "נא למלא שדה זה")

    """test 5"""
    def test_add_new_category_to_my_store_incorrectly_when_type_field_is_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # entering the categories page
        category.click_categories_navbar()

        # clicking on adding a category
        util.addBtn()
        time.sleep(2)
        driver.implicitly_wait(10)

        # insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.insert_new_category_name("גרב")
        driver.implicitly_wait(10)

        # insert department name
        category.insert_department_name("קוניאק")
        driver.implicitly_wait(10)

        # insert name field
        category.insert_field_name("גרב")
        driver.implicitly_wait(10)

        # # select type
        # category.type_option()
        time.sleep(3)

        # click on add
        category.click_on_category_add_button()
        time.sleep(5)
        util.assertFunc(util.valid_Message(category.type_field),"זהו שדה חובה.")

        """test 6"""
    def test_add_new_category_to_my_store_incorrectly_when_all_fields_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # entering the categories page
        category.click_categories_navbar()

        # clicking on adding a category
        util.addBtn()
        time.sleep(2)
        driver.implicitly_wait(10)

        # insert category name
        category.click_status_active_op()
        time.sleep(3)
        category.click_on_category_add_button()
        time.sleep(5)
        util.assertFunc(util.valid_Message(category.type_field), "זהו שדה חובה.")

        """test 7"""
    def test_add_new_category_to_my_store_incorrectly_when_category_is_exist_with_same_data(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)
        # entering the categories page
        category.click_categories_navbar()

        # clicking on adding a category
        util.addBtn()
        time.sleep(2)

        # insert category name
        category.click_status_active_op()
        time.sleep(3)

        category.insert_new_category_name("גרב")
        time.sleep(3)

        # insert department name
        category.insert_department_name("קוניאק")
        time.sleep(3)

        # insert name field
        category.insert_field_name("גרב")
        time.sleep(3)

        # select type
        category.type_option("טקסט")
        time.sleep(3)

        # click on add
        category.click_on_category_add_button()
        time.sleep(3)
        util.assertFunc(category.get_uniq_message(), "אחד או יותר מהשדות אינם ייחודיים")

        """test 8"""
    def test_search_for_specific_category_and_edit_a_category_correctly(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)

        category.click_status_active_op()
        time.sleep(3)

        # entering the categories page
        category.click_categories_navbar()
        time.sleep(5)

        #search for category
        category.search_category("שושי")
        time.sleep(5)

        category.click_indentify()
        time.sleep(5)

        # self.driver.find_element(By.XPATH,self.name_field).clear()
        category.insert_new_category_name("בובי")
        time.sleep(5)

        category.insert_field_name("בובי")
        time.sleep(5)
        category.type_option("טקסט")
        time.sleep(5)

        category.click_update_buttun()
        time.sleep(5)

        util.assertFunc(category.get_indentify(),"4jp555dl4dvbcra")

        """test 9"""
    def test_edit_category_incorrectly_when_type_field_null(self):
        driver = self.driver
        # using a func to connect the site
        util = Utilitis(driver)
        category = CategoriesPageFunc(driver)
        time.sleep(2)

        # entering the categories page
        category.click_categories_navbar()
        time.sleep(5)

        # search for category
        category.search_category("בובי")
        time.sleep(5)

        category.click_indentify()
        time.sleep(5)

        category.insert_new_category_name("סוכריה")
        time.sleep(5)

        category.insert_field_name("סוכריה")
        time.sleep(5)

        # category.type_option("טקסט")
        # time.sleep(5)

        category.click_update_buttun()
        time.sleep(5)

        util.assertFunc(util.valid_Message(category.type_field), "זהו שדה חובה.")
        # util.assertFunc(get_status(),"✓")































