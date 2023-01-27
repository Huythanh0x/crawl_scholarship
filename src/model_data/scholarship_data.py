class ScholarshipData():
    def __init__(self, preview_image, college_name, major_name, is_on_campus, preview_data, detailed_info_url, level_of_study, start_date, duration, study_mode, tutition_fees) -> None:
        self.preview_image = preview_image
        self.college_name = college_name
        self.major_name = major_name
        self.is_on_campus = is_on_campus
        self.preview_data = preview_data
        self.detailed_info_url = detailed_info_url
        self.level_of_study = level_of_study
        self.start_date = start_date
        self.duration = duration
        self.study_mode = study_mode
        self.tutition_fees = tutition_fees

    def to_dict_object(self):
        return dict({"preview_image": self.preview_image, "college_name": self.college_name, "major_name": self.major_name, "is_on_campus": self.is_on_campus, "preview_data": self.preview_data, "level_of_study": self.level_of_study, "start_date": self.start_date, "duration": self.duration, "study_mode": self.study_mode, "tutition_free": self.tutition_fees, "detailed_info_url": self.detailed_info_url})

    def __str__(self) -> str:
        return "|".join([self.preview_image, self.college_name, self.major_name, str(self.is_on_campus), self.preview_data, self.detailed_info_url, self.level_of_study, self.start_date, self.duration, self.study_mode, self.tutition_fees])
