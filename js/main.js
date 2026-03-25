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
            container.innerHTML += `
                <div class="faculty-card">
                    <div class="faculty-img">
                        ${member.image ? `<img src="data/${member.image}" alt="${member.name}" style="width: 100%; height: 100%; object-fit: cover; object-position: top; position: relative; z-index: 2;">` : `<i class="${member.icon}"></i>`}
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
