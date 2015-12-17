
app.pageguide = {};

/* THE DEFAULT PAGE GUIDE */

var setGuideIds = function(theme_index, subtheme_index) {
  st1_target = $('.accordion-heading').not('.subcategory-heading').eq(theme_index);
  st1_target.attr('id','dataguide-st1-target');
  if (subtheme_index >= 0 && $('#dataguide-st2-target').length == 0) {
    st2_target_index = subtheme_index;
  } else {
    st2_target_index = 0;
  }
  st2_target = st1_target.closest('.accordion-group').find('.btn-group-layer').eq(st2_target_index);
  st2_target.children('.btn-layer').attr('id','dataguide-st2-target');
  st3_target = st2_target.children('.btn-info-sign').eq(0);
  st3_target.attr('id','dataguide-st3-target');
}

var findValidLayer = function() {
  var ret_layer = null;
  for (var theme_index = 0; theme_index < app.viewModel.themes().length; theme_index++) {
    if (app.viewModel.themes()[theme_index].layers().length > 0) {
      return {
        'theme': app.viewModel.themes()[theme_index],
        'theme_index': theme_index,
        'subtheme': false,
        'subtheme_index': false,
        'layer': app.viewModel.themes()[theme_index].layers()[0]
      };
    }
    for (var subtheme_index = 0; subtheme_index < app.viewModel.themes()[theme_index].subthemes().length; subtheme_index++) {
      if (app.viewModel.themes()[theme_index].subthemes()[subtheme_index].layers().length > 0) {
        return {
          'theme': app.viewModel.themes()[theme_index],
          'theme_index': theme_index,
          'subtheme': app.viewModel.themes()[theme_index].subthemes()[subtheme_index],
          'subtheme_index': subtheme_index,
          'layer': app.viewModel.themes()[theme_index].subthemes()[subtheme_index].layers()[0]
        };
      }
    }
  }
};

// valid_layer_obj = findValidLayer();

var defaultGuide = {
  id: 'default-guide',
  title: 'Default Guide',
  steps: [
    // {
    //   target: '#help-button',
    //   content: $('#help-text-help-button').html(),
    //   direction: 'top',
    //   arrow: {offsetX: 10, offsetY: -10}
    // },
    {
      target: '#dataTab',
      content: $('#help-text-dataTab').html(),
      direction: 'bottom',
      arrow: {offsetX: 25, offsetY: -15}
    },
    {
      target: '#activeTab',
      content: $('#help-text-activeTab').html(),
      direction: 'bottom',
      arrow: {offsetX: 25, offsetY: -15}
    },
    {
      target: '#legendTab',
      content: $('#help-text-legendTab').html(),
      direction: 'bottom',
      arrow: {offsetX: 25, offsetY: -15}
    },
    {
      target: '.olControlZoom',
      content: $('#help-text-olControlZoom').html(),
      direction: 'top',
      arrow: {offsetX: -10, offsetY: -10}
    },
    {
      target: '#basemaps',
      content: $('#help-text-basemaps').html(),
      direction: 'left',
      arrow: {offsetX: -100, offsetY: 10}
    },
    {
      target: '#minimize-icon',
      content: $('#help-text-minimize-icon').html(),
      direction: 'right',
      arrow: {offsetX: 0, offsetY: 0}
    },
    {
      target: '#project-logo',
      content: $('#help-text-project-logo').html(),
      direction: 'right',
      arrow: {offsetX: 0, offsetY: 55}
    },
    {
      target: '#geosearch-field',
      content: $('#help-text-search-map').html(),
      direction: 'bottom',
      arrow: {offsetX: 0, OffsetY: 0}
    }
  ]
};

