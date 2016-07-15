# Travel-App-Backend

This is the backend built for Travel App with Flask framework.

Our tasks resource will use HTTP methods as follows:

| HTTP Method   | URI                                                   |Action                                     |
| ------------- |:-----------------------------------------------------:| -----------------------------------------:|
| GET           | http://[hostname]/FlyDubai/api/cities                 | Retrieve information of all cities        |
| GET           | http://[hostname]/FlyDubai/api/cities/[city_id]       | Retrieve information of a particular city |
| GET           | http://[hostname]/FlyDubai/api/cities/[city_name]     | Retrieve information of a particular city |
| POST           | http://[hostname]/FlyDubai/api/cities                | Create a new city in the list             |



#### We can define a city as having the following fields:

id: unique identifier for cities (Numeric type).<br>
city_name: name of the city (String type).<br>
about: rules and regulations followed by a city (Text type).<br>
helpline: numbers of police,ambulance,and tourist security,etc (Text type).<br>
explore: all the important landmarks a person must visit (Text type).<br>
done: task completion state (Boolean type).


