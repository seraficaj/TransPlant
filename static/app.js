$(document).ready(function () {
    $.getJSON(("static/plant.json"), function (json) {

        function setHtml(z) {
            $(".species").html('Species: ' + json[z].species)
            $(".difficulty").html('Level of Difficulty: ' + json[z].Difficulty)
            $(".water").html('Level of Watering: ' + json[z].watering)
            $('.plantImage').attr('src', json[z].image)
            $('.light').html('Amount of Light: ' + json[z].light)
        }

        //initial plant showing
        setHtml(0)

        let i = 0;


        $(".yesButton").click(function (e) {
            setHtml(i)
            if (e.target === undefined) return;

            i = (i + 1)
            //  % json.length;
            if (i == 0) {
                $('.yasPlants').append('<li>' + json[i].species + '</li>')
            } else {
                $('.yasPlants').append('<li>' + json[i - 1].species + '</li>')
            }

        }); //end of yes click function 


        $(".noButton").click(function () {
            i = (i + 1) % json.length;
            setHtml(i)
        }); //end of no click function
    }); //end of getJson function

}); //end of document.ready