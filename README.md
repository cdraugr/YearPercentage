# YearPercentage
This script will show how much percent has passed from the beginning of the year on a specific date.

## install & launch
```bash
git clone https://github.com/cdraugr/Year_Percentage ~/YearPercentage
cd ~/YearPercentage
./main.py -h  # main is executable but you still can use python3 to run it
```

## how to work with

One common output of the program:
```
==============
   February
==============
01 08.46995%
02 08.74317%
02 09.00000% 22:33
03 09.01639%
04 09.28962%
05 09.56284%
06 09.83607%
06 10.00000% 14:24
...
```
* Number between two short equals sign rows is a month (wow).

`02 08.74317%` means that, 2nd Feb at 12:00am (midnight) will be 8.74317% of year.

If smf is written after `'%'`, for example `02 09.0000% 22:33`, read it like:

2nd Feb at 22:33 will be 9% of a year.

So simply, how you can see!
