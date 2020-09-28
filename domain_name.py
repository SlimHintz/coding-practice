#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 08:14:18 2020
input is a URL name as a string. Returns the domain name as a string by itself.

@author: TjH
"""

def domain_name_verbose(url):
    if ('http://' or 'https://') in url and not 'www' in url:
        return url.split('//')[1].split('.')[0]
    elif 'www.' in url:
        return url.split('.')[1]
    elif 'www' and '//' in url:
        return url.split('//')[1].split('.')[1]

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
