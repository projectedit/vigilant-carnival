from robocorp.tasks import task
from task.news_scraper import NewsScraperBot


@task
def main():

    bot = NewsScraperBot()
    bot.run()