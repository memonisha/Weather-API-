from p5 import *

def setup():
  createCanvas(800,600)
  global button, api,place, apiKey, units, city, factor, api2, apiKey2
  #button = select('#submit')
  
  loadImage('thermo.png','thermo')
  
  city = select('#City')
  api = 'https://api.openweathermap.org/data/2.5/weather?q='

  apiKey = '&appid=77912d00c545eb1ff8f1363661fc5f53'
  units = '&units=metric'
  factor = 0

  api2 = 'https://api.unsplash.com/search/photos?query=$'
  apiKey2 = '&client_id=VswYW1uREitRqG20HI2S18m2Tz9-AXVWWp5IVqEyoyw'
  #https://api.unsplash.com/search/photos?query=$london&client_id=$VswYW1uREitRqG20HI2S18m2Tz9-AXVWWp5IVqEyoyw

  #loadImage('dkjasndjkasndkjsandklsandklsna','city')
  rectMode(CENTER)


def askImage():
  url = api2+city.value()+apiKey2
  loadJSON(url,gotData2)

def gotData2(data):
  full = data.results[floor(random(0,10))].urls.full
  loadImage(full,"full")
  print(full)
  
def askWeather():
  url = api+city.value()+apiKey+units
  loadJSON(url,gotData)
  
  
def gotData(data):
	global info, avg_temp, min_temp, max_temp, humid, cloud_cov
	info = data
	avg_temp = info.main.temp
	min_temp = info.main.temp_min
	max_temp =info.main.temp_max
	humid = info.main.humidity
	cloud_cov = 0
	#print(info['clouds']['all'])

	
def draw():
  global factor
  background("gray")
  drawTickAxes()

  
  #hs = avg_temp
  if keyIsDown(13):
     factor = 0
     askWeather()
     askImage()


  
  image(assets['full'],0,0,width,height)
  fill('white')
  stroke('black')
  textSize(20)
  text(info['name'], width/2-50,height-50)
  text("Temp: "+ str(avg_temp), 50,height-70)
  text("MinTemp: "+ str(min_temp), 50,height-90)
  text("MaxTemp: "+ str(max_temp), 50,height-110)
  text("Humidity: "+ str(humid), 50,height-130)
  text("Cloud Cover: "+str(cloud_cov), 50,height-150)



  hs = avg_temp
  factor = factor + 0.01
  push()
  noFill()
  stroke('black')
  rect(100,height/2, 100,height/2, 100)
  pop()
  push()
  stroke('green')
  textSize(20)
  #text('0 degrees',175,height/2)
  line(50,height/2,150,height/2)
  pop()
  push()
  rectMode(CORNER)
  if  0<hs < 10:
    fill('skyblue')
  elif 10<hs<20:
    fill('lightblue')
  elif 21<hs<30:
    fill('orange')
  elif 31<hs<40 or hs>40:
    fill('red')
  elif 0>hs>-10:
    fill('blue')
  elif -11>hs<-20:
    fill('steelblue')


  rect(75,height/2,50,(hs*3)*factor)
  pop()

  
  if factor >=1:
    factor = 1

  #print(factor)
  #push()
  #strokeWeight(10)
  #stroke('green')
  #line(50,200,100,200)
  #pop()
  
  #crosshair()

#def keyPressed():








#Display temp, min_temp,max_temp,humidity, cloud coverage
#How to take input box information and submit button to update the city weather information
#Create Thermometer to display temperatures
#Display humidity using water drops

  


