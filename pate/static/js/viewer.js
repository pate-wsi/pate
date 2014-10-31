function init_map(imginfo, imgservers){
    var imgsrv = imgservers['servers'][0] // ToDo: do something clever here!
    var imgurl = imgsrv + '?zoomify=' + imginfo['filename'] + '/';

    var crossOrigin = 'anonymous';

    var imgCenter = [imginfo['width'] / 2, - imginfo['height'] / 2];

    // Maps always need a projection, but Zoomify layers are not geo-referenced, and
    // are only measured in pixels.  So, we create a fake projection that the map
    // can use to properly display the layer.
    var proj = new ol.proj.Projection({
      code: 'ZOOMIFY',
      units: 'pixels',
      extent: [0, 0, imginfo['width'], imginfo['height']]
    });

    var source = new ol.source.Zoomify({
      url: imgurl,
      size: [imginfo['width'], imginfo['height']],
      crossOrigin: crossOrigin
    });

    var map = new ol.Map({
      controls: ol.control.defaults().extend([
                    new ol.control.FullScreen(),
                    new ol.control.ZoomSlider(),
                    //new ol.control.OverviewMap(),
                    ]),
      layers: [
        new ol.layer.Tile({
          source: source
        })
      ],
      renderer: 'canvas',
      target: 'map',
      view: new ol.View({
        projection: proj,
        center: imgCenter,
        zoom: 0
      }),
      logo: false,
    });
}
