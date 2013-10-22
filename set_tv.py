# Markus Geyer
# Set.TV Coding Test
# 10/21/2013

import argparse
import datetime
import json
import urllib
import urllib2

"""
This Class handles the input and output of the script.
"""
class flickr_api:

	args = None
	flickr_api_key = "045fcd6ce31361d6ae26a0fe099f3190"
	flickr_url = "http://api.flickr.com/services/rest/?method=flickr.photos.search&%s"
	results = {}
	yahoo_app_id = '42ce6cfc281462a7b1c079ebe428bf6b'
	yahoo_url = "http://where.yahooapis.com/v1/places.q(%s);start=0;count=1?appid=%s&format=json"
	woeid = None


	"""
	Whenever the class is instantiated it will run from argument handling all the way to printing the output
	"""
	def __init__(self):

		self.handleInput()
		self.woeid = self.getWOEID(self.args.location)
		self.getFlickrResults()
		self.printResults()


	"""
	This method handles the argument parsing of the script
	"""
	def handleInput(self):

		parser = argparse.ArgumentParser(description="Allow user to query flickr for photos taken in a set location")
		parser.add_argument('location', help="String of desired location")
		parser.add_argument('-t', '--tags', action='store_const', const=True, default=False, help="Group Count by Tags: (default=False)")
		parser.add_argument('-d', '--dates', metavar=('Start', 'End'), nargs=2, help="Start and End Date of Query")

		self.args = parser.parse_args()


	"""
	Given a location this method requests the WOEID using the Yahoo GeoLocation API
	"""
	def getWOEID(self, location):

		loc = json.loads(urllib2.urlopen(self.yahoo_url % (location, self.yahoo_app_id)).read())
		return loc['places']['place'][0]['woeid']


	"""
	Makes requests to the Flickr API and then sends its results to the aggregating function
	"""
	def getFlickrResults(self):

		now = datetime.datetime.now()
		one_week_ago = now - datetime.timedelta(days=7)

		args = {
			'api_key' : self.flickr_api_key,
			'woe_id' : self.woeid,
			'extras' : 'tags, date_taken',
			'format' : 'json',
			'nojsoncallback' : 1,
			'min_taken_date' : one_week_ago,
			'max_taken_date' : now
		}

		if self.args.dates:
			if self.args.dates[0]:
				args['min_taken_date'] = self.args.dates[0]
			if self.args.dates[1]:
				args['max_taken_date'] = self.args.dates[1]

		
		results = json.loads(urllib2.urlopen(self.flickr_url % (urllib.urlencode(args))).read())
		self.aggregateResults(results['photos']['photo'])

		if results['photos']['pages'] > 1:
			for page_number in range(2, results['photos']['pages'] + 1):
				args['page'] = page_number
				results = json.loads(urllib2.urlopen(self.flickr_url % (urllib.urlencode(args))).read())
				self.aggregateResults(results['photos']['photo'])


	"""
	Takes in the data from getFlickrResults and then accumulates the data into a dictionary
	"""
	def aggregateResults(self, photos):

		for photo in photos:
			timestamp = datetime.datetime.strptime(photo['datetaken'], '%Y-%m-%d %H:%M:%S')
			date = datetime.datetime.strftime(timestamp, '%Y-%m-%d')
			if self.args.tags:
				self.results[date] = self.results.get(date, {})
				for tag in photo['tags'].split(' '):
					self.results[date][tag] = self.results[date].get(tag, 0) + 1
			else:
				self.results[date] = self.results.get(date, 0) + 1			


	"""
	Prints in a sorted fashion the final results
	"""
	def printResults(self):
		if self.args.tags:
			for key in sorted(self.results.iterkeys()):
				print key
				for tag in sorted(self.results[key].iterkeys()):
					print "    %s : %s" % (tag, self.results[key][tag])
		else:
			for key in sorted(self.results.iterkeys()):
				print "%s : %s" % (key, self.results[key])
				sorted_result = (key, self.results[key])


flickr_api()
