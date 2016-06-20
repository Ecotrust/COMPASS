
app.clickAttributes = (function() {

	var getSurveyAttributes = function(data, activity) {
		attrs = [];
		if (activity !== 'All Activities') {
			for (var key in data) {
			  	if (data.hasOwnProperty(key) && data[key]) {
			  		if (key === activity) {
			  			if (data[key] === 1) {
			    			attrs.push({'display': key, 'data': data[key] + ' day'});
			  			} else {
			    			attrs.push({'display': key, 'data': data[key] + ' days'});
			  			}
			  		}
			  	}
			}
			attrs.push({'display': 'Total Activity Days (All Activities)', 'data': data['Total Activity Days']});
            // attrs.push({'display': 'UniqueID', 'data': data['UniqueID']});
		} else {
			// for (var key in data) {
			//   	if (data.hasOwnProperty(key) && data[key]) {
			//   		if (key !== 'Total Activity Days' && key !== 'Other' && key !== 'UniqueID') {
			//   			if (data[key] === 1) {
			//     			attrs.push({'display': key, 'data': data[key] + ' day'});
			//   			} else {
			//     			attrs.push({'display': key, 'data': data[key] + ' days'});
			//   			}
			//   		}
			//   	}
			// }
			// // alphabetize and then put Total at top (or bottom)
			// attrs = _.sortBy(attrs, function(obj){ return obj['display']; });
			// if (data['Other']) {
			// 	if (data['Other'] === 1) {
			// 		attrs.push({'display': 'Other', 'data': data['Other'] + ' day'});
			// 	} else {
			// 		attrs.push({'display': 'Other', 'data': data['Other'] + ' days'});
			// 	}
			// }
			attrs.unshift({'display': 'Total Activity Days (All Activities)', 'data': data['Total Activity Days']});
            // attrs.push({'display': 'UniqueID', 'data': data['UniqueID']});
		}
		return attrs;
	};

    // Called from utfGridClickHandling in map.js (for Planning Grid click handling)
    // IMPORTANT NOTE:
    // These use the case-sensitive field names from the original shapefile,
    //    not the internal names used elsewhere. The order is alphabetical based
    //    on the original field name as well.

    # species-id look up table
    var species_lut = {
      1: "one",
      2: "two",
      3: "three",
      4: "four",
      5: "five",
      6: "six",
      7: "seven",
      8: "eight",
      9: "nine"
    };

    // taken directly from TLindig and nus at http://stackoverflow.com/questions/1960473/unique-values-in-an-array#answer-14438954
    var onlyUnique(value, index, self) {
      return self.indexOf(value) === index;
    }

    var speciesLookup = function(data) {
      id_array = JSON.parse(data);
      species_array = [];
      for ( id_index in id_array ) {
        id = id_array[id_index];
        species_array.push(species_lut[id]);
      }
      return species_array.filter( onlyUnique );
    }

    var getGridAttributes = function (data) {
        attrs = [];

        if ('OBJECTID' in data) {
            attrs.push({'display': 'Hex ID', 'data': data['OBJECTID'].toLocaleString()});
        }
        if ('HABITAT' in data) {
            attrs.push({'display': 'Habitats', 'data': speciesLookup(data['HABITATS']).toLocaleString()});
        }
        if ('FISH' in data) {
            attrs.push({'display': 'Habitats', 'data': speciesLookup(data['FISH']).toLocaleString()});
        }
        if ('OBS_SPEC' in data) {
            attrs.push({'display': 'Habitats', 'data': speciesLookup(data['OBS_SPEC']).toLocaleString()});
        }
        if ('MOD_SPEC' in data) {
            attrs.push({'display': 'Habitats', 'data': speciesLookup(data['MOD_SPEC']).toLocaleString()});
        }
        

        return attrs;
    };

    return {
    	getGridAttributes: getGridAttributes,
    	getSurveyAttributes: getSurveyAttributes
    };

})();
