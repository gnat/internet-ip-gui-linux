# Build deb file for project.

# Refresh assets.
mkdir -p lanpack/usr/bin/
mkdir -p lanpack/usr/share/lanpack
cp -f ../lanpack.py lanpack/usr/bin/lanpack.py
cp -f ../lanpack.png lanpack/usr/share/lanpack/lanpack.png
cp -f ../lan.glade lanpack/usr/share/lanpack/lan.glade

# Run build.
dpkg-deb --build lanpack

# Clean assets.
rm -rf lanpack/usr/bin
rm -rf lanpack/usr/share/lanpack
