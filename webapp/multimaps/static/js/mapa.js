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

var mapaContainer = document.getElementById('mapa');

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

var eventoClimaticoMarkerClusterGroup = L.markerClusterGroup();
var eventosClimaticosGeoJson = L.geoJson(eventosClimaticosList, {
    onEachFeature: (feature, layer) => {
        let popupContent = feature.properties.popup_content;
        layer.bindPopup(popupContent);
        eventoClimaticoMarkerClusterGroup.addLayer(layer);
    },
    pointToLayer: (feature,latlng) => {
        return L.marker(latlng, {
            icon: L.AwesomeMarkers.icon({
                icon: "circle", 
                prefix: "fa", 
                markerColor: "blue"
            })
        });
    }
});

var fomeMarkerClusterGroup = L.markerClusterGroup();
var fomesGeoJson = L.geoJson(fomesList, {
    onEachFeature: (feature, layer) => {
        let popupContent = feature.properties.popup_content;
        layer.bindPopup(popupContent);
        fomeMarkerClusterGroup.addLayer(layer);
    },
    pointToLayer: (feature,latlng) => {
        return L.marker(latlng, {
            icon: L.AwesomeMarkers.icon({
                icon: "circle", 
                prefix: "fa", 
                markerColor: "black"
            })
        });
    }
});

var pesteMarkerClusterGroup = L.markerClusterGroup();
var pestesGeoJson = L.geoJson(pestesList, {
    onEachFeature: (feature, layer) => {
        let popupContent = feature.properties.popup_content;
        layer.bindPopup(popupContent);
        pesteMarkerClusterGroup.addLayer(layer);
    },
    pointToLayer: (feature,latlng) => {
        return L.marker(latlng, {
            icon: L.AwesomeMarkers.icon({
                icon: "circle", 
                prefix: "fa", 
                markerColor: "orange"
            })
        });
    }
});

mapa.addLayer(conflitoMarkerClusterGroup);
mapa.addLayer(eventoClimaticoMarkerClusterGroup);
mapa.addLayer(fomeMarkerClusterGroup);
mapa.addLayer(pesteMarkerClusterGroup);

var overlays = {
    "Conflitos": conflitoMarkerClusterGroup,
    "Eventos Climáticos": eventoClimaticoMarkerClusterGroup,
    "Fomes": fomeMarkerClusterGroup,
    "Pestes": pesteMarkerClusterGroup
};

L.control.layers(
    {}, 
    overlays, 
    {"autoZIndex": true, "collapsed": true, "position": "topright"}
).addTo(mapa);

const form = document.getElementById("form-filter");

form.addEventListener("submit", event => {
    event.preventDefault();

    let periodo = form.elements["periodo"].value;
    let url = filtroUrl + "?periodo=" + periodo;

    fetch(url)
    .then(response => response.json())
    .then(data => {
        conflitoMarkerClusterGroup.clearLayers();
        conflitosGeoJson.addData(JSON.parse(data.conflitos_geojson));

        eventoClimaticoMarkerClusterGroup.clearLayers();
        eventosClimaticosGeoJson.addData(JSON.parse(data.eventos_climaticos_geojson));

        fomeMarkerClusterGroup.clearLayers();
        fomesGeoJson.addData(JSON.parse(data.fomes_geojson));

        pesteMarkerClusterGroup.clearLayers();
        pestesGeoJson.addData(JSON.parse(data.pestes_geojson));
        
    });
});