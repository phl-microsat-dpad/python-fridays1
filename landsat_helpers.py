def get_scene_details(input):
	scene = {}
	scene["path"] = input[3:6]
	scene["year"] = input[9:13]
	scene["day"] = input[13:16]
	scene["row"] = input[6:9]
	return scene

if __name__ == '__main__':
    get_scene_details(scene)