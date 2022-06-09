import wget
import shutil
import datetime
import time
# Seconds between updates
wait_period = 300
# Image URL
url = 'https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/2500x1500.jpg'
# Startup Art
art = """
              _,\?dZkMHF&$*q#b..
          .//9MMMMMMM?:'HM\\"`-''`..               \ \ 
       ..`  :MMMMMMMMMMHMMMMH?_    `-\           o{  ]  GOES-16
     .     .dMMMMMMMMMMMMMM'"'"       `\.          \ \ 
    .       |MMMMMMMMMMMMMR              \\ 
   -        T9MMMMMHH##M"                `?
  :          (9MMM'    !':.               &k
 .:            HMM\_?p "":-b\.            `ML
-                "'"H&#,       :           |M|
:                     ?\,\dMH#b#.           9b
:                        |MMMMMMM##,        `*
:                   .   +MMMMMMMMMMMo_       -
:                       HMMMMMMMMMMMMMM#,    :
"""

i = 0

print (art)

for value in range (10):
	# Download new image
	filename = wget.download(url)
	# Replace old image
	shutil.move('2500x1500.jpg', '/home/phares/Pictures/Wallpapers/latest.jpg')
	now = datetime.datetime.now()
	print(' SATELLITE IMAGERY UPDATED')
	# Print update time
	print(str(now))
	time.sleep(wait_period)

print (str(value) + ' instances reached')
