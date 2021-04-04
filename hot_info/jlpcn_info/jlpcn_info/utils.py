import re

regex = r"\+\(\"(.*)\"\)\+"

test_str = "document.write('<input type=\"checkbox\" name=\"down_url_list_1\" class=\"down_url\" value=\"'+(\"magnet:?xt=urn:btih:6A680BBE004E650463D172D8CCCC393D8AD26DBD&dn=\\%e8\\%a5\\%bf\\%e7\\%8f\\%ad\\%e7\\%89\\%99\\%e8\\%be\\%b9\\%e5\\%a2\\%83\\%e6\\%8a\\%a4\\%e5\\%8d\\%ab\\%e9\\%98\\%9f\\%20\\%e7\\%ac\\%ac12\\%e9\\%9b\\%86--\\%e6\\%9b\\%b4\\%e5\\%a4\\%9a\\%e6\\%9b\\%b4\\%e6\\%96\\%b0\\%e7\\%9a\\%84\\%e7\\%ba\\%aa\\%e5\\%bd\\%95\\%e7\\%89\\%87\\%e8\\%af\\%b7\\%e8\\%ae\\%bf\\%e9\\%97\\%ae-\\%e5\\%a5\\%a5\\%e8\\%a7\\%86\\%e7\\%ba\\%aa\\%e5\\%bd\\%95\\%e7\\%89\\%87\\%e5\\%a4\\%a9\\%e5\\%9c\\%b0www.jlpcn.net.mkv&tr=http\\%3a\\%2f\\%2ftracker.gbitt.info\\%2fannounce&tr=http\\%3a\\%2f\\%2ft.nyaatracker.com\\%2fannounce&tr=udp\\%3a\\%2f\\%2fexplodie.org\\%3a6969\\%2fannounce&tr=udp\\%3a\\%2f\\%2ftracker.opentrackr.org\\%3a1337\\%2fannounce&tr=http\\%3a\\%2f\\%2fsukebei.tracker.wf\\%3a8888\\%2fannounce&tr=udp\\%3a\\%2f\\%2ftracker.coppersurfer.tk\\%3a6969\\%2fannounce&tr=udp\\%3a\\%2f\\%2ftracker.internetwarriors.net\\%3a1337&tr=udp\\%3a\\%2f\\%2ftracker.internetwarriors.net\\%3a1337\\%2fannounce&tr=udp\\%3a\\%2f\\%2fexodus.desync.com\\%3a6969\\%2fannounce&tr=udp\\%3a\\%2f\\%2fopen.stealth.si\\%3a80\\%2fannounce&tr=udp\\%3a\\%2f\\%2f9.rarbg.me\\%3a2730\\%2fannounce&tr=udp\\%3a\\%2f\\%2f9.rarbg.me\\%3a2730\\%2fannounce&tr=http\\%3a\\%2f\\%2fopen.acgnxtracker.com\\%2fannounce&tr=http\\%3a\\%2f\\%2ftracker2.itzmx.com\\%3a6961\\%2fannounce&tr=http\\%3a\\%2f\\%2fshare.camoe.cn\\%3a8080\\%2fannounce&tr=http\\%3a\\%2f\\%2fp4p.arenabg.com\\%3a1337\\%2fannounce\")+'\" file_name=\"西班牙边境护卫队 第12集\"checked />');"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

