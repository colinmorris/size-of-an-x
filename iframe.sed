s/<iframe/<iframe class="ngramchart"/

# Handle dimens with external css
/^<iframe/ s/height=500//
/^<iframe/ s/width=900//

# Jekyll freaks the fuck out if attribute values aren't quoted
/^<iframe/ s/ (\w+)=([^"][^ >]*)/ \1="\2"/g

# Use bootstrap classes to make tables pretty
/^<tabl/ s/>\s*$/ class="table table-condensed dataframe">/

# Fix img urls
/^<img/ s%src="/?([^"]*)"%src="/assets/sizeof/\1"%

/^!\[/ s%writeup_files/([^\)]*)%/assets/sizeof/\1%
