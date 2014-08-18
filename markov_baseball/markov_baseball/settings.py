# Scrapy settings for markov_baseball project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'markov_baseball'

SPIDER_MODULES = ['markov_baseball.spiders']
NEWSPIDER_MODULE = 'markov_baseball.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'markov_baseball (+http://www.yourdomain.com)'
