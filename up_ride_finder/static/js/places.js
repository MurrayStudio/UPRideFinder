function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 8,
    center: { lat: -34.397, lng: 150.644 }
  });
  var geocoder = new google.maps.Geocoder();

  var location;

  $.getJSON(window.location.href + "json", function (data) {
    location = data.dest_name;
    console.log(location);
    geocodeAddress(geocoder, map, location);
  });

}

function geocodeAddress(geocoder, resultsMap, address) {
  console.log(address);
  geocoder.geocode({ 'address': address }, function (results, status) {
    if (status === 'OK') {
      resultsMap.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
        map: resultsMap,
        position: results[0].geometry.location
      });
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}