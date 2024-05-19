import re
from datetime import datetime, timedelta

class DataExtractor:
    @staticmethod
    def extract_date(article_date):
        return article_date

    @staticmethod
    def contains_money(text):
        money_pattern = r"\$\d+(?:,\d{3})*(?:\.\d{2})?|(?:\d+ )?(?:dollars|USD)"
        return bool(re.search(money_pattern, text))

    @staticmethod
    def count_search_phrases(text, search_phrase):
        return text.lower().count(search_phrase.lower())

    @staticmethod
    def filter_articles_by_date(articles, start_date, end_date):
        return [article for article in articles if start_date <= article['date'] <= end_date]
