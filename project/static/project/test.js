function initMap() {
  const directionsRenderer = new google.maps.DirectionsRenderer();
  const directionsService = new google.maps.DirectionsService();
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: { lat: 37.77, lng: -122.447 },
  });

  directionsRenderer.setMap(map);
  calculateAndDisplayRoute(directionsService, directionsRenderer);
}

function calculateAndDisplayRoute(directionsService, directionsRenderer) {
  origin=document.getElementById("frfr").value.toString();
  dest=document.getElementById("toto").value.toString();
  console.log(origin)
  console.log(dest)
  directionsService
    .route({
      origin:origin,
      destination:dest,
      travelMode:"TRANSIT",
      region:"israel"
    })
    .then((response) => {
      directionsRenderer.setDirections(response);
    })
    .catch((e) => window.alert("Directions request failed due to " + status));
}
