import json
import pandas

def write_output_file(list_data_objects):
    write_data_to_csv(list_data_objects)
    write_data_to_json(list_data_objects)
    write_data_to_excel()
    
def write_data_to_json(list_data_objects):
    list_data_objects = [o.to_dict_object() for o in  list_data_objects]
    list_data_objects = [
        data_object for data_object in list_data_objects if data_object != None]
    with open("output/scholarship.json", "w") as f:
        f.writelines(json.dumps(
            {"update_time": "XXX", "results": list_data_objects}, indent=2))

def write_data_to_csv(list_data_objects):
    with open('output/scholarship.csv', 'w') as f:
        f.writelines("preview_image|college_name|major_name|is_on_campus|preview_data|detailed_data_url|level_of_study|start_date|duration|study_mode|tuition_fees")
    with open('output/scholarship.csv', 'w') as f:
        f.writelines("\n".join([str(o) for o in list_data_objects]))

def write_data_to_excel():
    pandas.read_csv('output/scholarship.csv',sep="|",header=0,low_memory=False,nrows=300).to_excel('output/schorlarship.xlsx')