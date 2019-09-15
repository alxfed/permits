# -*- coding: utf-8 -*-
import scrapy
import sqlite3


def agreement_failed(response):
    # //*[@id="agreement.errors"]
    NO_AGREEMENT_XPATH = '//*[@id="agreement.errors"]/text()'
    no_agreement = response.xpath(NO_AGREEMENT_XPATH).get()
    if no_agreement.startswith('Please agree to the term of the site to confinue.'):
        return True
    else:
        return False


def not_found(response):
    # TODO: check if this is a 'not found' page
    pass

class InspectionsListSpider(scrapy.Spider):
    name = 'insp_list_a'
    start_urls = ['https://webapps1.chicago.gov/buildingrecords/home']
    # DB_PATH = '/media/alxfed/toca/dbase/fifthbase.sqlite'
    # conn = sqlite3.connect(DB_PATH)  # , isolation_level=None) for working without commit
    # curs = conn.cursor()


    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formid='agreement',
            formdata = {"agreement": "Y",
                        "submit": "submit"},
            callback = self.after_agreement
        )

    def after_agreement(self, response):
        if agreement_failed(response):
            self.logger.error("agreement failed!")
            return
        else:
            item_list = 1, 2 # pd.read_csv('itemlist.csv', dtype=object)
        for item in item_list:
            yield scrapy.FormRequest.from_response(
                response,
                formid='search',
                formdata = {"fullAddress": item['Address'],
                            "submit": "submit"},
                callback = self.after_search
                )

    def after_search(self, response):
        print('ok')
        pass


"""
<form id="agreement" class="city-search-form" action="agreement" method="post">
<input type="hidden" name="_csrf" value="d8e9e354-f3c4-4f53-8403-0a9f17bd66d3">
<div class="row city-row city-row-form">
	<div class="input-xxs" style="width:30px;">
		<input id="rbnAgreement1" name="agreement" type="radio" value="Y">		
	</div>
	<div class="input-lg">		
		I accept the terms of this license 
	</div>
</div>	
<div class="form-row city-row-form">	
	<div class="input-xxs" style="width:30px;">
		<input id="rbnAgreement2" name="agreement" type="radio" value="N" checked="checked">
	</div>
	<div class="input-xl">
		I do
		&nbsp;<b>not</b>&nbsp;
		accept the terms of this license
	</div>
</div>
<div class="row city-row city-row-form">
	<div class="input-xxl">	
	</div>
</div>
<div class="row city-row city-row-form">	
	<div class="input-md">		
		<button id="submit" type="submit" name="submit" class="btn btn-primary" style="margin-top: 0;">		
			Submit
		</button>	
	</div>
</div>		
<div>
<input type="hidden" name="_csrf" value="d8e9e354-f3c4-4f53-8403-0a9f17bd66d3">
</div></form>
"""