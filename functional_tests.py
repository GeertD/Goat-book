import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_todo_list(self):
        # Edith checks out the new Todo app
        self.browser.get("http://localhost:8000")
        
        # She notices the page title
        self.assertIn("To-Do", self.browser.title)
        
        # She is invited to enter a to-do item
        self.fail("Finish the test!")

if __name__ == "__main__":
    unittest.main()