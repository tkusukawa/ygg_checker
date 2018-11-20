#! /bin/sh
egrep '^model name' < /proc/cpuinfo
echo
egrep '^MemTotal' < /proc/meminfo
echo
env -i df -hl --portability | ruby -pe 'sub(/^(\S+\s+\S+)\s+\S+\s+\S+\s+\S+\s+(\S+)/, "\\1 \\2")'
echo
cat /proc/version
