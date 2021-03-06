// save the initial load hash so we can use it if set
app.hash = window.location.hash;

app.onResize = function(percent) {

  var height = $(window).height();
  var width = $(window).width();
  // when fullscreen be odd?
  if (height) {
    //if (!app.embeddedMap) {
    if ( width > 767 && !app.embeddedMap ) {
        //$("#map").height(height);
        if ($('#map-panel').hasClass('fullscreen-data')) {
          $("#map-wrapper").height(height);
        } else {
          $("#map-wrapper").height(height-$('#compass-search-header').height());
        }
        // $(".tabs").height(height);
        //$("#legend-wrapper").height(height - 20);
        $("#data-accordion").height(height - 243 - (($.browser.msie && $.browser.version < 9)? 130: 96));
        $("#designs-accordion").height(height - 70 - (($.browser.msie && $.browser.version < 9)? 130: 232));
        //$("#active").height(height + 20 - (($.browser.msie && $.browser.version < 9)? 130: 96));
        $('#myTabContent').height(height - 295);
    }
    app.map.render('map');
  }

  app.viewModel.updateAllScrollBars();

  app.viewModel.hideTours(false);

};

$(window).on('resize', function() {
    app.onResize();
});

// add indexof for typeahead
if (!Array.prototype.indexOf) {

    Array.prototype.indexOf = function(obj, start) {
         for (var i = (start || 0), j = this.length; i < j; i++) {
             if (this[i] === obj) { return i; }
         }
         return -1;
    };
 }


// state of the app
app.state = {
  //list of active layer ids in order they appear on the map
  activeLayers: [],
  location: {}
};

// property to store the state of the map for restoring
app.restoreState = {};

ko.applyBindings(app.viewModel);
app.viewModel.loadLayersFromServer().done(function() {
  $('#fullscreen').show();
  app.viewModel.spinnerList.remove('loadLayersFromServer');
  // app.map.updateSize();
  app.onResize();

  // trigger events that depend on the map
  $(document).trigger('map-ready');

if (app.hash) {
  app.loadStateFromHash(app.hash);
} else if (app.MPSettings.default_hash) {
  app.loadStateFromDefaultHash(app.MPSettings.default_hash);
}

  // autocomplete for filter
  $('.search-box').typeahead({
    source: app.typeAheadSource
  });

  if ( ! ($.browser.msie && $.browser.version < 9) && ! app.embeddedMap ) {
    $("#data-accordion").jScrollPane();
  }
    //$("#legend-wrapper").jScrollPane();
  // }
});

