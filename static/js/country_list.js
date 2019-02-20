var country_select = document.getElementById('id_nominee_set-0-country');

if (country_select) {
    // Find the index of the last frequently used country (this is a hack - see function below)
    last_frequently_used_country = find_first_alphabetical_name(country_select);

    // Add option separator but only when any frequently selected countries have been found
    if (last_frequently_used_country != 1) {
        var option_separator = document.createElement("option");
        option_separator.text = "---------";
        country_select.add(option_separator, country_select[last_frequently_used_country])
    }
}

/**
 * Find the index of the last option before several alphabetically-ordered options
 * 
 * This is a bit of a hack to find the index of the last of the frequently-used
 * options. It relies on the (probable) assumptions that:
 *   - there won't be 5 frequently-used country names beginning with 'A'
 *   - the last of the frequently-used country names will not be one beginning
 *     with 'A'
 * This function finds the first five options that begin with 'A' and returns
 * the index of the option immediately before the first of those five.
 * 
 * @param {HTMLElement} country_select 
 */
function find_first_alphabetical_name(country_select) {
    var number_of_countries_to_count = 5;

    var count_of_alphabetical_countries = 0;
    var i = 0;
    do {
        var option = country_select[i];
        if (option.tagName != 'OPTION') { continue }
        if (option.text.substring(0, 1) === 'A') { 
            count_of_alphabetical_countries += 1;
        } else {
            count_of_alphabetical_countries = 0;
        }
        i++;
    } while (count_of_alphabetical_countries < number_of_countries_to_count)

    return i - number_of_countries_to_count;
}