var defaultGuideOverrides = {
  events: {
    open: function () {
      app.pageguide.defaultOpenStuff();

      //open the basemaps buttons and keep them open
      $('#basemaps').addClass('open');
      app.pageguide.preventBasemapsClose = true;

      //adjust the pageguide icon so it is left of the open basemaps buttons
      for (var i=0; i < defaultGuide.steps.length; i++) {
        if ( defaultGuide.steps[i].target === '#basemaps' ) {
            defaultGuide.steps[i].arrow.offsetX = 0;
        }
      }
      $('#dataTab').tab('show');
    },
    close: function () {
      app.pageguide.defaultCloseStuff();

      //deactivate the prevention of the basemaps buttons closing
      app.pageguide.preventBasemapsClose = true;
      //close the basemaps buttons
      $('#basemaps').removeClass('open');

      //return the offset of the pageguide icon so it doesn't move out of place as the guide closes
      for (var i=0; i < defaultGuide.steps.length; i++) {
        if ( defaultGuide.steps[i].target === '#basemaps' ) {
            defaultGuide.steps[i].arrow.offsetX = -95;
        }
      }
    }
  },
  step: {
    events: {
      select: function() {
        if (defaultGuide.steps[$(this).data('idx')].target == '#dataTab') {
          $('#dataTab').tab('show');
        }
        if (defaultGuide.steps[$(this).data('idx')].target == '#activeTab') {
            $('#activeTab').tab('show');
        }
        if (defaultGuide.steps[$(this).data('idx')].target == '#legendTab') {
            $('#legendTab').tab('show');
        }
      }
    }
  }
};

/* THE DATA PANEL PAGE GUIDE */
var dataGuide = {
  id: 'data-guide',
  title: 'Data Guide',
  steps: [
    {
      target: '#dataTab',
      content: $('#help-text-data-tour-dataTab').html(),
      direction: 'right',
      arrow: {offsetX: 0, offsetY: 0}
    },
    {
      target: '.search-form',
      content: $('#help-text-data-tour-form-search').html(),
      direction: 'right',
      arrow: {offsetX: -65, offsetY: 15}
    },
    {
      target: '#dataguide-st1-target',
      content: $('#help-text-data-tour-theme').html(),
      direction: 'right',
      arrow: {offsetX: -10, offsetY: 10}
    },
    {
      target: '#dataguide-st2-target',
      content: $('#help-text-data-tour-layer').html(),
      direction: 'right',
      arrow: {offsetX: -10, offsetY: 10}
    },
    {
      target: '#dataguide-st3-target',
      content: $('#help-text-data-tour-info-sign').html(),
      direction: 'right',
      arrow: {offsetX: 0, offsetY: 0}
    }
  ]
};

var dataGuideOverrides = {
  events: {
    open: function () {
      app.pageguide.defaultOpenStuff();
    },
    close: function () { // activated regardless of whether the 'tour' was clicked  or the 'close' was clicked?
      app.pageguide.defaultCloseStuff();
    }
  },
  step: {
    events: {
      select: function() {
        /// ALL
        var step = $(this).data('idx');
        var valid_layer_obj = findValidLayer();
        app.viewModel.closeAllThemes();
        /// Steps 1-4
        if (step < 4) {
          app.viewModel.closeDescription();
          if ($('#' + valid_layer_obj.layer.id + '_overview').hasClass('in')) {
            valid_layer_obj.layer.toggleDescription(valid_layer_obj.layer);
          }
          app.viewModel.closeAllSubThemes();
        }
        /// Steps 1-3
        if (step < 3) {
          app.viewModel.deactivateAllLayers();
        }
        /// ALL
        if (valid_layer_obj.theme && !(valid_layer_obj.theme.isOpenTheme())) {
          valid_layer_obj.theme.setOpenTheme();
          if (valid_layer_obj.subtheme && !(valid_layer_obj.subtheme.isOpenSubTheme())) {
            valid_layer_obj.subtheme.setOpenSubTheme();
          }
        }
        /// Steps 4-5
        if (step > 2) {
            valid_layer_obj.layer.activateLayer();
        }
        /// Step 5
        if (step > 3) {
            if (! $('#' + valid_layer_obj.layer.id + '_overview').hasClass('in')) {
              valid_layer_obj.layer.toggleDescription(valid_layer_obj.layer);
            }
        }
      }
    }
  }
};

