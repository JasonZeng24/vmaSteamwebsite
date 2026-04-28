// Matrix rain effect
const canvas = document.createElement('canvas');
canvas.id = 'matrix-bg';
document.body.insertBefore(canvas, document.body.firstChild);
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const chars = '0101010101';
const fontSize = 14;
const columns = canvas.width / fontSize;
const drops = [];

for (let i = 0; i < columns; i++) {
    drops[i] = 1;
}

function drawMatrix() {
    ctx.fillStyle = 'rgba(10, 25, 47, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#64ffda';
    ctx.font = fontSize + 'px monospace';

    for (let i = 0; i < drops.length; i++) {
        const text = chars[Math.floor(Math.random() * chars.length)];
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }
        drops[i]++;
    }
}

setInterval(drawMatrix, 50);

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

// Load events
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

// Load faculty
fetch('data/faculty.json')
    .then(response => response.json())
    .then(faculty => {
        const container = document.getElementById('faculty-container');
        faculty.forEach(member => {
            const imgHtml = member.image 
                ? `<img src="data/${member.image}" alt="${member.name}">`
                : `<i class="${member.icon}"></i>`;
            const hasImageClass = member.image ? ' has-image' : '';
            
            container.innerHTML += `
                <div class="faculty-card">
                    <div class="faculty-img${hasImageClass}">
                        ${imgHtml}
                    </div>
                    <div class="faculty-info">
                        <h3>${member.name}</h3>
                        <span class="role">${member.role}</span>
                        <p>${member.bio}</p>
                        <p><strong>Education:</strong> ${member.education}</p>
                        <div class="faculty-contact">
                            <a href="#"><i class="fas fa-envelope"></i> ${member.email}</a>
                            <a href="#"><i class="${member.contactIcon}"></i> ${member.contactLink}</a>
                        </div>
                    </div>
                </div>
            `;
        });
    });

// Load courses
fetch('data/courses.json')
    .then(response => response.json())
    .then(courses => {
        const container = document.getElementById('courses-container');
        courses.forEach(course => {
            container.innerHTML += `
                <div class="course-card">
                    <h3>${course.title}</h3>
                    <p>${course.description}</p>
                    <div class="course-details">
                        <div><i class="fas fa-clock"></i> ${course.duration}</div>
                        <div><i class="fas fa-star"></i> Prerequisites: ${course.prerequisites}</div>
                        <div><i class="${course.languagesIcon}"></i> ${course.languages}</div>
                        <div><i class="${course.extraIcon}"></i> ${course.extra}</div>
                    </div>
                </div>
            `;
        });
    });

// Animate stats on scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const counters = entry.target.querySelectorAll('.stat-number');
            counters.forEach(counter => {
                const target = parseInt(counter.getAttribute('data-target'));
                const duration = 2000;
                const step = target / (duration / 16);
                let current = 0;
                
                const updateCounter = () => {
                    current += step;
                    if (current < target) {
                        counter.textContent = Math.floor(current);
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.textContent = target;
                    }
                };
                
                updateCounter();
            });
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

const statsSection = document.querySelector('.about-stats');
if (statsSection) {
    observer.observe(statsSection);
}
