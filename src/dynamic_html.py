class DynamicHTML():
    def __init__(self,contentHTML) -> None:
        self.contentHTML = contentHTML
    def save_HTML(self,):
        with open('webpage/index.html','w') as f:
            f.writelines('<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>huythanh0x_college_scholarship</title><link rel="stylesheet" href="https://css.content-hci.com/study-cont/studyuk/css/client_main__13122022.css"/><link rel="stylesheet" type="text/css" href="https://css.content-hci.com/study-cont/studyuk/css/hc_course_finder__15112022.css"/><link rel="stylesheet" href="https://css.content-hci.com/study-cont/studyuk/css/hc_main_20092022.css" /> <link rel="stylesheet" href="https://css.content-hci.com/study-cont/studyuk/css/https/hc_embedded_objects_from_cdn_absolute_path__13072022.css"/></head><body><div style="max-width: 800px;margin: 0 auto; width: 80%;">')
            f.writelines(str(self.contentHTML))
            f.writelines('<div></body></html>')
