# snopes_scraper_v2
Python Crawler Based on Scrapy for summer research on fake news

## Dependency
Before using the spider, make sure you have installed following dependencies:
1. python3.6
2. Scrapy

## Usage

```
scrapy crawl snopes_spider -o output.csv 
```
or 
```
scrapy crawl snopes_spider -o output.json
```
The output is organized as:
| count |	title	link	| cover image url	| ground truth |
---
| 1	     |Did a Teenage Daughter Dressed in Dad’s ‘Stay Clear Boys’ Shirt Get Pregnant?	| https://www.snopes.com/fact-check/teenage-daughter-shirt-pregnant/ |	https://us-east-1.tchyn.io/snopes-production/uploads/2018/07/dad_shirt_pregnancy_not_same_girl_faux.jpg?resize=542,305 | false |
---
