import json

#
# movie_test = ["lord of rings", "harry potter", "Originals"]
# author_test = ["Emmanuel", "Shalom", "Esther"]
#
# # with open("sample.json", "w") as file:
# #     print("File Created Succesfully")
#
#
# def create_json(movie, author, json_name="sample.json"):
#     if len(movie) != len(author):
#         return "List items are not compatible"
#
#     for i in range(len(movie)):
#
#         new_dict = {f"{i+1}":
#                         {
#                             "Song name": movie[i],
#                             "Author Name": author[i],
#                             "Rank": i+1,
#
#                          }
#                     }
#         try:
#             with open(json_name, "r") as data_file:
#                 new_json = json.load(data_file)
#
#                 new_json.update(new_dict)
#         except FileNotFoundError:
#             with open(json_name, "w") as new_file:
#                 json.dump(new_dict, new_file, indent=4)
#
#         else:
#             with open(json_name, "w") as new_file:
#                 json.dump(new_json, new_file, indent=4)
#
#
# create_json(movie_test, author_test, json_name="Sample_2.json")

song_list = ["Like A G6", "DJ Got Us Fallin' In Love"]
artist_list = ["Far*East Movement Featuring Cataracs & Dev", "Usher Featuring Pitbull"]


output_song = remove_strange_characters(titles=song_list)
output_artist = remove_strange_characters(titles=artist_list)

print(output_song)
print(output_artist)

final_output_artist = remove_featuring(output_artist)
print(final_output_artist)