#!/usr/bin/env python
# coding: utf-8

# In[29]:


from mpi4py import MPI
import requests
from mastodon import Mastodon, StreamListener
import csv, os, time, json
from couchdb import Server
import re
#from datetime import datetime
from datetime import date, datetime


# In[ ]:


comm = MPI.COMM_WORLD
rank = comm.Get_rank()


def process_dict(d):
    for k, v in d.items():
        if isinstance(v, datetime):
            d[k] = v.isoformat()
        elif isinstance(v, dict):
            process_dict(v)
        elif isinstance(v, list):
            for i in range(len(v)):
                if isinstance(v[i], dict):
                    process_dict(v[i])
    return d

class KeywordStreamListener(StreamListener):
    def __init__(self, mortgage_db, homeless_db, mortgage_keywords, homeless_keywords):
        self.mortgage_db = mortgage_db
        self.homeless_db = homeless_db
        self.rent_db = rent_db
        self.income_db = income_db
        
        self.mortgage_keywords = mortgage_keywords
        self.homeless_keywords = homeless_keywords
        self.rent_keywords = rent_keywords
        self.income_keywords = income_keywords

    def on_update(self, status):
        content = re.sub('<[^>]*>', '', status['content'])
        status = process_dict(status)
        
        if any(keyword.lower() in content.lower() for keyword in self.mortgage_keywords):
            mortgage_status = status.copy()
            mortgage_status['_id'] = 'mortgage_' + str(mortgage_status['id'])
            self.mortgage_db.save(mortgage_status)
            #print('One mortgage add')
        if any(keyword.lower() in content.lower() for keyword in self.homeless_keywords):
            homeless_status = status.copy()
            homeless_status['_id'] = 'homeless_' + str(homeless_status['id'])
            self.homeless_db.save(homeless_status)
            #print('One homeless add')
        if any(keyword.lower() in content.lower() for keyword in self.income_keywords):
            income_status = status.copy()
            income_status['_id'] = 'income_' + str(income_status['id'])
            self.income_db.save(income_status)
            #print('One income add')
        if any(keyword.lower() in content.lower() for keyword in self.rent_keywords):
            rent_status = status.copy()
            rent_status['_id'] = 'rent_' + str(rent_status['id'])
            self.rent_db.save(rent_status)
            #print('One rent add')

def stream_to_couchdb(instance_url, access_token, 
                      mortgage_db, homeless_db, income_db, rent_db,
                      mortgage_keywords, homeless_keywords, income_keywords, rent_keywords
                     ):
    client = Mastodon(
        access_token=access_token,
        api_base_url=instance_url
    )
    listener = KeywordStreamListener(mortgage_db, homeless_db, mortgage_keywords, homeless_keywords)
    client.stream_public(listener)


if rank == 0:
    instance_url = 'https://aus.social'
    access_token = '1OM_w4sjj9sUkAxamkbDU_dSrz2CY3EPMVrDLz2-9NU'
elif rank == 1:
    instance_url = 'https://mastodon.au'
    access_token = 'riNvzdIeoXoyopIOsUonmVqHf6kLUsl21sOHzW2-9M0'

couch = couchdb.Server('http://jionghao:123456@172.26.134.63:5984/')

mortgage_keywords = ["mortgage", "pledge", "hypothec", "guaranty", "pawn"]
homeless_keywords = ["homeless", "tramp", "vagrant",'dispossessed', 'unhoused']
rent_keywords = ["rent", "chummage", "rental",'lease', 'renting', 'leasing', 'tenants']
income_keywords = ["income", "earning",'payroll', 'paycheque', 'paycheck']

mortgage_db_name = 'mortgage'
if mortgage_db_name not in couch:
    mortgage_db = couch.create(mortgage_db_name)
else:
    mortgage_db = couch[mortgage_db_name]

homeless_db_name = 'homeless'
if homeless_db_name not in couch:
    homeless_db = couch.create(homeless_db_name)
else:
    homeless_db = couch[homeless_db_name]
    
rent_db_name = 'rent'
if rent_db_name not in couch:
    rent_db = couch.create(rent_db_name)
else:
    rent_db = couch[rent_db_name]
    
income_db_name = 'income'
if income_db_name not in couch:
    income_db = couch.create(income_db_name)
else:
    income_db = couch[income_db_name]
    
#==================

stream_to_couchdb(instance_url, access_token, 
                  mortgage_db, homeless_db, income_db, rent_db,
                  mortgage_keywords, homeless_keywords, income_keywords, rent_keywords
                 )


# In[ ]:





# In[ ]:




