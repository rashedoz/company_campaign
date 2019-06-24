//fetch using a Request and a Headers objects
//using jsonplaceholder for the data




function MyController($scope, $http) {
    $scope.items = []

    $scope.getItems = function() {
     $http({method : 'GET',url : 'https://api.parse.com/1/classes/Users', headers: { 'X-Parse-Application-Id':'XXXXXXXXXXXXX', 'X-Parse-REST-API-Key':'YYYYYYYYYYYYY'}})
        .success(function(data, status) {
            $scope.items = data;
         })
        .error(function(data, status) {
            alert("Error");
        })
    }
}

const uri = 'http://127.0.0.1:8000/hello/';
console.log('requesting api');
//new Request(uri)
//new Request(uri, options)
//options - method, headers, body, mode
//methods:  GET, POST, PUT, DELETE, OPTIONS

//new Headers()
// headers.append(name, value)
// Content-Type, Content-Length, Accept, Accept-Language,
// X-Requested-With, User-Agent
let h = new Headers();
h.append('Accept', 'application/json');
h.append("Access-Control-Allow-Origin", "*");

let req = new Request(uri, {
    method: 'GET',
    headers: h,
    mode: 'no-cors'
});

fetch(req)
    .then( (response)=>{
        if(response.ok){
            return response.json();
        }else{
            throw new Error('BAD HTTP stuff');
        }
    })
    .then( (jsonData) =>{
        console.log(jsonData);
    })
    .catch( (err) =>{
        console.log('ERROR:', err.message);
    });



    var testApp = angular.module("testApp", []);

testApp.controller("testController", function($scope, $http) {
  $scope.home = "This is the homepage";

  $scope.getRequest = function() {
    console.log("I've been pressed!");
    $http.get("http://127.0.0.1:8000/hello/").then(
      function successCallback(response) {
        $scope.response = response;
      },
      function errorCallback(response) {
        console.log("Unable to perform get request");
      }
    );
  };
});
