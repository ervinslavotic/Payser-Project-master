$(document).ready(function() {

	var validator = new FormValidator('account-form', [{
	    name: 'name',
	    display: 'Name',    
	    rules: 'required'
	},{
	    name: 'email',
	    display: 'Email must be valid and Email',    
	    rules: 'required|valid_email'
	},{
	    name: 'company',
	    display: 'Company',    
	    rules: 'required'
	}], function(errors, event) {
	    if (errors.length > 0) {
	        var errorString = '';
	        
	        for (var i = 0, errorLength = errors.length; i < errorLength; i++) {
	            errorString += errors[i].message + '<br />';
	        }
	        
	        document.getElementById("errors").innerHTML = errorString;
	    }       
	});

});