import calendar
from datetime import datetime


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 18/04/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the constants
#

class Constants():
    LANGUAGE_NOT_FOUND: str = "This language was not found"
    USER_NOT_FOUND: str = "This user was not found"
    NOT_FOUND: str = "Not found"
    NOT_ENOUGH_PERMISSIONS: str = "Not enough permissions"
    MAX_URLS_REACHED = "You can't create more urls"
    CREATED: str = "Created"
    UP_TO_DATE: str = "Up To date"
    NOT_UP_TO_DATE: str = "Not Up To date"
    ALREADY_CREATED = "This resource was already created"
    INVALID_REQUEST: str = "Invalid request"

    COUNTRIES = {
        "AF": "Afghanistan",
        "AL": "Albania",
        "DZ": "Algeria",
        "AD": "Andorra",
        "AO": "Angola",
        "AR": "Argentina",
        "AM": "Armenia",
        "AU": "Australia",
        "AT": "Austria",
        "AZ": "Azerbaijan",
        "BS": "Bahamas",
        "BH": "Bahrain",
        "BD": "Bangladesh",
        "BB": "Barbados",
        "BY": "Belarus",
        "BE": "Belgium",
        "BZ": "Belize",
        "BJ": "Benin",
        "BT": "Bhutan",
        "BO": "Bolivia",
        "BA": "Bosnia and Herzegovina",
        "BW": "Botswana",
        "BR": "Brazil",
        "BN": "Brunei",
        "BG": "Bulgaria",
        "BF": "Burkina Faso",
        "BI": "Burundi",
        "KH": "Cambodia",
        "CM": "Cameroon",
        "CA": "Canada",
        "CV": "Cape Verde",
        "CF": "Central African Republic",
        "TD": "Chad",
        "CL": "Chile",
        "CN": "China",
        "CO": "Colombia",
        "KM": "Comoros",
        "CG": "Congo",
        "CR": "Costa Rica",
        "HR": "Croatia",
        "CU": "Cuba",
        "CY": "Cyprus",
        "CZ": "Czech Republic",
        "DK": "Denmark",
        "DJ": "Djibouti",
        "DM": "Dominica",
        "DO": "Dominican Republic",
        "EC": "Ecuador",
        "EG": "Egypt",
        "SV": "El Salvador",
        "GQ": "Equatorial Guinea",
        "ER": "Eritrea",
        "EE": "Estonia",
        "ET": "Ethiopia",
        "FJ": "Fiji",
        "FI": "Finland",
        "FR": "France",
        "GA": "Gabon",
        "GM": "Gambia",
        "GE": "Georgia",
        "DE": "Germany",
        "GH": "Ghana",
        "GR": "Greece",
        "GD": "Grenada",
        "GT": "Guatemala",
        "GN": "Guinea",
        "GW": "Guinea-Bissau",
        "GY": "Guyana",
        "HT": "Haiti",
        "HN": "Honduras",
        "HU": "Hungary",
        "IS": "Iceland",
        "IN": "India",
        "ID": "Indonesia",
        "IR": "Iran",
        "IQ": "Iraq",
        "IE": "Ireland",
        "IL": "Israel",
        "IT": "Italy",
        "JM": "Jamaica",
        "JP": "Japan",
        "JO": "Jordan",
        "KZ": "Kazakhstan",
        "KE": "Kenya",
        "KI": "Kiribati",
        "KP": "North Korea",
        "KR": "South Korea",
        "KW": "Kuwait",
        "KG": "Kyrgyzstan",
        "LA": "Laos",
        "LV": "Latvia",
        "LB": "Lebanon",
        "LS": "Lesotho",
        "LR": "Liberia",
        "LY": "Libya",
        "LI": "Liechtenstein",
        "LT": "Lithuania",
        "LU": "Luxembourg",
        "MK": "North Macedonia",
        "MG": "Madagascar",
        "MW": "Malawi",
        "MY": "Malaysia",
        "MV": "Maldives",
        "ML": "Mali",
        "MT": "Malta",
        "MH": "Marshall Islands",
        "MR": "Mauritania",
        "MU": "Mauritius",
        "MX": "Mexico",
        "FM": "Micronesia",
        "MD": "Moldova",
        "MC": "Monaco",
        "MN": "Mongolia",
        "ME": "Montenegro",
        "MA": "Morocco",
        "MZ": "Mozambique",
        "MM": "Myanmar",
        "NA": "Namibia",
        "NR": "Nauru",
        "NP": "Nepal",
        "NL": "Netherlands",
        "NZ": "New Zealand",
        "NI": "Nicaragua",
        "NE": "Niger",
        "NG": "Nigeria",
        "NO": "Norway",
        "OM": "Oman",
        "PK": "Pakistan",
        "PW": "Palau",
        "PA": "Panama",
        "PG": "Papua New Guinea",
        "PY": "Paraguay",
        "PE": "Peru",
        "PH": "Philippines",
        "PL": "Poland",
        "PT": "Portugal",
        "QA": "Qatar",
        "RO": "Romania",
        "RU": "Russia",
        "RW": "Rwanda",
        "KN": "Saint Kitts and Nevis",
        "LC": "Saint Lucia",
        "VC": "Saint Vincent and the Grenadines",
        "WS": "Samoa",
        "SM": "San Marino",
        "ST": "Sao Tome and Principe",
        "SA": "Saudi Arabia",
        "SN": "Senegal",
        "RS": "Serbia",
        "SC": "Seychelles",
        "SL": "Sierra Leone",
        "SG": "Singapore",
        "SK": "Slovakia",
        "SI": "Slovenia",
        "SB": "Solomon Islands",
        "SO": "Somalia",
        "ZA": "South Africa",
        "SS": "South Sudan",
        "ES": "Spain",
        "LK": "Sri Lanka",
        "SD": "Sudan",
        "SR": "Suriname",
        "SZ": "Eswatini",
        "SE": "Sweden",
        "CH": "Switzerland",
        "SY": "Syria",
        "TJ": "Tajikistan",
        "TZ": "Tanzania",
        "TH": "Thailand",
        "TL": "Timor-Leste",
        "TG": "Togo",
        "TO": "Tonga",
        "TT": "Trinidad and Tobago",
        "TN": "Tunisia",
        "TR": "Turkey",
        "TM": "Turkmenistan",
        "TV": "Tuvalu",
        "UG": "Uganda",
        "UA": "Ukraine",
        "AE": "United Arab Emirates",
        "GB": "United Kingdom",
        "US": "United States",
        "UY": "Uruguay",
        "UZ": "Uzbekistan",
        "VU": "Vanuatu",
        "VA": "Vatican City",
        "VE": "Venezuela",
        "VN": "Vietnam",
        "YE": "Yemen",
        "ZM": "Zambia",
        "ZW": "Zimbabwe"
    }

    YEARLY_CHART_SCHEMA = {
        "January": 0,
        "February": 0,
        "March": 0,
        "April": 0,
        "May": 0,
        "June": 0,
        "July": 0,
        "August": 0,
        "September": 0,
        "October": 0,
        "November": 0,
        "December": 0
    }

    @classmethod
    def MONTHLY_CHART_SCHEMA(cls):
        current_year = datetime.now().year
        current_month = datetime.now().month
        num_days = calendar.monthrange(current_year, current_month)[1]
        obj = {}
        i = 1
        while i < num_days:
            if i > 0:
                obj[str(i)+"/"+str(current_month) if i > 9 else "0"+str(i)+"/"+str(current_month)] = 0
            i += 1
        return obj

    WEEK_CHART_SCHEMA = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }
    DAY_CHART_SCHEMA = {
        "00:00": 0,
        "01:00": 0,
        "02:00": 0,
        "03:00": 0,
        "04:00": 0,
        "05:00": 0,
        "06:00": 0,
        "07:00": 0,
        "08:00": 0,
        "09:00": 0,
        "10:00": 0,
        "11:00": 0,
        "12:00": 0,
        "13:00": 0,
        "14:00": 0,
        "15:00": 0,
        "16:00": 0,
        "17:00": 0,
        "18:00": 0,
        "19:00": 0,
        "20:00": 0,
        "21:00": 0,
        "22:00": 0,
        "23:00": 0
    }

    EMAIL = 'crylletinc@gmail.com'
    PASSWORD = ''
    PASSWORD_FORGOTTEN_EMAIL: str = "Hey! \nHere's the link to recover your account: https://cryllet-fe.pages.dev/create_password/{token}"

    PAGE_NOT_FOUND = 'This page was not found. See our documentation'
    PAGE_METHOD_NOT_ALLOWED = 'Method not allowed. See our documentation'
    PAGE_UNKNOWN_ERROR = 'Unknown error'
