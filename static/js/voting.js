// //remove it
//from.removeAttr("disabled");

function vote (submit_id, callback) {
	$token = document.cookie.replace(/(?:(?:^|.*;\s*)csrftoken\s*\=\s*([^;]*).*$)|^.*$/, "$1");
	$.ajax({
		type : 'POST',
		url : '/vote/',
		data : { 'id' : submit_id  },
		cache : false,
		headers : { 'X-CSRFToken':$token },
		success : callback
	});
}
function change_look_vote ($this, $voteNode, $sign, $votes_div) {
		$result=''
		$submit_id=$($this).attr('data')	
		vote($submit_id, function($result){
			if($result.error === "None"){

				if($sign == 1){
					$($this).removeClass("btn-default")
					$($this).addClass("btn-success")	
				
				}else if($sign == -1){

					$($this).removeClass("btn-success")
					$($this).addClass("btn-default")

				}
				$counter=$sign 
				$($votes_div).text(Number($($votes_div).text())+$counter)
				return 

			}else if($result.error === "Yes"){
				login_panel()

			}else{
				alert($result)
			}
		});
		
}
$('.upvote').click(function (){
		if($(this).hasClass('btn-success')){
			change_look_vote($(this),$(this).next(),-1,$(this).next())
		}
		else{
			change_look_vote($(this),$(this).next(),1,$(this).next())
		}
	});

