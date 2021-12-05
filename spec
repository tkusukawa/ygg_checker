#! /bin/sh
egrep '^model name' < /proc/cpuinfo
echo
egrep '^MemTotal' < /proc/meminfo |
    sed 's/[0-9][0-9][0-9] kB/XXX kB/'
echo
env -i df -hl --portability | 
  grep -v '/run/user/' |
  ruby -pe 'sub(/^(\S+\s+\S+)\s+\S+\s+\S+\s+\S+\s+(\S+)/, "\\1 \\2")'
echo
cat /proc/version
