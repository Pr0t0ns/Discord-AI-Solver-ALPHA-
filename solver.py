import time
import httpx
import json

site_key = "4c672d35-0701-42b2-88c3-78380b0db560" # Current Discord Sitekey
sc = "1"
swa = "1"
host = "discord.com"
v = "90ee353"
hl = "en"
url_payload = f"v={v}&host={host}&sitekey={site_key}&sc={sc}&swa={swa}" # URL payload 

headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "text/plain",
    "origin": "https://newassets.hcaptcha.com",
    "referer": "https://newassets.hcaptcha.com/",
    "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.33 Safari/537.36"
}
data = httpx.post(f"https://hcaptcha.com/checksiteconfig?{url_payload}", headers=headers) # Fetches Token so we can get the captcha

if data.status_code == 200:
    req_JWT = data.json()['c']['req']
else:
    print("Error Checking Site Config!")
    exit(0)

url = f'https://hcaptcha.com/getcaptcha?s={site_key}'
unix_time = int(time.time())
end_unix = unix_time + 165
motion_data =  """{"st":1654819909761,"mm":[[127,57,1654820005472],[85,39,1654820006425],[98,54,1654820006441],[108,62,1654820006457],[114,65,1654820006477],[117,65,1654820006494],[120,65,1654820006513],[125,64,1654820006529],[127,62,1654820006547],[128,60,1654820006569],[129,57,1654820006585],[129,54,1654820006604],[129,54,1654820006668]],"mm-mp":13.818181818181818,"md":[[129,54,1654820006668]],"md-mp":0,"mu":[[129,54,1654820006724]],"mu-mp":0,"v":1,"topLevel":{"st":1654819909596,"sc":{"availWidth":1920,"availHeight":1040,"width":1920,"height":1080,"colorDepth":24,"pixelDepth":24,"availLeft":0,"availTop":0,"onchange":null,"isExtended":false},"nv":{"vendorSub":"","productSub":"20030107","vendor":"Google Inc.","maxTouchPoints":0,"scheduling":{},"userActivation":{},"doNotTrack":null,"geolocation":{},"connection":{},"pdfViewerEnabled":true,"webkitTemporaryStorage":{},"webkitPersistentStorage":{},"hardwareConcurrency":12,"cookieEnabled":true,"appCodeName":"Mozilla","appName":"Netscape","appVersion":"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.33 Safari/537.36","platform":"Win32","product":"Gecko","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.33 Safari/537.36","language":"en-US","languages":["en-US"],"onLine":true,"webdriver":false,"bluetooth":{},"clipboard":{},"credentials":{},"keyboard":{},"managed":{},"mediaDevices":{},"storage":{},"serviceWorker":{},"wakeLock":{},"deviceMemory":8,"ink":{},"hid":{},"locks":{},"mediaCapabilities":{},"mediaSession":{},"permissions":{},"presentation":{},"serial":{},"virtualKeyboard":{},"usb":{},"xr":{},"userAgentData":{"brands":[{"brand":".Not/A)Brand","version":"99"},{"brand":"Google Chrome","version":"103"},{"brand":"Chromium","version":"103"}],"mobile":false,"platform":"Windows"},"plugins":["internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer"]},"dr":"","inv":false,"exec":false,"wn":[],"wn-mp":0,"xy":[],"xy-mp":0,"mm":[[8,605,1654820005471],[149,100,1654820005999],[145,140,1654820006015],[144,172,1654820006031],[136,197,1654820006047],[116,228,1654820006063],[78,278,1654820006080],[26,343,1654820006096],[0,539,1654820006424]],"mm-mp":37.11918063314712},"session":[],"widgetList":["0maqaos1ws6g"],"widgetId":"0maqaos1ws6g","href":"https://discord.com/register","prev":{"escaped":false,"passed":false,"expiredChallenge":false,"expiredResponse":false}}"""

motion_data = motion_data.replace('"st":1654819909761,"mm"', f'"st":{unix_time},"mm"')
motion_data = motion_data.replace('"st":1654819909596,"sc"', f'"st":{end_unix},"sc"')
 
