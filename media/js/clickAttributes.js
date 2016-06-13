
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
    var getGridAttributes = function (data) {
        attrs = [];

        if ('OBJECTID' in data) {
            attrs.push({'display': 'Hex ID', 'data': data['OBJECTID'].toLocaleString()});
        }
        if ('ECOREGION' in data) {
            attrs.push({'display': 'Ecoregion', 'data': data['ECOREGION'].toLocaleString()});
        }
        if ('TCD_Mean' in data) {
            attrs.push({'display': 'Anchoring Density', 'data': data['TCD_Mean'].toFixed(5) + ' things'});
        }


        /*

        if ('AcervAreaM' in data) {
            attrs.push({'display': 'Mapped Dense Acropora cervicornis', 'data': data['AcervAreaM'].toLocaleString() + ' m&sup2;'});
        }
        if ('AncDen0913' in data) {
            attrs.push({'display': 'Anchoring Density', 'data': data['AncDen0913'].toFixed(1) + ' boats'});
        }
        // No Anchor0913
        if ('Anchorage' in data) {
            attrs.push({'display': 'Intersects with a designated anchorage', 'data': data['Anchorage']});
        }
        if ('ArtAreaM' in data) {
            attrs.push({'display': 'Artificial Habitats', 'data': data['ArtAreaM'].toLocaleString() + ' m&sup2;'});
        }
        if ('CoralPtCov' in data) {
            attrs.push({'display': 'Coral Cover', 'data': data['CoralPtCov']});
        }
        if ('CoralRich' in data) {
            attrs.push({'display': 'Coral Richness', 'data': data['CoralRich']});
        }
        if ('CorlDen_m2' in data) {
            attrs.push({'display': 'Coral Density', 'data': data['CorlDen_m2']});
        }
        if ('County' in data) {
            attrs.push({'display': 'County', 'data': data['County']});
        }
        // No "Divecnflct"
        if ('DnsAcrpPA' in data) {
            attrs.push({'display': 'Dense Acropora Presence', 'data': data['DnsAcrpPA']});
        }
        // No "Fishcnflct"
        if ('fishdivovr' in data) {
            attrs.push({'display': 'Diving and Fishing use overlap', 'data': data['fishdivovr']});
        }
        if ('GorgPtCov' in data) {
            attrs.push({'display': 'Soft Coral Percent Cover', 'data': data['GorgPtCov']});
        }
        if ('Impacted' in data) {
            attrs.push({'display': 'Mapped Impact Source', 'data': data['Impacted']});
        }
        if ('InjurySite' in data) {
            attrs.push({'display': 'Recorded Grounding or Anchoring Event', 'data': data['InjurySite']});
        }
        if ('InletDisMi' in data) {
            attrs.push({'display': 'Distance to Nearest Inlet', 'data': data['InletDisMi'].toFixed(1) + ' mi'});
        }
        if ('LgLiveCorl' in data) {
            attrs.push({'display': 'Large Live Coral', 'data': data['LgLiveCorl']});
        }
        if ('Max_RRI_SE' in data) {
            attrs.push({'display': 'Coral Resilience Index', 'data': data['Max_RRI_SE']});
        }
        if ('Max_SBII' in data) {
            attrs.push({'display': 'Coral Bleaching', 'data': data['Max_SBII']});
        }
        if ('Max_SDII' in data) {
            attrs.push({'display': 'Coral Disease', 'data': data['Max_SDII']});
        }
        if ('MaxDpth_ft' in data && 'MinDpth_ft' in data) {
            attrs.push({'display': 'Depth Range', 'data': data['MinDpth_ft'] + ' to ' + data['MaxDpth_ft'] + ' feet'});
        }
        if ('MeanDpth_f' in data) {
            attrs.push({'display': 'Average Depth', 'data': data['MeanDpth_f']});
        }
        if ('MoorngBuoy' in data) {
            attrs.push({'display': 'Mooring Buoy', 'data': data['MoorngBuoy']});
        }
        if ('MorDen0913' in data) {
            attrs.push({'display': 'Mooring Density', 'data': data['MorDen0913'].toFixed(1) + ' boats'});
        }
        if ('OFR_Total' in data) {
            attrs.push({'display': 'Total Use Intensity (OFR 2015)', 'data': data['OFR_Total']});
        }
        if ('OFRboating' in data) {
            attrs.push({'display': 'Boater Use Intensity (OFR 2015)', 'data': data['OFRboating']});
        }
        // No "OFRcomfish"
        if ('OFRextract' in data) {
            attrs.push({'display': 'Extractive Diving Use Intensity (OFR 2015)', 'data': data['OFRextract']});
        }
        if ('OFRh2osprt' in data) {
            attrs.push({'display': 'Water Sports (OFR 2015)', 'data': data['OFRh2osprt']});
        }
        if ('OFRrecfish' in data) {
            attrs.push({'display': 'Recreational Fishing Use Intensity (OFR 2015)', 'data': data['OFRrecfish']});
        }
        // No "OFRresearc"
        if ('OFRscuba' in data) {
            attrs.push({'display': 'Scuba Diving Use Intensity (OFR 2015)', 'data': data['']});
        }
        if ('OFRspear' in data) {
            attrs.push({'display': 'Spearfishing Use Intensity (OFR 2015)', 'data': data['OFRspear']});
        }
        if ('OutflDisMi' in data) {
            attrs.push({'display': 'Distance to Nearest Outfall', 'data': data['OutflDisMi'].toFixed(1) + ' mi'});
        }
        if ('PierDisMi' in data) {
            attrs.push({'display': 'Distance to Nearest Pier', 'data': data['PierDisMi'].toFixed(1) + ' mi'});
        }
        if ('PillarPres' in data) {
            attrs.push({'display': 'Pillar Coral Presence', 'data': data['PillarPres']});
        }
        if ('PrcntArt' in data) {
            attrs.push({'display': 'Percent Artificial Habitat', 'data': data['PrcntArt']});
        }
        if ('PrcntReef' in data) {
            attrs.push({'display': 'Percent Reef', 'data': data['PrcntReef']});
        }
        if ('PrcntSand' in data) {
            attrs.push({'display': 'Percent Sand', 'data': data['PrcntSand']});
        }
        if ('PrcntSG' in data) {
            attrs.push({'display': 'Percent Seagrass', 'data': data['PrcntSG']});
        }
        if ('RecComDens' in data) {
            attrs.push({'display': 'Recreationally and commercially important fishes', 'data': data['RecComDens']});
        }
        if ('ReefArea_m' in data) {
            attrs.push({'display': 'Reef Area', 'data': data['ReefArea_m'].toLocaleString() + ' m&sup2;'});
        }
        if ('Region' in data) {
            attrs.push({'display': 'Region', 'data': data['Region']});
        }
        if ('RVCden1213' in data) {
            attrs.push({'display': 'Reef Fish Density',
                        'data': data['RVCden1213'].toFixed(1) + ' units'});
        }
        if ('RVCrch1213' in data) {
            attrs.push({'display': 'Reef Fish Species Richness',
                        'data': data['RVCrch1213'].toFixed(1) + ' units'});
        }
        if ('SandArea_m' in data) {
            attrs.push({'display': 'Sand Area', 'data': data['SandArea_m'].toLocaleString() + ' m&sup2;'});
        }
        if ('SGarea_m' in data) {
            attrs.push({'display': 'Seagrass Area', 'data': data['SGarea_m'].toLocaleString() + ' m&sup2;'});
        }
        if ('ShoreDisMi' in data) {
            attrs.push({'display': 'Distance to Shore', 'data': data['ShoreDisMi'].toFixed(1) + ' mi'});
        }
        if ('SpngPtCov' in data) {
            attrs.push({'display': 'Sponge Percent Cover', 'data': data['SpngPtCov']});
        }

        */

        return attrs;
    };

    return {
    	getGridAttributes: getGridAttributes,
    	getSurveyAttributes: getSurveyAttributes
    };

})();
