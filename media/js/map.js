app.init = function() {
    // proj4.defs("EPSG:3643", "+proj=lcc +lat_1=43 +lat_2=45.5 +lat_0=41.75 +lon_0=-120.5 +x_0=400000 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs");
    Proj4js.defs["EPSG:3643"] = "+proj=lcc +lat_1=43 +lat_2=45.5 +lat_0=41.75 +lon_0=-120.5 +x_0=400000 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs";
    Proj4js.defs["EPSG:2992"] = "+proj=lcc +lat_1=43 +lat_2=45.5 +lat_0=41.75 +lon_0=-120.5 +x_0=399999.9999984 +y_0=0 +ellps=GRS80 +datum=NAD83 +to_meter=0.3048 +no_defs";
    Proj4js.defs["ESRI:102100"] = "+proj=merc +lon_0=0 +x_0=0 +y_0=0 +a=6378137 +b=6378137  +units=m +nadgrids=@null";
    Proj4js.defs["SR-ORG:6928"] = "";
    //OR LAMBERT CONFORMAL CONIC NAD83
    Proj4js.defs["ORNAD83M"] = "+proj=lcc +lat_1=43 +lat_2=45.5 +lat_0=41.75 +lon_0=-120.5 +x_0=1312336.0 +y_0=0 +ellps=GRS80 +datum=NAD83 +to_meter=1 +no_defs";
    // Proj4js.defs["SR-ORG:8252"] = "+proj=lcc +lat_1=43 +lat_2=45.5 +lat_0=41.75 +lon_0=-120.5 +x_0=1312336.0 +y_0=0 +ellps=GRS80 +datum=NAD83 +to_meter=1 +no_defs";
    Proj4js.defs["SR-ORG:45"] = "+proj=merc +lon_0=0 +k=1 +x_0=0 +y_0=0 +a=6378137 +b=6378137 +units=m +no_defs";
    Proj4js.defs["EPSG:3857"] = "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs";

    var max_zoom,
        min_zoom;
    //to turn basemap indicator off (hide the plus sign)
    //see email from Matt on 7/26 2:24pm with list of controls
    var map = new OpenLayers.Map(null, {
        //allOverlays: true,
        displayProjection: new OpenLayers.Projection("EPSG:4326"),
        projection: "EPSG:3857"
    });


    if (app.MPSettings && app.MPSettings.max_zoom) {
        max_zoom = app.MPSettings.max_zoom + 1;
    } else {
        max_zoom = 15;
    }

    esriOcean = new OpenLayers.Layer.XYZ("ESRI Ocean","http://services.arcgisonline.com/ArcGIS/rest/services/Ocean_Basemap/MapServer/tile/${z}/${y}/${x}", {
        sphericalMercator: true,
        isBaseLayer: true,
        numZoomLevels: max_zoom,
        attribution: "Sources: Esri, GEBCO, NOAA, National Geographic, DeLorme, NAVTEQ, Geonames.org, and others",
        buffer: 3
    });
    // esriOcean = new OpenLayers.Layer.WMTS({
    //     name: "ESRI Ocean",
    //     url: "http://services.arcgisonline.com/arcgis/rest/services/Ocean_Basemap/MapServer/0",
    //     layer: 0
    // });

    openStreetMap = new OpenLayers.Layer.OSM("OpenStreetMap", "http://a.tile.openstreetmap.org/${z}/${x}/${y}.png", {
        sphericalMercator: true,
        isBaseLayer: true,
        numZoomLevels: max_zoom,
        buffer: 3
    });
    // openStreetMap = new OpenLayers.Layer.OSM();

    // googleStreet = new OpenLayers.Layer.Google("Google Streets", {
    //     sphericalMercator: true,
    //     isBaseLayer: true,
    //     numZoomLevels: max_zoom,
    //     buffer: 3
    // });
    // googleTerrain = new OpenLayers.Layer.Google("Google Physical", {
    //     type: google.maps.MapTypeId.TERRAIN,
    //     sphericalMercator: true,
    //     isBaseLayer: true,
    //     numZoomLevels: max_zoom,
    //     buffer: 3
    // });
    // googleSatellite = new OpenLayers.Layer.Google("Google Satellite", {
    //     type: google.maps.MapTypeId.SATELLITE,
    //     sphericalMercator: true,
    //     isBaseLayer: true,
    //     numZoomLevels: max_zoom,
    //     buffer: 3
    // });

    esriStreets = new OpenLayers.Layer.XYZ("ESRI Streets", "http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/${z}/${y}/${x}", {
        sphericalMercator: true,
        isBaseLayer: true,
        numZoomLevels: max_zoom,
        attribution: "Sources: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, METI, TomTom, and others",
        buffer: 3
    });
    esriTopo = new OpenLayers.Layer.XYZ("ESRI Physical", "http://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/${z}/${y}/${x}", {
        sphericalMercator: true,
        isBaseLayer: true,
        numZoomLevels: max_zoom,
        attribution: "Sources: Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, and others",
        buffer: 3
    });
    esriImagery = new OpenLayers.Layer.XYZ("ESRI Satellite", "http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/${z}/${y}/${x}", {
        sphericalMercator: true,
        isBaseLayer: true,
        numZoomLevels: max_zoom,
        attribution: "Sources: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and others",
        buffer: 3
    });

    /*var bingHybrid = new OpenLayers.Layer.Bing( {
        name: "Bing Hybrid",
        key: "AvD-cuulbvBqwFDQGNB1gCXDEH4S6sEkS7Yw9r79gOyCvd2hBvQYPaRBem8cpkjv",
        type: "AerialWithLabels",
        sphericalMercator: true,
        isBaseLayer: true,
        numZoomLevels: 13
    });*/

    // need api key from http://bingmapsportal.com/
    /*var bingHybrid = new OpenLayers.Layer.Bing({
        name: "Bing Hybrid",
        key: "AvD-cuulbvBqwFDQGNB1gCXDEH4S6sEkS7Yw9r79gOyCvd2hBvQYPaRBem8cpkjv",
        type: "AerialWithLabels"
    });*/
    nauticalCharts = new OpenLayers.Layer.ArcGIS93Rest("Nautical Charts", "http://seamlessrnc.nauticalcharts.noaa.gov/arcgis/rest/services/RNC/NOAA_RNC/ImageServer/exportImage", {
        layers: 'null'
    }, {
        isBaseLayer: true,
        numZoomLevels: max_zoom,
        projection: "EPSG:3857",
        buffer: 3
    });

    map.addLayers([esriImagery, esriOcean, esriTopo, esriStreets, openStreetMap, nauticalCharts]);

    // map.addLayers([esriOcean]);
    // esriOcean.setZIndex(100);

    map.addControl(new SimpleLayerSwitcher());
    // map.addControl(new OpenLayers.Control.TouchNavigation());
    // map.addControl(new OpenLayers.Control.PinchZoom());

    // adding the following for IE10 touch events
    // obtained from the following blog post
    // http://dotnetbyexample.blogspot.com/2013/03/enabling-basic-openlayers-pinch-zooming.html
    // map.addControl(new OpenLayersWindowsPinchZoom());

    //Scale Bar
    var scalebar = new OpenLayers.Control.ScaleBar({
        displaySystem: "english",
        minWidth: 200, //default
        maxWidth: 250, //default
        divisions: 2, //default
        subdivisions: 2, //default
        showMinorMeasures: false //default
    });
    map.addControl(scalebar);

    map.zoomBox = new OpenLayers.Control.ZoomBox({
        //enables zooming to a given extent on the map by holding down shift key while dragging the mouse
    });
    map.addControl(map.zoomBox);

    // only allow onetime zooming with box
    map.events.register("zoomend", null, function() {
        if (app.MPSettings && app.MPSettings.min_zoom) {
            min_zoom = app.MPSettings.min_zoom;
        } else {
            min_zoom = 3;
        }
        if (map.zoomBox.active) {
            app.viewModel.deactivateZoomBox();
        }
        if (map.getZoom() < min_zoom) {
            map.zoomTo(min_zoom);
        }
    });

    map.events.register("moveend", null, function() {
        // update the url when we move
        app.updateUrl();
    });

    app.map = map;

    app.map.attributes = [];
    //app.map.clickOutput = { time: 0, attributes: [] };
    app.map.clickOutput = {
        time: 0,
        attributes: {}
    };

    map.coordsControl = new OpenLayers.Control.MousePosition({
        prefix: 'Mouse Coordinates: ',
        // separator: ', ',
        // numDigits: 2,
        emptyString: '',
        formatOutput: function( lonLat ) {
            // return 'Lat/Lng: (' + lonLat.lat.toFixed(3) + ', ' + lonLat.lon.toFixed(3) + ')';
            if (lonLat.lat > 0) {
                var degreesLat = Math.floor(lonLat.lat);
            } else {
                var degreesLat = Math.ceil(lonLat.lat);
            }
            var minutesLat = (lonLat.lat - degreesLat) * 60;

            if (lonLat.lon > 0) {
                var degreesLon = Math.floor(lonLat.lon);
            } else {
                var degreesLon = Math.ceil(lonLat.lon);
            }
            var minutesLon = (lonLat.lon - degreesLon) * 60;

            return degreesLat + "&deg; " + minutesLat.toFixed(3) + "\' N &nbsp;&nbsp;" + degreesLon + "&deg; " + minutesLon.toFixed(3) + "\' W";
        }
    });
    map.addControl(map.coordsControl);


    //UTF Attribution
    map.UTFControl = new OpenLayers.Control.UTFGrid({
        //attributes: layer.attributes,
        layers: [],
        //events: {fallThrough: true},
        handlerMode: 'click',
        callback: function(infoLookup, lonlat, xy) {
            app.map.utfGridClickHandling(infoLookup, lonlat, xy);
        }
    });
    map.addControl(map.UTFControl);

    app.map.utfGridClickHandling = function(infoLookup, lonlat, xy) {
        var clickAttributes = [];

        // identify which grid layers were clicked
        var gridLayersHit = [];
        for (var idx in infoLookup) {
            var info = infoLookup[idx];
            if (info && info.data) {
                var gridLayer = map.layers[idx];
                if (gridLayer && gridLayer.layerModel && gridLayer.layerModel.name) {
                    gridLayersHit[gridLayer.layerModel.name] = info;
                }
            }
        }

        // loop through visible layers and show attributes for any visible layers that match the grid layers that were clicked
        $.each(app.viewModel.visibleLayers(), function(layer_index, potential_layer) {
            var gridLayerInfo = gridLayersHit[potential_layer.name];
            if (gridLayerInfo) {
                var attributes = undefined;
                var attribute_objs = [];

                if (potential_layer.attributes) {
                    attributes = potential_layer.attributes;
                } else if (potential_layer.parent && potential_layer.parent.attributes) {
                    attributes = potential_layer.parent.attributes;
                }

                if (attributes) {
                    $.each(attributes, function(index, obj) {
                        if (potential_layer.compress_attributes) {
                            var display = obj.display + ': ' + gridLayerInfo.data[obj.field];
                            attribute_objs.push({
                                'display': display,
                                'data': ''
                            });
                        } else {
                            var value = gridLayerInfo.data[obj.field];
                            try {
                                //set the precision and add any necessary commas
                                value = value.toFixed(obj.precision).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                            } catch (e) {
                                //keep on keeping on
                            }
                            attribute_objs.push({
                                'display': obj.display,
                                'data': value
                            });
                        }
                    });
                    var title = potential_layer.name,
                        text = attribute_objs;
                    if ( title === 'Planning Grid' ) {
                        text = app.clickAttributes.getGridAttributes(gridLayerInfo.data);
                    }
                    clickAttributes[title] = {
                      'hasSublayers': false,
                      'subLayers': {}
                    };
                    clickAttributes[title].subLayers[title] = text;
                }
            }
            $.extend(app.map.clickOutput.attributes, clickAttributes);
            app.viewModel.aggregatedAttributes(app.map.clickOutput.attributes);
        });

        app.viewModel.updateMarker(lonlat);

    }; //end utfGridClickHandling

    app.markers = new OpenLayers.Layer.Markers("Markers");
    var size = new OpenLayers.Size(18, 28);
    var offset = new OpenLayers.Pixel(-(size.w / 2), -size.h);
    app.markers.icon = new OpenLayers.Icon('/media/img/red-pin.png', size, offset);

    app.map.addLayer(app.markers);

    app.map.extentWithinExtent = function (innerExtent, outerExtent) {
      if (outerExtent.contains(innerExtent.left, innerExtent.top) && outerExtent.contains(innerExtent.right, innerExtent.bottom)) {
          return true;
        } else {
          return false;
        }
    }

    app.map.panToFeature = function(feature) {
      var featExtent = feature.geometry.getBounds();
      var mapExtent = app.map.getExtent();
      if (app.map.extentWithinExtent(featExtent, mapExtent)) {
        var centroid = feature.geometry.getCentroid();
        var lonlat = new OpenLayers.LonLat(centroid.x, centroid.y);
        app.map.panTo(lonlat);
      }
    };

    app.map.removeLayerByName = function(layerName) {
        for (var i = 0; i < app.map.layers.length; i++) {
            if (app.map.layers[i].name === layerName) {
                app.map.removeLayer(app.map.layers[i]);
                i--;
            }
        }
    };

    app.utils = {};

    app.utils.pip = function(point, vs) {
        // substacks point in polygon
        // ray-casting algorithm based on
        // http://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html

        var x = point[0],
            y = point[1];

        var inside = false;
        for (var i = 0, j = vs.length - 1; i < vs.length; j = i++) {
            var xi = vs[i][0],
                yi = vs[i][1];
            var xj = vs[j][0],
                yj = vs[j][1];

            var intersect = ((yi > y) != (yj > y)) && (x < (xj - xi) * (y - yi) / (yj - yi) + xi);
            if (intersect) inside = !inside;
        }

        return inside;
    };

    app.utils.isNumber = function(n) {
        return !isNaN(parseFloat(n)) && isFinite(n);
    };

    app.utils.numberWithCommas = function(x) {
        // TODO: do not apply to 4 digits or less. year 2,015 looks weird.
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    };

    app.utils.isInteger = function(n) {
        return app.utils.isNumber(n) && (Math.floor(n) === n);
    };

    app.utils.formatNumber = function(n) {
        var number = Number(n);
        var preciseNumber;
        if (app.utils.isInteger(number)) {
            preciseNumber = number.toFixed(0);
        } else {
            preciseNumber = number.toFixed(1);
        }
        return app.utils.numberWithCommas(preciseNumber);
    };

    app.utils.trim = function(str) {
        if (str) {
            return str.replace(/^\s+|\s+$/g, '');
        } else {
            return '';
        }
    };

    app.utils.getObjectFromList = function(list, field, value) {
        for (var i = 0; i < list.length; i += 1) {
            if (list[i][field] === value) {
                return list[i];
            }
        }
        return undefined;
    };

    app.clickEvent = function(x,y) {
      if ( ! app.viewModel.hasOwnProperty('clickEvent') || app.viewModel.clickEvent.x != x || app.viewModel.clickEvent.y != y ) {
        app.viewModel.aggregatedAttributes(false);
        app.viewModel.clickEvent = {
          'x': x,
          'y': y,
          'features': []
        }
      }
    }

    app.map.events.register("featureclick", null, function(e) {
      var layer = e.feature.layer.layerModel || e.feature.layer.scenarioModel;
      var attrs;
      if (layer) {
          var text = [],
              title = layer.name;

          if (layer.scenarioAttributes && layer.scenarioAttributes.length) {
              attrs = layer.scenarioAttributes;
              for (var i = 0; i < attrs.length; i++) {
                  text.push({
                      'display': attrs[i].title,
                      'data': attrs[i].data
                  });
              }
          // } else if (layer.id === 374 || layer.id === 375 || layer.id === 377 || layer.id === 378) { // special case for Survey Results
          } else if (app.surveyResults.surveyLayerNames.indexOf(layer.name) !== -1) { // is Survey Results layer
              text = app.clickAttributes.getSurveyAttributes(e.feature.data, layer.name);
          } else if (layer.attributes.length) {
              attrs = layer.attributes;

              for (var idx=0; idx < attrs.length; idx++) {
                  if (e.feature.data[attrs[idx].field]) {
                      text.push({
                          'display': attrs[idx].display,
                          'data': e.feature.data[attrs[idx].field]
                      });
                  }
              }
          }

          // the following delay prevents the #map click-event-attributes-clearing from taking place after this has occurred
          setTimeout(function() {
              if (!app.map.clickOutput.attributes[title]) {
                  app.map.clickOutput.attributes[title] = text;
              }
              app.viewModel.aggregatedAttributes(app.map.clickOutput.attributes);
              app.viewModel.updateMarker(app.map.getLonLatFromViewPortPx(e.event.xy));
              //if (app.marker) {
              //    app.marker.display(true);
              //app.viewModel.updateMarker(lonlat);
              //}
          }, 100);

      }
    });

    app.featureClick = function(evt){
      app.clickEvent(evt.event.x, evt.event.y);
      for (var layerIndex=0; layerIndex < app.map.layers.length; layerIndex++) {
        var layer = app.map.layers[layerIndex];
        if (layer.hasOwnProperty('layerModelId') &&
            app.viewModel.layerIndex[layer.layerModelId].visible()) {
          layer.events.triggerEvent('click', evt.event);
        }
      }
    }

    app.mapClick = function(evt){
      app.clickEvent(evt.x, evt.y);
      for (var layerIndex=0; layerIndex < app.map.layers.length; layerIndex++) {
        var layer = app.map.layers[layerIndex];
        if (layer.hasOwnProperty('layerModelId') &&
            app.viewModel.layerIndex[layer.layerModelId].visible()) {
          layer.events.triggerEvent('click', evt);
        }
      }
      // featureclick events always trigger before map click events
          // therefore We want to turn 'featureClick' to false at end of mapclick
      app.viewModel.featureClick(false);
    }

    app.map.events.register('click',null, app.mapClick);
    app.map.events.register('featureclick',null, app.featureClick);

    // takes GeoJSON of a single feature and adds it to 'selected' layer on map.
    app.displaySelectedFeature = function(feature, layerModelId) {
      if (! feature ) {
        feature = app.viewModel.clickEvent.features[layerModelId.toString()];
      } else {
        app.viewModel.clickEvent.features[layerModelId.toString()] = feature;
      }
      if (app.map.getLayersByName('Selected Features').length === 0) {
        var vectorStyle = new OpenLayers.StyleMap({
          "default": new OpenLayers.Style({
            pointRadius: 5,
            fillColor: '#000000',
            fillOpacity: 0,
            strokeColor: '#FF9933',
            strokeOpacity: 1,
            strokeWidth: 3
          }),
          "select": new OpenLayers.Style({
            pointRadius: 5,
            fillColor: '#000000',
            fillOpacity: 0,
            strokeColor: '#FF9933',
            strokeOpacity: 1,
            strokeWidth: 3
          }),
          "temporary": new OpenLayers.Style({
            pointRadius: 5,
            fillColor: '#000000',
            fillOpacity: 0,
            strokeColor: '#FF9933',
            strokeOpacity: 1,
            strokeWidth: 3
          })
        });

        var selectedFeatureLayer = new OpenLayers.Layer.Vector(
          "Selected Features",
          {
            styleMap: vectorStyle,
            rendererOptions: {zIndexing: true}
          }
        );

        app.map.addLayer(selectedFeatureLayer);
      }
      var selFeatLayer = app.map.getLayersByName('Selected Features')[0];
      selFeatLayer.removeAllFeatures();
      selFeatLayer.addFeatures([feature]);
      app.viewModel.updateSelectionHighlight();
      // This should require a button like ODFW's Compass - don't zoom on click
      // app.map.panToFeature(feature);
      // app.map.zoomToExtent(selFeatLayer.getDataExtent());
    }

};

app.addLayerToMap = function(layer) {
    if (layer.name.toLowerCase() != 'oregon mask' ) {
      layer.addLegendToLayer();
    }
    if (!layer.layer) {
        if (layer.utfurl || (layer.parent && layer.parent.utfurl)) {
            app.addUtfLayerToMap(layer);
        } else if (layer.type === 'Vector') {
            app.addVectorLayerToMap(layer);
        } else if (layer.type === 'ArcRest') {
            app.addArcRestLayerToMap(layer);
        } else if (layer.type === 'WMS') {
            app.addWmsLayerToMap(layer);
        } else { //if XYZ with no utfgrid
            app.addXyzLayerToMap(layer);
        }
        if (layer.hasArcRestDataLayer) {
            layer.layer.arcRestInstanceId = layer.arcRestInstanceId;
            layer.layer.arcRestServiceName = layer.arcRestServiceName;
            layer.layer.arcRestOutFields = layer.arcRestOutFields;
            layer.layer.arcGisLayerId = layer.arcgislayers;
            if (layer.type !== "Vector") {
              layer.layer.events.register('click', null, app.queryEsriDataLayer);
            }
        }
    }

    layer.layer.layerModelId = layer.id;
    layer.layer.attribution = layer.data_source;
    app.map.addLayer(layer.layer);
    layer.layer.opacity = layer.opacity();
    layer.layer.setVisibility(true);
};

// add XYZ layer with no utfgrid
app.addXyzLayerToMap = function(layer) {
    var opts = {
        displayInLayerSwitcher: false
    };

    var url = app.modifyURL(layer.url);

    // adding layer to the map for the first time
    layer.layer = new OpenLayers.Layer.XYZ(layer.name,
        url,
        $.extend({}, opts, {
            sphericalMercator: true,
            isBaseLayer: false //previously set automatically when allOverlays was set to true, must now be set manually
        })
    );
};

app.modifyURL = function(url) {
    var dateStringStart = url.search(new RegExp("{(y{2,4}|M{1,4}|d{1,4})+")),
        today = url.indexOf('{today}'),
        tomorrow = url.indexOf('{tomorrow}'),
        yesterday = url.indexOf('{yesterday}'),
        newURL = url;

    if (dateStringStart !== -1) {
        var dateStringEnd = url.indexOf('}', dateStringStart);
        var dateStringSpecifier = url.slice(dateStringStart + 1, dateStringEnd);
        var dateString = Date.today().toString(dateStringSpecifier);
        newURL = url.substr(0, dateStringStart) + dateString + url.substring(dateStringEnd + 1);
    }
    if (today !== -1) {
        today = newURL.indexOf('{today}');
        var todayEnd = newURL.indexOf('}', today);
        newURL = newURL.substr(0, today) + Date.today().toString("yyyy-MM-dd") + newURL.substr(todayEnd + 1);
    }
    if (tomorrow !== -1) {
        tomorrow = newURL.indexOf('{tomorrow}');
        var tomorrowEnd = newURL.indexOf('}', tomorrow);
        newURL = newURL.substr(0, tomorrow) + Date.today().add({
            days: 1
        }).toString("yyyy-MM-dd") + newURL.substr(tomorrowEnd + 1);
    }
    if (yesterday !== -1) {
        yesterday = newURL.indexOf('{yesterday}');
        var yesterdayEnd = newURL.indexOf('}', yesterday);
        newURL = newURL.substr(0, yesterday) + Date.today().add({
            days: -1
        }).toString("yyyy-MM-dd") + newURL.substr(yesterdayEnd + 1);
    }

    return newURL;
};


