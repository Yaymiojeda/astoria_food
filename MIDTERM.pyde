#Name : Yaymi Ojeda
#Code Toolkit: Python Fall 2020
#Food Maps Astoria, NY


minlat = 40.758128
maxlat = 40.775545
minlong = -73.907352
maxlong = -73.926814
minframe = 100
maxframe = 600
sizerect = 25
yframe = 30
buttonsize = 80
offset = 30
os = 90


def setup():
    background(255)
    global data, font
    data = loadTable("food_data.csv","header")
    size(900,900)
    font = createFont("AnnieUseYourTelescope-Regular", 24)
    
    #BUG Font not working
    textFont(font)
    
    
    #Square frame
    fill(255)
    strokeWeight(5)
    rect( minframe, yframe, maxframe, maxframe)
    #buttons
    stroke(1)
    strokeWeight(2)
    for i in range (10):
        fill(1,135,20,70) 
        rect(minframe+maxframe+ 50+ offset, 24+yframe *i+offset*i, 100,buttonsize-12)
        
    #reset button
    fill(255)
    stroke(8)
    rect(minframe+ 80+maxframe,100+maxframe, 90, 90)
    stroke(3)
    fill(1)
    textSize(20)
    text("Reset", 800, 750)     
    textSize(15)


def draw():
    global data, minlat, maxlat, minlong, maxlong, minframe, maxframe, offset, buttonsize, yframe, os
    global font
    for row in data.rows():
        LATITUDE = row.getFloat("LATITUDE")
        LONGITUDE = row.getFloat("LONGITUDE")
        NAME = row.getString("NAME")
        TYPE = row.getString("TYPE")  

        x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
        y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
        if TYPE == 'supermarket':
            fill(255,0,0)
        else:
            fill(0,255,80)
        noStroke()
        circle (x, y, 5) 
   
    #buttons         
    textSize(15)
    strokeWeight(1)
    fill(1)
    text("Bananas", 785,60)
    text("Broccoli", 785,130)
    text("Tomato", 785, 200)
    text("Peppers", 785, 260)
    text("Couliflower", 783, 320)
    text("Milk", 800, 380)
    text("Almond milk", 785, 435)
    text("eggs", 800, 500)
    text("oats", 800, 560)
    text("chicken", 785, 620)  
    
     
      #Work in Progress
    stroke(1)
    fill(100, 200, 210)
    rect( 300, 660, 230, 10) 
    noStroke()
    
    textFont(font)
    fill(1)
    text("Astoria's Food Map: visualizing food \n prices across a neighboorhood",250,750)
    
    
    

    
