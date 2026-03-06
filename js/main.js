fetch('data/events.json')
    .then(response => response.json())
    .then(events => {
        const container = document.getElementById('events-container');
        events.forEach(event => {
            container.innerHTML += `
                <div class="event-item">
                    <div class="event-content">
                        <div class="event-date">${event.date}</div>
                        <h3>${event.title}</h3>
                        <p>${event.description}</p>
                        <a href="${event.link}" class="cta-button">Register Now</a>
                    </div>
                </div>
            `;
        });
    });
