// JavaScript Document
(function()
{
	var app = angular.module("lp", ['ngProgress']);
	app.controller("LandingpageController", ['$scope', '$http','$window','ngProgress', function($scope, $http,$window,ngProgress){
		lp=this;
		this.company=["IBM","Google","TCS","Accenture","Musigma","Cisco","Infosys","Cognizant","Bosch","Microsoft","Amazon"];
		this.companySelected=this.company[0];
		this.city=["City"];
		this.citySelected=this.city[0];
		this.area=["Area"];
		this.areaSelected=this.area[0];
		this.visibilityToggle=true;
		this.flatDetails=[];
		this.flatDetailsLeft=[];
		this.flatDetailsRight=[];

		this.cityError=false;
		this.areaError=false;
		this.visibility=false;
		
		console.log("Fiddling");
		
		this.submitReq=function(){
			var flag = false;
			if(this.citySelected=="City")
			{
				flag=true;
				this.cityError=true;
			}
			if(this.areaSelected=="Area")
			{
				flag=true;
				this.areaError=true;
			}
			if(true)
			{
				ngProgress.color("#1f8dd6");
				ngProgress.start();
				this.cityError=false;
				this.areaError=false;
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
					ngProgress.complete();
				});
			}
		};
		this.getCity=function(){
			$http.get('http://flatpicker.in/api/'+this.companySelected).success(function(data){
				lp.city=data["city"];
				if(lp.city.length ==0)
				{
					lp.city=["City"];
				}
				lp.citySelected=lp.city[0];
				lp.getArea();
			});
		};
		this.getCity();
		this.getArea=function(){
			$http.get('http://flatpicker.in/api/'+this.companySelected+"/"+this.citySelected).success(function(data){
				lp.area=data["area"];
				if(lp.area.length ==0)
				{
					lp.area=["Area"];
				}
				lp.areaSelected=lp.area[0];
			});
		};
	}]);
})();
