# def line_count():
#     file = open("story.txt","r")
#     count=0
#     for line in file:
#         if line[0] not in 'T':
#             count+= 1
#     file.close()
#     print("No of lines not starting with 'T'=",count)
#
# line_count()
#

# def count_word():
#     fp=open('story.txt','r')
#     data=fp.read()
#     # print(data)
#     word=data.split()
#     # print(word)
#     count=0
#     for i in word:
#         count=count+1
#     print(count)   count_word()

# import logging
# logging.debug("This is debug")
# logging.info("This is info")
# logging.warning("This is warning")
# logging.error("This is error")
# logging.critical("This is critical")

# from logging import *
# basicConfig(filename='logfile.log')
# warning("Warning")
# error("Error")
# critical("Critical")

# from logging import *
# basicConfig(filename='logfile.log',level=DEBUG)
# debug("DEBUG")
# info("INFO")
# warning("WARNING")
# error("ERROR")

# from logging import *
# basicConfig(filename='logfile.log',filemode='w',format='%(asctime)s -%(levelname)s -%(message)s',datefmt='%a')
# warning("Warning")
# error("Error")
# critical("Critical")

from logging import *
basicConfig(filename='logfile.log',level=DEBUG,format='%(asctime)s -%(level)s -%(message)s',datefmt='%b')
debug("Debug")
info("Info")
warning("Warning")
error("Error")
critical("Critical")
