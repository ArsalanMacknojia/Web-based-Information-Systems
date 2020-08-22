
$(document).ready(function(){
    $("#fadeButton").click(function(){
        $("#div1").fadeToggle(200);
        $("#div2").fadeToggle(500);
        $("#div3").fadeToggle(800);
    });

    $("#animationButton").click(function(){
        var div = $("#animationBox");
        div.animate({height: '300px', opacity: '0.4'}, "slow");
        div.animate({width: '300px', opacity: '0.8'}, "slow");
        div.animate({height: '100px', opacity: '0.4'}, "slow");
        div.animate({width: '100px', opacity: '0.8'}, "slow");
    });

    $("#flip").click(function(){
        $("#panel").slideToggle("slow");
    });

});

document.addEventListener('DOMContentLoaded', function() {
    let form = document.getElementById('flags');
    form.addEventListener('submit', function() {
        addFlagsToList(event);
        clearForm();
    });
});

function addFlagsToList(event) {
    event.preventDefault();
    let name = event.target.country.value;

    let container = document.createElement('div');
    container.id = name.toLowerCase();

    let content = document.createElement('p');
    content.innerHTML = `${name}`;
    container.appendChild(content);

    let image = document.createElement('img');
    image.src = `https://www.countryflags.io/${name.toLowerCase()}/shiny/64.png`;
    image.alt = name
    container.appendChild(image);

    let list = document.getElementById('my_flag-list');
    list.appendChild(container);
}

function clearForm() {
    document.getElementById('flags').reset();
}