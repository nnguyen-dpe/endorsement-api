import os
import pymongo
import uuid
import logging
import math
from datetime import datetime
from apis.exceptions import ApiError
from apis.models import Endorsement

log = logging.getLogger(__name__)

class EndorsementService(object):    
    def search(self, args):
        developer = args.get('developer')
        skill = args.get('skill')

        foundItems = Endorsement.get_all(developer, skill)
        
        items = []
        for it in foundItems:
            items.append(self.__mapOne(it))

        return self.__mapResponse(items)

    def __mapResponse(self, lst):
        totalRecords = len(lst)
        return {
            'totalRecords': totalRecords,
            'items': lst
        }

    def __mapOne(self, item):
        return {
            'developer': item.developer,
            'skill': item.skill,
            'count': item.count
        }

    def vote(self, data, action):
        if action != 'up' and action != 'down':
            raise Exception('Invalid action')
        try:
            record = Endorsement.get_one(data['developer'], data['skill'])
            if not record:
                record = Endorsement(developer=data['developer'],
                                    skill=data['skill'])
                record.save()
            else:
                if action == 'up':
                    record.up_vote()
                else:
                    record.down_vote()
                record.save()
            return self.__mapOne(record)
        except:
            raise Exception('Failed to update vote')

_srv = EndorsementService()
