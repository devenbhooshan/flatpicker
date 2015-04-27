// JavaScript Document
(function()
{
	var app = angular.module("flatlist", []);
	app.controller("FlatsController", ['$scope', '$http', function($scope, $http){
		flat=this;
		this.flatDetails=[{title:"3BHK Apartment for Rent",location:"Old Madras Road, Bangalore",price:"21,000/ M",size:"1400",bhk:"3",furnished:"",address:"Old Madras Road, Bangalore",url:"http://ak.is2.cfcdn.com/is/p/t20/642x483/public/property-listing-images/verified/actual_size/54f53f76c391f.gif",dist:""},{title:"3BHK Apartment for Rent",location:"Old Madras Road, Bangalore",price:"21,000/ M",size:"1400",bhk:"3",furnished:"",address:"Old Madras Road, Bangalore",url:"http://ak.is2.cfcdn.com/is/p/t20/642x483/public/property-listing-images/verified/actual_size/54f53f76c391f.gif"}];
		this.initialize=function(){
			// HTTP get requests
		};
	}]);
})();