// initialize the map
app.init();
// Google.v3 uses EPSG:900913 as projection, so we have to
// transform our coordinates
app.initializeMapLocation = function(mapInit) {
    if (mapInit) {
      var latitude = mapInit.latitude,
          longitude = mapInit.longitude,
          zoom = mapInit.zoom
    } else {
      var latitude = 40.46,
          longitude = -124.56,
          zoom = 5;

      if (app.MPSettings && app.MPSettings.latitude && app.MPSettings.longitude) {
          latitude = app.MPSettings.latitude;
          longitude = app.MPSettings.longitude;
      }
      if (app.MPSettings && app.MPSettings.zoom) {
          zoom = app.MPSettings.zoom;
      }
    }

    app.map.setCenter(new OpenLayers.LonLat(longitude, latitude).transform(
        new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")), zoom);

};
// if we have the hash state go ahead and load it now
var mapInit = false;
if (app.hash) {
  app.loadStateFromHash(app.hash);
  mapInit = {
    'latitude': app.state.y,
    'longitude': app.state.x,
    'zoom': app.state.z
  }
} else if (app.MPSettings.default_hash) {
  app.loadStateFromDefaultHash(app.MPSettings.default_hash);
}
app.initializeMapLocation(mapInit);

setTimeout(function() {
    app.map.mousedrag = false;
}, 800);


$(document).ready(function() {
  app.onResize();
  $(window).resize(app.onResize);

  //Do not display any warning for missing tiles
  OpenLayers.Util.onImageLoadError = function(){
    this.src = 'https://openlayers.org/api/img/blank.gif';
  };
  OpenLayers.Tile.Image.useBlankTile=false;

  // if we have the hash state go ahead and load it now
  /*if (app.hash && !app.loginHash) {
    console.log('document ready without #login hash');
    app.loadStateFromHash(app.hash);
  } */
  // handle coordinate indicator on pointer
  $('#map').bind('mouseleave mouseenter', function(e) {
    $('#pos').toggle();
  });
  $('#map').bind('mousemove', function(e) {
    $('#pos').css({
      left: e.pageX + 20,
      top: e.pageY + 20
    });
  });


  $('.form-search').find('.btn').on('click', function(event) {
     $(event.target).closest('form').find('input').val(null).focus();
  });

  if(app.MPSettings && app.MPSettings.enable_drawing === "True") {
    app.viewModel.enableDrawing(true);
  }


  //fixes a problem in which the data accordion scrollbar was reinitialized before the app switched back to the data tab
  //causing the data tab to appear empty
  //the following appears to fix that problem
  $('#dataTab[data-toggle="tab"]').on('shown', function(e) {
    app.viewModel.showBottomButtons(true);
    app.viewModel.updateScrollBars();
    app.viewModel.showLegend(false);
    $('#active').removeClass('in');
    $('#active').removeClass('active');
    $('#legend').removeClass('in');
    $('#legend').removeClass('active');
    $('#data').addClass('active');
    $('#data').addClass('in');
  });
  $('#activeTab[data-toggle="tab"]').on('shown', function(e) {
    app.viewModel.showBottomButtons(true);
    app.viewModel.updateScrollBars();
    app.viewModel.showLegend(false);
    $('#legend').removeClass('in');
    $('#legend').removeClass('active');
    $('#data').removeClass('in');
    $('#data').removeClass('active');
    $('#active').addClass('active');
    $('#active').addClass('in');
  });
  $('#legendTab[data-toggle="tab"]').on('shown', function(e) {
    app.viewModel.showBottomButtons(true);
    app.viewModel.showLegend(true);
    app.viewModel.updateScrollBars();
    $('#active').removeClass('in');
    $('#active').removeClass('active');
    $('#data').removeClass('in');
    $('#data').removeClass('active');
    $('#legend').addClass('active');
    $('#legend').addClass('in');
  });

  //the following appears to handle the bookmark sharing, while the earlier popover activation handles the design sharing
  setTimeout(function() {$('.group-members-popover').popover({html: true, trigger: 'hover', container: 'body'});}, 2000);

  //format the legend scrollbar
  //setTimeout(function() { $('#legend-content').jScrollPane(); }, 500);
  //setTimeout(function() { app.viewModel.updateScrollBars(); }, 500);

  //resizable behavior for overview-overlay
  //might not use the following after all...
  //(having problems setting minHeight, losing resizing ability
  /*
  $("#overview-overlay").resizable({
    handles: 'n',
    containment: 'parent'
    }
  })
  */

  $('#add-layer-modal').on('shown', function () {
    // do something…
    $('#add-layer-modal .icon-info-sign').popover({
      trigger: 'hover',
      container: 'body'
    });
  });

  app.fullscreen = {};
  // fullscreen stuff
  // for security reasons, this event listener must be bound directly
  if ( document.getElementById('btn-fullscreen') ) {
      if ( document.getElementById('btn-fullscreen').addEventListener ) {
          document.getElementById('btn-fullscreen').addEventListener('click', function() {
            if ( BigScreen.enabled ) {
              BigScreen.toggle(document.getElementById('fullscreen'));
              // You could also use .toggle(element)
            } else {
              // fallback for browsers that don't support full screen
              $('#fullscreen-error-overlay').show();
            }
          }, false);
      } else {
          $('#btn-fullscreen').on('click', function() {
            // fallback for browsers that don't support addEventListener
            $('#fullscreen-error-overlay').show();
          });
      }
  }

  // called when entering full screen
  BigScreen.onenter = function() {
    //app.map.updateSize();
    //app.map.render('map');
    //close page guide, hide legend, hide layers
    if ( $.pageguide('isOpen') ) {
        app.fullscreen.pageguide = true;
        //closing the guide here makes it difficult to return to the correct guide...
        //things might be working fine without closing the guide...
        //$.pageguide('close');
    }
    if ( app.viewModel.showLegend() ) {
        app.fullscreen.showLegend = true;
        app.viewModel.showLegend(false);
    }
    if ( app.viewModel.showLayers() ) {
        app.fullscreen.showLayers = true;
        app.viewModel.showLayers(false);
    }
    app.viewModel.isFullScreen(true);
    // make map fullscreen
    setTimeout( app.onResize(0.99), 500);
  };

  BigScreen.onexit = function() {
    // called when exiting full screen
    app.viewModel.isFullScreen(false);
    // return to normal size
    // Not exactly comfortable with the following 2 calls to resize,
    // but ff kept having problems when other strategies were tried...
    //for firefox
    setTimeout( app.onResize(), 300);
    //app.onResize();
    //app.onResize();
    //if applicable, open page guide, show legend, show layers
    if ( app.fullscreen.showLayers ) {
        app.viewModel.showLayers(true);
        app.fullscreen.showLayers = false;
    }
    if ( app.fullscreen.showLegend ) {
        app.viewModel.showLegend(true);
        app.fullscreen.showLegend = false;
    }
    if ( app.fullscreen.pageguide ) {
        app.viewModel.showLayers(true);
        setTimeout( function() {
            $.pageguide('open');
            if ($.pageguide().guide().id === 'default-guide') {
                setTimeout( function() {
                    $.pageguide('showStep', $.pageguide().guide().steps.length-1);
                }, 300 );
            }
        }, 500 );
        app.fullscreen.pageguide = false;
    }
    //for chrome
    setTimeout( app.onResize, 300);
  };

  // Basemaps button and drop-down behavior
  //hide basemaps drop-down on mouseout
  $('#basemaps').mouseleave( function(e) {
    if ( $(e.toElement).hasClass('basey') ) { //handler for chrome and ie
        $('#basemaps').addClass('open');
    } else if ( $(e.relatedTarget).hasClass('basey') ) { //handler for ff
        $('#basemaps').addClass('open');
    } else {
        $('.SimpleLayerSwitcher').hide();
    }
  });

  //hide icon butons on mouseleave
  $('.SimpleLayerSwitcher').mouseleave( function() {
    $('.SimpleLayerSwitcher').hide();
    if (!app.pageguide.preventBasemapsClose) {
        $('#basemaps').removeClass('open');
    }
  });

  //hide basemap list and icon buttons on click/select (and hopefully touchend)
  $('.SimpleLayerSwitcher').on( "touchend mouseup", function() {
    $('.SimpleLayerSwitcher').hide();
    if (!app.pageguide.preventBasemapsClose) {
        $('#basemaps').removeClass('open');
    }
  });

  //hide icon buttons on mousedown
  $('.SimpleLayerSwitcher').mousedown( function() {
      if (!app.pageguide.preventBasemapsClose) {
          $('#basemaps').removeClass('open');
      }
  });

  //show icon buttons on mouseenter
  $('.SimpleLayerSwitcher').mouseenter( function() {
    $('#basemaps').addClass('open');
  });

  $('#overview-overlay-dropdown').mouseleave( function() {
    $('#overview-overlay-dropdown').closest('.btn-group').removeClass('open');
  });

  $('#opacity-popover').mouseleave( function() {
    app.viewModel.hideOpacity();
  });

  $('#registration-modal').on('show', function() {
    $('.empty-input').val("");
  });

  $('#sign-in-modal').on('show', function() {
    $('.empty-input').val("");
  });

  $('#reset-password-modal').on('show', function() {
    $('.empty-input').val("");
  });

  $(document).on('click', 'a[name="start-default-tour"]', function() {
    app.viewModel.startDefaultTour();
  });

  $(document).on('click', '#continue-basic-tour', function() {
    app.viewModel.stepTwoOfBasicTour();
  });

  $(document).on('click', '#start-data-tour', function() {
    app.viewModel.startDataTour();
  });

  $(document).on('click', '#start-active-tour', function() {
    app.viewModel.startActiveTour();
  });

  $(document).on('click', '#share-option', function() {
    app.viewModel.scenarios.initSharingModal();
  });

  $(document).on('click', '#close-report-video-tutorial-button', function() {
    if ($("#video-tutorial-wrapper iframe").length > 0) {
      youtubeSrc = $("#video-tutorial-wrapper iframe").attr('src');
      $("#video-tutorial-wrapper iframe").attr('src', youtubeSrc);
    }
  })

  // hiding feature attributes on new click events (but ignoring map pan events)
  app.map.events.register('move', app.map, function() {
    app.map.mousedrag = true;
  });
  $('#map').mouseup( function() {
    if ( !app.map.mousedrag ) {
      if (!app.viewModel.featureClick()) {
        app.map.clickOutput.attributes = {};
        app.viewModel.closeAttribution();
        app.viewModel.closeDescription();
      }
    }
    app.map.mousedrag = false;
  });

  $('a[data-toggle="tab"]').on('shown', function (e) {
    app.updateUrl();
  });

  $('#legendTab a').click(function (e) {
    e.preventDefault();
    var legendBottom = $('#legend-bottom');
    var chevronIcon = $('#legendTab i');
    if (chevronIcon.attr('class') == "icon-chevron-up") {
      legendBottom.slideDown(400, function() {
        chevronIcon.attr('class', 'icon-chevron-down');
      });
    } else {
      legendBottom.slideUp(400, function() {
        chevronIcon.attr('class', 'icon-chevron-up');
      });
    }
  });

});

$('#bookmark-form').on('submit', function(event) {
  var inputs = {},
    $form = $(this);
  event.preventDefault();
  $(this).find('input, textarea').each(function(i, input) {
    var $input = $(input);
    inputs[$input.attr('name')] = $input.val();
  });
  $.post('/feedback/bookmark', inputs, function() {
    $form.closest('.modal').modal('hide');
  });
});

$('#feedback-form').on('submit', function (event) {
   var feedback = {}, $form = $(this);
   event.preventDefault();
   $(this).find('input, textarea').each(function (i, input) {
      var $input = $(input);
      feedback[$input.attr('name')] = $input.val();
   });
   feedback.url = window.location.href;
   $.post('/feedback/send', feedback, function () {
      $form.find('textarea').val('');
      $form.closest('.modal').modal('hide');
      //$('#thankyou-modal').modal('show');
   });
   $form.closest('.modal').modal('hide');
});

$(document).mousedown(function(e) {
  //removing bookmark popover from view
  if ($(e.target).closest('a').length && $(e.target).closest('a')[0].id === "bookmarks-button") {
    //do nothing as show/hide behavior is handled in viewModel
  } else if (!$(e.target).closest("#bookmark-popover").length) {
    $('#bookmark-popover').hide();
  }

  //ensure layer switcher is removed
  $('.SimpleLayerSwitcher').hide();

  //removing layer tooltip popover from view
  var layer_pvr_event = $(e.target).closest(".layer-popover").length;
  if (!layer_pvr_event) {
    $("#layer-popover").hide();
  }

  //removing opacity popover from view
  var op_pvr_event = $(e.target).closest("#opacity-popover").length;
  var op_btn_event = $(e.target).closest(".opacity-button").length;
  if (!op_pvr_event && !op_btn_event) {
    //$('#opacity-popover').hide();
    app.viewModel.hideOpacity();
  }
});
