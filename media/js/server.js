// load layers from fixture or the server
app.viewModel.loadLayers = function(data) {
	var self = app.viewModel;
	// load layers
	$.each(data.layers, function(i, layer) {
		var layerViewModel = new layerModel(layer);

		self.layerIndex[layer.id] = layerViewModel;
		// add sublayers if they exist
		if (layer.subLayers && layer.subLayers.length) {
			$.each(layer.subLayers, function(i, layer_options) {
				if (layer_options.type !== 'placeholder') {
					var subLayer = new layerModel(layer_options, layerViewModel);
					app.viewModel.layerIndex[subLayer.id] = subLayer;
					layerViewModel.subLayers.push(subLayer);
				}
			});
		}
	});

	// load themes
	$.each(data.themes, function(i, themeFixture) {
		var theme = new themeModel(themeFixture);
		var updateLayerSearchIndexWithThemeLayers = function(j, layer_id) {
			updateLayerSearchIndex(j, layer_id, null);
		};

		var updateLayerSearchIndex = function(j, layer_id, subtheme) {
			// create a layerModel and add it to the list of layers
			var layer = self.layerIndex[layer_id];
			var searchTerm = layer.name + ' (' + themeFixture.display_name + ')';
			layer.themes.push(theme);
			if (subtheme) {
				subtheme.layers.push(layer);
			} else {
				theme.layers.push(layer);
			}

			if (!layer.subLayers.length) { //if the layer does not have sublayers
                self.layerSearchIndex[searchTerm] = {
                    layer: layer,
                    theme: theme,
                    subtheme: subtheme
                };
        } else { //if the layer has sublayers
						$.each(layer.subLayers, function(i, subLayer) {
                var searchTerm = subLayer.name + ' (' + themeFixture.display_name + ' / ' + subLayer.parent.name + ')';
								if (subLayer.name !== 'Data Under Development') {
                		self.layerSearchIndex[searchTerm] = {
                    		layer: subLayer,
                        theme: theme,
                        subtheme: subtheme
                    };
                }
						});
				}
		}

		$.each(themeFixture.layers, updateLayerSearchIndexWithThemeLayers );
		$.each(themeFixture.subthemes, function (j, subtheme) {
				var subthemeMod = new subthemeModel(subtheme);
				theme.subthemes.push(subthemeMod);
				for (var layer_idx = 0; layer_idx < subtheme.layers.length; layer_idx++) {
					updateLayerSearchIndex(layer_idx, subtheme.layers[layer_idx], subthemeMod);
				}
		});

		self.themes.push(theme);
	});

	app.typeAheadSource = (function () {
            var keys = [];
            for (var searchTerm in app.viewModel.layerSearchIndex) {
                if (app.viewModel.layerSearchIndex.hasOwnProperty(searchTerm)) {
                    keys.push(searchTerm);
                }
            }
            return keys;
    })();

    //re-initialise the legend scrollbar
    //if ( ! app.embeddedMap ) {
    if ( $(window).width() > 767 && !app.embeddedMap ) {
        $('#legend-content').jScrollPane();
    }

};
app.viewModel.loadLayersFromFixture = function() {
	app.viewModel.loadLayers(app.fixture);
};


app.viewModel.loadLayersFromServer = function() {
		app.viewModel.spinnerList.push('loadLayersFromServer');
    var pathname = window.location.pathname,
        slug_name = pathname.substring(1, pathname.indexOf('/planner'));
    if (slug_name === '/') {
        slug_name = pathname.substring(1, pathname.indexOf('/visualize'));
    }
	return $.getJSON('/data_manager/get_json/'+slug_name, function(data) {
		app.viewModel.loadLayers(data);
	});
};
//test comment
