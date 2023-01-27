class DynamicHTML():
    def __init__(self, list_css_urls=[]) -> None:
        self.list_css_urls = list_css_urls

    def save_HTML(self, contentHTML):
        inserted_css_links = "".join(
            [f'<link rel="stylesheet" href="{url}">' for url in self.list_css_urls])
        with open('webpage/index.html', 'w') as f:
            f.writelines(
                f'<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>huythanh0x_college_scholarship</title>{inserted_css_links}</head><body><div style="max-width: 800px;margin: 0 auto; width: 80%;">')
            f.writelines(str(contentHTML))
            f.writelines('<div></body></html>')
