import os
from RPA.Excel.Files import Files
from RPA.HTTP import HTTP

class FileHandler:
    def __init__(self):
        self.excel = Files()
        self.http = HTTP()

    def download_image(self, url, save_path):
        response = self.http.download(url, target_file=save_path)
        return save_path if response else None

    def save_to_excel(self, articles, output_path):
        self.excel.create_workbook(output_path)
        self.excel.append_rows_to_worksheet(articles, header=True)
        self.excel.save_workbook()
