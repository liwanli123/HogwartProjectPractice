import pytest
import yaml


def get_data(file):
    if not '.yaml' in file:
        file += '.yaml'
    with open(f"../data/{file}", encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
    return yaml_data


def get_contact():
    res = get_data("contact")
    return res

