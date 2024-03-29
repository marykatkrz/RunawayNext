let req = new XMLHttpRequest();
let submit=document.getElementById("submit");
let token=document.getElementsByName("csrfmiddlewaretoken")[0];
let search=document.getElementById("search");
    req.addEventListener("progress", function(e) {
    });
    req.addEventListener("error", function(e) {
        target.innerText = "Error. Please Try Again.";
    });
    req.addEventListener("load", function(e) {
        let response = JSON.parse(req.responseText); 
        let value=JSON.parse(document.getElementById("loc-data").textContent);
        let my_obj=JSON.parse(value);
        mapboxgl.accessToken = '';
        let map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v9',
        center: [-94.7129, 37.0902],
        zoom: 3.2
    });
        let geocoder=new MapboxGeocoder({
            accessToken: mapboxgl.accessToken,
            mapboxgl: mapboxgl,
    });
        for(let i=0; i<my_obj.length; i++){
            let lng=my_obj[i].fields.lng
            let lat=my_obj[i].fields.lat
            let description=my_obj[i].fields.description
            let pk=my_obj[i].pk
            let spots=[lng,lat]
            let el = document.createElement('div');
            el.id = 'marker';
            new mapboxgl.Marker(el)
            let popup = new mapboxgl.Popup({ offset: 25 })
                .setHTML(`
                <div id="popup">
                  <h3><strong>${my_obj[i].fields.location}</strong></h3>
                   <p>${description}</p></br>
                   <p>
                   <a href="../post/${pk}/">Read More</a>
                   </p>
                </div>`)
            new mapboxgl.Marker(el)
                .setLngLat(spots)
                .setPopup(popup)
                .addTo(map)    
        }           
        geocoder.on('result', function(e){
            let input = e.result.geometry.coordinates
            function place(){
                if(e.result.place_type=="poi"){
                    return e.result.text
                }
                else if(e.result.place_type=="place"){
                    return e.result.place_name
            }
        }
            submit.addEventListener("click", function(){
                new mapboxgl.Marker(el)
                var popup = new mapboxgl.Popup({ offset: 25 })
                .setMaxWidth("350px")
                .setHTML(`
                <div id="popup">
                    <form action="../profiles/post/create/" method="post">
                    <input type="hidden" name="csrfmiddlewaretoken" value="${token.value}">
                    <input type="hidden" name="location" value="${place()}">
                    <input type="hidden" name="lng" value="${input[0]}">
                    <input type="hidden" name="lat" value="${input[1]}">
                    <h4>${place()}</h4>
                    <p>Short Description<p>
                    <input type="text" name="description">
                    <p>Add Post!</p>
                    <textarea type="text" name="post" placeholder="Favorite stops, recommendations, etc..."></textarea>
                    <button type="submit">Add a Post!</button>
                    <p><em>Marker will not save if a post is not added.</em></p>
                    </form>
                </div>`
                );              
                new mapboxgl.Marker(el)
                .setLngLat(input)
                .setPopup(popup) 
                .addTo(map)  
            });
            let el = document.createElement('div');
            el.id = 'marker';
        });
        map.addControl(geocoder)
        map.addControl(new mapboxgl.NavigationControl())
    });
req.open("GET", "https://api.mapbox.com/geocoding/v5/mapbox.places/portland.json?access_token=");
req.setRequestHeader("Authorization", 'Token token=""');
req.send()

