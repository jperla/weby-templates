#!/usr/bin/env python 
from BeautifulSoup import BeautifulSoup
import sys

soup = BeautifulSoup(sys.stdin.read())
sys.stdout.write(soup.prettify())
