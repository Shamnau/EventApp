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
    <img src="${event.img}" />
    <div class="card-content">
      <h3>${event.title}</h3>
      <p>${event.desc}</p>
      <button onclick="openModal('${event.title}')">Book Now</button>
    </div>
  `;

  eventsContainer.appendChild(card);
});

function openModal(title) {
  document.getElementById("modalTitle").innerText = title;
  document.getElementById("modal").style.display = "flex";
}

function closeModal() {
  document.getElementById("modal").style.display = "none";
}

function scrollToEvents() {
  document.getElementById("events").scrollIntoView({ behavior: "smooth" });
}
