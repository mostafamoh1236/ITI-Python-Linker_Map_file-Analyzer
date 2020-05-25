import sys
import os.path
import re



def main():
  for index in range(1,len(sys.argv)):
    textSize   = 0
    rodataSize = 0
    dataSize   = 0
    bssSize    = 0
    map_Handler = open('Project_Memory_Map_File.map','r')
    map_Handler.seek(0)
    lines = map_Handler.read()
    matchBss    = re.findall(r'\+(\w+)\s+.bss\s+'+sys.argv[index],lines)
    matchRodata = re.findall(r'\+(\w+)\s+.rodata\s+'+sys.argv[index],lines)
    matchData   = re.findall(r'\+(\w+)\s+.data\s+'+sys.argv[index],lines)
    matchText   = re.findall(r'\+(\w+)\s+.text\s+'+sys.argv[index],lines)
    for j in matchText:
      textSize = textSize + int(j,16);
    for j in matchBss:
      bssSize = bssSize + int(j,16);
    for j in matchRodata:
      rodataSize = rodataSize + int(j,16);
    for j in matchData:
      dataSize = dataSize + int(j,16);
    
    mod_handler = open(sys.argv[index]+'_info.txt','w')
    mod_handler.write('               ***** '+ sys.argv[index] +' component Info *****\n')
    mod_handler.write('Size of .text    section in '+sys.argv[index] +'component is = '+str(textSize)+' Bytes\n')
    mod_handler.write('Size of .rodata  section in '+sys.argv[index] +'component is = '+str(rodataSize)+' Bytes\n')
    mod_handler.write('\n')
    mod_handler.write('Size of .data    section in '+sys.argv[index] +'component is = '+str(dataSize)+' Bytes\n')
    mod_handler.write('Size of .bss     section in '+sys.argv[index] +'component is = '+str(bssSize)+' Bytes\n')
    mod_handler.write('\n')
    mod_handler.write('-> Size of ROM in '+sys.argv[index]+' component is = '+str(textSize+rodataSize)+' Bytes\n')
    mod_handler.write('-> Size of RAM in '+sys.argv[index]+' component is = '+str(bssSize+dataSize)+' Bytes\n')
  return
  
if __name__ == '__main__':
  main()