// JavaScript Document
(function()
{
	var app = angular.module("lp", []);
	app.controller("LandingpageController", ['$scope', '$http', function($scope, $http){
		lp=this;
		this.company=["IBM","Google","TCS","Accenture","Musigma","Cisco","Infosys","Cognizant","Bosch","Microsoft","Amazon"];
		this.companySelected=this.company[0];
		this.city=["Bangalore"];
		this.citySelected=this.city[0];
			this.area=["Vijay Nagar","Bannerghatta Main Rd","Nagawara, Outer Ring Road","Bennigana Halli","K R Puram","Electronic City","Sheshadri Road Gandhinagar","Audugodi","Mylasandra & Patanegere Villages","Bannerghatta Road","Bellandur","Bannerghatta Main Road","Cunningham Road","Whitefield","Brookfield","Brigade South Parade M.G. Road","Krishnarajpuram Hobli","Manipal Center","Koramangala","Electronics City","Manayata Tech Park","CV Raman Nagar","Sampangi Rama Nagar","Rustam Bagh Layout","Hosur Road Adugodi","Challaghatta","Ashok Nagar", "Rajkumar Road"];
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
			});
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
		};
	}]);
})();
