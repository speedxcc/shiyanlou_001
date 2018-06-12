import scrapy


class ShiyanlouCoursesSpider(scrapy.Spider):

    name = 'shiyanlou-courses'

    @property
    def start_urls(self):
        """ start_urls  ???????????????????????????????????????????
        """
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 4))
   #     return url_tmpl

    def parse(self, response):
        for course in response.css('li[itemprop]'):
            yield {
          #      'name': course.xpath('//h3/a/text()').re_first(' *(.+) *'),
                'name': course.css('h3 a::text').re_first(' *(.+) *'),
                'update_time': course.xpath('.//relative-time/@datetime').extract_first(),
         #       'type': course.css('div.course-footer span.pull-right::text').extract_first(),
          #      'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d+)[^\d]*')
            }
