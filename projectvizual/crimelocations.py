import urllib.request
import json
import dml
import datetime
import uuid
import requests
import numpy as np
import math
import prov.model

class crimelocations(dml.Algorithm):
    contributor = 'lc546_jofranco'
    #name of file being read
    reads = []
    writes = []
    @staticmethod
    def execute():
        return crimelocations()
    @staticmethod
    def provenance():
        pass
    def getlocations():
        client = dml.pymongo.MongoClient()
        repo = client.repo
        repo.authenticate('lc546_jofranco', 'lc546_jofranco')

        data = []
        return data
crimelocations.execute()
