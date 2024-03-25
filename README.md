Part A
Using socket programming, implement a simple complete web server in python that is listening on port 9977.
1-	if the request is / or /index.html or /main_en.html or /en (for example localhost:9977/ or localhost:9977/en) then the server should send main_en.html file with Content-Type: text/html. 
2-	If the request is /ar then the server response with main_ar.html which is an Arabic version of main_en.html 
3-	if the request is an .html file then the server should send the requested html file with Content-Type: text/html. 
4-	if the request is a .css file then the server should send the requested css file with Content-Type: text/css.
5-	if the request is a .png then the server should send the png image with Content-Type: image/png. 
6-	if the request is a .jpg then the server should send the jpg image with Content-Type: image/jpeg. 
7-	Use  the status code 307 Temporary Redirect to redirect the following
    a.	If the request is /yt then redirect to youtube website
    b.	If the request is /so then redirect to stackoverflow.com website
    c.	If the request is /rt then redirect to ritaj website
8-	If the request is wrong or the file doesn’t exist the server should return a simple HTML webpage that contains (Content-Type: text/html)

Part B
Using socket programming, implement UDP client and server applications in python. The server should listen on port 8855. The client sends broadcast messages every 2 seconds. 
