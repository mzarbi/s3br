import json
import os
import pathlib
from datetime import datetime

from filelock import FileLock


def last_updated():
    os.makedirs(os.path.join(os.environ["CACHE_PATH"], "MANIFEST"), exist_ok=True)
    manifest_path = os.path.join(os.environ["CACHE_PATH"], "MANIFEST")
    ls = [f for f in os.listdir(manifest_path) if f.startswith("structure_")]
    if len(ls) == 0:
        return "Unspecified"
    ls.sort()
    return datetime.strptime(ls[-1].split("_")[1].split(".")[0], '%d%m%Y').strftime("%m/%d/%Y")


def safe_filename(filename):
    substitute_chars = {'/': '__', '\\': '__', ' ': ''}
    return "".join(substitute_chars.get(c, c) for c in filename)


def access_log(key):
    os.makedirs(os.path.join(os.environ["CACHE_PATH"], "ACCESS_LOG"), exist_ok=True)
    access_log_path = os.path.join(os.environ["CACHE_PATH"], "ACCESS_LOG", f"{safe_filename(key)}.json")
    if not os.path.exists(access_log_path):
        return []
    else:
        with FileLock(f"{access_log_path}.lock"):
            with open(access_log_path, "r") as f:
                return json.load(f)


def file_columns(key):
    os.makedirs(os.path.join(os.environ["CACHE_PATH"], "METADATA"), exist_ok=True)
    safe = safe_filename(key)
    metadata_path = os.path.join(os.environ["CACHE_PATH"], "METADATA", f"{safe.split('__')[-1][:2].upper()}.json")
    if not os.path.exists(metadata_path):
        return []
    else:
        with FileLock(f"{metadata_path}.lock"):
            with open(metadata_path, "r") as f:
                return json.load(f).get(safe, [])


def add_to_bookmarks(key, user_id, group, label):
    bookmarks_path = os.path.join(os.environ["CACHE_PATH"], "BOOKMARKS", user_id)
    os.makedirs(bookmarks_path, exist_ok=True)
    dc = {}
    with FileLock(os.path.join(bookmarks_path, f'{group}.json.lock')):
        if os.path.exists(os.path.join(bookmarks_path, f'{group}.json')):
            with open(os.path.join(bookmarks_path, f'{group}.json'), "r") as f:
                dc = json.load(f)

        dc.update({
            key: label
        })
        with open(os.path.join(bookmarks_path, f'{group}.json'), "w") as f:
            json.dump(dc, f)


def bookmark_groups(user_id):
    bookmarks_path = os.path.join(os.environ["CACHE_PATH"], "BOOKMARKS", user_id)
    os.makedirs(bookmarks_path, exist_ok=True)
    return [pathlib.Path(f).stem for f in os.listdir(bookmarks_path)]


def bookmark_groups_keys(user_id, ls):
    bookmarks_path = os.path.join(os.environ["CACHE_PATH"], "BOOKMARKS", user_id)
    dc = {}
    ls = [f["name"] for f in ls]
    for tmp in os.listdir(bookmarks_path):
        if pathlib.Path(tmp).stem in ls:
            with FileLock(os.path.join(bookmarks_path, f'{tmp}.lock')):
                with open(os.path.join(bookmarks_path, f'{tmp}'), "r") as f:
                    dc.update(json.load(f))
    return dc


def get_script_list():
    return [
        {
            "name": "GZip Decompress",
            "developer": "Mohamed Zied El Arbi",
            "description": """This script will decompress all the selected GZip files, uncompressed files will 
            remain the same."""
        },
        {
            "name": "CSV Converter",
            "developer": "Mohamed Zied El Arbi",
            "description": """This script will convert any xlsx or parquet files to csv, if the xlsx have multiple
            sheets, they will extract in singular csv files"""
        },
        {
            "name": "Parquet Converter",
            "developer": "Mohamed Zied El Arbi",
            "description": """This script will convert any xlsx or csv files to parquet, if the xlsx have multiple
            sheets, the script will create separate parquet files for each sheet"""
        },
        {
            "name": "XLSX Converter",
            "developer": "Mohamed Zied El Arbi",
            "description": """This script will convert any parquet or csv files to xlsx."""
        }
    ]


if __name__ == "__main__":
    os.environ["CACHE_PATH"] = r"C:\Users\medzi\Desktop\bnp\s3-browser\cache"
    file_columns("art_of_war")
