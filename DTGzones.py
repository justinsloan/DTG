#print(Y.zone_code)
#print(Y.city)
#print(Y.offset)


class timeZone(object):
    __attributes__ = "zone_code, city, offset, DST_offset, abbr, utc"

    def __init__(self, zone_code, city, offset, DST_offset, abbr, utc):
        self.zone_code = zone_code
        self.city = city
        self.offset = offset
        self.DST_offset = DST_offset
        self.abbr = abbr
        self.utc = utc

Z  = timeZone('Z', 'Zulu Time',              int(0),   int(0),   'GMT','UTC+0')
Y  = timeZone('Y', 'Fiji',                   int(-12), int(-12), '???','UTC-12')
X  = timeZone('X', 'American Samoa',         int(-11), int(-11), '???','UTC-11')
W  = timeZone('W', 'Honolulu, HI',           int(-10), int(-10), 'HST','UTC-10')
Vi = timeZone('Vi','French Polynesia',       int(-9.5),int(-9.5),'UNK','UTC-9.5')
V  = timeZone('V', 'Juneau, AK',             int(-9),  int(-10), '???','UTC-9')
U  = timeZone('U', 'Los Angeles, CA',        int(-8),  int(-8),  'PST','UTC-8')
T  = timeZone('T', 'Denver, CO',             int(-7),  int(-7),  'MST','UTC-7')
S  = timeZone('S', 'Dallas, TX',             int(-6),  int(-6),  'CST','UTC-6')
R  = timeZone('R', 'New York, NY',           int(-5),  int(-5),  'EST','UTC-5')
Qi = timeZone('Qi', 'Caracus, Venezuala',     int(-4.5),int(-4.5),'UNK','UTC-4.5')
Q  = timeZone('Q', 'Halifax, Nova Scotia',   int(-4),  int(-4),  'UNK','UTC-4')
Pi = timeZone('Pi', 'Newfoundland',           int(-3.5),int(-3.5),'UNK','UTC-3.5')
P  = timeZone('P', 'Buenos Aires, Argentina',int(-3),  int(-3),  'UNK','UTC-3')
O  = timeZone('O', 'Godthab, Greenland',     int(-2),  int(-2),  'UNK','UTC-2')
N  = timeZone('N', 'Azores',                 int(-1),  int(-1),  'UNK','UTC-1')
M  = timeZone('M', 'Wellington, New Zealand',int(12),  int(12),  'UNK','UTC+12')
L  = timeZone('L', 'Sydney, Australia',      int(11),  int(11),  'UNK','UTC+11')
K  = timeZone('K', 'Brisbane, Australia',    int(10),  int(10),  'UNK','UTC+10')
I  = timeZone('I', 'Tokyo, Japan',           int(9),   int(9),   'UNK','UTC+9')
Hi = timeZone('Hi','Eucla, Australia',       int(8.75),int(8.75),'UNK','UTC+8.75')
H  = timeZone('H', 'Beijing, China',         int(8),   int(8),   'UNK','UTC+8')
G  = timeZone('G', 'Bangkok, Thailand',      int(7),   int(7),   'UNK','UTC+7')
Fi = timeZone('Fi','Yangon, Myanmar',        int(6.5), int(6.5), 'UNK','UTC+6.5')
F  = timeZone('F', 'Dhaka, Bangladesh',      int(6),   int(6),   'UNK','UTC+6')
Eii = timeZone('Eii','Kathmandu, Nepal',       int(5.75),int(5.75),'UNK','UTC+5.75')
Ei = timeZone('Ei','Delhi, India',           int(5.5), int(5.5), 'UNK','UTC+5.5')
E  = timeZone('E', 'Lahore, Pakistan',       int(5),   int(5),   'UNK','UTC+5')
Di = timeZone('Di','Kabul, Afghanistan',     int(4.5), int(4.5), 'UNK','UTC+4.5')
D  = timeZone('D', 'Moscow, Russia',         int(4),   int(4),   'UNK','UTC+4')
Ci = timeZone('Ci','Tehran, Iran',           int(3.5),int(3.5),'UNK','UTC+3.5')
C  = timeZone('C', 'Riyadh, Saudi Arabia',   int(3),   int(3),   'AST','UTC+3')
B  = timeZone('B', 'Athens, Greece',         int(2),   int(2),   'UNK','UTC+2')
A  = timeZone('A', 'Paris, France',          int(1),   int(1),   'UNK','UTC+1')

"""
CONSIDER REVISING THE city ATTRIBUTE TO BE A TUPLE REPRESENTING
MULTIPLE CITY NAMES
3: C (Arab Standard Time, Iraq, Bahrain, Kuwait, Saudi Arabia, Yemen, Qatar)
4: D (Used for Moscow, Russia and Afghanistan, however Afghanistan is technically +4:30 from UTC
5: E (Pakistan, Kazakhstan, Tajikistan, Uzbekistan and Turkmenistan)
"""