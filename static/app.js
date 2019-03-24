$(document).ready(function () {
    $.getJSON(("static/plant.json"), function (json) {
        function setHtml(z) {
            $(".species").html('Species: ' + json[z].species)
            $(".difficulty").html('Level of Difficulty: ' + json[z].Difficulty)
            $(".water").html('Level of Watering: ' + json[z].watering)
            $('.plantImage').attr('src', json[z].image)
            $(".previousImage").attr("src", json[z].image).animate({"margin-right": '400px' ,width: '400px', opacity: '1'},"slow")
            $('.light').html('Amount of Light: ' + json[z].light)
        }

        let userPlantArray = []
        //initial plant showing
        let i = 0;
        setHtml(0)
        //navigate thru cards
        $('.yesButton').click(() => {
            if (i < json.length) {
               //add plant to saved bbz list
                $('.yasPlants').append(`<li>${json[i].species}`);
                userPlantArray.push(json[i].species)
                $('#userPlants').val(userPlantArray)

                $(".plantImage").animate({ opacity: '0'},"fast");
                $(".plantImage").hide().attr("src", json[i].image).animate({"margin-left": '500px' ,width: '400px', opacity: '0'},"fast");
                $(".plantImage").animate({"margin-left": '0px', width: '400px', opacity: '1'}, "fast");



                //go onto next card
                i++;
                setHtml(i);
            } else if (i == json.length) {
                $('.swipedThru').css("display", "block");
            } else {
                $('.swipedThru').css("display", "block");
            }
        })
        //thank u next button
        $('.noButton').click(() => {
            if (i < json.length - 1) {
                i++;
                setHtml(i);

            } else {
                $('.swipedThru').css("display", "block");
            }
        })
        $('.mySpan').hide()
        $('.editButton').click(function (e) {
            $('.mySpan').show()
            console.log("!!!!!!!!!!!!!!!!!!!!!!EDIT CLICKED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        })

        $('.editProfileSpan').hide()
        $('.editProfileButton').click(function (e) {
            $('.editProfileSpan').show()
            console.log("!!!!!!!!!!!!!!!!!!!!!!EDIT CLICKED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        })
        


    });


    // !! slider stuff
    $(document).ready(function () {
        $('#slides').superslides({
            animation: 'fade',
            play: 5000,
            pagination: false
        });

    

    })



}) //end of document.ready