app.addWmsLayerToMap = function(layer) {

    layer.layer = new OpenLayers.Layer.WMS(layer.name, layer.url, {
        layers: layer.wms_slug,
        transparent: "true",
        format: "image/png"
    }, {
        // singleTile: true
        // 'buffer': 0
    });


};

app.addArcRestLayerToMap = function(layer) {
    layer.arcIdentifyControls = [];
    for (var layerIdIndex in layer.arcgislayers.split(',')) {
      layerIdIndex = parseInt(layerIdIndex);
      var layerId = layer.arcgislayers.split(',')[layerIdIndex].trim();
      var identifyUrl = layer.url.replace('export', layerId + '/query');
      var outfields = layer.arcRestOutFields;
      if (outfields.length < 1) {
        outfields = "*";
      }

      layer.arcIdentifyControls[layerIdIndex] = new OpenLayers.Control.ArcGisRestIdentify({
          eventListeners: {
              // arcfeaturequery: function(evt) {
              //   TODO: clear out current aggreatedAttributes for this layer
              //      Maybe replace with a spinner?
              // },
              //the handler for the return click data
              resultarrived: function(responseText, xy) {
                  var clickAttributes = {},
                      jsonFormat = new OpenLayers.Format.JSON(),
                      returnJSON = jsonFormat.read(responseText.text);
                  var attributeObjs;
                  if (returnJSON.features && returnJSON.features.length) {
                      attributeObjs = [];
                      returnJSON.olGeometries = [];
                      var selectedFeature = false;
                      $.each(returnJSON.features, function(index, feature) {
                          if (index === 0) {
                              var attributeList = feature.attributes;

                              if ('fields' in returnJSON) {
                                  if (layer.attributes.length) {
                                      for (var i = 0; i < layer.attributes.length; i += 1) {
                                          if (attributeList[layer.attributes[i].field]) {
                                              var data = attributeList[layer.attributes[i].field],
                                                  field_obj = app.utils.getObjectFromList(returnJSON.fields, 'name', layer.attributes[i].field);
                                              if (field_obj && field_obj.type === 'esriFieldTypeDate') {
                                                  data = new Date(data).toDateString();
                                              } else if (app.utils.isNumber(data)) {
                                                  data = app.utils.formatNumber(data);
                                              }
                                              if (app.utils.trim(data) !== "") {
                                                  attributeObjs.push({
                                                      'display': layer.attributes[i].display,
                                                      'data': data
                                                  });
                                              }
                                          }
                                      }
                                  } else {
                                      $.each(returnJSON.fields, function(fieldNdx, field) {
                                          if (field.name.indexOf('OBJECTID') === -1 && field.name.indexOf('objectid') === -1) {
                                              var data = attributeList[field.name];
                                              if (field.type === 'esriFieldTypeDate') {
                                                  data = new Date(data).toDateString();
                                              } else if (app.utils.isNumber(data)) {
                                                  data = app.utils.formatNumber(data);
                                              }
                                              if (app.utils.trim(data) !== "") {
                                                  attributeObjs.push({
                                                      'display': field.alias,
                                                      'data': data
                                                  });
                                              }
                                          }
                                      });
                                  }
                              }

                              if (feature.hasOwnProperty('geometry')) {
                                if (feature.geometry.hasOwnProperty('x') && feature.geometry.hasOwnProperty('y')) {
                                  returnJSON.olGeometries.push(new OpenLayers.Geometry.Point(feature.geometry.x, feature.geometry.y));
                                } else if (feature.geometry.hasOwnProperty('rings')) {
                                  var linearRings = [];
                                  for (var i=0; i < feature.geometry.rings.length; i++) {
                                    var ring = feature.geometry.rings[i];
                                    var points = [];
                                    for (var j=0; j < ring.length; j++) {
                                      points.push(new OpenLayers.Geometry.Point(ring[j][0], ring[j][1]));
                                    }
                                    linearRings.push(new OpenLayers.Geometry.LinearRing(points));
                                  }
                                  returnJSON.olGeometries.push(new OpenLayers.Geometry.Polygon(linearRings));
                                } else if (feature.geometry.hasOwnProperty('paths')) {
                                  for (var i=0; i < feature.geometry.paths.length; i++) {
                                    var path = feature.geometry.paths[i];
                                    var points = [];
                                    for (var j=0; j < path.length; j++) {
                                      points.push(new OpenLayers.Geometry.Point(path[j][0], path[j][1]));
                                    }
                                  }
                                  returnJSON.olGeometries.push(new OpenLayers.Geometry.LineString(points));
                                }
                              }
                              return;
                          }
                      });
                      var featCollection = new OpenLayers.Geometry.Collection(returnJSON.olGeometries);
                      selectedFeature = new OpenLayers.Feature.Vector(featCollection);
                  } else {
                    // clickAttributes[layer.name] = {};
                    //TODO if not all sublayers are hit, remove all missed ones and update (if priors)
                  }

                  var layerName = layer.name;
                  if (layer.legend && layer.legend.layers.length >= layerIdIndex){
                    layerName = layer.legend.layers[layerIdIndex].layer.title;
                  } else if (returnJSON.hasOwnProperty("displayFieldName")) {
                    layerName = returnJSON.displayFieldName;
                  }

                  if (attributeObjs && attributeObjs.length) {
                      if (!clickAttributes.hasOwnProperty(layer.name)) {
                        clickAttributes[layer.name] = {
                          'hasSublayers': (layer.arcgislayers.split(',').length !== 1),
                          'subLayers': {}
                        };
                      }
                      clickAttributes[layer.name].subLayers[layerName] = attributeObjs;
                      $.extend(app.map.clickOutput.attributes, clickAttributes);
                      app.viewModel.aggregatedAttributes(app.map.clickOutput.attributes);
                      if (selectedFeature) {
                        app.displaySelectedFeature(selectedFeature, layer.id);
                      } else {
                        app.viewModel.updateMarker(app.map.getLonLatFromViewPortPx(responseText.xy));
                      }
                  }
              }
          },
          url: identifyUrl,
          layerid: layer.arcgislayers,
          sr: '3857',
          clickTolerance: 3,
          outFields: outfields,
          maxAllowableOffset: 100
      });

      app.map.addControl(layer.arcIdentifyControls[layerIdIndex]);

    }

    layer.layer = new OpenLayers.Layer.ArcGIS93Rest(
        layer.name,
        layer.url, {
            layers: "show:" + layer.arcgislayers,
            srs: 'EPSG:3857',
            transparent: true
        }, {
            isBaseLayer: false,
            singleTile: true,
            ratio: 1
        }
    );
};

