# -*- coding: utf-8 -*-
"""https://jsonlines.readthedocs.io/en/latest/
"""
import jsonlines
import pandas as pd


def read_into_pd(inpfile):
    data = pd.read_json(inpfile, lines=True)
    return data

def write_pd_to_jl(data, outfile):
    data.to_json(outfile, orient='records', lines=True)
    return

def main():
    # renovation_alteration_scraped.jl
    INP_FILE = '/home/alxfed/dbase/new_construction_scraped.jl'
    OUT_FILE = '/home/alxfed/dbase/new_construction_procssd.jl'
    insp_types = ['BOILER ANNUAL INSPECTION', 'FIRE PREVENTION PUMPS LEGACY', 'PERMIT INSPECTION',
                  'CONST EQ COMPLAINT INSPECTION', 'PLUMBING INSPECTION', 'ELEVATOR LEGACY INSPECTION',
                  'PLUMBING COMPLAINT INSPECTION', 'DOB GARAGE INSPECTION', 'SIGN LEGACY INSPECTION',
                  'CHECKLIST INSPECTION', 'REFRIGERATION ANNUAL', 'VENTILATION COMPLAINT INSPECT',
                  'DOB NEW CONSTRUCTION INSP', 'BLDG_PERM IRON PERMIT INSP', 'DOB VENT/FURNACE INSPECTION',
                  'RE-INSPECTION', 'REFIGERATION COMPLAINT INSPECT', 'ASSEMBLY/AMUSEMENT ANNUAL INSP',
                  'DGHS COMPLAINT INSPECT', 'VENT/HEAT PERMIT INSPECTION', 'BOILER LEGACY INSPECTION',
                  'SIGN PERMIT INSPECTION', 'DOB REFRIGERATION INSPECTION', 'STRUCTURAL SIGN INSPECTION',
                  'ANNUAL INSPECTION', 'ELECTRIC COMPLAINT INSPECTION', 'ANNUAL AUTOMATIC SPRINKLER',
                  'PUMP ACCEPTANCE TEST', 'SIGN COMPLAINT INSPECTION', 'VENT ANNUAL', 'PPA COMPLAINT INSPECTION',
                  'BACKFILL', 'WATER DEPT PERMIT INSPECTION', 'ELECTRICAL PERMIT INSPECTION', 'PUMP CASE',
                  'FINAL INSPECTION', 'SIGN ANNUAL INSPECTION', 'CONSTRUCTION EQUIPMENT PERMIT',
                  'CONSERVATION ANNUAL', 'STRATEGIC TASK FORCE INSP.', 'PORCH/DECK PERMIT INSPECTION',
                  'DOB PLUMBING INSPECTION', 'IRON LEGACY INSPECTION', 'BOILER PERMIT INSPECTION',
                  'CONSERVATION COMPLAINT INSPECT', 'EXPOSED METAL', 'DEMO COURT', 'EQUIPMENT INSPECTION',
                  'NEW CONSTRUCTION COMPLAINT', 'COMPLAINT INSPECTION']
    renovation_insp = ['PORCH COMPLAINT INSPECTION', 'CONSERVATION ANNUAL', 'WATER DEPT PERMIT INSPECTION',
                       'DEMO COURT', 'PPA COMPLAINT INSPECTION', 'PLUMBING COMPLAINT INSPECTION',
                       'NEW CONSTRUCTION COMPLAINT', 'VENT ANNUAL', 'CONST EQ COMPLAINT INSPECTION',
                       'CONSERVATION COMPLAINT INSPECT', 'ASSEMBLY/AMUSEMENT ANNUAL INSP', 'PLUMBING INSPECTION',
                       'CHECKLIST INSPECTION', 'PUMP CASE', 'SIGN LEGACY INSPECTION', 'FTD CERTIFICATION INSPECTION',
                       'ELECTRIC COMPLAINT INSPECTION', 'VENT/HEAT PERMIT INSPECTION', 'DOB REFRIGERATION INSPECTION',
                       'DOB VENT/FURNACE INSPECTION', 'SIGN COMPLAINT INSPECTION', 'ELEVATOR LEGACY INSPECTION',
                       'ANNUAL INSPECTION', 'BOILER LEGACY INSPECTION', 'TBI COMPLAINT INSPECTION',
                       'VENTILATION COMPLAINT INSPECT', 'PORCH/DECK PERMIT INSPECTION', 'ELEVATOR FIRE SERVICE INSP',
                       'RE-INSPECTION', 'EQUIPMENT INSPECTION', 'BOILER ANNUAL INSPECTION', 'DGHS COMPLAINT INSPECT',
                       'BLDG_PERM IRON PERMIT INSP', 'ANNUAL AUTOMATIC SPRINKLER', 'SIGN PERMIT INSPECTION',
                       'CONSTRUCTION EQUIPMENT PERMIT', 'BOILER COMPLAINT INSPECTION', 'FTD DETERMINATION INSPECTION',
                       'STRATEGIC TASK FORCE INSP.', 'FIRE PREVENTION PUMPS LEGACY', 'EXPOSED METAL',
                       'REFRIGERATION ANNUAL', 'BOILER PERMIT INSPECTION', 'DOB NEW CONSTRUCTION INSP',
                       'IRON LEGACY INSPECTION', 'DOB PLUMBING INSPECTION', 'DOB GARAGE INSPECTION',
                       'PUMP ACCEPTANCE TEST', 'ELECTRICAL PERMIT INSPECTION', 'REFIGERATION COMPLAINT INSPECT',
                       'STRUCTURAL SIGN INSPECTION', 'PERMIT INSPECTION', 'COMPLAINT INSPECTION',
                       'SIGN ANNUAL INSPECTION']
    #df = read_into_pd(INP_FILE)
    #res = write_pd_to_jl(df, OUT_FILE)
    with jsonlines.open(INP_FILE, mode='r') as reader:
        with jsonlines.open(OUT_FILE, mode='a') as writer:
            for line in reader:
                full_address = line['full_address']
                input_address = line['input_address']
                range_address = line['range_address']
                insp_table = pd.DataFrame.from_records(line['insp_table'])
                perm_table = pd.DataFrame.from_records(line['perm_table'])
                # transform
                writer.write(line)
        writer.close()
    reader.close()
    return


if __name__ == '__main__':
    main()
    print('main - done')