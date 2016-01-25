def get_scene_details(filename):
    scene_details = {
        'path': filename[3:6],
        'row': filename[6:9],
        'year': filename[9:13],
        'day': filename[13:16] 
    }
    return scene_details