app.getEsriJSONFieldName = function(fields, key){
    for(var field_idx=0; field_idx < fields.length; field_idx++) {
        if (fields[field_idx].name == key){
            return fields[field_idx].alias;
        }
    }
    return null;
};

app.getTopOffset = function(element) {
  var windowTop = $('window').scrollTop();
  elementOffset = element.offset().top;
  return (elementOffset - windowTop);
};

app.queryEsriDataLayer = function(evt){
    app.clickEvent(evt.x,evt.y);
    var self = this;
    if (!self.hasOwnProperty('arcGisLayerId')) {
      self = evt.object;
      evt = evt.event;
    }
    var pixel_buffer = 1;
    var leftOffset = evt.object.map.div.offsetParent.offsetLeft;
    var topOffset = app.getTopOffset($('#map-wrapper'));
    if (!evt.hasOwnProperty('x')) {
      evt.x = evt.clientX;
    }
    if (!evt.hasOwnProperty('y')) {
      evt.y = evt.clientY;
    }
    var px = new OpenLayers.Pixel(evt.x-leftOffset,evt.y-topOffset);
    var nwpx = new OpenLayers.Pixel(evt.x-pixel_buffer-leftOffset,evt.y-pixel_buffer-topOffset);
    var sepx = new OpenLayers.Pixel(evt.x+pixel_buffer-leftOffset,evt.y+pixel_buffer-topOffset);
    var coords = self.getLonLatFromViewPortPx(px);
    var nwCoords = self.getLonLatFromViewPortPx(nwpx);
    var seCoords = self.getLonLatFromViewPortPx(sepx);

    var geometry = {
      xmin: nwCoords.lon,
      ymin: seCoords.lat,
      xmax: seCoords.lon,
      ymax: nwCoords.lat,
      spatialReference: {
        wkid:102100
      }
    };

    var geomQuery = JSON.stringify(geometry);
    app.esriQueryClickEvent = {};
    app.esriQueryClickEvent.px = px;
    app.esriQueryClickEvent.lonlat = coords;
    if (evt.object.hasOwnProperty('name')){
      app.esriQueryClickEvent.layerName = evt.object.name;
    } else {
      app.esriQueryClickEvent.layerName = self.name;
    }
    var instanceId = self.arcRestInstanceId;            //Needed from layer manager
    var serviceName = self.arcRestServiceName;          //Needed from layer manager
    var outFields = self.arcRestOutFields;              //Needed from layer manager
    var layerId = self.arcGisLayerId;
    var ajaxUrl= "http://services.arcgis.com/" +
        instanceId + "/arcgis/rest/services/" +
        serviceName + "/FeatureServer/" + layerId + "/query?geometry=" + encodeURIComponent(geomQuery) +
        "&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelIntersects" +
        "&units=esriSRUnit_Meter&outFields=" +
        outFields + "&returnGeometry=true&f=json";
    $.ajax({
      url: ajaxUrl
    }).done(function(res) {
      var feats = JSON.parse(res);
      if (feats.features.length > 0) {
        // TODO: gather all features and allow user to cycle through
        var attributes = feats.features[0].attributes;
        var keys = Object.keys(attributes);
        var out = '';
        var clickAttributes = {};
        clickAttributes[app.esriQueryClickEvent.layerName] = {
            'hasSublayers':(layerId.split.length !== 1),
            'subLayers': {}
        };
        var layerAttributes = [];
        for(var key_idx=0; key_idx < keys.length; key_idx++) {
            var label = app.getEsriJSONFieldName(feats.fields, keys[key_idx]);
            if (out.length !== 0){
                out += "\n\r";
            }
            out+= label + ": " + attributes[keys[key_idx]];
            layerAttributes.push({
              'display': label,
              'data':attributes[keys[key_idx]]
            });
        }
        var layerName = app.esriQueryClickEvent.layerName;
        var namedLayers = app.map.layers.filter(function(layer){return layer.name == app.esriQueryClickEvent.layerName;});
        if (namedLayers.length > 0) {
          if (namedLayers[0].hasOwnProperty('layerModel')) {
            // TODO: Untested, and cannot test well until a proper layer candidate appears
            layerName = namedLayers[0].layerModel.legend.layers[parseInt(namedLayers[0].argGisLayerId)].layer.title;
          }
        }
        clickAttributes[app.esriQueryClickEvent.layerName].subLayers[layerName] = layerAttributes;
        $.extend(app.map.clickOutput.attributes, clickAttributes);
        app.viewModel.aggregatedAttributes(app.map.clickOutput.attributes);
        // app.viewModel.updateMarker(app.esriQueryClickEvent.lonlat);
        var projection;
        if (feats.spatialReference.hasOwnProperty('wkid')) {
          projection = new OpenLayers.Projection("EPSG:" + feats.spatialReference.wkid.toString());
        } else {
          projection = new OpenLayers.Projection("EPSG:3857")
        }

        var feature = feats.features[0];
        var attributes = {};
        if (feature.hasOwnProperty('attributes')) {
          attributes = feature.attributes;
        }
        if (feature.hasOwnProperty('geometry')) {
          var geometry = feature.geometry;
          if (geometry.hasOwnProperty('rings')){
            if (geometry.rings.length == 1) {
              var featureRingsIdx = 0;
              var points = [];
              for (var i = 0; i < geometry.rings[featureRingsIdx].length; i++) {
                var point = new OpenLayers.Geometry.Point(geometry.rings[featureRingsIdx][i][0], geometry.rings[featureRingsIdx][i][1]);
                point.transform(projection, new OpenLayers.Projection("EPSG:3857"))
                points.push(point);
              }
              var ring = new OpenLayers.Geometry.LinearRing(points);
              var polygon = new OpenLayers.Geometry.Polygon([ring]);
              var layerFeature = new OpenLayers.Feature.Vector(polygon, attributes);
            } else {
              // TODO: remove this
              debugger;
            }
          }
        }

        app.displaySelectedFeature(layerFeature, self.layerModelId);

      }
    });

};

