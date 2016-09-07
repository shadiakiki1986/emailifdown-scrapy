# emailifdown-scrapy
[Scrapy](https://scrapy.org) spider that sends a notification email if a URL is down.
Can be deployed to the [Scrapy cloud](http://scrapinghub.com/scrapy-cloud/) using their free plan.

# Usage
1. Install [pew](https://github.com/berdario/pew)
2. Initialize
```bash
pew new emailifdown-scrapy
pip install scrapy
```
3. Configure by copying `emailifdown_scrapy/settings-sample.py` to `emailifdown_scrapy/settings.py` and editing it (especially the section marked `EDIT THIS SECTION`)
 * the `MAIL_...` are mandatory if `-a emailTo=...` below is not skipped
 * These settings are the [scrapy mail settings](http://doc.scrapy.org/en/1.1/topics/email.html#mail-settings)

4. Run:
```bash
scrapy runspider emailIfDownSpider.py \
  -L WARNING \
  -a url="https://duckduckgo.com" \
  -a emailTo="my@email.com" \
```
 * skip `-a emailTo=....` for no email to be sent

# Depoloy to scrapinghub.com
1. Follow instructions in `Usage` above
2. Register on [Scrapy cloud](http://scrapinghub.com/scrapy-cloud/)
 * Start a new project
 * Copy the project's "target number" and your API key
3. Install [shub](https://github.com/scrapinghub/shub): `pip install shub`
4. Deploy: `shub deploy` (will prompt for target number copied above)
5. Schedule: `shub schedule 12345/emailifdown` where `12345` is your target number
6. Navigate to the scrapy cloud / project / periodic jobs dashboard
7. Add a new job (should automatically get `emailifdown` in dropdown)
8. add arguments "url" and "emailTo" and  select times at which to run
9. Check logs in dashboard
