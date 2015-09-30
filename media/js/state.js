// represents whether or not restoreState is currently being updated
// example use:  saveStateMode will be false when a user is viewing a bookmark
app.saveStateMode = true;

// save the state of app
app.getState = function () {
    if (app.map.getCenter()) {

        var center = app.map.getCenter().transform(
                new OpenLayers.Projection("EPSG:900913"), new OpenLayers.Projection("EPSG:4326")),
                    layers = $.map(app.viewModel.activeLayers(), function(layer) {
                        //return {id: layer.id, opacity: layer.opacity(), isVisible: layer.visible()};
                        return [ layer.id, layer.opacity(), layer.visible() ];
                    });
        return {
            x: center.lon.toFixed(2),
            y: center.lat.toFixed(2),
            z: app.map.getZoom(),
            logo: app.viewModel.showLogo(),
            dls: layers.reverse(),
            basemap: app.map.baseLayer.name,
            themes: {ids: app.viewModel.getOpenThemeIDs()},
            tab: $('#myTab').find('li.active').data('tab'),
            print: app.viewModel.printMode()
            // legends: app.viewModel.showLegend() ? 'true': 'false',
            // layers: app.viewModel.showLayers() ? 'true': 'false'
            //and active tab
        };
    } else {
      var ret = setTimeout(function() { return app.getState();}, 50);
      return ret;
    }

};

$(document).on('map-ready', function () {
    app.state = app.getState();
});

app.layersAreLoaded = false;
app.establishLayerLoadState = function () {
    var loadTimer, status;
    if (app.map.layers.length === 0) {
        app.layersAreLoaded = true;
    } else {
        loadTimer = setInterval(function () {
            status = true;
            $.each(app.map.layers, function (i, layer) {
                if (layer.loading === true) {
                    status = false;
                }
            });
            if (status === true) {
                app.layersAreLoaded = true;
                clearInterval(loadTimer);
            }
        }, 100);
    }

};

app.displayActiveTab = function (state) {
  // active tab -- the following prevents theme and data layers from loading in either tab (not sure why...disbling for now)
  // it appears the dataTab show in state.themes above was causing the problem...?
  // timeout worked, but then realized that removing datatab show from above worked as well...
  // Reinstating the timeout which seems to fix the toggling between tours issue (toggling to ActiveTour while already in ActiveTab)
  if (state.tab && state.tab === "active") {
        $('#activeTab').tab('show');
  } else if (state.tab && state.tab === "legend") {
        $('#legendTab').tab('show');
  } else {
        $('#dataTab').tab('show');
  }
}

app.getScopeBounds = function(scope) {
  //list of known scopes
    //represented as [left, bottom, right, top]
  var scopes = {
    'OR': [-124.7,41.8,-116.3,46.3], //Oregon State
    'CP': [-121.5,44.7,-118.0,46] //Columbia Plateau
  }

  var bounds_array = [];
  if (scopes.hasOwnProperty(scope.toUpperCase())) {
    bounds_array = scopes[scope.toUpperCase()];
  } else {
    bounds_array = scopes['OR'];
  }

  var bounds = new OpenLayers.Bounds(bounds_array);
  return bounds;
}

