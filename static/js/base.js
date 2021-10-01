const video_block = document.querySelectorAll('.blanc_page_blocktype_video');
const body = document.querySelector('body');

video_block.forEach((block) => {

    const play = block.querySelector('.video__play');
    const close = block.querySelector('.close');
    const lightbox = block.querySelector('.lightbox');

    if (lightbox) {
        const lightbox_append = lightbox.querySelector('.iframe__container');

        // Append video iframe using data attribute
        play.onclick = (event) => {
            event.preventDefault();
            lightbox_append.innerHTML = lightbox_append.dataset.append;
            lightbox.classList.add('active');
            body.classList.add('no-scroll');
        };

        close.onclick = (event) => {
            event.preventDefault();
            lightbox.classList.remove('active');
            lightbox_append.innerHTML = '';
            body.classList.remove('no-scroll');
        };
    }
});
var elem = document.querySelector('.lives-grid');
var pckry = new Packery( elem, {
  // options
  itemSelector: '.lifeblock',
  gutter: 0
});
