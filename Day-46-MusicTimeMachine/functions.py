import json


def create_json(song, author, json_name="sample.json"):
    if len(song) != len(author):
        return "List items are not compatible"

    for i in range(len(song)):

        new_dict = {f"{i+1}":
                        {
                            "Song name": song[i],
                            "Author Name": author[i],
                            "Rank": i+1,

                         }
                    }
        try:
            with open(json_name, "r") as data_file:
                new_json = json.load(data_file)

                new_json.update(new_dict)
        except FileNotFoundError:
            with open(json_name, "w") as new_file:
                json.dump(new_dict, new_file, indent=4)

        else:
            with open(json_name, "w") as new_file:
                json.dump(new_json, new_file, indent=4)

    return "Successful"


def remove_strange_characters(titles: list) -> list:
    """
    Checks for char in the invalid_char list and removes
     them and returns a list of the corrected songs and song authors

     """
    stripped_title = ""
    titles_output = []

    invalid_characters = ['*', '!', '@', '#', '$', '%', '^', '\'', '-', '+', '=', '&', ':', ';']

    for title in titles:
        # print(title)
        for char in invalid_characters:
            if char in title:
                stripped_title = title.replace(char, "")
                # print(stripped_title)

                break
        if len(stripped_title) < 1:
            stripped_title = title

        titles_output.append(stripped_title)
        stripped_title = ""
    # print(titles_output)
    return titles_output


def remove_featuring(titles: list) -> list:
    tag = "Featuring"
    titles_without_tag = []

    for title in titles:
        if tag in title:
            # print(f"Title has {tag}")

            title_edit = title.replace(tag, '|')
            ind = title_edit.index("|") - 1

            final_title = title_edit[:ind]

        else:
            final_title = title

        titles_without_tag.append(final_title)

    return titles_without_tag


