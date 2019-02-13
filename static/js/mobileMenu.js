mobile_nav_button = document.querySelector('.nav__mobile-button');

// Toggle aria-expanded for menu elements
function updateMenuAria(element) {
    let aria_expanded = element.getAttribute('aria-expanded');

    if (aria_expanded === 'true') {
        element.setAttribute('aria-expanded', 'false');
        aria_expanded = 'false';
    } else {
        element.setAttribute('aria-expanded', 'true');
        aria_expanded = 'true';
    }
}

if (mobile_nav_button) {
    mobile_nav_button.addEventListener('click', function() {
        updateMenuAria(mobile_nav_button);
    });
}
