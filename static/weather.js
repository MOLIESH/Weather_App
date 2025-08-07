// Weather App JS - fetches weather data and updates the UI
const form = document.getElementById('weather-form');
const cityInput = document.getElementById('city-input');
const weatherInfo = document.getElementById('weather-info');
const tempElem = document.getElementById('temp');
const cityElem = document.getElementById('city');
const iconElem = document.getElementById('icon');
const conditionElem = document.getElementById('condition');
const errorMessage = document.getElementById('error-message');

const API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'; // <-- Replace with your OpenWeatherMap API key

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const city = cityInput.value.trim();
  if (!city) return;
  errorMessage.textContent = '';
  weatherInfo.style.display = 'none';
  try {
    const res = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${API_KEY}&units=metric`);
    if (!res.ok) throw new Error('City not found');
    const data = await res.json();
    tempElem.textContent = `${Math.round(data.main.temp)}° C`;
    cityElem.textContent = data.name;
    iconElem.innerHTML = `<img src="http://openweathermap.org/img/w/${data.weather[0].icon}.png" width="120px">`;
    conditionElem.innerHTML = `<p>${data.weather[0].description}</p><p>${new Date().toLocaleDateString(undefined, { weekday: 'long' })}</p>`;
    weatherInfo.style.display = 'flex';
  } catch (err) {
    errorMessage.textContent = 'City information is not available or invalid city name.';
  }
});