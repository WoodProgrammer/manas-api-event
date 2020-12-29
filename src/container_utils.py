import logging


def check_image(image_name, allowed_list):
    try:
        split_str = image_name.split("/")
        status = any(map(lambda x: x in split_str[0], allowed_list))
    except Exception as exp:
        logging.warning(exp)
        return False
    return status


def get_allowed_list():
    with open("/opt/allowed.repo_list", "r") as repos:
        repo_list = repos.read().splitlines()
    return list(repo_list)

