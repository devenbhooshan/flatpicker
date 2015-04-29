// JavaScript Document
(function()
{
	var app = angular.module("lp", []);
	app.controller("LandingpageController", ['$scope', '$http', function($scope, $http){
		lp=this;
		this.company=["IBM","Google","TCS","Accenture","Musigma","Cisco","Infosys","Cognizant","Bosch","Microsoft","Amazon"];
		this.companySelected=this.company[0];
		this.city=[];
		this.area=[];
		this.areaSelected=this.area[0];
		this.visibilityToggle=true;
		this.initialize=function(){
			// HTTP get requests
		};
		this.flatDetails=[];
		this.flatDetailsLeft=[];
		this.flatDetailsRight=[];
		this.submitReq=function(){
			this.visibilityToggle=false;
			$http.get('http://flatpicker.in/api/'+this.companySelected+"/"+this.citySelected+"/"+this.areaSelected).success(function(data){
				lp.flatDetails=data['flats'];
				var length;
				if(lp.flatDetails.length%2==0)
				{
					length=lp.flatDetails.length;
					
				}
				else
				{
					length=lp.flatDetails.length+1;
				}
					lp.flatDetailsLeft=lp.flatDetails.slice(0,length/2);
					lp.flatDetailsRight=lp.flatDetails.slice(length/2,length);
			});
		};
		this.getCity=function(){
			$http.get('http://flatpicker.in/api/'+this.companySelected).success(function(data){
				lp.city=data["city"];
				lp.citySelected=lp.city[0];
			});
		};
		this.getArea=function(){
			$http.get('http://flatpicker.in/api/'+this.companySelected+"/"+this.citySelected).success(function(data){
				lp.area=data["area"];
				lp.areaSelected=lp.area[0];
			});
		};
	}]);
})();
