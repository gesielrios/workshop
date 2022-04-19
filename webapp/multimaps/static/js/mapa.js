let mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
            '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        mbUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw';

let streets  = L.tileLayer(mbUrl, {
    id: 'mapbox/streets-v11', 
    tileSize: 512, 
    zoomOffset: -1, 
    attribution: mbAttr
});

const mapaContainer = document.getElementById('mapa');

let mapa = L.map(mapaContainer, {
    center: [40.847, -2.878],
    zoom: 6,
    layers: [streets]
});

//Markers for Events with clusters
var conflitoMarkerClusterGroup = L.markerClusterGroup();
var conflitosGeoJson = L.geoJson(conflitosList, {
    onEachFeature: (feature, layer) => {
        let popupContent = feature.properties.popup_content;
        layer.bindPopup(popupContent);
        conflitoMarkerClusterGroup.addLayer(layer);
    },
    pointToLayer: (feature,latlng) => {
        return L.marker(latlng, {
            icon: L.AwesomeMarkers.icon({
                icon: "circle", 
                prefix: "fa", 
                markerColor: "red"
            })
        });
    }
});

mapa.addLayer(conflitoMarkerClusterGroup);

var overlays = {
    "Conflitos": conflitoMarkerClusterGroup,
};

L.control.layers(
    {}, 
    overlays, 
    {"autoZIndex": true, "collapsed": true, "position": "topright"}
).addTo(mapa);