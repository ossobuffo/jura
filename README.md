# Jura

Jura Font Project by Daniel Johnson (il dot basso dot buffo at gmail dot com)

N.B. The Jura family has an unfortunate name clash with Ed Merritt's Jura serif font, which may be found [here](http://www.tenbytwenty.com/products/typefaces/jura).

July 2016 Alexei Vanyashin redesigned Jura as part of Google Fonts Improvement project. This repo contains both legacy v2.26, and the new v.3.

[Jura Design Guidelines](documentation/v3.001design-guide.md)

## Specimen

![Jura](documentation/images/jura-specimen.jpg)
![Jura](documentation/images/jura-before-after.jpg)


#### Web Specimen Deployment Tip

As you may have noticed this repo includes a [**webspecimen**](webspecimen) folder.
This is were the html files for the web specimen page are hosted. 
They are accessible online here: [http://alexeiva.github.io/jura](http://alexeiva.github.io/jura)

Normally to achieve this you would create a separate **gh-pages** branch, but it 
would be tediuos to switch between branches for each webpage update. 

There is a simple alternative deployment method:

1. Create a **webspecimen**[or any other name] folder with your html files in your **master** branch. Run these commands:

---
	gid add webspecimen && git commit -m "webpage update"
	git subtree push --prefix webspecimen origin gh-pages
 
2. Now your html files are accesible via http://[username/orgname].github.io/[projectname]
3. If you don't want this folder to appear in the master branch, add it to the .gitingore file, or use [subtree split](https://makingsoftware.wordpress.com/2013/02/16/using-git-subtrees-for-repository-separation/).

 
#### Goals of the new v.3 redesign:

- Redraw all glyphs in the GF Latin Plus range from scratch
- Add Bold weight
- Complete GF Cyrillic Core/Plus encoding


#### Roadmap of redesign

	[x] Concept
		[x] Light Master
		[x] Bold Master
		[x] Test weights
	[ ] Design
		[x] ASCII
		[x] GF Latin PLus
		[x] Kerning
		[x] OT Features
	[x] Production
	[x] Push


## License

This Font Software is licensed under the SIL Open Font License, Version 1.1. 
This license is copied below, and is also available with a FAQ at 
http://scripts.sil.org/OFL

## Repository Layout

This font repository follows the Unified Font Repository v2.0, 
a standard way to organize font project source files. Learn more at 
https://github.com/raphaelbastide/Unified-Font-Repository

