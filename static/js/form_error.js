// If page loads with form errors - scroll to first form error list
var error_list = document.querySelector('form .errorlist');

if (error_list) {
    error_list.scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'nearest' });
}
