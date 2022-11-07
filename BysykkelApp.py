#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from tkinter import *
from pandastable import Table, TableModel
import requests
import pandas as pd
import logging


#import json
# https://stackoverflow.com/questions/4564559/get-exception-description-and-stack-trace-which-caused-an-exception-all-as-a-st


def check_response_status_code(response):
    """
    This function is checking if the response status code is within the correct range.
    Args:
        response (Response): API response data
        
    Raises:
        ConnectionError if status code is suggesting a connection error   
    """

    if 200 <= response.status_code < 300:
        print('Request succeeded!')
    else:
        print(f'We got response code {response.status_code}...')
        raise ConnectionError


def fetch_response(url, my_header):
    """
    This function is fetching response data from API. In case of an exception
    it is logged with trace data and system exits. 
    Args:
        url (String): url address
        my_header (String): value to identify my app to the server.
    Returns:
        response (Response): data from the API or None if exceptions are not handled 
    """
    response = None
    try:
        response = requests.get(url, my_header)
        check_response_status_code(response)
    except requests.exceptions.HTTPError as errh:
        logger.exception(errh)
        sys.exit(1)
    except requests.exceptions.ConnectionError as errc:
        logger.exception(errc)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        logger.exception(err)
        sys.exit(1)

    return response

# setting up logger to
logger = logging.getLogger(__name__)

url_stations_information = 'https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json'
url_stations_status = 'https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json'
my_client_identifier = 'jovand-codeoppgave'
my_header = {'Client-Identifier': my_client_identifier}

response_stations = fetch_response(url_stations_information, my_header)  
response_stations_status_info = fetch_response(url_stations_status, my_header)

# as additional check we check if responses are not none. 
# This is the case when for some reason we dont get a response 
# and this is not handled by fetch_data. 
if  response_stations and  response_stations_status_info is not None:
    
    data_stations = response_stations.json() 
    data_stations_status_info = response_stations_status_info.json() 
    # panda data frames with station id, name and etc but not availability data
    data_frame_stations_info = pd.DataFrame.from_dict(data_stations['data']['stations'])
    # panda data frames with station id, and availability data
    data_frame_stations_availability = pd.DataFrame.from_dict(data_stations_status_info['data']['stations'])
    # merging two data frames on station id
    merged_df = pd.merge(data_frame_stations_info,data_frame_stations_availability, on='station_id')
    merged_selection = merged_df[["station_id",'name', 'capacity','num_bikes_available','num_docks_available']] #, 'name', 'capacity','is_installed','is_renting','is_returning','last_reported','num_bikes_available','num_docks_available']
    


class TestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('800x400')
            self.main.title('Bysykkel app')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            #df = TableModel.getSampleData()
            self.table = pt = Table(f, dataframe=merged_selection,
                                    showtoolbar=False, showstatusbar=False)
            pt.show()
            return

if __name__=='__main__':
    # This is placed in try/except to provide info in case where responses are None
    # and merged_selection is undefined. Idea is to provide some info on 
    # what has happened.
    try:
        app = TestApp()
            #launch the app
        app.mainloop()
    
    except NameError as ne: 
        logger.exception(ne)

