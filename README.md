# DogsTrust
Quick and Dirty Scraping Script to Quickly See New Dogs at DogsTrust

Written to run on MacOS - Notifications are probably pretty specific

Dependencies:
- csv
- requests
- bs4
- pync

There's no error checking in this - so run the following in the exec dir first:

    touch tmp_dogs_list.csv

I'm running this as a cronjob - suggest the following:

     */5 8-19 * * * ~/.../run.sh > /dev/null 2>&1
