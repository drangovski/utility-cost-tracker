
![Utility Cost Tracker cover](https://user-images.githubusercontent.com/13369413/145307242-52b80cd9-967f-4a38-936b-c529465e538d.png)

# Utility Cost Tracker

Utility Cost Tracker connects various smart home devices to Django application. 
Through this project you can easily control them, track the activity sessions duration for each device and based on that, calculate the cost for each activity session.

UCT connects the devices through Tuya IoT Platform and it is using their Cloud API endpoints in order to fetch the information and status of any devices that are connecting on the same network, as well as to send commands for controling devices' state.

This is initial version of the project and it is still very basic, but there is a potential for greater improvements in the future.

Feel free to play with it and make your own versions. I'll be glad if you let me know if someday you build something on the top of it.

To read more details on the process so far and some tips for setting up this project, you can check this article:

###[Link to the article](https://dev.to/drango/utility-cost-tracker-for-smart-home-devices-with-python-and-django-4llo)


## Installation

I consider that you have the basic understanding on how to set up a Django project, so I won’t get into the details here on how to do it.

Key points:

* Create your virtual environment.
* Start a Django project
* Check out the settings for Secret Key and Database settings (SECRET_KEY is removed from the current settings.py)
* Install requirements
```
pip install -r requirements.txt
```
* Make an account at Tuya IoT platform and create a Cloud project
* Create env.py with config settings for connecting to Tuya Cloud inside your 'devices' app folder

```
ACCESS_ID = "<Insert your Tuya Cloud ACCESS_ID here>"
ACCESS_KEY = "<Insert your Tuya Cloud ACCESS_KEY here>"
API_ENDPOINT = "https://openapi.tuyaeu.com"  # note EU after tuya
MQ_ENDPOINT = "wss://mqe.tuyaeu.com:8285/"  # note EU after tuya
```

---

If you liked this project, please consider subscribing to my mailing list - That will be a great supportive move and you won't miss any update in the future. Plus occasionally you will receive exclusive, subscriber-only content: Behind the scenes information on upcoming development projects, ui/ux tips & tricks and so on. No spam, no BS.

To subscribe please visit my TinyLetter profile.

https://tinyletter.com/drango








