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
3. Configure SMTP email settings by copying `emailifdown_scrapy/settings-sample.py` to `emailifdown_scrapy/settings.py` and editing it (section marked `EDIT THIS SECTION`)
 * these `MAIL_...` settings are mandatory if `-a emailTo=...` below is not skipped
 * These settings are the [scrapy mail settings](http://doc.scrapy.org/en/1.1/topics/email.html#mail-settings)
 * Alternatively, pass the settings directly to scrapy as parameters using `-s` (check below for run example)

4. Run:
```bash
scrapy runspider emailIfDownSpider.py \
  -L WARNING \
  -a url="https://duckduckgo.com" \
  -a emailTo="my@email.com"
```
 * add the below settings if not put in settings.py (check above note)
```bash
  ...
  -s MAIL_USER="another@email.com" \
  -s MAIL_HOST="smtp.email.com" \
  -s MAIL_PORT=123 \
  -s MAIL_PASS="password"
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
 * Maybe `shub` supports `-a` and `-s` parameters similar to `scrapy` but it probably didnt work for me
6. Navigate to the scrapy cloud / project / periodic jobs dashboard
7. Add a new job (should automatically get `emailifdown` in dropdown)
8. add arguments "url" and "emailTo" and  select times at which to run
9. Check logs in dashboard
