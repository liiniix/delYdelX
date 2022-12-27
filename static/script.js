$( document ).ready(function() {
    $('[data-toggle="tooltip"]').tooltip();

    $('.bi-lightning-charge-fill').click(function(){
        $('#word-of-week-1-serial-1-accordion-header button').addClass('text-danger')
    });

    $('.card').click(function(){
        const url = $(this).data('redirect-url');
        location.href = url;
    });
});