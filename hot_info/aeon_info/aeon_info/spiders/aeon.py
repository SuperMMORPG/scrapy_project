import scrapy
from scrapy.http import headers
from bs4 import BeautifulSoup 
import json

class AeonSpider(scrapy.Spider):
    name = 'aeon'
    #start_urls = ['https://aeon.co/science/popular?page=2']

    def start_requests(self):

        url = 'https://aeon.co/science/popular?page=3'

        headers = {
            'cookie': '_ga=GA1.2.678102842.1618317414; _hjid=9f756d81-350b-4618-a26a-b2d3efbd907a; aeon_group=0; aeon_newsletter=%7B%22subscribed%22%3Afalse%2C%22page_views%22%3A1%2C%22suspend_until%22%3A1618358400000%2C%22retired%22%3Afalse%7D; _gid=GA1.2.448714757.1618497082; _hjAbsoluteSessionInProgress=1; aeon_session=vQHQw0alxFTjM3n%2FBmTdtT4QSxN5Ox7fhUHqNo2%2FDwkPoDv%2BOwQZJRIxJaFt5kU5o97%2F7bvpZEjHk8w%2FyckyFgYb%2BuB1YFz78%2BvQ%2FIGKGSI3Dh%2FAbm8lN60KgYb7SrByF844JUpBAHZXULoXzfompvDyEJ9I%2FfftT2FVES2aP%2FyIJsvyQ41CNbXyMcwGJArDMO4Ap%2BuxW0F9%2FSN0Ikj83lkU%2FU2apAhqZjw9R6K5M%2BhnltSb09e2EFOK9uVPeiWBcsRsrHlHCTu0vjcHDYdjImqdHk2pCL2QroPNJAYTNDi3T7%2BSX7nQIAEVxtuZ2LGT2xysK1Wrcu0K8mrgsugArqUydUgGdCsi7M26BytYa0ao%2BEpNybyBnhO%2BO%2F6GCB1z277l0cpeEQWqunUtRwHTpPt8%2B78fPS22C1eSECcVtyGwDk4XwE2Qkft0--dOPINrrMzs2HdFwA--Qah9ihADE0G4MYaVpSip3Q%3D%3D',
            'if-none-match': 'W/"fd142fcb770f6ed9d630dfae34ba1fad"',
            'referer': 'https://aeon.co',
            'authority': 'aeon.co',
            'method': 'GET',
            'path': '/science/popular?page=3',
            'scheme': 'https',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest',
        }

        yield scrapy.Request(url,callback=self.parse,headers=headers)

    def parse(self, response):

        html_text = json.loads(response.body)['html']
        details_soup = BeautifulSoup(html_text,'lxml')
        a_data_list = details_soup.find_all('a',class_='article-card__title')
        for a in a_data_list:
            print(a.text)