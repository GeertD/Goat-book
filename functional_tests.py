import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def tearDown(self):
        pass
        # self.browser.quit()
        
    def test_can_start_todo_list(self):
        # Edith checks out the new Todo app
        self.browser.get("http://localhost:8000")
        
        # She notices the page title and header
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)
        
        # She is invited to enter a to-do item
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")
        
        # She types "Buy peakcock feathers" into text box
        inputbox.send_keys("Buy peacock feathers")
        
        # She hits enter, page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in the to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(any(row.text == "1: Buy peacock feathers" for row in rows))
        
        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        self.fail("Finish the test!")
        
        # The page updates again, nowshows both items in the list
        
        

if __name__ == "__main__":
    unittest.main()