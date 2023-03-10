#!/usr/bin/python3
"""JSON"""
import json


def load_from_json_file(filename):
    """load from json"""
    with open(filename, mode='r', encoding="utf-8") as f:
        return (json.load(f))
