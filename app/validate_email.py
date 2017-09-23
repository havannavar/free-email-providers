'''
Created on 23 Aug 2017

@author: havannavar
'''
'''
Refering to below link created the list of email providers.
Future if there is new provider, please add to rejection list
 http://mashable.com/2007/09/05/email-toolbox/ 
 
'''

from flask import jsonify, make_response, request
from functools import wraps
import re


mailServiceProviders = ['gmail',
                        'hotmail',
                        'rediff',
                        'outlook',
                        'yahoo',
                        'icloud',
                        'aol',
                        'gmx',
                        'zoho',
                        'yndex',
                        'aim',
                        'mail',
                        'inbox',
                        '30Gigs',
                        'aussiemail',
                        'bigstring',
                        'bluebottle',
                        'boarderemail',
                        'canada',
                        'canoe',
                        'care2',
                        'dcemail',
                        'dbzmail',
                        'didamail',
                        'emailaccount',
                        'fastermail',
                        'fastmail',
                        'gawab',
                        'graffiti',
                        'hotpop',
                        'hushmail',
                        'icqmail',
                        'indiatimes',
                        'inmail24',
                        'jubii',
                        'linuxmail',
                        'litepost',
                        'mail.lycos',
                        'mail2world',
                        'mailsnare',
                        'merseymail',
                        'MuchoMail',
                        'msn',
                        'myway',
                        'outgun',
                        'postmaster',
                        'prontomail',
                        'runbox',
                        'sacmail',
                        'safe-mail',
                        'ureach',
                        'vfemail',
                        'zilladog',
                        'earthclassmail',
                        'futureme',
                        'hoaxmail',
                        'l8r',
                        'postful',
                        'pranketh',
                        'shinyletter',
                        '2prong',
                        'dodgeit',
                        'e4ward',
                        'emailias',
                        'gishpuppy',
                        'guerrillamail',
                        'mailexpire',
                        'mailnator',
                        'pookmail',
                        'spam',
                        'spambox',
                        'spamex',
                        'spamgourmet',
                        'tempinbox',
                        'zoemail',
                        'live',
                        'me']

freeEmailProviders = set(mailServiceProviders)

def validate(f):      
    
    @wraps(f)
    def decorated(*args, **kwargs):
        email = request.json.get('businessEmail')
        if email is None:
            # Unauthorized
            return make_response(jsonify({'message':'Provide the email'}), 401)
        else:
            if len(email) > 7:
                if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:            
                    org_name = re.split(r'[@.]+', email)
                    if any("edu" in s for s in org_name):
                        return make_response(jsonify({'email':email, 'message':'you are an education institution, please contact our administrators for any help'}))
                    
                    if org_name[1].lower() in freeEmailProviders:
                        return jsonify({'message':'Register with a valid business email'}, 401)                                    
            
        return f(*args, **kwargs)
    return decorated