/* THE ACTIVE PANEL PAGE GUIDE */

var activeGuide = {
  id: 'active-guide',
  title: 'Active Guide',
  steps: [
    {
      target: '#activeTab',
      content: $('#help-text-active-tour-activeTab').html(),
      direction: 'top',
      arrow: {offsetX: 50, offsetY: 0}
    },
    {
      target: '#active .btn-layer',
      content: $('#help-text-active-tour-layer-button').html(),
      direction: 'top',
      arrow: {offsetX: 155, offsetY: 0}
    },
    {
      target: '#active .opacity-button',
      content: $('#help-text-active-tour-opacity-button').html(),
      direction: 'top',
      arrow: {offsetX: 15, offsetY: 0}
    },
    {
      target: '#active .deactivate-button',
      content: $('#help-text-active-tour-deactivate-button').html(),
      direction: 'right',
      arrow: {offsetX: 0, offsetY: 10}
    },
    {
      target: '#active .ui-sortable',
      content: $('#help-text-active-tour-ui-sortable').html(),
      direction: 'bottom',
      arrow: {offsetX: 120, offsetY: 0}
    }
  ]
};

var activeGuideOverrides = {
  events: {
    open: function () {
        app.pageguide.defaultOpenStuff();
    },
    close: function () { // activated regardless of whether the 'tour' was clicked  or the 'close' was clicked?
      app.pageguide.defaultCloseStuff();
    }
  },
  step: {
    events: {
      select: function() {
        if ($(this).data('idx') === 0) {
            $('#activeTab').tab('show');
        } else if ($(this).data('idx') === 2) {
            $('#activeTab').tab('show');
            $('.opacity-button:first').click();
        } else if ($(this).data('idx') === 3) {
            $('#activeTab').tab('show');
        }
      }
    }
  }
};

app.pageguide.defaultOpenStuff = function() {
    app.pageguide.tourIsActive = true;
    app.viewModel.hideMapAttribution();

    //increase the z-value of SimpleLayerSwitcher so it falls on top of the pageguide icon
    $('.SimpleLayerSwitcher').css('z-index', 1100);
};
app.pageguide.defaultCloseStuff = function() {
    app.viewModel.closeDescription();
    //if ( ! app.viewModel.showOverview() ) {
    app.viewModel.showMapAttribution();
    //}

    //for some reason it seems that the following 4 lines are needed both here and in the 'tour' click event handler
    app.viewModel.deactivateAllLayers();
    app.viewModel.closeAllThemes();

    //return the zindex of the SimpleLayerSwitcher to its original value
    $('.SimpleLayerSwitcher').css('z-index', 1005);

    //only save state if tour is activated from a normal (non-tour) state)
    //if tour is closing to start another tour, then don't resave/reload original state (wait till tours are closing rather than toggling)
    if ( ! app.pageguide.togglingTours ) {
      app.loadState(app.pageguide.state);
      app.saveStateMode = true;
    }

    $('#overview-overlay').height(186);

    app.pageguide.tourIsActive = false;

    $.pageguide(defaultGuide, defaultGuideOverrides);
};

$(function() {
  // Load the default guide!
  $.pageguide(defaultGuide, defaultGuideOverrides);

  $('#help-tab').on('click', function() {
    if ( $.pageguide('isOpen') ) { // activated when 'tour' is clicked
        // close the pageguide
        $.pageguide('close');

        //restore the state to what it was before the tour
        app.loadState(app.pageguide.state);
        app.saveStateMode = true;
    } else {
        // start the pageguide

        //show the data layers panel
        app.viewModel.showLayers(true);

        //save state
        app.pageguide.state = app.getState();
        app.saveStateMode = false;

        //start the tour
        setTimeout( function() { $.pageguide('open'); }, 200 );

    }
  });


});
