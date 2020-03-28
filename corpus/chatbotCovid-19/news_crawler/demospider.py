from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
 
 
class DemospiderSpider(CrawlSpider):
  handle_httpstatus_list = [403, 404]
  name = 'demospider'
  allowed_domains = ['doh.gov.ae']
  start_urls = ['https://www.doh.gov.ae/covid-19/news/News19']
  custom_settings = {
    'LOG_FILE': 'logs/demospider.log',
    'LOG_LEVEL': 'DEBUG'
  }
 
  rules = (
    Rule(
      LinkExtractor(
        tags='a',
        attrs='href',
        unique=True
      ),
      callback='parse_item'
      follow=True
    ),
  )
 
  def parse_item(self, response):
    pass