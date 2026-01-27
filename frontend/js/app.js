const events = [
  {
    title: "Corporate Events",
    desc: "Professional planning for corporate meetings",
    img: "https://images.unsplash.com/photo-1503428593586-e225b39bddfe"
  },
  {
    title: "Wedding Planning",
    desc: "Make your special day unforgettable",
    img: "images/wedding.jpg"
  },
  {
    title: "Music Concerts",
    desc: "Live shows with amazing experience",
    img: "images/music.jpg"
  },
  {
    title: "Tech Conferences",
    desc: "Innovative technology events",
    img: "https://images.unsplash.com/photo-1551836022-d5d88e9218df"
  }
];

const eventsContainer = document.getElementById("events");

events.forEach(event => {
  const card = document.createElement("div");
  card.className = "card";

  card.innerHTML = `
    <img src="${event.img}" alt="${event.title}" />
    <div class="card-content">
      <h3>${event.title}</h3>
      <p>${event.desc}</p>
     <a href="http://localhost:8001/booking/?event=${encodeURIComponent(event.title)}">
        <button>Book Now</button>
      </a>
    </div>
  `;

  eventsContainer.appendChild(card);
});
