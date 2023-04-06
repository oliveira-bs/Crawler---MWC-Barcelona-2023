import json

from scrapy.spiders import SitemapSpider


class MWBarcelonaSpider(SitemapSpider):
    name = 'mwcbarcelona_crawl'
    allowed_domains = ['www.mwcbarcelona.com']
    sitemap_urls = ['https://www.mwcbarcelona.com/sitemaps-1-sitemap.xml']

    sitemap_follow = [
        r'[\d\w:/.-]+(exhibitors)[\d\w:/.-]+'
    ]

    custom_settings = {
        'CONCURRENT_REQUESTS': 16,
        'CONCURRENT_REQUESTS_PER_IP': 16,
        'DOWNLOAD_DELAY': 0.514,
        'FEED_EXPORT_ENCODING': "utf-8",
        'RANDOMIZE_DOWNLOAD_DELAY': True,
        'REDIRECT_ENABLED': True,
        'RETRY_ENABLED': False,
        # 'RETRY_TIMES': 8,
    }

    def parse(self, response):
        dict_base = response.xpath(
            '//*[@id="add-to-favourites-app"]/@data-props').get()
        dict_base = json.loads(dict_base)
        name_company = dict_base.get('name')

        contact_company = response.xpath(
            '//li[@class="flex w-full md:w-1/3 pr-2"]/a/@href').getall()
        if contact_company != []:
            for link in contact_company:
                if 'http' in link:
                    site_company = link
                    break
                else:
                    site_company = None
        else:
            site_company = None

        links_company = response.xpath(
            '//div[@class="w-full pb-4 mb-4 border-b border-gray-300"]\
/*//@href').getall()
        if links_company != []:
            for link in links_company:
                if 'linkedin' in link:
                    linkedin_company = link
                    break
                else:
                    linkedin_company = None
        else:
            linkedin_company = None

        description = response.xpath(
            '//*[@id="exhibitor-container"]/main/p/text()').getall()
        if isinstance(description, list):
            description = [item for item in description if item != '\n']
            description = "".join(description)
            description = description.replace('\n', ' ').strip()
        else:
            description = None

        yield {
            'company_name': name_company,
            'linkedIn_url': linkedin_company,
            'website': site_company,
            'company_description': description,
        }
