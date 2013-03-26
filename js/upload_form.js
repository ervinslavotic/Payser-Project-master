$(document).ready(function() {
	if($("#type-selector").val() == "payslip") {
		var validator = new FormValidator('upload-form', [{
		    name: 'company',
		    display: 'Company',    
		    rules: 'required'
		}, {
		    name: 'income',
		    display: 'Income field must be numeric and Income',    
		    rules: 'required||numeric'
		},{
		    name: 'tax',
		    display: 'Tax field must be numeric and Tax',    
		    rules: 'required||numeric'
		},{
		    name: 'beginning',
		    display: 'beginning',    
		    rules: 'required'
		},{
		    name: 'ending',
		    display: 'ending',    
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
	}else{
		var validator = new FormValidator('upload-form', [{
		    name: 'title',
		    display: 'Title',    
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
	}
	
});


