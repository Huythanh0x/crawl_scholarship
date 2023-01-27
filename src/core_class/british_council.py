import requests
from bs4 import BeautifulSoup as BeautfitulSoup
from helper_class.dynamic_html import DynamicHTML
from model_data.scholarship_data import ScholarshipData
import helper_class.file_helper as file_helper
from base_class.scholarship_extractor import ScholarShipExtractor


class BritishCouncil(ScholarShipExtractor):
    def __init__(self) -> None:
        self.BASE_URL = "https://search-study-uk.britishcouncil.org"
        self.SEACRH_ADDRESS = "/course/search-results.html?"
        self.SEARCH_PARAMETERS = "onlineFlag=Y&OnCampusNowFlag=Y&OnCampusLaterFlag=Y&"
        self.NUMBER_OF_PAGE = 3
        self.dynamic_html = DynamicHTML(["https://css.content-hci.com/study-cont/studyuk/css/client_main_24012023.css", "https://css.content-hci.com/study-cont/studyuk/css/hc_course_finder__15112022.css", "https://css.content-hci.com/study-cont/studyuk/css/hc_main_24012023.css", "https://images1.content-hci.com/study-cont/studyuk/img/clnt_imgs/favicons/favicons.ico", "https://css.content-hci.com/study-cont/studyuk/css/https/hc_embedded_objects_from_cdn_absolute_path__13072022.css"])
    def extract_data_from_html(self, html):
        list_scholarship_objects = []
        preview_image = html.find(
            "img", attrs={"name": "thumb-images"})['src'].strip().replace("\n", "")
        tab_wrp = html.find("div", {"class": "tab_wrp"})
        college_name = tab_wrp.find(
            "h2", attrs={"class": "univ_tit"}).get_text().strip().replace("\n", "")

        number_of_major_within_college = len(
            tab_wrp.find_all("div", attrs={"class": "rs_cnt"}))
        if "Show all matching" in tab_wrp.get_text():
            number_of_major_within_college -= 1
        for idx in range(number_of_major_within_college):
            data_container = tab_wrp.find_all(
                "div", attrs={"class": "rs_cnt"})[idx]
            major_name = data_container.find(
                "h3", attrs={"class": "crs_tit univ_tit"}).get_text().strip().replace("\n", "")
            is_on_campus = "Online study" not in data_container.find(
                "span", attrs={"class": "onl_tg_cam tag_End"}).get_text()
            preview_data = data_container.find("p").get_text(
            ).strip().replace("\n", "").replace("'", "")
            detailed_data_url = data_container.find("p").find(
                "a")['href'].strip().replace("\n", "")
            level_of_study, start_date, duration, study_mode, tuition_fees = [row.find(
                "span").get_text().strip().replace("\n", "") for row in data_container.find("div", attrs={"class": "tb_cl fl_w100"}).find_all("div", attrs={"class": "fl_w100"})]
            list_scholarship_objects.append(ScholarshipData(preview_image, college_name, major_name, is_on_campus,
                                                            preview_data, detailed_data_url, level_of_study, start_date, duration, study_mode, tuition_fees))
        return list_scholarship_objects

    def extract_raw_html_from_html(self, html):
        return html.find_all("div", attrs={"class": "sr_p brd_btm"})

    def main_extract_to_data_file(self):
        all_data_objects = []
        all_data_raw_html = []
        error_count = 0
        for page_index in range(1, self.NUMBER_OF_PAGE):
            print(f"INDEX PAGE = {page_index}")
            page_parameter = f"pageno={page_index}"
            r = requests.get(self.BASE_URL + self.SEACRH_ADDRESS +
                             self.SEARCH_PARAMETERS + page_parameter)
            soup = BeautfitulSoup(r.text)
            list_scholarships = self.extract_raw_html_from_html(soup)
            all_data_raw_html += list_scholarships
            for scholarship in list_scholarships:
                try:
                    list_data_objects = self.extract_data_from_html(
                        scholarship)
                    all_data_objects += list_data_objects
                except Exception as e:
                    print(e)
                    error_count += 1
        self.dynamic_html.save_HTML(all_data_raw_html,"british_council.html")
        file_helper.write_output_file(all_data_objects)
        print(f"ERROR COUNT {error_count}")