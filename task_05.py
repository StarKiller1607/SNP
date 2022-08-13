def date_in_future(integer=0):
    import datetime as d
    if type(integer) != int:
        return d.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    date = d.datetime.now() + d.timedelta(days=integer)
    return date.strftime('%d-%m-%Y %H:%M:%S')
print(date_in_future([]))