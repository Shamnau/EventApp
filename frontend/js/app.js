const events = [
  {
    name: "Music Concert",
    date: "25 Jan 2026",
    location: "Chennai",
    image: "images/music.jpg"
  },
  {
    name: "Tech Conference",
    date: "10 Feb 2026",
    location: "Bangalore",
    image: "images/tech.jpg"
  },
  {
    name: "Wedding Expo",
    date: "18 Mar 2026",
    location: "Kochi",
    image: "images/wedding.jpg"
  }
];

const eventsDiv = document.getElementById("events");

events.forEach(event => {
  eventsDiv.innerHTML += `
    <div class="card">
      <img src="${event.image}" />
      <div class="card-content">
        <h3>${event.name}</h3>
        <p>${event.date} | ${event.location}</p>
        <button>Register</button>
      </div>
    </div>
  `;
});
