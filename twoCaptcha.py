from twocaptcha import TwoCaptcha


class Two2Captcha:

    def __init__(self):
        self.config = {
            'server': 'rucaptcha.com',
            'apiKey': '<KEY>',
            'defaultTimeout': 150,
            'pollingInterval': 10,
        }
        self.options = {
            'numeric': '4',
            'minLength': '6',
            'language': '2',
        }
        self.solver = TwoCaptcha(**self.config)

    def solve_captcha(self, file):
        try:
            result = self.solver.normal(file, **self.options)
            print(result)
            return result['code']
        except Exception as e:
            print(e)
