
    
initXMLHttpRequest('GET','http://127.0.0.1:8000/hello/','c85c0db20a11fdc080ee9379d684e6165384d0d9')
    var url = 'http://127.0.0.1:8000/hello/'
    var request = new XMLHttpRequest()
    const proxyurl = "https://cors-anywhere.herokuapp.com/";
    fetch(proxyurl + url) 
request.open('GET', url)
request.setRequestHeader('Authorization' , 'c85c0db20a11fdc080ee9379d684e6165384d0d9')
request.onload = function() {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)

  if (request.status >= 200 && request.status < 400) {
    data.forEach(movie => {
      console.log(movie.event_heading)
    })
  } else {
    console.log('error')
  }
}

request.send()
function initXMLHttpRequest(method, url, jwtoken){
    let xmlHttpRequest = new XMLHttpRequest();
    xmlHttpRequest.open(method, url);
    xmlHttpRequest.setRequestHeader('Authorization', 'Bearer ' + jwtoken);
    return xmlHttpRequest;
}