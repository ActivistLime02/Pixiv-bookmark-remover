import webbrowser

# Process links in file
with open("post_id.txt") as post_id :
	list_of_post_id_to_process = post_id.readlines()
	list_of_links = list()
	for post_id in list_of_post_id_to_process :
		link_prefix = "https://www.pixiv.net/en/artworks/"
		link = link_prefix + post_id
		list_of_links.append(link)

# Open links 10 at a time
count = 0
for link in list_of_links :
	count += 1
	webbrowser.open(link)
	if count >= 10 :
		count = 0
		input("Press enter to open up another 10 tabs")