n = "4311b4d55c329777a91ed79eb81570fb37a0c197eefe42933c8fda2ca06f0fb888e33c472de545f86bbc373e2413787967e968f842042e26569215f94cc868c4f20c005b285428e029e9996f1763f337cefac82de6aacbb09d64062c7e2b35c8462c964fec9609cf16e74b6ec7d981feb4161498b166828b68363da675a186e15e0347edb7523ed911664492218563cc23d82273d2bd3916a53e6885b0c6752450723311a65ddaa63a57630e784511123c87b721c52ac368c1ccd69ec84e6f1b20a9fa04ca79839172daf1d52dab4b33adee02563d611c7b1e9a3dcea50050704685a4dba0a79de194c34f267eadf7e061b7d2b733c6b96f0f37de35462d8b68e2324dea864e6b55f417330b1d989d28cf6f2794f18ccb3735935e3a03004c14f5520ba129d0d61ad1507d1fb8dc83c07c3d83f837d7d401be1fe03afe57530690e96f11ba59136a3a7c0c122951ca6f6384c94ebc6a94ae0a5a0c430ac6f51dba80dc96252880183b1a4d8b7960a9e24fab8b2dd6ad520458e65efc7382272a00d6bdd24dc3f29691c8e0b88253cc8eadf3fb4681a635bc78779ebf05996beab3ae0f179b9cfbdee6571bf284704769e7605bd381c4cf3026600cd58d427e47bbf37318fd9a151bcac1402e29915d96133a9b97b04bff3562e829e68de4122cd28075da5b73f3c61d5f01cf81db2435369cd2879d061574c5da2026bac25b118daafdfbc0ca5aaafacfc240b555eb18a4cb6dd2f1e6cbb90d8425f449dd5fc78d9f878b0c9a6b8cd08401fd242952b8787b0ea910be3a93474fe33071b338541bd4530b7049518a14249ddd44cae31a56a63600bfdfe7719024e2d318fbaeccc3e305c2d374efbd14554f40f6f1185cc6511f1cb667a8bda6537ff5b41f8fd0b3d80fe9f60990eb2a4283100d04b05815fa84b3f5e71e1d153a0dd1535aa0376b4737e86e90bebafcb476233bdb7574c378732a7784698cf64777f181890b292024dc0771b52245fe89c311babc4e691b9fa0a092a24b288a19b470165b0511c4cb7fad12400ef025124a0958d991553d2d5c571372c75069887cd1e222e4ca508a65dd2f09b827649764a2bcd962dcb37967c5da8b1a306c4b96fe327dd5853167d1e0f69e1f42e78b8cb24df3484d589018281cb4746782ec5c9f0ae63940084e7b341e293b5449d4af4bb072660ff008735f1fb57b8d2fa84c9d817f3905a73385d973664135f8ba0e12d0067f94df9e26b33ba4fcb97f7f93728d6a048fad849b5a27016f870aa096db1fe14d58a4f6fdfa2d0cfa34891d63f97eb96b992708df5bacc75dccb7fa533a65856757afa17ad95086f597d0c07667535a795d3b9f12d2283e32b0efbdb3971de02b88c18e511d1bb2c80074eadf6d81038d600633f927b6109bf0c4535d4901448b3baa44a23fbfb3d9fcf9509f03d3d4b2426621739781facca7795978e150b07ce1152dd539d439d47d246031dbb411adc340cf68ad78ac67341cc84d2307d4a86e5ac385b02c0f87c37dd27b013c121cc981597e4833a386517cde4fb4bc11fc22ab28768600525803b4bbf1f927877a2a6a2e7ec46cc78bc6fd4152894f9fa71db4f08c572f2d994046ece210236762453b885ea81323c11f4c04b475b2c1fa37c0c1d19fdfae876250952a0b9a7d43b18e3de95295258c101933c63ac52859e4cebbcf86acc68eebd48ed0e9dd2b59372b662d1f7afa6fef4fb7d6812925f221d865d751b30d5b2e4d753354bbba32f79e7b48f1403322929a0ff3e1af5ff914e1e648775e21e674e2da274caeff572e1f316032d37cba7a11b3b747ee118ba43f36efa3cb9bc943f71188c23ada84956caa76b5c1d3bfe8094fe8173cefa6b36f7e40c5746ad14100059cd3b2efda727dcae99014fdec5911583a577a99549506164200d01ecb4323ba05c92ab5d0fdd3fad5f5eaf80bd1f2a02198e09f7a70ebb11e087430b58b850574c9ea132030e0ff321784357c4e0675f774aab7748dce8ef8f7529edf3c52ffac2fb39bfc35cbbfc39738a6286b5b4e1131d2721d104786c91dd02a27643bc7e9c7821956f3c93b0666a58df16ff4d87e333e1241e0561bc268892a9859f699ae893d4cb1368eaab93824a1236a99d8cfd71a2393402d34ee43b0220952002fb6cacc95c9484ac6eea4b008a6d604e9747051ba3d3775fbcf3fa5ac5eb5f746a479411b5b44811db76fd4f9f0d47dbfc3a30d6cb10a161275b040ba20c3d1fe3ee5ee69b78cbf5ce035bf7c24c1920903c7e6e090a794993aa540140a888cb5ba49152ad5beddda1b31c86ad87f255eba35dd34d91bdb7f91a70e32bf26f4ca494039f9e163dc8ac75160da66df72a614a942f34a8daf6eb8530693b33b0f7fcd052fcd9bb0e3d79d9e4f04b9e7f127dfe62744cf33c5f0c0fab89c7fb9e26a43e15d9022c4534b73bc8af1cc902289ee5e85f3f23faafdb11aaccd12cdf271107817dbf4f7c928eb18f4b5412cf31e73424152850b9ce5572a5ff74ac07b8732920f4ef46fb9118a59a206e7900c78bf7e9c37bffb60ed87ecc596ff3fc248d35c228f2917faa3e541ee36c7784bda3273bf39586c2d0e41cac4c7fabfc790e436b2721f86b1b43d1f41bd5625572566b221d7da2844c1f98b6b8bc715d919d9588bfc97a7a19ad402e67e25d73bd8594a4c4451ef9ea2e73a9d4345e786219bd119743a0ab1f2a8469633243f2808db9904c44d7fcec2ed21a445261ea8f6c232c16ad1ab21c5d53ffb4c98e5670879a7440bfe9e2079c9e7d5ff91e97f67fd9f7166899a95089e86db54709e7854cddf75a9ee2ce4ac020768a8d126c05ada7f888d277e75916fa549ccda277f8ca8b65ca5330e2ad5ac351f06ad374f84f4e6825f96eab74dad6f08c5d541650b6dd2a18680b8dd06c2734f76f6b20e82c7cee80a5c3acbd3955297c7e55048098905e1973b20c463e4d1328126ba3dfa27a67fe8bdca23e642a2cafac03b47b8be7fc42851325e19f3ed7eb2bedb4bb9d3a1b4cf22e1bbcbe154eba98ae4634fbbd6d57ecc67ea150d6d0eb6db9be8d3e23bb4d2e527614f9897c4bba80390949cdeaeaa900ac1ddfcc739bdf03671931144bf3fd0466b58bc0d553ae9c56e7b745edf203db08ea3ec271de1c901d3aaabc8a3d5853a41fb5d7150139f5a93fe6a597c5bbbc18d692fccd4884c533327dc9b1379babab2416fb25f6333d4bcebaedee5b823f7468ce1878aa29a85ef93acaa399990d713ec2292c25373190e233775ae52b9763d0d43d1b8ffd6b01f7dfe632ec9d7d69e3c958767054cb482e04f36cee2fb82b1633ee1286070849c60c28e18ca426281bb69a43e7be9f99fa200b9c7a18404ab68b270b97a857c68625fe68d7ca24ea18c8fca44b886c9c6eca324f9db516ee8e2dcae044bf813656a51799288c11d50bc22f4ce1a17492a271ead45d522248d7cb57a43d79f62b68c7f59a7585f7e7cb84d8b5441b2b4843cf0f912ee2f3e608043787a0000a841b1d9d9614d4a5e8887a89ffd0c6dc63037f3a12c5e0b19d8d5c572fb7cf743e24d41618085b8edc53ccc80124688b37f28498d79227f7481f0cc48486e88ec1de9c16b970216abbad2599b85e34e6c5aaf935eaf5be4bef5ec90f826d837bcffc1c2d7b3f5170d744c10cb0a91e156c0517c666a2263b653df9f7bf840413b013b510193abe01b7054f05808dd6bcec4c95663f383232ee60c194174ede45bb0fe705c40717057c56eb5319de9fe985b5c8164febf1805e479a4d1515ecdfad00d13728d2c09fe6190a2145ad8d5dd3fa7d21df03e2015e88b489fdf1945fabe8d9c12b5f3ea38aa3e5ea500060e647d3492163e41b7760c57708f0e9bad15eda02fb546a66d815ac3719f42ffbed655055aadc9cef44bd3b90e83f13bdeb40170f011dfcda726b5eba2634927d9d04cfc11a6d8d49caf426ec5c526559d839ffd4e7be6eb22fb7b8129b83ef06c9352225aaa474a085378b9a2f978e1e332cef6163f1ad9f61bab92a97c093d7c189e40e3dbb5619b004042f17453934d4fab5fe90cee609f3fe40b38cd808a97cc4f5ff0d5be2870467f513be7e8c483473e607deda2f3907b32bee85c3d448af23d099faa381e232d90aba61f99fc8e48e6397425f48c2f50280717a7066efcc691716226e996cfd3a45dffe8c198b0f015af213f5fa90cbcdd69d1eae9cc1c71ffc01d7b26877564394b2aa03d4a9a58778ccadbeb1ff5107886f598e5fa8ab06ca68e658074f0adf472f024a7ef0ec63a80e5f5b5fe9386bf53ed9848442556d15c4f24baae891d50977aeb56993f41f260e932c0c763efcaa22603b3a3b100023a6e81612bb20ba006df2962567b0c0ccbfcfe3b9464f149d98c5983c134f5e9e245472632e182490fbed0654829d327ee7e90b234227cdabc283e4d09160a2c6dba9e52c3811ba31a668cd3830cddb9477d53140ff02e17b8d87f82a0ee76cdc4a3b6ae5772b855c79ee85503513f4afed48fc3df3ec5ab42452c4257afa7b49c38d0ecc27360e2de835268b756de1de4028b486821ed29da6b00"
headers = {
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://newassets.hcaptcha.com",
    "referer": "https://newassets.hcaptcha.com/",
    "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.33 Safari/537.36"
}

