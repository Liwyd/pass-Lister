README.md#  pass-Lister

## How To Install
```
git clone https://github.com/Liwyd/pass-Lister.git
```

## How To Use
- open your terminal (linux/windows)
- you can use (" , ") to seprate your keywords, chars or even datas
```
-w   --KeyWords     help=keyWords to iterate
```
```
-c   --characters   help=characters to join
```
```
-d   --data         help=data to iterate
```
```
-out --output       help=output of wordlist file
```

- example:
```
python3 passwdLister.py -w=computers,linux,passlist,liwyd -c=@,#,! -d=liwyd,github,1234,qwerty -out=output/wordlist.txt
```

- Result:
```
[ELAPSED]: 0.00 min
-> 'output/wordlist.txt'


$cat output/wordlist.txt
liwydliwyd
liwyd@liwyd
liwydliwyd
liwyd#liwyd
liwydliwyd
liwyd!liwyd
liwydgithub
liwyd1234
liwyd@1234
liwyd1234
liwyd#1234
github1234
github!1234
githubqwerty
github@qwerty
github!qwerty
1234liwyd
1234@liwyd
1234liwyd
1234#liwyd
1234liwyd
1234!liwyd
and so on ...
```

- use it peacefuly :)