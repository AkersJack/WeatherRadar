import geotiler



if __name__ == "__main__": 
    map = geotiler.Map(center=(-6.069, 53.390), zoom=16, size=(512, 512))
    map.extent
    image = geotiler.render_map(map) 
    image.save('map.png') 