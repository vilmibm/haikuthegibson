#!/usr/bin/env python
# This program is part of haikuthegibson.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import sys

from prosaic.generation import poem_from_template
from prosaic.models import Database
import tweepy

import haikuthegibson.secret as secret

HAIKU_TEMPLATE = [{'syllables': 5},
                  {'syllables': 7},
                  {'syllables': 5},]

DATABASE = Database()
# LOL
CORPUS_ID=6

def get_auth():
    auth = tweepy.OAuthHandler(secret.API_KEY, secret.API_SECRET)
    auth.set_access_token(secret.ACCESS_TOKEN, secret.ACCESS_SECRET)
    return auth

def get_api_client(auth):
    return tweepy.API(auth_handler=auth)

def main():
    twitter_auth = tweepy.OAuthHandler(secret.API_KEY, secret.API_SECRET)
    twitter_auth.set_access_token(secret.ACCESS_TOKEN, secret.ACCESS_SECRET)

    twitter_client = tweepy.API(twitter_auth)

    poem_lines = poem_from_template(HAIKU_TEMPLATE, DATABASE, CORPUS_ID)
    poem_raw_lines = map(lambda l: l['raw'], poem_lines)

    try:
        return twitter_client.update_status(status='\n'.join(poem_raw_lines))
    except tweepy.error.TweepError as e:
        return e

if __name__ == '__main__':
    result = main()

    if isinstance(result, tweepy.error.TweepError):
        code = 1
    else:
        code = 0

    sys.exit(code)
