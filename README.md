# Yuyu Scanner

<img src='https://raw.githubusercontent.com/justakazh/Yuyu_Scanner/master/y.png'>

Yuyu Scanner is a Web Reconnaissance & Web Analysis Scanner to find assets and information about targets.


I'm a Bad Coder, so dont expect to much 😵




## Preview 

### GUI
This Gui is made using Electron JS and Bootstrap<br>
<img src="https://raw.githubusercontent.com/justakazh/Yuyu_Scanner/master/Screenshot_7.png">
NOTE : COMING SOON FOR GUI VERSION :P

### CLI
This CLI was created using the python language program
<img src="https://raw.githubusercontent.com/justakazh/Yuyu_Scanner/master/Screenshot_8.png">

### REPORTING
<img src="https://raw.githubusercontent.com/justakazh/Yuyu_Scanner/master/Screenshot_9.png">
NOTE : COMING SOON FOR REPORTING :P

## Features 
- Available for Gui Version
- Subdomain Discovery with Passive Method from Public Api

                http://web.archive.org/
                https://threatcrowd.org/
                https://urlscan.io/
                https://rapiddns.io/
                https://otx.alienvault.com/
                https://dnsdumpster.com/
                https://crt.sh/
                https://api.threatminer.org/
                https://api.certspotter.com/
                https://api.hackertarget.com/
                https://riddler.io/
                http://index.commoncrawl.org/
                
- Port scanning with NMAP
- Url Discovery from waybackurl
- IP Discovery 
- Title Discovery of target
- Web Server Check
- Common sensitive files Discovery
- Status code Discovery from subdomain result 
- Reverse IP with Passive Method  from Public Api
- Checking Live Host and IP Address
- Email Address Discovery with Passive Method from Public Api
- WHOIS Lookup 
- Missing Security Headers Check
- CORS Missconfiguration Check 
- Save all Discovery result
- Generate HTML Report
- Generate JSON Report
- You can use Stdin for mass scanning 
  - cat domain.txt | yuyu.py [arg]
- Custom ur timeout

## Usage
- Basic Arguments:

                ~$ python3 yuyu.py -u domain.com [arg]
                ~$ cat domain.txt | yuyu.py [arg]

                -h, --help            show this help message and exit
                -u URL, --url URL     Target URL
                -f FILE, --file FILE  Target URL
                -g, --gui             Run Yuyu in Gui Mode
                -cl, --checklive      Check host live or not
                -ci, --collectinginformation
                                    Collecting Information
                -sh, --securityheaders
                                    Check For Missing Security Headers
                -ri, --revip          Reverse IP from target URL
                -ws, --whois          Whois Lookup from target URL
                -cu, --collecturl     Collect URL from WaybackURL
                -ed, --emaildiscover  Email Discovery
                -sp, --scanport       Port Discovery from Discovery IP
                -cc, --corscheck      CORS missconfiguration Check
                -fs, --filesensitive  Find Sensitive Files from Subdomain Result
                -to [TIMEOUT], --timeout [TIMEOUT] Timeout for requests, default : 5

## Publication
- https://www.researchgate.net/publication/352295423_PENGEMBANGAN_APLIKASI_INFORMATION_GATHERING_MENGGUNAKAN_METODE_HYBRID_SCAN_BERBASIS_GRAPHICAL_USER_INTERFACE

## Contact me
- [akazh](https://twitter.com/akazh18/) - Twitter

## References
- https://github.com/screetsec/Sudomy
- https://github.com/aboul3la/Sublist3r

## Credits & Thanks
- [Deddy Hariyadi](https://www.instagram.com/milisd4d/) 
- [Redho Maland](https://github.com/screetsec/)
