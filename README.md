# autobrr filter
* an autobrr filter to stop adding torrent when network is busy


## download 

```sh
git clone https://github.com/ccf-2012/autobrr_filter
# mkdir ~/autobrr_filter
# wget -O  ~/autobrr_filter/psfilter.py  https://raw.githubusercontent.com/ccf-2012/autobrr_filter/main/psfilter.py
```



## autobrr setup
* filter -> <your_filter> -> External -> Script section
    * COMMAND : python3
    * ARGUMENTS :  /home/<your_name>/autobrr_filter/psfilter.py



