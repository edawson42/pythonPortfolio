# Military time conversion function
# Copyright 2018, Eric Dawson, All rights reserved.

def timeConversion(s):
    """ (str) -> str
    Return time in military (24 hour) format
    >>> timeConversion('07:05:45PM')
    '19:05:45'
    >>> timeConversion('07:05:45AM')
    '07:05:45'
    >>> timeConversion('12:00:00AM')
    '00:00:00'
    >>> timeConversion('12:00:00PM')
    '12:00:00'
    >>> timeConversion('11:00:00PM')
    '23:00:00'
    >>> timeConversion('11:00:00AM')
    '11:00:00'
    >>> timeConversion('10:00:00PM')
    '22:00:00'
    >>> timeConversion('10:00:00AM')
    '10:00:00'
    """
    military_time = ''
    hours = ''
    hours = s[0] + s[1]
    
    if hours == '12' and s[8] == 'A':
        military_time = '00'
    elif hours == '12' and s[8] == 'P':
        military_time = '12'
    elif int(hours) < 10 and s[8] == 'A':
        hours = int(hours)
        military_time = military_time + '0' + str(hours)
    elif int(hours) > 9 and s[8] == 'A':
        hours = int(hours)
        military_time = military_time + str(hours)
    elif int(hours) < 12 and s[8] == 'P': 
        hours = int(hours) + 12
        military_time = military_time + str(hours)
    
    # Add back the minutes and seconds without the AM or PM
    for i in range(2, 8):
        military_time = military_time + s[i]
        
    return military_time



if __name__ == '__main__':
    import doctest
    doctest.testmod()
