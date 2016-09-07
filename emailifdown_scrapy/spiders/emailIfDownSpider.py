import scrapy
from scrapy.mail import MailSender

class EmailIfDownSpider(scrapy.Spider):
    name = 'emailifdown'

    # http://doc.scrapy.org/en/1.1/topics/spiders.html#spider-arguments
    def __init__(self, url=None, emailTo=None, *args, **kwargs):
        super(EmailIfDownSpider, self).__init__(*args, **kwargs)
        if url is None:
          raise Exception("Url not passed in spider -a argument as url='http://something'")
        self.start_urls = [url]
        self.emailTo = emailTo

    # http://doc.scrapy.org/en/1.1/topics/request-response.html#using-errbacks-to-catch-exceptions-in-request-processing
    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse,
                                    errback=self.errback,
                                    dont_filter=True)

    def parse(self, response):
        if len(response.css('ul li a::attr("href")')) == 4:
          self.logger.warning(response.url+" is up")
        else:
          self.email("Unknown reason",response.url)

    def errback(self,failure):
        self.email(repr(failure),failure.request.url)

    def email(self,failure,url):
        msg=url+" is down"
        self.logger.warning(msg)
        self.logger.warning(failure)

        if self.emailTo is not None:
          for field in ['MAIL_USER','MAIL_PASS']:
            if self.settings.attributes[field].value is None:
              msg = "Requested sending email but forgot to pass -s "+field+"='...' to the spider. Fields list available at http://doc.scrapy.org/en/1.1/topics/email.html#mail-settings"
              raise scrapy.exceptions.NotSupported(msg)

          self.logger.warning("Sending email from "+self.settings.attributes["MAIL_USER"].value)
          mailer = MailSender.from_settings(self.settings)
          mailer.send(to=[self.emailTo], subject=msg, body=failure) #, cc=["another@example.com"])

