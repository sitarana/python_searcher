#!/usr/bin/python
# coding: UTF-8
import glob


def search_files(dir_path, extensions=["*"], recursive=False):

    find_files = []
    search_path = dir_path
    # 再帰探索なら、パスを追加
    if recursive is True:
        search_path += "/**/"
    # 拡張子ごとに、探索して、結果をまとめる
    for extension in extensions:
        find_files.append(glob(search_path+"*."+extension, recursive))

    return find_files

def search_string(file_path, search_word):
    return "s"