// load compressed state (the url was getting too long so we're compressing it
app.loadCompressedState = function(state) {
    // turn off active laters
    // create a copy of the activeLayers list and use that copy to iteratively deactivate
    var activeLayers = $.map(app.viewModel.activeLayers(), function(layer) {
        return layer;
    });
    $.each(activeLayers, function (index, layer) {
        layer.deactivateLayer();
    });
    // turn on the layers that should be active
    if (state.dls) {
        var unloadedDesigns = [];
        for (x=0; x < state.dls.length; x=x+3) {
            var id = state.dls[x+2],
                opacity = state.dls[x+1],
                isVisible = state.dls[x];

            if (app.viewModel.layerIndex[id]) {
                app.viewModel.layerIndex[id].activateLayer();   //IMPORTANT!
                app.viewModel.layerIndex[id].opacity(parseFloat(opacity));
                //must not be understanding something about js, but at the least the following seems to work now...
                if (isVisible || !isVisible) {
                    if (isVisible !== 'true' && isVisible !== true) {
                        app.viewModel.layerIndex[id].toggleVisible();
                    }
                }
            } else {
                unloadedDesigns.push({id: id, opacity: opacity, isVisible: isVisible});
            }
       }
       if ( unloadedDesigns.length ) {
            app.viewModel.unloadedDesigns = unloadedDesigns;
            // $('#designsTab').tab('show'); //to activate the loading of designs
            // better yet...
            if (app.viewModel.hasOwnProperty('scenarios')) {
              app.viewModel.scenarios.loadDesigns();
            }
       }
    }

    if ( !state.logo || state.logo === 'false') {
        app.viewModel.hideLogo();
    }

    if (state.print === 'true') {
        app.setPrintMode();
    }
    if (state.borderless === 'true') {
        app.borderLess();
    }

    if (state.basemap) {
        app.map.setBaseLayer(app.map.getLayersByName(state.basemap)[0]);
    }

    app.establishLayerLoadState();
    // data tab and open themes
    if (state.themes) {
        //$('#dataTab').tab('show');
        $.each(app.viewModel.themes(), function (i, theme) {
            if ( $.inArray(theme.id, state.themes.ids) !== -1 || $.inArray(theme.id.toString(), state.themes.ids) !== -1 ) {
                if ( app.viewModel.openThemes.indexOf(theme) === -1 ) {
                    //app.viewModel.openThemes.push(theme);
                    theme.setOpenTheme();
                }
            } else {
                if ( app.viewModel.openThemes.indexOf(theme) !== -1 ) {
                    app.viewModel.openThemes.remove(theme);
                }
            }
        });
    }

    //if (app.embeddedMap) {
    if ( $(window).width() < 768 || app.embeddedMap ) {
        state.tab = "data";
    }

    if (state.tab && app.getState().tab) {
        app.displayActiveTab(state);
    }

    if ( state.legends && state.legends === 'true' ) {
        app.viewModel.showLegend(true);
    } else {
        app.viewModel.showLegend(false);
    }

    if (state.layers && state.layers === 'false') {
        app.viewModel.showLayers(true);
        //app.viewModel.showLayers(false);
        //app.map.render('map');
    } else {
        app.viewModel.showLayers(true);
    }

    // map title for print view
    if (state.title) {
        app.viewModel.mapTitle(state.title);
    }

    // Google.v3 uses EPSG:900913 as projection, so we have to
    // transform our coordinates
    if (state.hasOwnProperty('scope')) {
      var bounds = app.getScopeBounds(state.scope);
      //Bounds should come in as EPSG:4326, let's convert to 900913
      bounds.transform(new OpenLayers.Projection('EPSG:4326'),new OpenLayers.Projection('EPSG:900913'));
      app.map.zoomToExtent(bounds);
    } else {
      app.setMapPosition(state.x, state.y, state.z);
    }
    //app.map.setCenter(
    //    new OpenLayers.LonLat(state.x, state.y).transform(
    //        new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913") ), state.z);

    // is url is indicating a login request then show the login modal
    // /visualize/#login=true
    if (!app.is_authenticated && state.login) { // not sure
        $('#sign-in-modal').modal('show');
    }

};

app.setMapPosition = function(x, y, z) {
    app.map.setCenter(
        new OpenLayers.LonLat(x, y).transform(
            new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913") ), z);
};

// hide buttons and other features for printing
app.setPrintMode = function () {
    $('body').addClass('print');
    app.viewModel.printMode(true);
    // TODO: I don't know why this works.
    // var iframeLegend = $('#legend-content').clone();
    // iframeLegend.appendTo('#map-wrapper');
};

// also hide logo and rules
app.borderLess = function () {
    $('body').addClass('borderless');
};

// load state from fixture or server

app.loadState = function(state) {
    var loadTimer;
    if (state.z || state.login || state.scope) {
        return app.loadCompressedState(state);
    } else {
        var slug = Object.keys(state)[0],
            layer = app.viewModel.getLayerBySlug(slug);
        app.loadCompressedState(state);
        if (layer) {
            //activate layer (/planner/#<layer-name>)
            app.viewModel.layerIndex[layer.id].activateLayer();
            //set open theme
            layer.themes()[0].setOpenTheme();
        }
        return;
    }


};

// load the state from the url hash

app.loadStateFromHash = function (hash) {
    app.loadState($.deparam(hash.slice(1)));
};

app.loadStateFromDefaultHash = function (default_hash) {
    var hash = default_hash.replace(/&amp;/g, '&');
    app.loadState($.deparam(hash.slice(1)));
};

// update the hash
app.updateUrl = function () {
  setTimeout(function(){
    var state = app.getState();

    // save the restore state
    if (app.saveStateMode) {
        app.restoreState = state;
    }
    window.location.hash = $.param(state);
    app.viewModel.currentURL(window.location.pathname + window.location.hash);
    app.state = state;
  }, 10);
};
