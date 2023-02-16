import random
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

metro_areas = {
            'Alabama': ['Birmingham', 'Huntsville', 'Mobile', 'Montgomery', 'Tuscaloosa'],
            'Alaska': ['Anchorage', 'Fairbanks', 'Juneau', 'Badger', 'Fairview'],
            'Arizona': ['Flagstaff', 'Phoenix', 'Prescott', 'Tucson', 'Yuma'],
            'Arkansas': ['Little Rock', 'Fayetteville', 'Fort Smith', 'Texarkana', 'Jonesboro'],
            'California': ['Los Angeles', 'San Francisco', 'San Diego', 'Oakland', 'Sacramento'],
            'Colorado': ['Denver', 'Boulder', 'Colorado Springs', 'Fort Collins', 'Greeley'],
            'Connecticut': ['Hartford', 'New Haven', 'Norwich', 'Bridgeport', 'Trenton'],
            'Delaware': ['Wilmington', 'Dover', 'Newark', 'Middletown', 'Bear'],
            'Florida': ['Miami', 'Tampa', 'Orlando', 'Jacksonville', 'Daytona Beach'],
            'Georgia': ['Atlanta', 'Augusta', 'Savannah', 'Columbus', 'Athens'],
            'Hawaii': ['Wailuku', 'Kapaʻa', 'Hilo', 'Honolulu', 'Kahului'],
            'Idaho': ['Boise', 'Idaho Falls', "Coeur d'Alene", 'Pocatello', 'Sandpoint'],
            'Illinois': ['Chicago', 'Aurora', 'Rockford', 'Springfield', 'Bloomington'],
            'Indiana': ['Indianapolis', 'Fort Wayne', 'South Bend', 'Lafayette', 'Evansville'],
            'Iowa': ['Des Moines', 'Cedar Rapids', 'Davenport', 'Sioux City', 'Iowa City'],
            'Kansas': ['Kansas City', 'St. Joseph', 'Wichita', 'Leavenworth', 'Dodge City'],
            'Kentucky': ['Louisville', 'Lexington', 'Bowling Green', 'Owensboro', 'Covington'],
            'Louisiana': ['New Orleans', 'Baton Rouge', 'Shreveport', 'Lafayette', 'Lake Charles'],
            'Maine': ['Portland', 'Lewiston', 'Bangor', 'Auburn', 'Augusta'],
            'Maryland': ['Baltimore', 'Columbia', 'Germantown', 'Silver Spring', 'waldorf'],
            'Massachusetts': ['Boston', 'Worcester', 'Springfield', 'Cambridge', 'Lowell'],
            'Michigan': ['Detroit', 'Grand Rapids', 'Warren', 'Sterling Heights', 'Ann Arbor'],
            'Minnesota': ['Minneapolis', 'Saint Paul', 'Rochester', 'Duluth', 'Bloomington'],
            'Mississippi': ['Jackson', 'Gulfport', 'Southaven', 'Biloxi', 'Hattiesburg'],
            'Missouri': ['Kansas City', 'Saint Louis', 'Springfield', 'Columbia', 'Independence'],
            'Montana': ['Billings', 'Missoula', 'Great Falls', 'Bozeman', 'Butte'],
            'Nebraska': ['Omaha', 'Lincoln', 'Bellevue', 'Grand Island', 'Kearney'],
            'Nevada': ['Las Vegas', 'Henderson', 'Reno', 'Paradise', 'Carson City'],
            'New_Hampshire': ['Manchester', 'Nashua', 'Concord', 'Dover', 'Rochester'],
            'New_Jersey': ['Newark', 'Jersey City', 'Paterson', 'Elizabeth', 'Edison'],
            'New_Mexico': ['Albuquerque', 'Las Cruces', 'Rio Rancho', 'Santa Fe', 'Roswell'],
            'New_York': ['New York City', 'Buffalo', 'Yonkers', 'Rochester', 'Syracuse'],
            'North_Carolina': ['Charlotte', 'Raleigh', 'Greensboro', 'Durham', 'Winston-Salem'],
            'North_Dakota': ['Fargo', 'Bismarck', 'Grand Forks', 'Minot', 'West Fargo'],
            'Ohio': ['Columbus', 'Cleveland', 'Cincinnati', 'Toledo', 'Akron'],
            'Oklahoma': ['Oklahoma City', 'Tulsa', 'Norman', 'Broken Arrow', 'Edmond'],
            'Oregon': ['Portland', 'Salem', 'Corvallis', 'Gresham', 'Cannon Beach'],
            'Pennsylvania': ['Philadelphia', 'Pittsburgh', 'Allentown', 'Erie', 'Reading'],
            'Rhode_Island': ['Providence', 'Cranston', 'Warwick', 'Pawtucket', 'East Providence'],
            'South_Carolina': ['Charleston', 'Columbia', 'North Charleston', 'Mount Pleasant', 'Rock Hill'],
            'South_Dakota': ['Sioux Falls', 'Rapid City', 'Aberdeen', 'Brookings', 'Watertown'],
            'Tennessee': ['Nashville', 'Memphis', 'Knoxville', 'Chattanooga', 'Clarksville'],
            'Texas': ['Houston', "San Antonio", 'Dallas', 'Austin', 'Fort Worth'],
            'Utah': ['Salt Lake City', 'West Valley City', 'Provo', 'West Jordan', 'Orem'],
            'Vermont': ['Burlington', 'South Burlington', 'Colchester', 'Rutland', 'Bennington'],
            'Virginia': ['Virgina Beach', 'Norfolk', 'Chesapeake', 'Richmond', 'Arlington'],
            'Washington': ['Seattle', 'Spokane', 'Tacoma', 'Vancouver', 'Believue'],
            'West_Virginia': ['Charleston', 'Huntington', 'Morgantown', 'Parkersburg', 'Wheeling'],
            'Wisconsin': ['Milwaukee', 'Madison', 'Green Bay', 'Kenosha', 'Racine'],
            'Wyoming': ['Cheyenne', 'Casper', 'Laramie', 'Gillette', 'Rock Springs']
             }


def generate_city_and_state():

    randomstatenumber = random.randrange(1, 50, 1)
    randomcitynumber = random.randrange(1, 5, 1)
    state_to_return = list(metro_areas)[randomstatenumber]
    city_to_return = metro_areas[state_to_return][randomcitynumber]
    return state_to_return, city_to_return

while True:
    #  Wait for next request from client
    message = socket.recv_string()
    print(f"Received request: {message}")

    if message == '1':
        city_and_state = generate_city_and_state()
        json_city_state = json.dumps(city_and_state)
        socket.send_json(json_city_state)
        print(f"Send data: {json_city_state}")
    else:
        not_valued_request = "invalid request- string sent was not '1' "
        nvrjson = json.dumps(not_valued_request)
        socket.send_json(nvrjson)
        print(f"Sent data: {nvrjson}")
    #  Send reply back to client
