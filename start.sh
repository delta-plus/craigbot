#!/bin/bash

mapfile -t < $1
for i in {0..9}
do
  python autocraig.py "${MAPFILE[$i]}" $2 account1@email.com password1
  sleep 120s 
  # Can't post too fast.
done

mapfile -t < $3
for i in {0..9}
do
  python autocraig.py "${MAPFILE[$i]}" $4 account2@email.com password2
  sleep 120s
  # Two accounts posting at once for maximum efficiency.
done

find_missing () {
  grep -oh "\w*.craigslist*\w*" /var/www/html/links.html > /home/user/craigbot/received
  grep -v -f /home/user/craigbot/received /home/user/craigbot/$1 > /home/user/craigbot/fix1
  grep -v -f /home/user/craigbot/received /home/user/craigbot/$3 > /home/user/craigbot/fix2
  mapfile -t < /home/user/craigbot/fix1
  for i in {0..$(cat /home/user/craigbot/fix1 | wc -l)}
  do
    python autocraig.py "${MAPFILE[$i]}" $2 account1@email.com password1
    sleep 120s
  done
  mapfile -t < /home/user/craigbot/fix2
  for i in {0..$(cat /home/user/craigbot/fix2 | wc -l)}
  do
    python autocraig.py "${MAPFILE[$i]}" $4 account2@email.com password2
    sleep 120s
  done
  fix_missing
}

if [$(cat /var/www/html/links.html | sed '/^\s*$/d' | wc -l) -ne 20]
then
  fix_missing
  # Double check if you missed a spot.
fi
