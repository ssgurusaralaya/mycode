uflag='false'
cflag='false'
pflag='false'
hflag='false'
fflag='false'
dflag='false'
Dflag='false'
iflag='false'
aflag='false'
rflag='false'
files='false'
sflag='false'
oflag='false'

# Options
# f - Filename to parse
# h - Help

while getopts "D:a:o:f:c:u:p:hdisr" flag; do
 case "${flag}" in
   u) uflag="${OPTARG}" ;;
   d) dflag='true' ;;
   D) Dflag="${OPTARG}" ;;
   c) cflag="${OPTARG}" ;;
   p) pflag="${OPTARG}" ;;
   i) iflag='true' ;;
   r) rflag='true' ;;
   h) hflag='true' ;;
   s) sflag='true' ;;
   o) oflag="${OPTARG}" ;;
   a) aflag="${OPTARG}" ;;
   f) fflag="${OPTARG}" ;;
   #*) error "Unexpected flag ${flag}" ;;
   *)exit ;;
 esac
done

if [ $hflag == 'true' -o $# == '0' ]
then
echo ''
echo '==================================================================='
echo ' Options:'
echo ' -f : Filename to upload/download'
echo ' -c : CSP Name or IP Address'
echo ' -d : Download file from CSP'
echo ' -D : Delete a configured resource setting (DNS, Logging, etc...)'
echo ' -i : Get Info on all files hosted on CSP'
echo ' -a : Add a resource setting (DNS, Logging, etc...)'
echo ' -o : URI appendable Options'
echo ' -r : Get Info about CSP Resources (IP, dns, logging, etc...)'
echo ' -s : Get Services hosted on CSP'
echo ' -u : Username'
echo ' -h : Show Help Dialog'
echo ' '
echo ' Examples: ./csp_util.sh -f filename -u <username> -c <CSP Address>'
echo '           ./csp_util.sh -i -u <username> -c <CSP Address>'
echo '           ./csp_util.sh -s -u <username> -c <CSP Address>'
echo '           ./csp_util.sh -r -o dns_server -u <username> -c <CSP Address>'
echo "           ./csp_util.sh -a syslog_server -o '<server1> <server2>' -u <username> -c <CSP Address>"
echo "           ./csp_util.sh -D syslog_server -o '<server1> <server2>' -u <username> -c <CSP Address>"
echo '==================================================================='
echo ' '
exit
fi
my_https_proxy=$https_proxy
declare -x https_proxy=""
#start
# Read Password
echo -n Password for $uflag:
read -s pflag
echo
printf "\n"
if [ $aflag == 'syslog_server' ]; then
 printf "Updating Syslog Servers on $cflag\n"
 printf "\n"
 # Build syslog destination array
 read -a ip_array <<< $oflag
 ipcount=${#ip_array[*]}
 if [ $ipcount = '1' ]; then
   printf "Adding $oflag as syslog server to $cflag\n"
   curl -k -u $uflag:$pflag -X PATCH https://$cflag/api/running/resources/resource/csp-2100 -H "Content-Type: application/vnd.yang.data+json" -d "{\"resource\": {\"syslog_server\": {\"host\":\"$oflag\"}, \"rsyslog_udp_port\": \"514\"}}"
 elif [ $ipcount = '2' ]; then
   printf "Adding following syslog servers to $cflag:\n"
   printf "${ip_array[*]}\n"
   curl -k -u $uflag:$pflag -X PATCH https://$cflag/api/running/resources/resource/csp-2100 -H "Content-Type: application/vnd.yang.data+json" -d "{\"resource\": {\"syslog_server\": [{\"host\":\"${ip_array[0]}\"}, {\"host\":\"${ip_array[1]}\"}]}}"
 else
   printf "*** API Requires one or two syslog destination servers\n\n"
 fi
 printf "\n"
 printf "Setting Proxy: $my_https_proxy \n"
 declare -x https_proxy=$my_https_proxy
 exit
fi
 #
if [ $Dflag == 'syslog_server' ]; then
 printf "Deleting Syslog Servers on $cflag\n"
 printf "\n"
 # Build syslog destination array
 read -a ip_array <<< $oflag
#
for val in "${ip_array[@]}";
 do
  printf "Removing Server $val\n"
  curl -k -u $uflag:$pflag -X DELETE https://$cflag/api/running/resources/resource/csp-2100/syslog_server/$val -H "Content-Type: application/vnd.yang.data+json"
  printf "$val server removed\n"
 done
#
 #
 printf "\n"
 printf "Setting Proxy: $my_https_proxy \n"
 declare -x https_proxy=$my_https_proxy
 exit
fi
if [ $rflag == 'true' ]; then
 printf "Getting resource info for $cflag\n"
 printf "\n"
 if [ $oflag == 'false' ]; then
   curl -k -u $uflag:$pflag -X GET -H "X-Requested-With: XMLHttpRequest" https://$cflag/api/running/resources/resource/csp-2100/
 else
   curl -k -u $uflag:$pflag -X GET -H "X-Requested-With: XMLHttpRequest" https://$cflag/api/running/resources/resource/csp-2100/$oflag
 fi
 printf "\n"
 printf "Setting Proxy: $my_https_proxy \n"
 declare -x https_proxy=$my_https_proxy
 exit
fi
if [ $iflag == 'true' ]; then
 printf "Getting files hosted on  $cflag\n"
 printf "\n"
 curl -k -u $uflag:$pflag -X POST -H "X-Requested-With: XMLHttpRequest" https://$cflag/api/operational/repository/_operations/get_images -H "Content-Type:application/vnd.yang.data+json"
 printf "\n"
 printf "Setting Proxy: $my_https_proxy \n"
 declare -x https_proxy=$my_https_proxy
 exit
fi
if [ $sflag == 'true' ]; then                                                                                                        
 printf "Getting services hosted on  $cflag\n"                                                                                          
 printf "\n"                                                                                                                         
 curl -k -u $uflag:$pflag -X GET https://$cflag/api/running/services?deep
 printf "\n"                                                                                                                         
 printf "Setting Proxy: $my_https_proxy \n"                                                                                          
 declare -x https_proxy=$my_https_proxy                                                                                              
 exit                                                                                                                                
fi                            
if [ $dflag == 'false' ]; then
 printf "Uploading $fflag to $cflag\n"
 printf "\n"
 curl -k -u $uflag:$pflag -c csp_cookie.txt -X POST -H "X-Requested-With: XMLHttpRequest" https://$cflag/api/login
 printf "\n"
 curl -k -b csp_cookie.txt -F 'file=@'$fflag -X POST https://$cflag/api/uploadfile | cat
 printf "\n"
 curl -k -b csp_cookie.txt -X POST -H "X-Requested-With: XMLHttpRequest" https://$cflag/api/logout
 printf "\n"
 rm -f csp_cookie.txt
fi
if [ $dflag == 'true' ]; then
 printf "Downloading $fflag from $cflag\n"
 printf "\n"
 curl -k -u $uflag:$pflag -c csp_cookie.txt -X POST -H "X-Requested-With: XMLHttpRequest" https://$cflag/api/login
 printf "\n"
 curl -k -b csp_cookie.txt -o $fflag -X GET https://$cflag/api/getfile/image/$fflag
 printf "\n"
 curl -k -b csp_cookie.txt -X POST -H "X-Requested-With: XMLHttpRequest" https://$cflag/api/logout
 printf "\n"
 rm -f csp_cookie.txt
fi
printf "Setting Proxy: $my_https_proxy \n"
declare -x https_proxy=$my_https_proxy
