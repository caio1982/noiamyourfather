DESTDIR=
fortunedir=/usr/share/games/fortunes/

fortune=noiamyourfather/translations

fortunedat = $(addsuffix .dat, $(fortune))

srcfiles = $(fortune) Makefile

pkgfiles = $(fortunedat) $(srcfiles)

all: tar

download:
	@lynx -dump -nolist http://noiamyourfather.org | sed '/Twitter!/,/Copyleft/!d;//d;s/^$$/%/' > $(fortune)
	@strfile $(fortune)

install:
	for i in $(fortune); do \
		install -m 644 -D $${i} $(DESTDIR)$(fortunedir)/$${i}; \
	done 
	for i in $(fortunedat); do \
		install -m 644 -D $${i} $(DESTDIR)$(fortunedir)/$${i}; \
	done

tar: download
	@tar cjvf fortune-noiamyourfather.tar.bz2 $(pkgfiles)

dist: tar

clean:
	find -name "*~" -exec rm -f {} \;
	rm -f $(fortunedat) $(fortune)

.PHONY: download install tar clean
