import scrapy

CLASSES = {
    "crypto_card": "._1dSou6YbrT4POv2E7HhT6L",
    "growth": "._2SYFxGdmPGEAqHRZI8P__k",
    "volume": ".Zmdo0BEwYVGMrFKtfC5_V",
    "price": "._3XNm6CSrchU-MNbu1Zh3m2"
}

class CryptoPriceTracker(scrapy.Spider):
    name = "price"
    start_urls = ['https://cryptowat.ch/']

    def parse(self, response):
        for crypto_card in response.css(CLASSES.get("crypto_card")):
            yield {
                "crypto_type": crypto_card.css('h2::text').get(),
                "price": crypto_card.css(f'div span{CLASSES.get("price")}::text').get(),
                "growth": crypto_card.css(f'div span{CLASSES.get("growth")} span::text').get(),
                "volume": crypto_card.css(f'div{CLASSES.get("volume")}::text').get()
            }
