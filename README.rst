Tumblr Image Poster
===================

Description:
------------
Post a random image to a tumblr blog using OAuth1.
Reads images from ./images/new/ and moves used images to ./images/used/.

Usage:
------
.. code-block:: pycon
	>>> python tumblr_poster.py

Register as an App with tumblr to get the client token and secret key. Save the client key in a file named 'consumer_key' and the secret as 'consumer_secret'.

Can be run as a cron job but it has to be running from the same directory as the script. An example:
.. code-block:: bash
	$ 0 0 * * * cd /home/user/poster; /usr/local/bin/python /home/user/poster/tumblr_poster.py ablog

Dependencies:
-------------
| requests (http://docs.python-requests.org/en/latest/)
| requests_oauthlib (https://github.com/requests/requests-oauthlib)
| pytumblr (https://github.com/tumblr/pytumblr)

License:
--------

The MIT License (MIT)

Copyright (c) 2013 Imad Mouhtassem

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
