var obj;


console.log(index)

//Create the XHR Object
let xhr = new XMLHttpRequest;
    //Call the open function, GET-type of request, url, true-asynchronous
    xhr.open('GET', 'http://127.0.0.1:8000/event/?format=json')
    xhr.setRequestHeader ("Authorization", "Bearer " + 'c85c0db20a11fdc080ee9379d684e6165384d0d9');
    //call the onload 
    xhr.onload = function() 
        {
            //check if the status is 200(means everything is okay)
            if (this.status >= 200 && this.status < 400) 
                {
                    //return server response as an object with JSON.parse
                    // console.log(this.response);
                    // console.log(this.responseText);
                    obj = JSON.parse(this.responseText);
                    console.log(obj)

                    // create grid for all objects
                    
                    obj.forEach(campaign => {
                      // Log each movie's title
                     console.log(campaign.event_heading);

                    })

                    //Heading
                    document.getElementById("event_heading").innerHTML = obj[index].event_heading

                    //evengt details
                    document.getElementById("event_body").innerHTML = obj[index].event_details

                    
                    //event date
                    document.getElementById("event_date").innerHTML = obj[index].event_date

                    // event_image background-image:url(http://127.0.0.1:8000/media/gallery/intro_4.jpg)
                    // Event Image
                    var event_bg_img = obj[index].event_banner
                    var img_str = "background-image:url(" +event_bg_img + ")"
                    var eventImage = document.getElementById("event_image")
                    eventImage.style = img_str

                    
                    
        }
                }
    //call send
    xhr.send();
    //Common Types of HTTP Statuses
    // 200: OK
    // 404: ERROR
    // 403: FORBIDDEN


function myFunction() {
    console.log(obj[5].event_banner);
  document.getElementById("myImg").src = obj[5].event_banner;
}

