import csv
import json
import os
import pprint


def get_preferences(file_name: str):
    print("")
    print(f"Getting preferences from {file_name}")
    with open(file_name) as f:
        file_content = f.read()

    parsed_json = json.loads(file_content)

    preferences = []
    for topic in parsed_json["topics_your_topics"]:
        preference_name = topic["string_map_data"]["Name"]["value"]

        preferences.append(preference_name)

    return preferences


sir_tails_preferences = get_preferences("sir_tails.json")
elvocool_preferences = get_preferences("elvocool.json")

all_preferences = set(sir_tails_preferences + elvocool_preferences)


with open("nodes.csv", "w", newline="") as f:
    print("Created nodes.csv")
    writer = csv.writer(f)
    title = ["id", "label", "is_preference"]
    writer.writerow(title)

    # Add users to nodes.csv
    writer.writerow(["sir_tails", "sir_tails", "false"])
    writer.writerow(["elvocool", "elvocool", "false"])
    print("Added users to nodes.csv")

    # Add preferences to nodes.csv
    for preference in all_preferences:
        writer.writerow([preference, preference, "true"])

    print("Added preferences to nodes.csv")


def add_edges(json_file_name: str, writer: csv.writer):
    with open(json_file_name) as json_f:
        file_content = json_f.read()

    parsed_json = json.loads(file_content)

    for topic in parsed_json["topics_your_topics"]:
        preference_name = topic["string_map_data"]["Name"]["value"]
        user_name = os.path.splitext(json_file_name)[0]
        writer.writerow([user_name, preference_name])


with open("edges.csv", "w", newline="") as f:
    print("Created edges.csv")
    writer = csv.writer(f)
    title = ["source", "target"]
    writer.writerow(title)

    add_edges("sir_tails.json", writer)
    add_edges("elvocool.json", writer)

    print("Added all edges")
