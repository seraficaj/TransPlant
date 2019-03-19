$( document ).ready(function() {
    $.getJSON("static/dummy.json", function(json) {
          
        var i = 0;    
        //initial plant showing
        $(".species").html(json[i].name)
        $(".difficulty").html(json[i].difficulty)
        $(".water").html(json[i].water)
        $('.plantImage').attr('src', json[i].image)
        

        $(".yesButton").click(function(){
            i= (i+1)%json.length;
            $( ".species" ).html(json[i].name) ;
            $(".difficulty").html(json[i].difficulty)
            $(".water").html(json[i].water)
            $('.plantImage').attr('src', json[i].image)    
            if (i==0){
                $('.yasPlants').append('<li>' + json[json.length-1].name+ '</li>')
            }else{
                $('.yasPlants').append('<li>' + json[i-1].name+ '</li>')
            }
            console.log(i, "!!!!")

        }); //end of yes click function 
        
        $(".noButton").click(function(){
            i= (i+1)%json.length;
            $( ".species" ).html(json[i].name) ;
            $(".difficulty").html(json[i].difficulty)
            $(".water").html(json[i].water)
            $('.plantImage').attr('src', json[i].image)    
        }); //end of no click function
    });//end of getJson functuion

}); //end of document.ready  