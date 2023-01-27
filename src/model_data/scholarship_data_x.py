class ScholarshipDataX():
    def __init__(self, scholarship_name, college_name, deadline, campus, course_starts, host_institution, level_field_of_study, number_of_scholarships, target_group, scholarship_value, eligibility, application_instructions, website) -> None:
        self.scholarship_name = scholarship_name
        self.college_name = college_name
        self.deadline = deadline
        self.campus = campus
        self.course_starts = course_starts
        self.host_institution = host_institution
        self.level_field_of_study = level_field_of_study
        self.number_of_scholarships = number_of_scholarships
        self.target_group = target_group
        self.scholarship_value = scholarship_value
        self.eligibility = eligibility
        self.application_instructions = application_instructions
        self.website = website

    def to_dict_object(self):
        return dict({"scholarship_name": self.scholarship_name, "college_name": self.college_name, "deadline": self.deadline, "campus": self.campus, "course_starts": self.course_starts, "host_institution": self.host_institution, "level_field_of_study": self.level_field_of_study, "number_of_scholarships": self.number_of_scholarships, "target_group": self.target_group, "scholarship_value": self.scholarship_value, "eligibility": self.eligibility, "application_instructions": self.application_instructions, "website": self.website})

    def __str__(self) -> str:
        return "|".join([self.scholarship_name, self.college_name, self.deadline, self.campus, self.course_starts, self.host_institution, self.level_field_of_study, self.number_of_scholarships, self.target_group, self.scholarship_value, self.eligibility, self.application_instructions, self.website])
