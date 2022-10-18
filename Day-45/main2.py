from selenium import webdriver
import time

website = "https://www.empireonline.com/movies/features/best-movies-2/"
path = 'chromedriver/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

movies = []
selector = 1

# try:
#     test = driver.find_element(by='xpath', value='//*[@id="__next"]/main/article/div[3]/div[2]/div[8]/h3')
# except:
#     print("No title has the xpath")
# else:
#     new_title = test.text
#     print(new_title)
#     movies.append(new_title)

for i in range(1, 150):
    if i % 3 == 0:
        selector += 1
        continue
    try:
        title = driver.find_element(by='xpath', value=f'//*[@id="__next"]/main/article/div[3]/div[2]/div[{selector}]/h3')

    except:
        print("No title has the xpath")
    else:
        new_title = title.text
        print(new_title)
        movies.append(new_title)

    time.sleep(10)
    selector += 1

for movie in movies[::-1]:

    with open("chromedriver/text.txt", "a") as file:
        file.write(f"\n{movie}")
