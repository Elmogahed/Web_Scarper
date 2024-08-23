from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
import time
import tabulate

options = FirefoxOptions()
options.add_argument('--headless')

def get_youtube_channer_data(): 
    channel = input('What channel are you looking for? ')
    with webdriver.Firefox(options=options) as driver: 
        driver.get('https://www.youtube.com/@'+ channel +'/videos')
        time.sleep(3)

        page = driver.find_element(By.TAG_NAME, 'html')


        for i in range(3): 
            time.sleep(2)
            page.send_keys(Keys.END)

        try: 
            content = driver.find_element(By.ID, 'contents')
            video_titles = content.find_elements(By.ID, 'video-title-link')
            videos = []
            for title in video_titles: 
                videos.append([title.text, title.get_property('href')])

            videos_metadata = []

            video_metadata = content.find_elements(By.ID, 'details')

            for meta in video_metadata: 
                span_tags = meta.find_elements(By.ID, 'meta')

                span_data = []
                for span in span_tags: 
                    span_data.append(span.text)
                videos_metadata.append(span_data)
            results = []
            for item in zip(videos, videos_metadata): 
                results.append(item[0] + item[1])

            print(tabulate.tabulate(results, headers=['title', 'URL', 'Views', 'Date of Puplish'], tablefmt='fancy_grid'))


        except: 
            print('Tha page was not found!')
            return



if __name__ == '__main__':
    get_youtube_channer_data()


