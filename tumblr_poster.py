#!/usr/bin/python

import pytumblr
import os
import sys
import random
import shutil
import requests
from requests_oauthlib import OAuth1Session


def get_image(new_folder, used_folder):
	'''Return a random image name from the new images folder then move the image to the used folder.'''
	try:
		image_name = random.choice(os.listdir(new_folder))
	except:
		image_name = None
	else:
		shutil.move(new_folder + image_name, used_folder + image_name)

	return used_folder + image_name

def auth(client_key, client_secret, request_token_url, base_authorization_url, access_token_url, callback_uri):
	'''Create a tumblr OAuth session. If the user token and secret dont exist, request new tokens.'''
	if os.path.exists('./user_token') and os.path.exists('./user_secret'):
		token_file = open('./user_token', 'r')
		user_token = token_file.readline().strip()
		token_file.close()

		secret_file = open('./user_secret', 'r')
		user_secret = secret_file.readline().strip()
		secret_file.close()

	else:
		oauth_session = OAuth1Session(client_key,client_secret=client_secret, callback_uri=callback_uri)
		oauth_session.fetch_request_token(request_token_url)
		auth_url = oauth_session.authorization_url(base_authorization_url)
	
		print 'Please go here and authorize:\n', auth_url
		redirect_response = raw_input('Paste the full redirect URL here:\n')
		oauth_session.parse_authorization_response(redirect_response)
		oauth_tokens = oauth_session.fetch_access_token(access_token_url)

		user_token = oauth_tokens.get('oauth_token')
		user_secret = oauth_tokens.get('oauth_token_secret') 

		token_file = open('./user_token', 'w')
		print >>token_file, user_token
		token_file.close()

		secret_file = open('./user_secret', 'w')
		print >>secret_file, user_secret
		secret_file.close()

	client = create_client(client_key, client_secret, user_token, user_secret)

	return client

def create_client(client_key, client_secret, user_token, user_secret):
	'''Create a tumblr client session.'''
	client = pytumblr.TumblrRestClient(client_key, client_secret, user_token, user_secret)
	return client

if __name__ == '__main__':

	blog_name = None # change to blog name

	if not blog_name and len(sys.argv) > 1:
		blog_name = sys.argv[1]

	new_folder = './images/new/'
	used_folder = './images/used/'
	
	### OAuth details
	if os.path.exists('./consumer_key'):
		consumer_key_file = open('./consumer_key', 'r')
		consumer_key = consumer_key_file.readline().strip()
		consumer_key_file.close()
	else:
		print 'consumer_key file missing'
		sys.exit(1)

	if os.path.exists('./consumer_secret'):
		consumer_secret_file = open('./consumer_secret', 'r')
		consumer_secret = consumer_secret_file.readline().strip()
		consumer_secret_file.close()
	else:
		print 'consumer_secret file missing'
		sys.exit(1)

	request_token_url = 'http://www.tumblr.com/oauth/request_token'
	base_authorization_url = 'http://www.tumblr.com/oauth/authorize'
	access_token_url = 'http://www.tumblr.com/oauth/access_token'
	callback_uri = 'http://www.tumblr.com/dashboard'
	###

	client = auth(consumer_key, consumer_secret, request_token_url, base_authorization_url, access_token_url, 
					callback_uri)
	
	image_name = get_image(new_folder, used_folder)
	
	
	client.create_photo(blog_name, data=image_name)

