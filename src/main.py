import requests
from bs4 import BeautifulSoup as BeautfitulSoup
import dynamic_html
from scholarship_data import ScholarshipData
import file_helper as file_helper

BASE_URL = "https://search-study-uk.britishcouncil.org"
SEACRH_ADDRESS = "/course/search-results.html?"
SEARCH_PARAMETERS = "onlineFlag=Y&OnCampusNowFlag=Y&OnCampusLaterFlag=Y&"
NUMBER_OF_PAGE = 30

def extract_data_from_html(html: BeautfitulSoup):
    list_scholarship_objects = []
    preview_image = html.find("img", attrs={"name": "thumb-images"})['src'].strip().replace("\n","")
    tab_wrp = html.find("div", {"class": "tab_wrp"})
    college_name = tab_wrp.find("h2",attrs={"class":"univ_tit"}).get_text().strip().replace("\n","")

    number_of_major_within_college = len(
        tab_wrp.find_all("div", attrs={"class": "rs_cnt"}))
    if "Show all matching" in tab_wrp.get_text():
        number_of_major_within_college -= 1
    for idx in range(number_of_major_within_college):
        data_container = tab_wrp.find_all("div",attrs={"class":"rs_cnt"})[idx]
        major_name = data_container.find(
            "h3", attrs={"class": "crs_tit univ_tit"}).get_text().strip().replace("\n","")
        is_on_campus = "Online study" not in data_container.find(
            "span", attrs={"class": "onl_tg_cam tag_End"}).get_text()
        preview_data = data_container.find("p").get_text().strip().replace("\n","").replace("'","")
        detailed_data_url = data_container.find("p").find("a")['href'].strip().replace("\n","")
        level_of_study, start_date, duration, study_mode, tuition_fees = [row.find(
            "span").get_text().strip().replace("\n","") for row in data_container.find("div", attrs={"class": "tb_cl fl_w100"}).find_all("div", attrs={"class": "fl_w100"})]
        list_scholarship_objects.append(ScholarshipData(preview_image, college_name, major_name, is_on_campus,
                                       preview_data, detailed_data_url, level_of_study, start_date, duration, study_mode, tuition_fees))
    return list_scholarship_objects

def extract_raw_html_from_html(html):
    return html.find_all("div", attrs={"class": "sr_p brd_btm"})

def main_extract_to_data_file():
    all_data_objects = []
    all_data_raw_html = []
    error_count = 0
    for page_index in range(1,NUMBER_OF_PAGE):
        print(f"INDEX PAGE = {page_index}")
        page_parameter = f"pageno={page_index}"
        r = requests.get(BASE_URL + SEACRH_ADDRESS + SEARCH_PARAMETERS + page_parameter)
        soup = BeautfitulSoup(r.text)
        list_scholarships = soup.find_all("div", attrs={"class": "sr_p brd_btm"})
        all_data_raw_html += list_scholarships
        for scholarship in list_scholarships:
            try:
                list_data_objects = extract_data_from_html(scholarship)
                all_data_objects += list_data_objects
            except Exception as e: 
                print(e) 
                error_count += 1
    dynamic_html.DynamicHTML(all_data_raw_html).save_HTML()
    file_helper.write_output_file(all_data_objects)
    print(f"ERROR COUNT {error_count}")

def main_extract_to_webfile():
    all_data_objects = []
    error_count = 0
    for page_index in range(1,NUMBER_OF_PAGE):
        print(f"INDEX PAGE = {page_index}")
        page_parameter = f"pageno={page_index}"
        r = requests.get(BASE_URL + SEACRH_ADDRESS + SEARCH_PARAMETERS + page_parameter)
        soup = BeautfitulSoup(r.text)
        list_scholarships = soup.find_all("div", attrs={"class": "sr_p brd_btm"})
        all_data_objects += list_scholarships
    print(f"ERROR COUNT {error_count}")
    dynamic_html.DynamicHTML(all_data_objects).save_HTML()

# main_extract_to_data_file()
file_helper.write_data_to_excel()