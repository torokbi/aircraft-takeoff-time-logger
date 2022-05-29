# aircraft-takeoff-time-logger
This python web app help you for monitoring the time of since last takeoff. The app can sotre the datas of aircraft and autorefresh the time before next takeoff.
## The main html and views
The main views inlcude the table of datas with action buttons and the close day button. When you send a new plane the app will tyr to find it in database. If it find it add an error deffiniton to the context dictionary with message (A <"reg"> lajstromjelű repülőgép már egyszer rögzítésre került.) Else the system get the hour and minutes from system in string format and save they. Both siouacion the system reload the site.
The main html has a script what reload site every minutes, because of updating datas in table.
The color of row is depends on how many minutes has the plane before next takeoff. If it has more than 0 the background color is yellow, if it hasn't time the color is green. When the plane time is not 0 the django generate a warning window in html. This will open when you try taking of this plane, so you have to confirm your decision.
### The retakeoff views
The retakoff module start its work whe you click the "Felszállá" yellow button. The module wait the id of plane, but the django automatically extend the url of module with the id.