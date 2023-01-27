import requests
from bs4 import BeautifulSoup as BeautfitulSoup
from helper_class.dynamic_html import DynamicHTML
from model_data.scholarship_data_x import ScholarshipDataX
import helper_class.file_helper as file_helper
from base_class.scholarship_extractor import ScholarShipExtractor


class Scholars4Dev(ScholarShipExtractor):
    def __init__(self) -> None:
        self.BASE_URL = "https://www.scholars4dev.com"
        self.SEACRH_ADDRESS = "/category/country/europe-scholarships/uk-scholarships"
        self.SEARCH_PARAMETERS = ""
        self.NUMBER_OF_PAGE = 16
        self.dynamic_html = DynamicHTML(["https://css.content-hci.com/study-cont/studyuk/css/client_main__13122022.css", "https://css.content-hci.com/study-cont/studyuk/css/hc_course_finder__15112022.css",
                                        "https://css.content-hci.com/study-cont/studyuk/css/hc_main_20092022.css", "https://css.content-hci.com/study-cont/studyuk/css/https/hc_embedded_objects_from_cdn_absolute_path__13072022.css"])

    def extract_data_from_html(self, html):
        list_scholarship_objects = []

        detailed_url = html.find("h2").find("a")['href']
        detail_html = BeautfitulSoup(requests.get(
            detailed_url).text, features="lxml")
        entry_clearfix = detail_html.find(
            "div", attrs={"class": "entry clearfix"})

        scholarship_name, college_name, deadline, campus, course_starts, host_institution, level_field_of_study, number_of_scholarships, target_group, scholarship_value, eligibility, application_instructions, website = "", "", "", "", "", "", "", "", "", "", "", "", ""
        # html.find("", attrs={"": ""})
        scholarship_name = detail_html.find("h1").get_text(strip=True).replace("\n","")
        list_paragraphs = entry_clearfix.find_all("p")
        for idx, value in enumerate(list_paragraphs):
            if ("University" in value.get_text() or "Universities" in value.get_text()) and college_name == "":
                college_name = value.get_text(strip=True).replace("\n","")
            elif "Deadline" in value.get_text():
                deadline = value.get_text(strip=True).replace("\n","").split("Study in:")[0]
                campus = value.get_text(strip=True).replace("\n","").split("Study in:")[1].split("Course starts ")[0].replace("\u00a0","").strip()
                course_starts = value.get_text(strip=True).replace("\n","").split("Course starts ")[1]
            elif "Host Institution" in value.get_text():
                host_institution = list_paragraphs[idx+1].get_text(strip=True).replace("\n","")
            
            
            elif "Number of Scholarships" in value.get_text():
                number_of_scholarships = list_paragraphs[idx+1].get_text(strip=True)
            elif "Field of study" in value.get_text() or " of Study" in value.get_text() or " of study" in value.get_text():
                level_field_of_study = list_paragraphs[idx +
                                                       1].get_text(strip=True).replace("\n","")
            elif "Target group" in value.get_text():
                target_group = list_paragraphs[idx+1].get_text(strip=True).replace("\n","")
            elif "Scholarship value" in value.get_text():
                scholarship_value = list_paragraphs[idx+1].get_text(strip=True).replace("\n","")

            elif "Eligibility:" in value.get_text():
                eligibility = list_paragraphs[idx+1].get_text(strip=True).replace("\n","") + list_paragraphs[idx+2].get_text(strip=True).replace("\n","")

            elif "Application instructions:" in value.get_text():
                application_instructions = list_paragraphs[idx+1].get_text(strip=True).replace("\n","")

            elif "Website" in value.get_text():
                website = list_paragraphs[idx].get_text(strip=True).replace("\n","")

        list_ems = entry_clearfix.find_all("em")
        for idx, value in enumerate(list_ems):
            print(idx,value.get_text())
        
        
        return [ScholarshipDataX(scholarship_name, college_name, deadline, campus, course_starts, host_institution, level_field_of_study, number_of_scholarships, target_group, scholarship_value, eligibility, application_instructions, website)]

    def extract_raw_html_from_html(self, html):
        return html.find_all("div", attrs={"class": "post clearfix"})

    def main_extract_to_data_file(self):
        all_data_objects = []
        all_data_raw_html = []
        error_count = 0
        for page_index in range(1, self.NUMBER_OF_PAGE):
            print(f"INDEX PAGE = {page_index}")
            page_parameter = f"/page/{page_index}"
            r = requests.get(self.BASE_URL + self.SEACRH_ADDRESS +
                             self.SEARCH_PARAMETERS + page_parameter)
            soup = BeautfitulSoup(r.text, features="lxml")
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
                    # raise e
        self.dynamic_html.save_HTML(all_data_raw_html,"scholars4dev.html")
        file_helper.write_output_file(all_data_objects)
        print(f"ERROR COUNT {error_count}")