def mousePressed():
    global data, minlat, maxlat, minlong, maxlong, minframe, maxframe, offset, buttonsize, yframe, os, buttonr
        
    
        

    for row in data.rows():
        LATITUDE = row.getFloat("LATITUDE")
        LONGITUDE = row.getFloat("LONGITUDE")
        NAME = row.getString("NAME")
        TYPE = row.getString("TYPE")

        x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
        y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
    
        if dist(mouseX,mouseY, x,y) < 25/2:
            print("User clicked on " + NAME +" " + TYPE+ " store") 
                
        #reset button     
    if mouseX>= 770 and mouseX <= 860 and mouseY>= 730 and mouseY <= 850:
        for row in data.rows():
            LATITUDE = row.getFloat("LATITUDE")
            LONGITUDE = row.getFloat("LONGITUDE")
            NAME = row.getString("NAME")
            TYPE = row.getString("TYPE")
            x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
            y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
            fill(255)
            circle(x, y, 58)
            textSize(15)
            noStroke()
            fill(1)
            noStroke()
            textSize(15)
            text(NAME, x+30, y+10)
      
        

                         
          #broccoli      
    if mouseX >= 770 and mouseX <= 860 and mouseY>=85 and mouseY <=145:        
        for row in data.rows():
            LATITUDE = row.getFloat("LATITUDE")
            LONGITUDE = row.getFloat("LONGITUDE")
            NAME = row.getString("NAME")
            TYPE = row.getString("TYPE")
            broccoli = row.getFloat("broccoli")  
            x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
            y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
            mean_broccoli = map ( broccoli, 1.99, 4.99, 40, 58)
            noStroke()
            textSize(15)
            fill(1)
            text(NAME, x+30, y+10)
            
            if TYPE == 'supermarket':
                fill(255,120,10,40)
            else:
                fill(0,255,0,40)
            circle(x, y, mean_broccoli)
        #banana      
    if mouseX >= 770 and mouseX <= 860 and mouseY>= 40 and mouseY <= 80:      
        for row in data.rows():
            LATITUDE = row.getFloat("LATITUDE")
            LONGITUDE = row.getFloat("LONGITUDE")
            NAME = row.getString("NAME")
            TYPE = row.getString("TYPE")
            x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
            y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
            banana = row.getFloat("bananas")  
            mean_banana = map ( banana, 0.49, 0.79, 45,58)
            if TYPE == 'supermarket':
                fill(255,120,10,40)
            else:
                fill(0,255,0,40)
            noStroke()
            textSize(15)
            circle(x, y, mean_banana)
            fill(1)
            text(NAME, x+30, y+10)
                
        #tomato    
    if mouseX >= 770 and mouseX <= 860 and mouseY>= 150 and mouseY <= 200:     
        for row in data.rows():
            LATITUDE = row.getFloat("LATITUDE")
            LONGITUDE = row.getFloat("LONGITUDE")
            NAME = row.getString("NAME")
            TYPE = row.getString("TYPE")
            x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
            y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
            tomato = row.getFloat("tomato")  
            mean_tomato = map ( tomato, 0.99, 2.49, 45,58)
            if TYPE == 'supermarket':
                fill(255,120,10,40)
            if TYPE == 'Produce':
                fill(0,255,0,40)
            if tomato == 0:
                fill(200)        
            noStroke()
            circle(x, y, mean_tomato)
            fill(1)
            textSize(15)
            text(NAME, x+30, y+10)
                
    #peppers
    if mouseX >= 780 and mouseX <= 860 and mouseY>= 200 and mouseY <= 250:     
        for row in data.rows():
            LATITUDE = row.getFloat("LATITUDE")
            LONGITUDE = row.getFloat("LONGITUDE")
            NAME = row.getString("NAME")
            TYPE = row.getString("TYPE")
            x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
            y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
            peppers = row.getFloat("peppers")  
            mean_peppers = map(peppers, 0, 3.99, 40,55)
            if TYPE == "supermarket" or TYPE == "Produce" and peppers ==0:
                fill(200)
            if peppers > 0 and TYPE == "Produce":
                fill(0,255,0,40) 
            if peppers > 0 and TYPE == "supermarket":
                    fill(255,120,10,40)
            noStroke()
            circle(x, y, mean_peppers)
            fill(1)
            textSize(15)
            text(NAME, x+30, y+10)
                    
        #cauliflower        #BUG / no displaying on the screen
    if mouseX >=780 and mouseX <= 860 and mouseY>= 260 and mouseY <= 320:     
        for row in data.rows():
            LATITUDE = row.getFloat("LATITUDE")
            LONGITUDE = row.getFloat("LONGITUDE")
            NAME = row.getString("NAME")
            TYPE = row.getString("TYPE")
            x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
            y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
            cauliflower = row.getFloat("cauliflower")  
            mean_cauliflower = map ( cauliflower, 2, 4.99, 45,50)
            if TYPE == 'supermarket':
                fill(255,120,10,40)
            else:
                fill(0,255,0,40)
            noStroke()
            circle(x, y, mean_cauliflower)
            fill(1)
            text(NAME, x+30, y+10)
    
        #milk            
    if mouseX >= 780 and mouseX <= 850 and mouseY>= 322 and mouseY <362:  
        for row in data.rows():
            LATITUDE = row.getFloat("LATITUDE")
            LONGITUDE = row.getFloat("LONGITUDE")
            NAME = row.getString("NAME")
            TYPE = row.getString("TYPE")
            x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
            y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
            milk = row.getFloat("milk")  
            mean_milk = map ( milk, 1.99, 3.99, 45,55)
            if TYPE == 'supermarket':
                fill(255,120,10,40)
            else:
                fill(0,255,0,40)
            noStroke()
            textSize(15)
            circle(x, y, mean_milk)
            fill(1)
            textSize(15)
            text(NAME, x+30, y+10)
                    
        #almond milk            
    if mouseX >= 780 and mouseX <= 850 and mouseY>= 365 and mouseY <=445:   
        for row in data.rows():
            LATITUDE = row.getFloat("LATITUDE")
            LONGITUDE = row.getFloat("LONGITUDE")
            NAME = row.getString("NAME")
            TYPE = row.getString("TYPE")
            x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
            y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
            almond_milk = row.getFloat("almond_milk")  
            mean_almond_milk = map (almond_milk, 0, 5.99, 40,55)
            if almond_milk == 0:
                fill(200)
            if almond_milk > 0 and TYPE == "Produce":
                fill(0,255,0,40) 
            if almond_milk > 0 and TYPE == "supermarket":
                    fill(255,120,10,40)
            noStroke()
            circle(x, y, mean_almond_milk)
            fill(1)
            textSize(15)
            text(NAME, x+30, y+10)
            
        #eggs           
    if mouseX >= 780 and mouseX <= 850 and mouseY>= 480 and mouseY <=520:      
        for row in data.rows():
            LATITUDE = row.getFloat("LATITUDE")
            LONGITUDE = row.getFloat("LONGITUDE")
            NAME = row.getString("NAME")
            TYPE = row.getString("TYPE")
            x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
            y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
            eggs = row.getFloat("eggs")  
            mean_eggs = map ( eggs, 1.99, 3.99, 45,60)
            if eggs == 0:
                fill(200)
            if TYPE == 'supermarket' and eggs > 0:
                fill(255,120,10,40)
            if TYPE == 'Produce' and eggs > 0:
                fill(0,255,0,40)
                noStroke()
            circle(x, y, mean_eggs)
            fill(1)
            noStroke()
            textSize(15)
            text(NAME, x+30, y+10)
         
         #oats           
    if mouseX >= 770 and mouseX <= 850 and mouseY>= 525 and mouseY <=570:      
        for row in data.rows():
            LATITUDE = row.getFloat("LATITUDE")
            LONGITUDE = row.getFloat("LONGITUDE")
            NAME = row.getString("NAME")
            TYPE = row.getString("TYPE")
            x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
            y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
            oats= row.getFloat("oats")  
            mean_oats = map (oats,4.99, 8, 40,58)
            if TYPE == "supermarket" and oats >0:
                fill(255,120,10,40)
            if TYPE == "Produce" and oats >0:
                     fill(0,255,0,40)
            if oats == 0:
                fill(200)
            noStroke()
            circle(x, y, mean_oats)
            fill(1)
            noStroke()
            textSize(15)
            text(NAME, x+30, y+10)
            
                
            #chicken
                
    if mouseX >= 770 and mouseX <= 850 and mouseY>= 580 and mouseY <=620:      
        for row in data.rows():
            LATITUDE = row.getFloat("LATITUDE")
            LONGITUDE = row.getFloat("LONGITUDE")
            NAME = row.getString("NAME")
            TYPE = row.getString("TYPE")
            x = map(LONGITUDE, minlong,maxlong, minframe, maxframe)
            y = map(LATITUDE, minlat, maxlat,maxframe,minframe)
            chicken = row.getFloat("chicken")  
            mean_chicken = map (chicken,1.99, 9.99, 40,58)
            if TYPE == 'supermarket' and chicken > 0:
                fill(255,120,10)
            if TYPE == 'Produce' and chicken >0:
                fill(0,255,0)
            if chicken == 0:
                fill(200)
            circle(x, y, mean_chicken)
            fill(1)
            noStroke()
            textSize(15)
            text(NAME, x+30, y+10)
                
            


            
            
    
            
                
            
    
    
            
            
        
    
