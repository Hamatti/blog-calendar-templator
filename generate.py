import sys
import calendar


def generate(year):
    cal = calendar.Calendar()
    week_number = 1
    for month in range(1, 13):
        print(f'**{calendar.month_name[month]}**')
        for week in cal.monthdatescalendar(year, month):
            wednesday = week[2]
            if wednesday.month != month:
                continue
            print(f'{week_number}: ')
            week_number += 1
        print()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python generate.py [year]')
        sys.exit(1)
    try:
        year = int(sys.argv[1])
    except ValueError:
        print('Year argument must be an integer in format YYYY')
        sys.exit(1)
    
    generate(year)