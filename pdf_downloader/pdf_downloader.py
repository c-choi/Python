# import requests
# for i in range(20170101, 20170331):
#     res = requests.get('http://www.koreafashion.org/newsletter2/file/special_report_' + str(i) + '.pdf')
#     try:
#         res.raise_for_status()
#         playFile = open(str(i) + '.pdf', 'wb')
#         for chunk in res.iter_content(100000):
#             playFile.write(chunk)
#         playFile.close()
#     except Exception as exc:
#         # print('There was a problem: %s' % (exc))
#         continue


## Pork Price PDF Download##
import requests
# d = {
# "August-25",
# "August-18",
# "August-11",
# "August-4",
# "July-28",
# "July-21",
# "July-14",
# "July-7",
# "June-30",
# "June-23",
# "June-16",
# "June-9",
# "June-2",
# "May-26",
# "May-19",
# "May-12",
# "May-5",
# "April-28",
# "April-21",
# "April-14",
# "April-7",
# "March-31",
# "March-24",
# "March-17",
# "March-10",
# "March-3",
# "February-24",
# "February-17",
# "February-10",
# "February-3",
# "January-27",
# "January-20",
# "January-13",
# "January-6"}

# for i in d:
for i in range(20170101, 20170901):
    # res = requests.get('http://www.porkretail.org/filelibrary/' + str(i) + '-Pork-Price-Summary.pdf')
    res = requests.get('http://www.porkretail.org/filelibrary/Retail/WeeklyPriceSummaries/'+ str(i) + '%20Pork%20Price%20Summary.pdf')
    try:
        res.raise_for_status()
        playFile = open(str(i) + '.pdf', 'wb')
        for chunk in res.iter_content(100000):
            playFile.write(chunk)
        playFile.close()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
        continue