from flask import Flask,jsonify
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)

cities = [
{
	"id":1,
	"city_name":u"Hyderabad",
	"about":u"Points to Note: Don't overload your plate, you are expected to finish everything.Remove your shoes when entering someone's home, even if they tell you it is all right to wear your shoes. It is almost never all right.Smoking is prohibited in public buses, elevators, theaters, cinemas, air-conditioned restaurants, shopping centers and government offices.Don't take photograph without permission.",

	"helpline":u"Police:100,Ambulance: 102,Fire: 101,Police Control Room: 23232222,Child Line: 1098,Tourist Information: 1363",
	"explore":u"Places to visit: Salar Jung Museum,Golconda Fort,Nehru Zoological Garden,Charminar,Jagannath Temple,Ramoji Film City,Hussain Sagar,Mecca Masjid,Lumbini Park andFalaknuma Palace",
	"done":False
	
},
{
	"id":2,
	"city_name":u"Dubai",
	"about":u"Points to Note: It is also not appropriate for men to go around without a top on away from the beach.Do not take any photographs of any local residents without permission.If you have broken the law, then you will be arrested and taken to police station, questioned and instructed to make a statement.If you are caught driving with any level of alcohol in your blood expect a jail sentence.",
			
	"helpline":u"Police: 999,Fire Department: 997,Ambulance: 999,Tourist Security Department of Dubai Police: 800-4438",
	"explore":u"Places to visit:Burj Khalifa,Bur Dubai,The Dubai Mall,Palm Jumeirah,Dubai Creek,Dubai Marina,Al Fahidi Historical Neighbourhood,Madinat Jumeirah and Ski Dubai",
	"done":False
}
]




@app.route('/FlyDubai/api/cities', methods=['GET'])
def get_tasks():
    return jsonify({'cities': cities})

@app.route('/FlyDubai/api/cities/<int:city_id>',methods = ['GET'])
def get_task(city_id):
	city = [city for city in cities if city['id'] == city_id]
	if len(city) == 0:
		abort(404)
	return jsonify({"cities":city[0]})

@app.route('/FlyDubai/api/cities/<name>',methods = ['GET'])
def get_detail(name):
	info = [city for city in cities if city["city_name"] == name]
	return jsonify({"city":info[0]})


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/FlyDubai/api/cities',methods= ["POST"])
def create_task():
	if not request.json or not 'city_name' in request.json:
		abort(404)

	city = {
	'id':int(cities[-1]['id'])+1,
	'city_name':request.json['city_name'],
	'about':request.json.get("about",""),
	'helpline':request.json.get("helpline",""),
	'explore':request.json.get("explore",""),
	'done':False
	}
	cities.append(city)
	return jsonify({"city":city}),201



if __name__ == '__main__':
    app.run(debug=True,threaded=True)
















































