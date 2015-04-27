// JavaScript Document
(function()
{
	var app = angular.module("lp", []);
	app.controller("LandingpageController", ['$scope', '$http', function($scope, $http){
		lp=this;
		this.company=["Company","Google", "Microsoft","TCS","Wipro", "Accenture"];
		this.companySelected=this.company[0];
		this.city=["City","Bangalore"];
		this.citySelected=this.city[0];
		this.area=["Area", "All"];
		this.areaSelected=this.area[0];
		this.visibilityToggle=true;
		this.initialize=function(){
			// HTTP get requests
		};
		this.submitReq=function(){
			this.visibilityToggle=false;
		};
	}]);
})();
