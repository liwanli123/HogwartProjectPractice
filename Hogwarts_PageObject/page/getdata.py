import yaml


def get_data(file):
    with open(file, encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
    return yaml_data


def get_employee_one():
    res = get_data("../data/one_emp.yaml")
    return res

def get_otherdepar():
    res = get_data("../data/other_depar.yaml")
    return res


def get_employee():
    res = get_data("../data/employee.yaml")
    return res


def get_department():
    res = get_data("../data/department.yaml")
    return res
