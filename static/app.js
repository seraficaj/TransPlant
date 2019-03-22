$( document ).ready(function() {
    $.getJSON(("static/plant.json"), function(json) {
        function setHtml(z){
            $(".species").html('Species: '+json[z].species)
            $(".difficulty").html('Level of Difficulty: '+json[z].Difficulty)
            $(".water").html('Level of Watering: ' + json[z].watering)
            $('.plantImage').attr('src', json[z].image)
            $('.light').html('Amount of Light: ' + json[z].light)
        }
        //initial plant showing
        let i = 0;
        setHtml(0)
        //navigate thru cards
        $('.yesButton').click( () => {
            if (i < json.length) {
                //add plant to saved bbz list
                $('.yasPlants').append(`<li>${json[i].species}`);
                //go onto next card
                i++;
                setHtml(i);
                console.log(i);
            } else if (i == json.length) { 
                $('.swipedThru').css("display","block");
            } else {
                $('.swipedThru').css("display","block");
            }
        })
        //thank u next button
        $('.noButton').click( () => {
            if (i < json.length - 1) {
                i++;
                setHtml(i);
                console.log(i);
            }
            else {
                $('.swipedThru').css("display","block");
            }
        })
        $('.mySpan').hide()
        $('.editButton').click(function(e){
            $('.mySpan').show()
            console.log("!!!!!!!!!!!!!!!!!!!!!!EDIT CLICKED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        })
    }); //end of document.ready
})