app.addVectorLayerToMap = function(layer) {
    var url = layer.url,
        proj = layer.proj || 'EPSG:3857';
    if (layer.hasOwnProperty('stylemap')){
      var styleMap = layer.stylemap;
    } else {
      var styleMap = new OpenLayers.StyleMap({
        'default': new OpenLayers.Style({
          fillColor: layer.color,
          fillOpacity: layer.fillOpacity,
          //strokeDashStyle: "dash",
          //strokeOpacity: 1,
          strokeColor: layer.color,
          strokeOpacity: layer.defaultOpacity,
          //strokeLinecap: "square",
          //http://dev.openlayers.org/apidocs/files/OpenLayers/Feature/Vector-js.html
          //title: 'testing'
          pointRadius: 2,
          externalGraphic: layer.graphic,
          graphicWidth: 8,
          graphicHeight: 8,
          graphicOpacity: layer.defaultOpacity
        })
      });
    }
    if (!styleMap.styles.hasOwnProperty('select')){
      styleMap.select = new OpenLayers.Style({
        fillColor: layer.color,
        fillOpacity: layer.fillOpacity,
        strokeColor: "#0077FF",
        strokeWidth: 1
      })
    }
    if (layer.proxy_url) {
        url = '/proxy/layer/' + layer.id;
    }

    if (app.surveyResults.surveyLayerNames.indexOf(layer.name) !== -1) { // is Survey Results layer
        var surveyStylingRules = app.surveyResults.getSurveyStylingRules(layer.name);
        styleMap.styles['default'].addRules(surveyStylingRules);
    } else if (layer.lookupField) {
        var mylookup = {};
        $.each(layer.lookupDetails, function(index, details) {
            var fillOp = 0.5;

            mylookup[details.value] = {
                strokeColor: details.color,
                strokeDashstyle: details.dashstyle,
                fill: details.fill,
                fillColor: details.color,
                fillOpacity: fillOp,
                externalGraphic: details.graphic
            };
        });
        styleMap.addUniqueValueRules("default", layer.lookupField, mylookup);
    }

    vectorLoadEndListener = function(ret) {
        var layerModel = ret.object.layerModel;
        ret.object.styleMap = layerModel.stylemap;
        if (ret.object.features.length >= 1000) {
          // Arc maxes out at 1000 features. The map will not be complete.
          alert('You are too far zoomed out to load data for ' +
          layerModel.name + '. Please zoom in and try again.');
          layerModel.deactivateLayer();
        } else if (!layerModel.visible() || !layerModel.loaded) {
            layer.loaded = true;
            setGeom(layer);
            try {
              ret.object.redraw();
            } catch (err) {
              console.log('Error redrawing vector layer:');
              console.log(err.toString());
            }
        } else {
          ret.object.redraw();
        }

        if (app.viewModel.vectorLayersLoading().length != 0) {
          app.viewModel.vectorLayersLoading.remove(layerModel.name);
          if (app.viewModel.vectorLayersLoading().length == 0) {
            // if slow-loading vector layers were added and are now all loaded:
            //swap layer order, then undo, with 50ms timeout to make sure that we don't jump the gun.
            setTimeout(function() {
              app.viewModel.activeLayers()[0].lowerLayer(app.viewModel.activeLayers()[0], false);
              app.viewModel.activeLayers()[0].lowerLayer(app.viewModel.activeLayers()[0], false);
            }, 50);
            //Force the correct tab to show
            app.displayActiveTab(app.getState());
          }
        }
        layerModel.selectControl.activate();
    }

    getGeom = function(layer) {
        var extent = app.map.getExtent();
        geometry = {
          xmin: extent.left,
          ymin: extent.bottom,
          xmax: extent.right,
          ymax: extent.top,
          spatialReference: {
            wkid:102100
          }
        };
        return geometry;
    }

    setGeom = function(layer) {
      var geometry = getGeom(layer);
      if (layer.hasOwnProperty('layer') && layer.layer.hasOwnProperty('protocol') && layer.layer.protocol.hasOwnProperty('params')) {
        layer.layer.protocol.params.geometry = JSON.stringify(geometry);
        layer.layer.protocol.params.returnGeometry = true;
      }
    }

    bBoxStrategy = new OpenLayers.Strategy.BBOX({
      ratio: 1.2,
      update: function(options){
        setGeom(layer);
        var mapBounds = this.getMapBounds();
        if (mapBounds !== null && ((options && options.force) ||
                                   this.invalidBounds(mapBounds))) {
            this.calculateBounds(mapBounds);
            this.resolution = this.layer.map.getResolution();
            this.triggerRead(options);
        }
      }
    });

    layer.layer = new OpenLayers.Layer.Vector(
        layer.name, {
            projection: new OpenLayers.Projection(proj), // 3857
            displayInLayerSwitcher: false,
            strategies: [
              bBoxStrategy
            ],
            protocol: new OpenLayers.Protocol.HTTP({
                url: url.split('?')[0],
                format: new OpenLayers.Format.GeoJSON(),
                params: {
                  'geometryType':'esriGeometryEnvelope',
                  'spatialRel':'esriSpatialRelIntersects',
                  'units':'esriSRUnit_Meter',
                  'outFields':'*',
                  'returnGeometry':true,
                  'f':'pgeojson',
                  'geometry': JSON.stringify(getGeom()),
                  'maxAllowableOffset': 100
                }
            }),
            styleMap: styleMap,
            layerModel: layer
        }
    );
    app.viewModel.vectorLayersLoading.push(layer.name);
    layer.layer.events.on({"loadend": vectorLoadEndListener});

    layer.selectControl = new OpenLayers.Control.SelectFeature(
        layer.layer,
        {
          clickOut: true,
          toggle: false,
          multiple: false,
          hover: false
          // multipleKey: "ctrlKey",
          // box: true
        }
    );

    // Allow clicking + dragging on feature layer
    layer.selectControl.handlers.feature.stopDown = false;

    app.map.addControl(layer.selectControl);

    layer.layer.events.register('featureclick', layer.layer, function(event) {
        // featureclick events always trigger before map click events
          // Therefore we want to turn featureclick on at beginning of featureclick
        app.viewModel.featureClick(true);

        var attributes = event.feature.attributes;
        var keys = Object.keys(attributes);
        var clickAttributes = {};
        clickAttributes[event.feature.layer.name] = {
          'hasSublayers': (event.feature.layer.arcGisLayerId.split(',').length !== 1),
          'subLayers': {}
        };
        var layerAttributes = [];
        for(var key_idx=0; key_idx < keys.length; key_idx++) {
            var label = event.object.layerModel.fieldMap[keys[key_idx]];
            layerAttributes.push({
              'display': label,
              'data':attributes[keys[key_idx]]
            });
        }
        var layerName = event.feature.layer.name;
        if (event.feature.layer.layerModel.hasOwnProperty('legend')) {
          if (event.feature.layer.layerModel.legend.hasOwnProperty('layers')) {
            var layerId = event.object.arcGisLayerId; // TODO - identify actual sublayer!!!
            layerName = event.feature.layer.layerModel.legend.layers[layerId].title;
          }
        }
        clickAttributes[event.feature.layer.name].subLayers[layerName] = layerAttributes;
        $.extend(app.map.clickOutput.attributes, clickAttributes);
        app.viewModel.aggregatedAttributes(app.map.clickOutput.attributes);
        // return false;
        app.displaySelectedFeature(event.feature.clone(), event.feature.layer.layerModelId);
    });
};

