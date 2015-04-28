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
		this.flatDetails=[{title:"3BHK Apartment for Rent",location:"Old Madras Road, Bangalore",price:"21,000/ M",size:"1400",bhk:"3",furnished:"",address:"Old Madras Road, Bangalore",pic_url:"http://ak.is2.cfcdn.com/is/p/t20/642x483/public/property-listing-images/verified/actual_size/54f53f76c391f.gif",dist:""},{title:"3BHK Apartment for Rent",location:"Old Madras Road, Bangalore",price:"21,000/ M",size:"1400",bhk:"3",furnished:"",address:"Old Madras Road, Bangalore",pic_url:"http://ak.is2.cfcdn.com/is/p/t20/642x483/public/property-listing-images/verified/actual_size/54f53f76c391f.gif"}];
		this.submitReq=function(){
			this.visibilityToggle=false;
			$http.get('/api/'+this.companySelected+"/"+this.citySelected+"/"+this.areaSelected).success(function(data){
				console.log(data);
				lp.flatDetails=data['flats'];
			});
		};
	}]);
})();
