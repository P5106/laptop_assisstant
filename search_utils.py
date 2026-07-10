import os
import difflib
from config import SEARCH_FOLDERS, START_MENU_FOLDERS, APP_SEARCH_FOLDERS, WEBSITES, APPS, SPECIAL_FOLDERS


def find_path_by_name(target_name):
    target_name = target_name.lower().strip()

    for base_folder in SEARCH_FOLDERS:
        if not os.path.exists(base_folder):
            continue

        for root, dirs, files in os.walk(base_folder):
            for folder in dirs:
                if target_name in folder.lower():
                    return os.path.join(root, folder)

            for file in files:
                if target_name in file.lower():
                    return os.path.join(root, file)

    return None


def find_app_in_start_menu(app_name):
    app_name = app_name.lower().strip()

    for base_folder in START_MENU_FOLDERS:
        if not base_folder or not os.path.exists(base_folder):
            continue

        for root, dirs, files in os.walk(base_folder):
            for file in files:
                file_lower = file.lower()
                if app_name in file_lower and (file_lower.endswith(".lnk") or file_lower.endswith(".exe")):
                    return os.path.join(root, file)

    return None


def find_exe_in_common_locations(app_name):
    app_name = app_name.lower().strip()

    for base_folder in APP_SEARCH_FOLDERS:
        if not base_folder or not os.path.exists(base_folder):
            continue

        for root, dirs, files in os.walk(base_folder):
            for file in files:
                file_lower = file.lower()

                if file_lower == f"{app_name}.exe":
                    return os.path.join(root, file)

                if app_name in file_lower and file_lower.endswith(".exe"):
                    return os.path.join(root, file)

    return None


def find_app_path(app_name):
    path = find_app_in_start_menu(app_name)
    if path:
        return path

    path = find_exe_in_common_locations(app_name)
    if path:
        return path

    return None


def get_all_searchable_names():
    names = set()
    names.update(WEBSITES.keys())
    names.update(APPS.keys())
    names.update(SPECIAL_FOLDERS.keys())

    for base_folder in SEARCH_FOLDERS:
        if os.path.exists(base_folder):
            try:
                for item in os.listdir(base_folder):
                    names.add(item.lower())
            except Exception:
                pass

    return list(names)


def suggest_similar_name(name, max_results=3):
    all_names = get_all_searchable_names()
    return difflib.get_close_matches(name.lower(), all_names, n=max_results, cutoff=0.5)