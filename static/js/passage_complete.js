$(function() {
    $( "#id_ship_name" ).autocomplete({
        source: function( request, response ) {
            $.ajax({
                url: "/ajax_lookup",
                data: { q : request.term },
                dataType: "json",
                success: function( data ) {
                    response( $.map( data.vessels, function( item ) {
                        return {
                            label: item.ship_name,
                            value: item.ship_name,
                            details: item
                        };
                    }));
                }
            });
        },
        minLength: 2,
        select: function( event, ui ) {
            console.log(event);
            console.log(ui);
            selectedItem = ui.item.details;
            for (var i in selectedItem) {
                // Need to do something special for a checkbox
                if( $('#id_' + i ).attr('type') == 'checkbox' ){
                    // Do we need true or false?
                    if (selectedItem[i]) {
                        $('#id_' + i ).attr('checked', true);
                    } else {
                        $('#id_' + i ).attr('checked', false);
                    }
                } else {
                    $('#id_' + i ).val( selectedItem[i] );
                }
            }
        },
        open: function( ) {
            
        },
        close: function( ) {
            
        }
    });
});