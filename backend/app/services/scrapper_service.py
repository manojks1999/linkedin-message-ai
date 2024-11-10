# from ..platforms.linkedin import LinkedIn
from ..lib.linkedin_api import Linkedin
from ..models.llm.openai import OpenAiLlmClient
from ..ai_models import AiModel
# from selenium import webdriver
# from linkedin_scraper import Person, actions
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import selenium

class ScrapperService:
    def __init__(self):
        # self.__linkedin = LinkedIn()
        pass

    def get_person(self, profile_name, username, password):
        try:
            api = Linkedin(username, password)
            posts = api.get_profile_posts(profile_name)
            profile_data = api.get_profile(profile_name)
            first_name = profile_data.get('firstName')
            last_name = profile_data.get('lastName')
            summary = profile_data.get('summary')
            if(len(posts) == 0):
                return {
                'success': False,
                'message': 'No posts found'
            }
            filtered_posts = self.get_only_posts(posts)
            filtered_posts.append({
                'first_name': first_name,
                'last_name': last_name
            })
            filtered_posts.append({
                'summary': summary
            })
            print("dknksdfs", filtered_posts)
            response = self.form_message(filtered_posts)
            return {
                'success': True,
                'data': response
            }
        except Exception as error:
            print("Eororororo", error)
            return {
                'success': False,
                'message': f'Error {error}'
            }
    
    def get_only_posts(self, posts_data):
        try:
            posts = []
            for post in posts_data:
                commentory = post.get('commentary')
                data = commentory.get('text').get('text')
                posts.append(data)
            print("jdjjdjkjsdkjeww", posts)
            return posts
        except Exception as error:
            print("error in getting posts")
            raise error

    def form_message(self, message):
        try:
            model_instance = AiModel(OpenAiLlmClient(), 'gpt-3.5-turbo')
            print("jkdkjkds", message)
            response = model_instance.chat_completion(f'{message}')
            return response
        except Exception as error:
            raise error

# ScrapperService().get_person('dkfddd')