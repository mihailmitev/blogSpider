import scrapy

class BlogSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://www.aspentimes.com/news/looking-toward-the-future-right-here-on-planet-earth/']

    def parse(self, response):
        for title in response.css('article > h1'):
            yield {'title': title.css('::text').get()}

        for author in response.css("h6 > a[rel='author']"):
            yield {'author': author.css('::text').get()}    

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)