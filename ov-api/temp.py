# import time
# import datetime
# #d = datetime.date(date())
#
# d=(datetime.datetime.now())
#
# unixtime = time.mktime(d.timetuple()) * 1000 -200
# print(type(unixtime))



# {"TelnetGenericRequestObject":{"requestType":"delete","objectType":"ScriptingLogFile","valueObjects":[
# {"ScriptingLogFileVO":{"fileName":"health_check_script-20200730_15-54-45.log","ipAddress":"10.255.128.208","macAddress":"e8:e7:32:fb:76:c3"}},
# {"ScriptingLogFileVO":{"fileName":"show_system_script-20200730_15-47-33.log","ipAddress":"10.255.128.211","macAddress":"e8:e7:32:24:4c:aa"}},
# {"ScriptingLogFileVO":{"fileName":"show_system_script-20200730_15-46-06.log","ipAddress":"10.255.128.208","macAddress":"e8:e7:32:fb:76:c3"}},
# {"ScriptingLogFileVO":{"fileName":"show_system_script-20200730_15-46-05.log","ipAddress":"10.255.128.209","macAddress":"e8:e7:32:de:93:07"}},
# {"ScriptingLogFileVO":{"fileName":"show_system_script-20200730_15-44-47.log","ipAddress":"10.255.128.209","macAddress":"e8:e7:32:de:93:07"}},
# {"ScriptingLogFileVO":{"fileName":"show_system_script-20200730_15-44-47.log","ipAddress":"10.255.128.208","macAddress":"e8:e7:32:fb:76:c3"}},
# {"ScriptingLogFileVO":{"fileName":"kaveh-script-20200619_16-19-01.log","ipAddress":"10.255.128.211","macAddress":"e8:e7:32:24:4c:aa"}}
# ]}}



# {'TelnetGenericRequestObject': {'requestType': 'delete', 'objectType': 'ScriptingLogFile', 'valueObjects': [
# {'ScriptingLogFileVO': {'fileName': 'health_check_script-20200730_15-54-45.log', 'ipAddress': '10.255.128.208', 'macAddress': 'e8:e7:32:fb:76:c3'}},
# {'ScriptingLogFileVO': {'fileName': 'show_system_script-20200730_15-47-33.log', 'ipAddress': '10.255.128.211', 'macAddress': 'e8:e7:32:24:4c:aa'}},
# {'ScriptingLogFileVO': {'fileName': 'show_system_script-20200730_15-46-06.log', 'ipAddress': '10.255.128.208', 'macAddress': 'e8:e7:32:fb:76:c3'}},
# {'ScriptingLogFileVO': {'fileName': 'show_system_script-20200730_15-46-05.log', 'ipAddress': '10.255.128.209', 'macAddress': 'e8:e7:32:de:93:07'}},
# {'ScriptingLogFileVO': {'fileName': 'show_system_script-20200730_15-44-47.log', 'ipAddress': '10.255.128.209', 'macAddress': 'e8:e7:32:de:93:07'}},
# {'ScriptingLogFileVO': {'fileName': 'show_system_script-20200730_15-44-47.log', 'ipAddress': '10.255.128.208', 'macAddress': 'e8:e7:32:fb:76:c3'}}
# ]}}




header_item1={'ScriptingLogFileVO':{}}
header_item1['ScriptingLogFileVO'].update({'fileName':"myfile"})
header_item1['ScriptingLogFileVO'].update({'Ipaddr':"myip"})


print(header_item1)


# header_start={"TelnetGenericRequestObject":{"requestType":"delete","objectType":"ScriptingLogFile","valueObjects":[]}}
# header_item1={"ScriptingLogFileVO":{"fileName":"health_check_script-20200730_15-54-45.log","ipAddress":"10.255.128.208","macAddress":"e8:e7:32:fb:76:c3"}}
# header_item2={"ScriptingLogFileVO":{"fileName":"show_system_script-20200730_15-46-05.log","ipAddress":"10.255.128.209","macAddress":"e8:e7:32:de:93:07"}}
#
# header_start['TelnetGenericRequestObject']['valueObjects'].append(header_item1)
# header_start['TelnetGenericRequestObject']['valueObjects'].append(header_item2)
#
# print(header_start)
