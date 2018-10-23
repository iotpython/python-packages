 webiopi().ready(function() {
        		webiopi().setFunction(17,"out");
        		webiopi().setFunction(18,"out");
        		webiopi().setFunction(22,"out");
        		webiopi().setFunction(23,"out");
    
        		
        		var content, button;
        		content = $("#content");
        		
        		button = webiopi().createGPIOButton(17,"Room 1 Light");
        		content.append(button);
        		
        		button = webiopi().createGPIOButton(18,"Room 2 Light");
        		content.append(button);
        		
        		button = webiopi().createGPIOButton(22,"Room 3 Light");
        		content.append(button);
        		
        		button = webiopi().createGPIOButton(23,"Room 4 Light");
        		content.append(button);
        		
        	
        		
        });