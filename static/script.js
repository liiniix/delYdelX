$( document ).ready(function() {
    $('[data-toggle="tooltip"]').tooltip();

    $('.bi-lightning-charge-fill').click(function(){
        $('#word-of-week-1-serial-1-accordion-header button').addClass('text-danger')
    });

    $('.card').click(function(){
        const url = $(this).data('redirect-url');
        location.href = url;
    });

    $(document).on('click', '.mark-icon', function(){
        markWord(this);
    });
});

function markWord(element) {
    const alreadyMarked = $(element).closest('.word-and-buttons').hasClass('red')
    
    if(alreadyMarked){
        $(element).closest('.word-and-buttons').removeClass("red");
        return;
    }

    $(element).closest('.word-and-buttons').addClass("red");
}