app.addUtfLayerToMap = function(layer) {
    var opts = {
        displayInLayerSwitcher: false
    };
    layer.utfgrid = new OpenLayers.Layer.UTFGrid({
        layerModel: layer,
        url: layer.utfurl ? layer.utfurl : layer.parent.utfurl,
        sphericalMercator: true,
        //events: {fallThrough: true},
        utfgridResolution: 4, // default is 2
        displayInLayerSwitcher: false,
        useJSONP: layer.utfjsonp
    });
    app.map.addLayer(layer.utfgrid);

    if (layer.type === 'ArcRest') {
        app.addArcRestLayerToMap(layer);
    } else if (layer.type === 'XYZ') {
        //maybe just call app.addXyzLayerToMap(layer)
        app.addXyzLayerToMap(layer);
    } else {
        //debugger;
    }
};

app.setLayerVisibility = function(layer, visibility) {
    // if layer is in openlayers, hide/show it
    if (layer.layer) {
        layer.layer.setVisibility(visibility);
    }
};

app.setLayerZIndex = function(layer, index) {
    layer.layer.setZIndex(index);
};


app.reCenterMap = function() {
    app.map.setCenter(new OpenLayers.LonLat(app.state.x, app.state.y).transform(
        new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:3857")), 7);
};

// block mousehweel when over overlay
$("#overview-overlay-text").hover(
    // mouseenter
    function() {
        var controls = app.map.getControlsByClass('OpenLayers.Control.Navigation');
        for (var i = 0; i < controls.length; ++i) {
            controls[i].disableZoomWheel();
        }

    },
    function() {
        var controls = app.map.getControlsByClass('OpenLayers.Control.Navigation');
        for (var i = 0; i < controls.length; ++i) {
            controls[i].enableZoomWheel();
        }
    }
);
