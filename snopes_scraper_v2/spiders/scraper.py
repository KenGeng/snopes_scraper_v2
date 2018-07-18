import scrapy
import re
# run in bash: scrapy runspider scraper.py ; scrapy crawl snopes_spider -o TitleAndLink2.csv


class SnopesSetSpider(scrapy.Spider):
    def __init__(self):
        self.n = 0
        self.flag =1

    name = 'snopes_spider'
    start_urls = ['https://www.snopes.com/fact-check/category/photos/']

    def parse(self, response):

        SET_SELECTOR = '.list-wrapper'

        for fauxset in response.css(SET_SELECTOR).css('article '):
            self.n += 1
            NAME_SELECTOR = '.title ::text'

            # PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'

            IMAGE_SELECTOR = '.article-link-image'
            temp =  fauxset.extract()
            childurl  = "".join(re.findall(r'href="(.*?)"',temp))
            truth = "".join(re.findall(r'fact_check_rating-(.*?) |"', temp))
            image_url = "".join(re.findall(r'data-bg="(.*?)"', "".join(fauxset.css(IMAGE_SELECTOR).extract())))

            yield {
                'count':self.n,
                'title': fauxset.css(NAME_SELECTOR).extract(),
                'link': childurl,
                'cover image url': image_url,
                'ground truth':truth.replace('"','')
            }

        NEXT_PAGE_SELECTOR = '.pagination-inner-wrapper a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract()
        print("De:")
        print(next_page)
        if next_page:
            # handle last page
            if len(next_page) < 2 and self.flag==0:
                return
            # first page
            elif len(next_page) < 2 and self.flag==1:
                self.flag = 0
                yield scrapy.Request(
                    response.urljoin(next_page[0]),
                    callback=self.parse,
                    dont_filter=True
                )

            else:
                # normal page
                yield scrapy.Request(
                    response.urljoin(next_page[1]),
                    callback=self.parse,
                    dont_filter=True
                )

        print("Done!")
