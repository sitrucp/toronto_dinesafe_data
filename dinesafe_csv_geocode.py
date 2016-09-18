#Uses MapQuest's Nominatim mirror.

import anydbm
import urllib2
import csv
import json
import time

# set up the cache. 'c' means create if necessary
cache = anydbm.open('geocode_cache', 'c')

# Use MapQuest's open Nominatim server.
# http://developer.mapquest.com/web/products/open/nominatim
API_ENDPOINT = 'http://open.mapquestapi.com/nominatim/v1/search.php?format=json&q={}'

def geocode_location(location):
    '''
    Fetch the geodata associated with the given address and return
    the entire response object (loaded from json).
    '''
    if location not in cache:
        # construct the URL
        url = API_ENDPOINT.format(urllib2.quote(location))
        
        # load the content at the URL
        print 'fetching %s' % url
        result_json = urllib2.urlopen(url).read()
        
        # put the content into the cache
        cache[location] = result_json
        
        # pause to throttle requests
        time.sleep(1)
    
    # the response is (now) in the cache, so load it
    return json.loads(cache[location])

if __name__ == '__main__':
    # open the input and output file objects
    with open('dinesafe.csv') as infile, open('dinesafe_geocoded.csv', 'w') as outfile:
      
        # wrap the files with CSV reader objects.
        # the output file has two additional fields, lat and lon
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, reader.fieldnames + ['lat', 'lon'])
        
        # write the header row to the output file
        writer.writeheader()
        
        # iterate over the file by record 
        for record in reader:
            # construct the full address
            address = record['establishment_address']
            address += ', Toronto, ON, Canada'
            
            # log the address to the console
            print address
            
            try:
                # Nominatim returns a list of matches; take the first
                geo_data = geocode_location(address)[0]
                record['lat'] = geo_data['lat']
                record['lon'] = geo_data['lon']
            except IndexError:
                # if there are no matches, don't raise an error
                pass
            writer.writerow(record)