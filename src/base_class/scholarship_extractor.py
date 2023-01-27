from abc import abstractmethod


class ScholarShipExtractor():
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def extract_raw_html_from_html(self):
        pass

    @abstractmethod
    def main_extract_to_data_file(self):
        pass

    @abstractmethod
    def extract_data_from_html(self):
        pass
