import scrapy
import json
import requests
from scrapy.http import headers, request
from forbes_info.items import ForbesInfoItem
class ForbesSpider(scrapy.Spider):

    name = 'forbes'
    url = r'https://www.forbes.com/simple-data/editors-picks/'

    def start_requests(self):

        #res = requests.get(self.url)
        #print(res.status_code)
        
        HEADERS = {
            'cookie': 'client_id=6898a05bfbb10e79981f07b76daed0870c5; usprivacy=1---; notice_behavior=none; lux_uid=161780308976132247; __aaxsc=2; gaWelcomPageTracked=true; __gads=ID=a219030404b15f19:T=1617803103:S=ALNI_MZga_92HvwgK9-Gv3p_J14IWjQnCg; __pnahc=0; __tbc=%7Bjzx%7DIFcj-ZhxuNCMjI4-mDfH1Lq573L8YhojbTsx04mMwSii3FYAQFi1kQQdt5MlvKULSCkuDYd7DxS4ew34IDV79g; __pat=-14400000; xbc=%7Bjzx%7DCTv_w-ivPQG52xHHQoXuwItg6Z9sgVtZaoCLyZ72ZItOmfo-DabaEsl_JnjfUsA1_6bYJ0MmLc8o8VDIKXY1Z9fy7yODfwqOGIHw0LUsQ5-IBf23yz42ytGCS46rjqUvzAzOpi93mxqyZkvyowXaQ55H8syvuSaVG7heC_ZBdaJC_qGry6QSyvltq0r-2SMGiUUO1nrS2OeovpkLhPGFkXsAo0VfzvdCM3RW1SNCTIYJ-jVrfCaXEX9JeRfC5EF6mQCwFEg5przUHdYmBYNbq6lycf-5Eg8QE8UIHOW823KfkTGoSnD6zjKMKivIMJGLY0SV955WaRS1z3bzB4x0CziGDkFChZvgPU_dCwFxw4EzkTu6yVzep93xApAYuJhmUilr5cXW4ni6JEAUCvN9SbUGa9Z3Q_9YRUvT_dFOs1HCkEYk-uy0VR6Z7D8bJGrj0b8hSPmw2F6SkjZvAf7nynF2dJig6JuuqcmTS7aJ-rOlVNdgiJkfxcUa4QDAm9ynsTh6sjiOEo-CL82VfZLmEjX2E1LrK4gmLqyYwk-qP-ZhHcZcst5vv78c-2q5PBk-F1Zg4BTXMejM2NPXpZGYNahU6lx24khx_NJniBkk7qcOF5apWjYZovBZ9oq9h-M-dKskPT5JJYr_Lq9cU1b3bA84dOuDzZsuVMnQc3lOxRWVaYzt8BrLFoiPQMrY-bTo_qPn7Ilwu_zD0XiXqkQKvB_oYXLJen2HVkuz1u1dRE28cvCxn1VB93VNm0rsquSR57nsP0VgdTiHt6ZAQGRYlysNXvVkJzOxxwXG2IfmTZezbMLvDtyNgam9vmKDt2QmGfBDDKQnsJTT1Xosc98ZRVj_y_Oet3-oDlgKZd1Gdm61FSMJ2nXZvdZ3fkFKXLHJTWa_Mymq8RmeToKUy14wOg-ssZ5Ub1Gra4CFzLb-7fTu0CVKcBpTVo6NjQVhRIJdZ1JsVYSExK5Lj9Z3EN5pwneQ1LDwB7Jb6jvi7z4RWKpmcvaE44DfilYqYSst5LChE9q34w7-n7pNL8NX4zh7Nd4eMOd5gBpOCLH1AN7ZqWLMIiY8Ty5wHDDpnMBRymHTKjKe4AAAFCIAvpZaAEuSTyO6ugsXTb5JsKHLhIQxnT6M0AtpGlwGgILNYXV22hiEzhuVwlPNWzC3H2EtvHWUDATEnwEZSYOKU6HlVUsh8fA; _ga=GA1.2.946481091.1617803097; _gid=GA1.2.1891843556.1617803107; __qca=P0-1490385268-1617803102943; cX_S=kn7i79ymit5znh6q; mnet_session_depth=2%7C1617803090087; aasd=2%7C1617803090486; malcolm=B; forbesbeta=B; __pvi=%7B%22id%22%3A%22v-kn7i7t2kld8xrgu9%22%2C%22domain%22%3A%22.forbes.com%22%2C%22time%22%3A1617803136236%7D',
        }

        yield scrapy.Request(self.url ,callback=self.parse,headers=HEADERS)

    def parse(self, response):

        print(response.status)

        text_list = json.loads(response.text)
        for text in text_list:

            blogName = text['blogName']
            blogType = text['blogType']
            title = text['title']
            uri = text['uri']
            author = text['author']['name']

            item = ForbesInfoItem()
            item['blogName'] = blogName
            item['blogType'] = blogType
            item['title'] = title
            item['uri'] = uri
            item['author'] = author

            yield item

