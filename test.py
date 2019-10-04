<h3> <u> Added
Cities
Weather </u> </h3>
{ %
for city_weather in weather_data %}
<div


class ="box">

<article


class ="media">

<div


class ="media-left">

<figure>
<img
src = "http://openweathermap.org/img/w/{{ city_weather.icon }}.png"
alt = "Image">
</figure>
</div>
<div


class ="media-content">

<div


class ="content">

<p>
<span


class ="title"> {{city_weather.city}} </span>

<br>
<span


class ="subtitle"> {{city_weather.temperature}}° C </span>

<br> {{city_weather.description}}
</p>
</div>
</div>
<div


class ="media-right">

<a
href = "{% url 'delete_city' city_weather.city %}">
<button


class ="delete"> </button>

</a>
</div>
</article>
</div>
{ % endfor %}
