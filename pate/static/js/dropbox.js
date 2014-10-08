$(document).ready(function(){

	dropbox = $('#dropbox');
	message = $('.message', dropbox);
	info    = $('.info', dropbox);
	progressbar_template = '<div class="progress"><div class="progress-bar" role="progressbar"></div></div>';

	dropbox.filedrop({
		paramname: 'file',
		maxfiles: 10,
		url: 'upload',

		uploadFinished:function(i,file,response){
		    progressbar = $.data(file);
		    if (response['success'] != undefined){
		        if (response['success']){
                    progressbar.attr('class', 'progress-bar progress-bar-success');
                    return;
		        } else {
		            progressbar.attr('class', 'progress-bar progress-bar-danger');
                    progressbar[0].innerText = progressbar[0].innerText + ' - ' + response['error_msg'];
                    return;
                }
		    }
			progressbar.attr('class', 'progress-bar progress-bar-danger');
		    return;
		},

    	error: function(err, file) {
			switch(err) {
				case 'BrowserNotSupported':
					showMessage('Your browser does not support HTML5 file uploads!');
					break;
				case 'TooManyFiles':
					alert('Too many files! Please select ' + this.maxfiles + ' at most!');
					break;
				default:
					break;
			}
		},

		uploadStarted:function(i, file, len){
	        t = $(progressbar_template);
	        progressbar = t.find('.progress-bar');
	        progressbar[0].innerText = file.name;
            t.appendTo(info);
            $.data(file, progressbar)
		},

		progressUpdated: function(i, file, progress) {
			$.data(file).width(progress+'%');
		}

	});

});