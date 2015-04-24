function login_panel () {
	$('#login_link').click()
	return false;
}
$('#feedback_submit').click(function  () {
	
	$comment=$(document.getElementsByName('feedback_comment')).val()
	$email=$(document.getElementsByName('feedback_email')).val()

	if( $comment.length <=5 ){
		$('#feedback_alert').show()
	}else{
		$token = document.cookie.replace(/(?:(?:^|.*;\s*)csrftoken\s*\=\s*([^;]*).*$)|^.*$/, "$1");
		$.ajax({
			type : 'POST',
			url : '/feedback/new',
			data : { 'comment' : $comment , 'email' : $email },
			cache : false,
			headers : { 'X-CSRFToken':$token },
			success : function (data) {
				$('#feedback_alert').hide()
				$('#feedback_success').show()
				$(document.getElementsByName('feedback_comment')).val('')
			}
		});

	}

});

$("#next_feed").click(function () {
	if( $(this).attr("disabled") == "disabled" )
		return
	$page=parseInt($(this).attr('data'))
	$token = document.cookie.replace(/(?:(?:^|.*;\s*)csrftoken\s*\=\s*([^;]*).*$)|^.*$/, "$1");
		$.ajax({

			type : 'GET',
			url : '/allactivity/',
			data : {'page':$page,'feed_type':1},
			success : function (data) {
				if (data[0] == true){
					$("#next_feed").attr('disabled','disabled')
				}
					$("#next_feed").attr('data',$page+1)
					$("#previous_feed").attr('data',$page-1)
					$("#previous_feed").removeAttr('disabled')

					data=data[1]
				var ii =''
				for (var i = 0; i < data.length; i++) {
					
					ii +='<li style="min-height:80px" class="list-group-item" >'+ data[i][0] +'<div style="text-align:right"> ' + data[i][1] + ' </div></li>'
					
				};
				$("#feed_content").html(ii)
			}
		});
});

$("#previous_feed").click(function () {
	if( $(this).attr("disabled") == "disabled" )
		return
	$page=parseInt($(this).attr('data'))
	$token = document.cookie.replace(/(?:(?:^|.*;\s*)csrftoken\s*\=\s*([^;]*).*$)|^.*$/, "$1");
		$.ajax({

			type : 'GET',
			url : '/allactivity/',
			data : {'page':$page,'feed_type':1},
			success : function (data) {

				if ($page == 1){	
					$("#previous_feed").attr('disabled','disabled')
				}
				$("#next_feed").removeAttr('disabled')
				$("#next_feed").attr('data',$page+1)
				$("#previous_feed").attr('data',$page-1)

				data=data[1]
				var ii =''
				for (var i = 0; i < data.length; i++) {
					ii +='<li style="min-height:80px" class="list-group-item"> '+ data[i][0] +'<div style="text-align:right"> ' + data[i][1] + ' </div></li>'
				};
				$("#feed_content").html(ii)
			}
		});
});

 $(window).load(function(){
        $('#dedicated_link').modal('show');
    });