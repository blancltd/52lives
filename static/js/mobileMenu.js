mobile_nav_button = document.querySelector('.nav__mobile-button');
mobile_nav_label = document.querySelector('.nav__mobile-label')

// Toggle aria-expanded for menu elements and change label
function toggleMenu(element, label) {
    let aria_expanded = element.getAttribute('aria-expanded');

    if (aria_expanded === 'true') {
        element.setAttribute('aria-expanded', 'false');
        label.innerHTML = 'Open Menu';
        aria_expanded = 'false';
    } else {
        element.setAttribute('aria-expanded', 'true');
        label.innerHTML = 'Close Menu';
        aria_expanded = 'true';
    }
}

if (mobile_nav_button) {
    mobile_nav_button.addEventListener('click', function() {
        toggleMenu(mobile_nav_button, mobile_nav_label);
    });
}
