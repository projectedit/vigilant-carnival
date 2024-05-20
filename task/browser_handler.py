from RPA.Browser.Selenium import Selenium, By

class BrowserHandler:
    def __init__(self):
        self.browser = Selenium()

    def open_browser(self, url):
        self.browser.open_available_browser(url)

    def search_phrase(self, phrase):

        try:
            self.browser.click_button('css=button.no-styles-button')
            self.browser.input_text('css=input.search-bar__input')
        except Exception :
            self.browser.click_button('css=button[data-testid="menu-trigger"]')
            self.browser.input_text('css=input[role="searchbox"]', 'technology')
        

        self.browser.press_keys('css=input[role="searchbox"]', 'ENTER')
        

    def filter_category(self, category):
        # Wait for the dropdown to be present
        self.browser.wait_until_element_is_visible('id=search-sort-option', timeout=10)
        
        # Select the sorting option by date
        self.browser.select_from_list_by_value('id=search-sort-option', 'date')
        try:
            self.browser.click_link("latest")
        except:
            print(f"Category latest not found. Proceeding without category filter.")

    def get_articles(self):
        self.browser.wait_until_page_contains_element("//div[@class='search-result__list']", timeout=30)

        # Get the search result list element
        return self.browser.find_elements("//div[@class='search-result__list']//article")
        

    def get_article_details(self, element):
        title = element.find_element(By.CSS_SELECTOR, '.gc__title').text
        date_str = element.find_element(By.CLASS_NAME, 'gc__meta').text
        description = element.find_element(By.CSS_SELECTOR, '.gc__excerpt').text
        image_url = element.find_element(By.CSS_SELECTOR, '.article-card__image').get_attribute('src')
        return title, date_str, description, image_url

    def close_browser(self):
        self.browser.close_browser()
