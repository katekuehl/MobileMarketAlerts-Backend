from datetime import datetime

# Datetime import check
#test_datetime = datetime(2021, 6, 18, 15)
#print('From data.py', test_datetime)

# Data to be imported into database. Structured as list of dicts.
mock_users_data = [
    {
        'id': 1,
        'cellphone_number': '111-111-1111',
        'zip_code': 55411
    },
    {
        'id': 2,
        'cellphone_number': '222-222-2222',
        'zip_code': 55411
    },
    {
        'id': 3,
        'cellphone_number': '333-333-3333',
        'zip_code': 55411
    }
]

providers_data = [
    {
        'id': 1,
        'name': 'West Broadway Farmers Market',
        'address': '2034 W Broadway Ave, Minneapolis, MN 55411',
        'description': 'Friday, weekly. Between 6/18/2021 - 10/1/2021.',
        'website': 'https://www.facebook.com/westbroadwayfarmersmarket/',
        'service_type_id': 1
    },
    {
        'id': 2,
        'name': 'Minneapolis Farmers Market',
        'address': '312 East Lyndale Ave N, Minneapolis, MN 55405',
        'description': '',
        'website': 'https://www.mplsfarmersmarket.com/FreshNews/ebt/',
        'service_type_id': 1
    },
    {
        'id': 3,
        'name': 'Minneapolis Northeast Farmers Market',
        'address': '629 NE 2nd St, Minneapolis, MN 55413',
        'description': 'Saturday, weekly. Between 5/15/2021 - 10/16/2021.',
        'website': 'https://www.northeastfarmersmarket.com/',
        'service_type_id': 1
    },
    {
        'id': 4,
        'name': 'Loaves & Fishes at Salvation Army North',
        'address': '2024 Lyndale Ave N, Minneapolis, MN 55411',
        'description': 'Monday - Friday, weekly',
        'website': 'https://www.loavesandfishesmn.org/dining-sites/salvation-army-north-parkview/',
        'service_type_id': 2
    },
    {
        'id': 5,
        'name': 'Loaves & Fishes at New Bethel',
        'address': '1115 30th Ave North, Minneapolis, MN 55411',
        'description': 'Monday - Friday, weekly',
        'website': 'https://www.loavesandfishesmn.org/dining-sites/new-bethel-baptist-church/',
        'service_type_id': 2
    },
    {
        'id': 6,
        'name': 'Al-Maa’uun',
        'address': '1729 Lyndale Avenue North, Minneapolis, MN 55411',
        'description': 'Every 3rd Saturday, monthly',
        'website': 'http://masjidannur.org/al-maauun-food-program/',
        'service_type_id': 2
    },
    {
        'id': 7,
        'name': 'NorthPoint Health & Wellness Food Shelf',
        'address': '1835 Penn Ave N, Minneapolis, MN 55411',
        'description': 'Monday - Thursday, weekly',
        'website': 'https://www.northpointhealth.org/',
        'service_type_id': 3
    },
    {
        'id': 8,
        'name': 'Al-Maa’unn Food Shelf',
        'address': '1729 Lyndale Ave N, Minneapolis, MN 55412' ,
        'description': 'Every 3rd Saturday, monthly',
        'website': 'http://masjidannur.org/partners-affiliation/al-maauun/food-program/',
        'service_type_id': 3
    },
    {
        'id': 9,
        'name': 'Food in the Hood - Beacon of Hope Church',
        'address': '2827 Newton Ave N, Minneapolis, MN 55411',
        'description': 'Every 2nd & 4th Thursday, monthly',
        'website': 'https://www.goodinthehood.org/our-programs/feeding-the-future/food-in-the-hood/',
        'service_type_id': 3
    }
]

service_types_data = [
    {
        'id': 1,
        'service_type': 'Farmers Market'
    },
    {
        'id': 2,
        'service_type': 'Free Meals'
    },
    {
        'id': 3,
        'service_type': 'Food Shelf'
    }
]

events_data = [
    {
        'id': 1,
        'start_datetime': datetime(2021, 6, 18, 15),
        'end_datetime': datetime(2021, 6, 18, 19),
        'providers_id': 1
    },
    {
        'id': 2,
        'start_datetime': datetime(2021, 4, 3, 9),
        'end_datetime': datetime(2021, 4, 3, 12),
        'providers_id': 2
    },
    {
        'id': 3,
        'start_datetime': datetime(2021, 5, 15, 9),
        'end_datetime': datetime(2021, 5, 15, 13),
        'providers_id': 3
    },
    {
        'id': 4,
        'start_datetime': datetime(2021, 3, 29, 11, 30), 
        'end_datetime': datetime(2021, 3, 29, 12, 30),
        'providers_id': 4
    },
    {
        'id': 5,
        'start_datetime': datetime(2021, 3, 29, 17, 30),
        'end_datetime': datetime(2021, 3, 29, 18, 30),
        'providers_id': 5
    },
    {
        'id': 6,
        'start_datetime': datetime(2021, 4, 17, 15),
        'end_datetime': datetime(2021, 4, 17, 17, 30),
        'providers_id': 6
    },
    {
        'id': 7,
        'start_datetime': datetime(2021, 3, 29, 10),
        'end_datetime': datetime(2021, 3, 29, 16),
        'providers_id': 7
    },
    {
        'id': 8,
        'start_datetime': datetime(2021, 4, 17, 8),
        'end_datetime': datetime(2021, 4, 17, 21, 30),
        'providers_id': 8
    },
    {
        'id': 9,
        'start_datetime': datetime(2021, 4, 8, 17),
        'end_datetime': datetime(2021, 4, 8, 20),
        'providers_id': 9
    }
]