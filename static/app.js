$( document ).ready(function() {
    $.getJSON(("static/plant.json"), function(json) {
        function setHtml(z){
            $(".species").html('Species: '+json[z].species);
            $(".difficulty").html('Level of Difficulty: '+json[z].Difficulty);
            $(".water").html('Level of Watering: ' + json[z].watering);
            $('.plantImage').attr('src', json[z].image);
            $('.light').html('Amount of Light: ' + json[z].light);
        }
        //initial plant showing
        let i = 0;
        setHtml(0)

        $('.yesButton').click( () => {
            if (i < json.length - 1) {
                i++;
                setHtml(i);
                console.log(i);
            }
        })
        $('noButton').click( () => {
        })


        // $(".yesButton").click(function(){
        //     i= (i+1)%json.length;
        //     setHtml(i)
        //     if (i==0){
        //         $('.yasPlants').append('<li>' + json[json.length-1].species+ '</li>')
        //     }else{
        //         $('.yasPlants').append('<li>' + json[i-1].species+ '</li>')
        //     }

        // }); //end of yes click function 

        // $(".noButton").click(function(){
        //     i= (i+1)%json.length;
        //     setHtml(i)
        // }); //end of no click function
    });//end of getJson functuion

}); //end of document.ready  