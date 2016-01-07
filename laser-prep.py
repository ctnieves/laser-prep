import sys
from PIL import Image

def main(argv):
	image = Image.open(sys.argv[1])
	result = image.convert('P', dither=Image.FLOYDSTEINBERG) #dithering in PIL behaves oddly, have to execute on separate line
 	if len(sys.argv) > 2:
 		print "Using " + sys.argv[2] + " colors"
 		result = result.convert('P', palette=Image.ADAPTIVE, colors=int(sys.argv[2]))

 	else:
 		result = result.convert('P', palette=Image.ADAPTIVE, colors=8)
 	result = result.convert("L")
 	result.show()
 	result.save("prepped_" + argv[1])
if __name__ == "__main__":
    main(sys.argv)