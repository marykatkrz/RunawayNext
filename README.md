# RunawayNext
RunawayNext is a social media site for both travelers and wannabe travelers. Users can personalize their own maps to show places that they have visited by adding a blog post of what they liked or didn't like about the location. Other users can then comment and interact in order to gain information and plan their own trips!

The design of the site is intentionally simple. It can be easy for a social media site to feel cluttered and that would take away from the point of this site. 

Mapbox GL JS allowed me to use JavaScript as a way of implementing maps to user's personal profile pages. When a user is signed in, they can search a location on the map, add a marker to that place, and then write their blog post of their time in that area. The latitude and longitude of the post is then saved in the database which I then used to place as points on the map upon page load. Only the user that is logged in can edit or delete their own posts. 

Blog posts are then displayed on the homepage where anyone logged in on the site can see what other people are saying and add their own comments/opinions/suggestions.



