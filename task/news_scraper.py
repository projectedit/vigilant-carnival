import os
from datetime import datetime, timedelta
from task.browser_handler import BrowserHandler
from task.data_extractor import DataExtractor
from task.file_handler import FileHandler
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NewsScraperBot:
    def __init__(self):
        self.browser_handler = BrowserHandler()
        self.data_extractor = DataExtractor()
        self.file_handler = FileHandler()


    def get_parameters(self):
        
        # try:
        #     self.work_items.get_input_work_item()
        #     params = self.work_items.get_work_item_variables()
        #     print(params)
        # except KeyError as e:
        #     logger.warning(f"Missing environment variable: {e}. Using local devdata/input.json for parameters.")

        # Simulate work item parameters for local testing
        
        import json
        with open('devdata/input.json') as f:
            params = json.load(f)
        
        self.search_phrase = params.get('search_phrase', 'technology')
        self.news_category = params.get('news_category', 'latest')
        self.months = int(params.get('months', 1))

    def scrape_news(self):
        url = "https://www.aljazeera.com/"
        self.browser_handler.open_browser(url)
        self.browser_handler.search_phrase(self.search_phrase)
        self.browser_handler.filter_category(self.news_category)

        end_date = datetime.now()
        start_date = end_date - timedelta(days=self.months * 30)

        articles_data = []
        article_elements = self.browser_handler.get_articles()
        for element in article_elements:
            title, date_str, description, image_url = self.browser_handler.get_article_details(element)
            article_date = self.data_extractor.extract_date(date_str)
            print(article_date)


            # image_filename = None
            # if image_url:
            #     image_filename = os.path.join("output", os.path.basename(image_url))
            #     self.file_handler.download_image(image_url, image_filename)

            articles_data.append({
                "title": title,
                "date": article_date,
                "description": description,
                "image_filename": image_url,
                "search_phrase_count": self.data_extractor.count_search_phrases(title, self.search_phrase) + self.data_extractor.count_search_phrases(description, self.search_phrase),
                "contains_money": self.data_extractor.contains_money(title) or self.data_extractor.contains_money(description)
            })

        self.browser_handler.close_browser()
        return articles_data

    def save_results(self, articles):
        output_file = os.path.join(os.getenv("ROBOT_ROOT", "."), "output", "news_data.xlsx")
        self.file_handler.save_to_excel(articles, output_file)


    def run(self):
        self.get_parameters()
        articles = self.scrape_news()
        self.save_results(articles)

