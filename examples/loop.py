from calculateMatches import CalculateMatches

pigAlgorithm = CalculateMatches() # Constructor that does nothing

pigAlgorithm.calculateImages("im1.jpg", "im2.jpg")
pigAlgorithm.calculateImages("roma_1.jpg", "roma_2.jpg")
pigAlgorithm.calculateImages("building_1.jpg", "building_2.jpg")
# TODO 1: Change waitkey to save image to disk
# TODO 2: Use for loop to read images