var obj;
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
                     //console.log(campaign.event_heading);

                    var cardApp = document.getElementById('introBody')
                    //console.log(cardApp)

                    //create intro container
                    var introContainer = document.createElement('div')
                    introContainer.setAttribute('class','intro_item')
                    cardApp.appendChild(introContainer)

                    //intro image 
                    var introImageContainer = document.createElement('div')
                    introImageContainer.setAttribute('class','intro_image')
                    introContainer.appendChild(introImageContainer)

                    //container image
                    const banner = document.createElement('img')
                    banner.src = campaign.event_banner
                    introImageContainer.appendChild(banner)

                    //intro body
                    var introBody = document.createElement('div')
                    introBody.setAttribute('class','intro_body')
                    introContainer.appendChild(introBody)

                    //intro title
                    var introTitle = document.createElement('div')
                    introTitle.setAttribute('class','intro_title')
                    introBody.appendChild(introTitle)

                    //into link text
                    var introLink = document.createElement('a')
                    introLink.text = campaign.event_heading
                    introTitle.appendChild(introLink)
                    })
                    
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

//creating body dynamically 

// var app = document.getElementById('campaign_card')
// console.log(app)
// //create banner img
// const banner = document.createElement('img')
// banner.src = 'http://127.0.0.1:8000/media/gallery/event_2.jpg'

// //create container
// const container = document.createElement('div')
// container.setAttribute('class','container')

// //append elements in child
// app.appendChild(banner)
// app.appendChild(container)

// console.log('creating grids')
// //console.log(obj)
// for (i = 0; i < 5; i++){}