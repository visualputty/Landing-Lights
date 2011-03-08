$(function() {
    $( "#id_ship_name" ).autocomplete({
        source: function( request, response ) {
            $.ajax({
                url: "/passages/ajax_lookup",
                data: { q : request.term },
                dataType: "json",
                success: function( data ) {
                    response( $.map( data.passages, function( item ) {
                        return {
                            label: item.ship_name,
                            value: item.ship_name
                        };
                    }));
                }
            });
        },
        minLength: 2,
        select: function( event, ui ) {
            
        },
        open: function( ) {
            
        },
        close: function( ) {
            
        }
    });
});