payload = {
    "v": v,
    "sitekey": site_key,
    "host": host,
    "hl": hl,
    "motionData": motion_data,
    "n": n,
    "c": {"type": "hsw", "req": f"{req_JWT}"}
}
print(payload)
data = httpx.post(url, headers=headers, data=payload) # Error Here. Thrown Error ->  ({'c': {'type': 'hsw', 'req': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmIjowLCJzIjoyLCJ0IjoidyIsImQiOiJYL0h2bmhjQy9ldlhlWkU1MmFES1hBQ1orb2RONkN3VUdCcVZQYU5kOEhOTTY5ZlBkWTIwSjREU0pQODYvL05ranNMdys2ZE1oQnJWWDJDSXFJbmg0RkMvN1VUN0s0a3NjUGIrTWZuMzlKM3NKRTllb1VQTWhaSHdrWnpOT2d3Y0lDOVhPRDVPWGVsMDIwaWE0SWs2cHVGSTJETTZlcHYvUXp3VmYwQjFEbERFQWdINU1jc1BDQ0haZFE9PWU0aFZlcnJhSU1HbHN0NDAiLCJsIjoiaHR0cHM6Ly9uZXdhc3NldHMuaGNhcHRjaGEuY29tL2MvM2QzZjkxZTAiLCJlIjoxNjU1MDkwODExfQ.IHRia-Tqa1M4cK0Zqn43Ob4Mu18SRlwcQH1SSzTBb1g'}, 'success': False, 'error-codes': []}) 
# ^^ Error Message doesn't even provide the error XD, if you think you know what's wrong feel free to share it so I can try and fix it
print(data.status_code)
data = data.json()
print(data)
subject = data['requester_question']['en']
print(subject)
