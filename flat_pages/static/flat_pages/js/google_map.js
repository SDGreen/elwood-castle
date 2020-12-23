let map;
const elwoodCastle = { lat: 51.915530, lng: -2.019524 }
function initMap() {

    map = new google.maps.Map(document.getElementById("map"), {
        center: elwoodCastle,
        zoom: 12,
    });

    const marker = new google.maps.Marker({
        position: elwoodCastle,
        map: map,
    });

}


