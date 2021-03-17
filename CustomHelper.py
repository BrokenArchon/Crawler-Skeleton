def getProductGroupCondition():
    import argparse

    parser = argparse.ArgumentParser(description = 'Custom web scrapper')
    parser.add_argument('--search', default = 'test', help = 'Search parametr')
    args = parser.parse_args()

    return args.search # python app.py --search "search string"

def initiateLogger(file_name = 'crawler.log'):

    import os
    import logging

    if os.path.isfile(file_name) and (os.path.getsize(file_name)/1024)/1024.0 > 2:
        os.remove(file_name) # file reset to zero every 2M

    logging.basicConfig(
        level = logging.INFO,
        format = '%(asctime)s %(levelname)-8s %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S',
        filename = file_name,
        filemode = 'a'
    )

    logging.info('Initialize Logger')

def saveAsFile(content, file_name = 'crawler.json'):

    import json

    with open(file_name, 'w') as outfile:
        json.dump(content, outfile)

# def saveAsFile(content, file_name = 'crawler.yaml'):

#     import yaml

#     with open(file_name, 'w') as outfile:
#         yaml.dump(content, outfile, default_flow_style = False)