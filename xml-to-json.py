def traverseNode(node, storage, substorage):
	for child in node:
		info_dict = {}
		if child.tag.startswith("{http://wordpress.org/export/1.2/}"):
			substorage[child.tag.replace("{http://wordpress.org/export/1.2/}", "")] = traverseNode(child, storage, info_dict)
		elif child.tag.startswith("{http://purl.org/rss/1.0/modules/content/}"):
			substorage[child.tag.replace("{http://purl.org/rss/1.0/modules/content/}", "")] = traverseNode(child, storage, info_dict)
		elif child.tag.startswith("{http://wellformedweb.org/CommentAPI/}"):
			substorage[child.tag.replace("{http://wellformedweb.org/CommentAPI/}", "")] = traverseNode(child, storage, info_dict)
		elif child.tag.startswith("{http://wordpress.org/export/1.2/excerpt/}"):
			substorage[child.tag.replace("{http://wordpress.org/export/1.2/excerpt/}", "")] = traverseNode(child, storage, info_dict)
		elif child.tag.startswith("{http://purl.org/dc/elements/1.1/}"):
			substorage[child.tag.replace("{http://purl.org/dc/elements/1.1/}", "")] = traverseNode(child, storage, info_dict)
		else:
			substorage[child.tag] = traverseNode(child, storage, info_dict)


	return substorage

def traverseNodeFuther(node, currentDict, key):
	info_dict = {}
	for child in node:
		info_dict

def main():
	import xml.etree.ElementTree as ET

	tree = ET.parse('nacc.xml')
	root = tree.getroot()
	storage = {}
	substorage = {}
	data = traverseNode(root, storage, substorage)
	print data

if __name__ == '__main__':
	main()