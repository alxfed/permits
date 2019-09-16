# -*- coding: utf-8 -*-
import scrapy
import sqlite3


def agreement_failed(response):
    # TODO: check the response
    pass


def not_found(response):
    # TODO: check if this is a 'not found' page
    pass

class InspectionsListSpider(scrapy.Spider):
    name = 'insp_list_b'

    def start_requests(self):
        DB_PATH = '/home/alxfed/dbase/fifthbase.sqlite'
        conn = sqlite3.connect(DB_PATH)  # , isolation_level=None) for working without commit
        conn.row_factory = sqlite3.Row
        curs = conn.cursor()
        curs.execute('SELECT "PERMIT#", "STREET_NUMBER", "STREET DIRECTION", "STREET_NAME", "SUFFIX"  FROM permits')
        permits_list = []
        for row in curs.fetchall():
            permits_list.append({'permit_n': row['PERMIT#'],
                                 'street_n': row["STREET_NUMBER"],
                                 'street_dir': row["STREET DIRECTION"],
                                 'street_name': row["STREET_NAME"],
                                 'suffix': row["SUFFIX"]})
        conn.close()
        return [scrapy.Request('https://webapps1.chicago.gov/buildingrecords',
                               dont_filter=True, callback=self.parse,
                               meta={'permits_list': permits_list})]

    # https://docs.scrapy.org/en/latest/topics/spiders.html?highlight=start_requests#spiders

    def parse(self, response):
        permits_list = response.meta['permits_list']
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
            item_list = 1, 2 # item_list = pd.read_csv('itemlist.csv', dtype=object)
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