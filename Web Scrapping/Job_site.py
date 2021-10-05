import requests
from bs4 import BeautifulSoup
import time

wanted_skill = input("Provide your skill: ")
print(f'Showing jobs related to your skill : {wanted_skill}')


def get_jobs():
    html_text =  requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text ,'lxml')


    job = soup.find_all('li', class_ ="clearfix job-bx wht-shd-bx")
    for jobs in job:
        posted = jobs.find('span' , class_= 'sim-posted').span.text
        if 'few' in posted:
            company_name = jobs.find('h3', class_ = "joblist-comp-name").text.lstrip()
            skills = jobs.find('span',class_="srp-skills").text.lstrip().replace(' ','').upper()

            if wanted_skill in skills:
                posted = jobs.find('span' , class_= 'sim-posted').span.text
                #apply = jobs.find('div',class_ = "applied-dtl clearfix").a['href']
                more_info = jobs.header.h2.a['href']
                
                print(f'Company Name : {company_name.strip()}')
                print("")
                print(f'Skills : {skills.strip()}')
                print("")
                print(f'More info here : {more_info}')
                print("")
                print("")
                print("")

if __name__ == "__main__":
    while True:

        get_jobs() 
        wait_time = 1
        print(f'Waiting fot {wait_time} minutes')
        time.sleep(wait_time * 60)
        break
