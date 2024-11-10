from ..services.scrapper_service import ScrapperService
import json

class ScrapperController:
    def __init__(self):
        # self.__scrapper_service = ScrapperService()
        pass

    def get_person(self, request):
        try:
            headers = request.headers
            body = json.loads(request.data)
            print("dkfklsdfsd", body)
            profile_name = body.get("profile_name")
            username = body.get('username')
            password = body.get('password')
            if profile_name is None or username is None or password is None:
                return {
                    'err': 'inp_err',
                    'message': 'Input Error'
                }
            scrapper_service = ScrapperService()
            result = scrapper_service.get_person(profile_name, username, password)
            if 'success' in result and result.get('success') == True:
                return result
            return {
                'err': 'inp_err',
                'message': result.get('message')
            }
        except Exception as error:
            raise error